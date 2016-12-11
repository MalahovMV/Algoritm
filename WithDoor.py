import sys

def input_dz(nfaila):
    from Test import TestIn
    TestIn(nfaila)
    file = open('Input/' + nfaila + '.txt', 'r')
    labirint = []
    for s in file:
        s = s[:-1]
        labirint.append(list(s))

    file.close()

    return labirint

class Labirint:

    def __init__(self, labirint):
         self.count = 0
         self.lab = []
         self.new_doors = []
         for line in labirint:
             l = line[:]
             for element in l:
                 if (element == '<') or (element == '>') or (element == '^') or (element == '/'):
                     l[l.index(element)] = ' '

                 if element == 'S':
                     l[l.index(element)] = 0

             self.lab.append(l)

         self.keys = []
         alfabet = 'a'
         while alfabet[-1] < 'z':
             alfabet += chr(ord(alfabet[-1]) + 1)

         for line in self.lab:
            for elem in line:
                if str(elem) in alfabet:
                    self.keys.append(elem)
                    self.keys.append(-1)

         self.keys.append('f')
         self.keys.append(0)
         alfabet = 'A'

         while alfabet[-1] < 'Z':
            alfabet += chr(ord(alfabet[-1]) + 1)

         self.doors = []
         for line in self.lab:
             for elem in line:
                 if ((str(elem) in alfabet) and str(elem) != 'F'):
                     self.doors.append(elem)
                     self.doors.append(-1)

         self.doors.extend(('F', -1))

    def calculate_keys_way (self, labirint):
        flag = True
        while flag:
            flag = False
            for i in range(len(self.lab)):
                for j in range(len(self.lab[i])):
                    try:
                        bool_keys = (self.lab[i][j] >= 'a') and (self.lab[i][j] <= 'z') and (self.keys[self.keys.index(self.lab[i][j]) + 1] == self.count)
                    except:
                        bool_keys = False

                    try:
                        bool_doors = (self.lab[i][j] >= 'A') and (self.lab[i][j] <= 'Z') and (self.doors[self.doors.index(self.lab[i][j]) + 1] == self.count)
                    except:
                        bool_doors = False

                    if ((self.lab[i][j] == self.count) or bool_keys or bool_doors):
                        if (self.lab[i][j + 1] == ' ') and (
                                (labirint[i][j] == '>') or (labirint[i][j] == ' ') or (self.lab[i][j] == 0)or bool_keys or bool_doors):
                            self.lab[i][j + 1] = self.count + 1
                            flag = True

                        if (self.lab[i][j - 1] == ' ') and (
                                (labirint[i][j] == '<') or (labirint[i][j] == ' ') or (self.lab[i][j] == 0) or bool_keys or bool_doors):
                            self.lab[i][j - 1] = self.count + 1
                            flag = True

                        if (self.lab[i + 1][j] == ' ') and (
                                (labirint[i][j] == '/') or (labirint[i][j] == ' ') or (self.lab[i][j] == 0) or bool_keys or bool_doors):
                            self.lab[i + 1][j] = self.count + 1
                            flag = True

                        if (self.lab[i - 1][j] == ' ') and (
                                (labirint[i][j] == '^') or (labirint[i][j] == ' ') or (self.lab[i][j] == 0) or bool_keys or bool_doors):
                            self.lab[i - 1][j] = self.count + 1
                            flag = True

                        if ((str(self.lab[i][j + 1]) >= 'a')  and (str(self.lab[i][j + 1]) <= 'z')) and (
                                    (labirint[i][j] == '>') or (labirint[i][j] == ' ') or (self.lab[i][j] == 0) or bool_keys or bool_doors):
                            if (self.count < self.keys[self.keys.index(self.lab[i][j + 1]) + 1]) or (self.keys[self.keys.index(self.lab[i][j + 1]) + 1] == -1):
                                self.keys[self.keys.index(self.lab[i][j + 1]) + 1] = self.count + 1
                                flag = True

                        if ((str(self.lab[i][j - 1]) >= 'a') and (str(self.lab[i][j - 1]) <= 'z')) and (
                                    (labirint[i][j] == '<') or (labirint[i][j] == ' ') or (self.lab[i][j] == 0) or bool_keys or bool_doors):
                            if (self.count < self.keys[self.keys.index(self.lab[i][j - 1]) + 1]) or (self.keys[self.keys.index(self.lab[i][j - 1]) + 1] == -1):
                                self.keys[self.keys.index(self.lab[i][j - 1]) + 1] = self.count + 1
                                flag = True

                        if ((str(self.lab[i + 1][j]) >= 'a') and (str(self.lab[i + 1][j]) <= 'z')) and (
                                    (labirint[i][j] == '/') or (labirint[i][j] == ' ') or (self.lab[i][j] == 0)  or bool_keys or bool_doors):
                            if (self.count < self.keys[self.keys.index(self.lab[i + 1][j]) + 1]) or (self.keys[self.keys.index(self.lab[i + 1][j]) + 1] == -1):
                                self.keys[self.keys.index(self.lab[i + 1][j]) + 1] = self.count + 1
                                flag = True

                        if ((str(self.lab[i - 1][j]) >= 'a') and (str(self.lab[i - 1][j]) <= 'z')) and (
                                    (labirint[i][j] == '^') or (labirint[i][j] == ' ') or (self.lab[i][j] == 0) or bool_keys or bool_doors):
                            if (self.count < self.keys[self.keys.index(self.lab[i - 1][j]) + 1]) or (self.keys[self.keys.index(self.lab[i - 1][j]) + 1] == -1):
                                self.keys[self.keys.index(self.lab[i - 1][j]) + 1] = self.count + 1
                                flag = True

            self.count += 1


    def number_del(self, labirint):
        self.lab = []
        for line in labirint:
            l = line[:]
            for element in l:
                if (element == '<') or (element == '>') or (element == '^') or (element == '/'):
                    l[l.index(element)] = ' '

                if element == 'S':
                    l[l.index(element)] = 0

            self.lab.append(l)

    def set_count(self, count):
        self.count = count

    def calculate_way_between(self, labirint, obj1, obj2):
        self.number_del(labirint)
        self.count = 1
        if obj1 == obj2:
            return 0

        alfabet = 'a'
        while alfabet[-1] < 'z':
            alfabet += chr(ord(alfabet[-1]) + 1)
            if alfabet[-2] == obj2:
                alfabet = alfabet[:-2] + alfabet[-1]

        for i in range(len(self.lab)):
            for j in range(len(self.lab[i])):
                if self.lab[i][j] == obj1:
                    self.lab[i][j] = 1

        flag = True
        while flag:
            flag = False
            for i in range(len(self.lab)):
                for j in range(len(self.lab[i])):
                    if self.lab[i][j] == self.count :
                        if ((self.lab[i][j + 1] == ' ') or (str(self.lab[i][j + 1]) in alfabet)) and (
                                            (labirint[i][j] == '>') or (labirint[i][j] == ' ') or ((str(labirint[i][j]) >= 'a') and (str(labirint[i][j] <= 'z')))):
                            self.lab[i][j + 1] = self.count + 1
                            flag = True

                        if ((self.lab[i][j - 1] == ' ') or (str(self.lab[i][j - 1]) in alfabet)) and (
                                            (labirint[i][j] == '<') or (labirint[i][j] == ' ')or ((str(labirint[i][j]) >= 'a') and (str(labirint[i][j] <= 'z')))):
                            self.lab[i][j - 1] = self.count + 1
                            flag = True

                        if ((self.lab[i + 1][j] == ' ') or (str(self.lab[i + 1][j]) in alfabet)) and (
                                            (labirint[i][j] == '/') or (labirint[i][j] == ' ')or ((str(labirint[i][j]) >= 'a') and (str(labirint[i][j] <= 'z')))):
                            self.lab[i + 1][j] = self.count + 1
                            flag = True


                        if ((self.lab[i - 1][j] == ' ') or (str(self.lab[i - 1][j]) in alfabet)) and (
                                            (labirint[i][j] == '^') or (labirint[i][j] == ' ')or ((str(labirint[i][j]) >= 'a') and (str(labirint[i][j] <= 'z')))):
                            self.lab[i - 1][j] = self.count + 1
                            flag = True

                        if (str(self.lab[i][j + 1]) == obj2) and (
                                            (labirint[i][j] == '>') or (labirint[i][j] == ' ')or ((str(labirint[i][j]) >= 'a') and (str(labirint[i][j] <= 'z')))):
                            self.number_del(labirint)
                            return self.count

                        if (str(self.lab[i][j - 1]) == obj2) and (
                                            (labirint[i][j] == '<') or (labirint[i][j] == ' ')or ((str(labirint[i][j]) >= 'a') and (str(labirint[i][j] <= 'z')))):
                            self.number_del(labirint)
                            return self.count

                        if (str(self.lab[i + 1][j]) == obj2) and (
                                            (labirint[i][j] == '/') or (labirint[i][j] == ' ')or ((str(labirint[i][j]) >= 'a') and (str(labirint[i][j] <= 'z')))):
                            self.number_del(labirint)
                            return self.count

                        if (str(self.lab[i - 1][j]) == obj2) and (
                                            (labirint[i][j] == '^') or (labirint[i][j] == ' ')or ((str(labirint[i][j]) >= 'a') and (str(labirint[i][j] <= 'z')))):
                            self.number_del(labirint)
                            return self.count

            self.count += 1

        return -1


    def calculate_dif_way(self, labirint):
        i = 0
        self.new_doors = []
        while i < len(self.keys) - 2:
            lis = self.keys[i : i + 2]
            j = 0
            while j < len(self.doors) - 2:
                key = chr(ord(self.doors[j]) + ord('a') - ord('A'))
                lis.append(self.doors[j])
                betw0 = self.calculate_way_between(labirint, self.keys[i], key)
                betw1 = self.calculate_way_between(labirint, key, self.doors[j])
                betw2 = self.calculate_way_between(labirint, self.keys[i], self.doors[j])
                way1_2 = self.keys[i + 1] + betw1
                way2_1 = self.keys[self.keys.index(key) + 1] + betw2
                if (betw0 > -1) and (betw1 > -1) and (betw2 > -1):
                    if way1_2 > way2_1:
                        lis.append(way2_1 + betw0)

                    else:
                        lis.append(way1_2 + betw0)

                else:
                    lis.append(-1)

                if betw0 > 0:
                    lis.append(self.keys[i])
                    lis.append(betw0 + self.keys[self.keys.index(key) + 1])
                j += 2

            i += 2

            self.new_doors.append(lis)


    def calculate_door_ways(self, labirint, door, key):
        flag = True
        while flag:
            flag = False
            for i in range(len(self.lab)):
                for j in range(len(self.lab[i])):
                    try:
                        bool_keys = (self.lab[i][j] >= 'a') and (self.lab[i][j] <= 'z') and (
                            self.keys[self.keys.index(self.lab[i][j]) + 1] == self.count)
                    except:
                        bool_keys = False

                    try:
                        bool_doors = False
                        for lis in self.new_doors:
                            if lis[0] == key:
                                bool_doors = (self.lab[i][j] >= 'A') and (self.lab[i][j] <= 'Z') and (
                                    lis[lis.index(self.lab[i][j]) + 1] == self.count) and (self.lab[i][j] != 'F')

                            if key == 'f':
                                bool_doors = (self.lab[i][j] >= 'A') and (self.lab[i][j] <= 'Z') and (
                                    self.doors[self.doors.index(self.lab[i][j]) + 1] == self.count) and (self.lab[i][j] != 'F')

                    except:
                        bool_doors = False

                    if ((self.lab[i][j] == self.count)  or bool_keys or bool_doors):
                        if (self.lab[i][j + 1] == ' ') and (
                                            (labirint[i][j] == '>') or (labirint[i][j] == ' ') or (
                                        self.lab[i][j] == 0) or ((str(labirint[i][j]) >= 'a') and (str(labirint[i][j]) <= 'z')) or bool_doors):
                            self.lab[i][j + 1] = self.count + 1
                            flag = True

                        if (self.lab[i][j - 1] == ' ') and (
                                            (labirint[i][j] == '<') or (labirint[i][j] == ' ') or (
                                        self.lab[i][j] == 0) or ((str(labirint[i][j]) >= 'a') and (str(labirint[i][j]) <= 'z')) or bool_doors):
                            self.lab[i][j - 1] = self.count + 1
                            flag = True

                        if (self.lab[i + 1][j] == ' ') and (
                                            (labirint[i][j] == '/') or (labirint[i][j] == ' ') or (
                                        self.lab[i][j] == 0) or ((str(labirint[i][j]) >= 'a') and (str(labirint[i][j]) <= 'z')) or bool_doors):
                            self.lab[i + 1][j] = self.count + 1
                            flag = True


                        if (self.lab[i - 1][j] == ' ') and (
                                            (labirint[i][j] == '^') or (labirint[i][j] == ' ') or (
                                        self.lab[i][j] == 0) or ((str(labirint[i][j]) >= 'a') and (str(labirint[i][j]) <= 'z')) or bool_doors):
                            self.lab[i - 1][j] = self.count + 1
                            flag = True

                        if (str(self.lab[i][j + 1]) == door) and (
                                            (labirint[i][j] == '>') or (labirint[i][j] == ' ') or (
                                        self.lab[i][j] == 0) or ((str(self.lab[i][j]) >= 'a') and (str(self.lab[i][j]) <= 'z')) or bool_doors):
                            if (self.count < self.doors[self.doors.index(door) + 1]) or (
                                self.doors[self.doors.index(door) + 1] == -1):
                                self.doors[self.doors.index(door) + 1] = self.count + 1
                                flag = False

                        if (str(self.lab[i][j - 1]) == door )  and (
                                            (labirint[i][j] == '<') or (labirint[i][j] == ' ') or (
                                        self.lab[i][j] == 0) or ((str(self.lab[i][j]) >= 'a') and (str(self.lab[i][j]) <= 'z')) or bool_doors):
                            if (self.count < self.doors[self.doors.index(door) + 1]) or (
                                self.doors[self.doors.index(door) + 1] == -1):
                                self.doors[self.doors.index(door) + 1] = self.count + 1
                                flag = False

                        if (str(self.lab[i + 1][j]) == door) and (
                                            (labirint[i][j] == '/') or (labirint[i][j] == ' ') or (
                                        self.lab[i][j] == 0) or ((str(self.lab[i][j]) >= 'a') and (str(self.lab[i][j]) <= 'z')) or bool_doors):
                            if (self.count < self.doors[self.doors.index(door) + 1]) or (
                                self.doors[self.doors.index(door) + 1] == -1):
                                self.doors[self.doors.index(door) + 1] = self.count + 1
                                flag = False

                        if (str(self.lab[i - 1][j]) == door) and (
                                            (labirint[i][j] == '^') or (labirint[i][j] == ' ') or (
                                        self.lab[i][j] == 0) or ((str(self.lab[i][j]) >= 'a') and (str(self.lab[i][j]) <= 'z')) or bool_doors):
                            if (self.count < self.doors[self.doors.index(door) + 1]) or (
                                self.doors[self.doors.index(door) + 1] == -1):
                                self.doors[self.doors.index(door) + 1] = self.count + 1
                                flag = False

            self.count += 1

    def kill_key(self, key):
        for i in range(len(self.lab)):
            for j in range(len(self.lab[i])):
                if ((str(self.lab[i][j]) >= 'a') and (str(self.lab[i][j]) <= 'z')) and (str(self.lab[i][j]) != key):
                    self.lab[i][j] = ' '

    def come_back(self, labirint, st):
        key_and_door = self.keys[:]
        key_and_door.extend(self.doors)
        for lis in self.new_doors:
            key_and_door.extend(lis)

        while True:
            for i in range(len(self.lab)):
                for j in range(len(self.lab[i])):
                    if (self.lab[i][j] == self.count) or (str(self.lab[i][j]) == st):
                        if (self.lab[i][j + 1] == ' ') and (
                                (labirint[i][j + 1] == '<') or (labirint[i][j + 1] == ' ')):
                            self.lab[i][j + 1] = self.count - 1

                        if (self.lab[i][j - 1] == ' ') and (
                                (labirint[i][j - 1] == '>') or (labirint[i][j - 1] == ' ')):
                            self.lab[i][j - 1] = self.count - 1

                        if (self.lab[i + 1][j] == ' ') and (
                                (labirint[i + 1][j] == '^') or (labirint[i + 1][j] == ' ')):
                            self.lab[i + 1][j] = self.count - 1

                        if (self.lab[i - 1][j] == ' ') and (
                                (labirint[i - 1][j] == '/') or (labirint[i - 1][j] == ' ')):
                            self.lab[i - 1][j] = self.count - 1

                        try:
                            k = 0
                            bool = False
                            while k < len(key_and_door):
                                if key_and_door[k] == self.lab[i][j + 1]:
                                    bool = (key_and_door[k + 1]  == self.count - 1) or bool

                                k += 2

                        except:
                            bool = False

                        if (str(self.lab[i][j + 1]) >='A') and (str(self.lab[i][j + 1]) <= 'z') and (self.lab[i][j + 1] != st) and bool:
                            self.count -= 1
                            return (self.lab[i][j + 1], self.count)

                        try:
                            k = 0
                            bool = False
                            while k < len(key_and_door):
                                if key_and_door[k] == self.lab[i][j - 1]:
                                    bool = (key_and_door[k + 1] == self.count - 1) or bool

                                k += 2

                        except:
                            bool = False

                        if (str(self.lab[i][j - 1]) >='A') and (str(self.lab[i][j - 1]) <= 'z') and (self.lab[i][j - 1] != st) and bool:
                            self.count -= 1
                            return (self.lab[i][j - 1], self.count)

                        try:
                            bool = False
                            k = 0
                            while k < len(key_and_door):
                                if key_and_door[k] == self.lab[i + 1][j]:
                                    bool = (key_and_door[k + 1] == self.count - 1) or bool

                                k += 2

                        except:
                            bool = False

                        if (str(self.lab[i + 1][j]) >='A') and (str(self.lab[i + 1][j]) <= 'z') and (self.lab[i + 1][j] != st) and bool:
                            self.count -= 1
                            return (self.lab[i + 1][j], self.count)

                        try:
                            k = 0
                            bool = False
                            while k < len(key_and_door):
                                if key_and_door[k] == self.lab[i - 1][j]:
                                    bool = (key_and_door[k + 1] == self.count - 1) or bool

                                k += 2

                        except:
                            bool = False

                        if (str(self.lab[i - 1][j]) >='A') and (str(self.lab[i - 1][j]) <= 'z') and (self.lab[i - 1][j] != st) and bool:
                            self.count -= 1
                            return (self.lab[i - 1][j], self.count)

                    if self.count == 0:
                        return ('f', 0)

            self.count -= 1

    def paint_way(self, st, fin, count_fin, labirint):
        while self.count < count_fin:
            for i in range(len(self.lab)):
                for j in range(len(self.lab[i])):
                    if self.lab[i][j] == self.count:
                        if (self.lab[i][j + 1] == ' ') and (
                            (labirint[i][j] == '>') or (labirint[i][j] == ' ') or (self.lab[i][j] == st)):
                            self.lab[i][j + 1] = self.count + 1

                        if (self.lab[i][j - 1] == ' ') and (
                            (labirint[i][j] == '<') or (labirint[i][j] == ' ') or (self.lab[i][j] == st)):
                            self.lab[i][j - 1] = self.count + 1

                        if (self.lab[i + 1][j] == ' ') and (
                            (labirint[i][j] == '/') or (labirint[i][j] == ' ') or (self.lab[i][j] == st)):
                            self.lab[i + 1][j] = self.count + 1

                        if (self.lab[i - 1][j] == ' ') and (
                            (labirint[i][j] == '^') or (labirint[i][j] == ' ') or (self.lab[i][j] == st)):
                            self.lab[i - 1][j] = self.count + 1

            self.count += 1

        pos_fin =[]
        for i in range(len(self.lab)):
            for j in range(len(self.lab[i])):
                if str(self.lab[i][j]) == fin:
                    pos_fin.extend((i,j))

        alfabet = 'a'
        while alfabet[-1] < 'z':
            alfabet += chr(ord(alfabet[-1]) + 1)

        alfabet += 'A'
        while alfabet[-1] < 'Z':
            alfabet += chr(ord(alfabet[-1]) + 1)

        while self.count >= st:
            if (self.lab[pos_fin[0] + 1][pos_fin[1]] == self.count) and (
                            (labirint[pos_fin[0] + 1][pos_fin[1]] == '^') or (labirint[pos_fin[0] + 1][pos_fin[1]] == ' ') or (
                                str(labirint[pos_fin[0] + 1][pos_fin[1]]) in alfabet)):
                self.lab[pos_fin[0] + 1][pos_fin[1]] = '*'
                pos_fin.extend((pos_fin[0] + 1, pos_fin[1]))
                pos_fin = pos_fin[2:]

            if (self.lab[pos_fin[0] - 1][pos_fin[1]] == self.count) and (
                            (labirint[pos_fin[0] - 1][pos_fin[1]] == '/') or (labirint[pos_fin[0] - 1][pos_fin[1]] == ' ') or (
                                str(labirint[pos_fin[0] - 1][pos_fin[1]]) in alfabet)):
                self.lab[pos_fin[0] - 1][pos_fin[1]] = '*'
                pos_fin.extend((pos_fin[0] - 1, pos_fin[1]))
                pos_fin = pos_fin[2:]


            if (self.lab[pos_fin[0]][pos_fin[1] - 1] == self.count) and (
                            (labirint[pos_fin[0]][pos_fin[1] - 1] == '>') or (labirint[pos_fin[0]][pos_fin[1] - 1] == ' ') or (
                                str(labirint[pos_fin[0]][pos_fin[1] - 1]) in alfabet)):
                self.lab[pos_fin[0]][pos_fin[1] - 1] = '*'
                pos_fin.extend((pos_fin[0], pos_fin[1] - 1))
                pos_fin = pos_fin[2:]

            if (self.lab[pos_fin[0]][pos_fin[1] + 1] == self.count) and (
                            (labirint[pos_fin[0]][pos_fin[1] + 1] == '<') or (labirint[pos_fin[0]][pos_fin[1] + 1] == ' ') or (
                                str(labirint[pos_fin[0]][pos_fin[1] + 1]) in alfabet)):
                self.lab[pos_fin[0]][pos_fin[1] + 1] = '*'
                pos_fin.extend((pos_fin[0], pos_fin[1] + 1))
                pos_fin = pos_fin[2:]

            self.count -= 1

        for i in range(len(self.lab)):
            for j in range(len(self.lab[i])):
                if self.lab[i][j] != '*':
                    self.lab[i][j] = labirint[i][j]

def print_lab(labirint):
    ans = ''
    for l in labirint:
        prom = ''
        for el in l:
            prom += str(el)
        prom += '\n'
        ans += prom

    return ans

def output(nfaila, ans):
    f = open('Output/' + nfaila + '.txt', 'a')
    f.write(ans)
    f.write('\n')
    f.close()

if __name__ == '__main__':
    nfaila = sys.argv[1]
    labirint = input_dz(nfaila)
    class_labirint = Labirint(labirint)
    class_labirint.calculate_keys_way(labirint)
    class_labirint.number_del(labirint )
    class_labirint.calculate_dif_way(labirint)
    i = 0
    while i < (len(class_labirint.keys) - 2):
        class_labirint.number_del(labirint )
        if class_labirint.keys[i + 1] > 0:
            class_labirint.set_count(class_labirint.keys[i + 1])
            class_labirint.kill_key(class_labirint.keys[i])
            class_labirint.calculate_door_ways(labirint, chr(ord(class_labirint.keys[i]) + ord('A') - ord('a')),class_labirint.keys[i] )

        i += 2

    doors = class_labirint.doors[:-2]
    keys = class_labirint.keys[:-2]
    doors_1 = []
    keys_1 = []
    while ( doors != doors_1) or (keys != keys_1):
        class_labirint.number_del(labirint )
        class_labirint.calculate_keys_way(labirint)
        class_labirint.number_del(labirint )
        class_labirint.calculate_dif_way(labirint)
        i =0
        while i < (len(class_labirint.keys) - 2):
            class_labirint.number_del(labirint )
            if class_labirint.keys[i + 1] > 0:
                class_labirint.set_count(class_labirint.keys[i + 1])
                class_labirint.kill_key(class_labirint.keys[i])
                class_labirint.calculate_door_ways(labirint, chr(ord(class_labirint.keys[i]) + ord('A') - ord('a')), class_labirint.keys[i])

            i += 2
            doors_1 = doors
            keys_1 = keys
            doors = class_labirint.doors[:-2]
            keys = class_labirint.keys[:-2]

    i = 0
    while (i < (len(class_labirint.doors) - 2)):
            class_labirint.number_del(labirint )
            class_labirint.set_count(class_labirint.doors[i + 1])
            class_labirint.calculate_door_ways(labirint, 'F', 'f')
            i += 2

    class_labirint.number_del(labirint )
    class_labirint.set_count(0)
    class_labirint.calculate_door_ways(labirint, 'F', 'f')
    class_labirint.number_del(labirint )
    st = 'F'
    key_and_door = class_labirint.keys[:]
    key_and_door.extend(class_labirint.doors)
    way = ['F']
    class_labirint.set_count(key_and_door[key_and_door.index(st) + 1])
    long =[]
    while class_labirint.count != 0:
        class_labirint.number_del(labirint )
        st, count = class_labirint.come_back(labirint, st)
        way.append(st)
        long.append(count)

    way.reverse()
    long.reverse()
    long = long[1:]
    long.append(class_labirint.doors[-1])
    way[0] = '0'
    pred = 0
    f = open('Output/' + nfaila + '.txt', 'w')
    f.write('')
    f.close()
    for i in range(1,len(way)):
        class_labirint.number_del(labirint )
        class_labirint.set_count(pred)

        for k in range(len(class_labirint.lab)):
            for j in range(len(class_labirint.lab[k])):
                if class_labirint.lab[k][j] == way[i - 1]:
                    class_labirint.lab[k][j] = class_labirint.count

        class_labirint.paint_way(class_labirint.count, way[i], long[i - 1], labirint)
        pred = int(key_and_door[key_and_door.index(way[i]) + 1] - 1)
        output(nfaila, print_lab(class_labirint.lab))

    if class_labirint.doors[-1] == 0:
        output(nfaila, 'Лабиринт невозможно пройти',)