# < - only left, > - only right, ^ - only app, / - only down

class Labirint:
    def __init__(self):
        self.count = 0

    def calculate_start_and_finish(self, st, fin):
        self.finish = []
        self.start = []
        for l in labirint:
            try:
                self.start.append(l.index(str(st)))
                self.start.append(labirint.index(l))
            except:
                pass

            try:
                self.finish.append(l.index(str(fin)))
                self.finish.append(labirint.index(l))
            except:
                pass

    def transform_labirint(self):
        self.lab = []
        for line in labirint:
            l = line[:]
            for element in l:
                if (element == '<') or (element == '>') or (element == '^') or (element == '/'):
                    l[l.index(element)] = ' '
                if element == 'S':
                    l[l.index(element)] = 0

            self.lab.append(l)

    def withoutways(self):
        flag = 0
        for i in range(len(self.lab)):
            for j in range(len(self.lab[i])):
                if self.lab[i][j] == self.count:
                    if (self.lab[i][j + 1] == ' ') and (
                            (labirint[i][j] == '>') or (labirint[i][j] == ' ') or (self.lab[i][j] == 0)):
                        flag += 1
                    if (self.lab[i][j - 1] == ' ') and (
                            (labirint[i][j] == '<') or (labirint[i][j] == ' ') or (self.lab[i][j] == 0)):
                        flag += 1
                    if (self.lab[i + 1][j] == ' ') and (
                            (labirint[i][j] == '/') or (labirint[i][j] == ' ') or (self.lab[i][j] == 0)):
                        flag += 1
                    if (self.lab[i - 1][j] == ' ') and (
                            (labirint[i][j] == '^') or (labirint[i][j] == ' ') or (self.lab[i][j] == 0)):
                        flag += 1

        return bool(flag)

    def wave(self):
        for i in range(len(self.lab)):
            for j in range(len(self.lab[i])):
                if self.lab[i][j] == self.count:
                    if (self.lab[i][j + 1] == ' ') and (
                            (labirint[i][j] == '>') or (labirint[i][j] == ' ') or (self.lab[i][j] == 0)):
                        self.lab[i][j + 1] = self.count + 1
                    if (self.lab[i][j - 1] == ' ') and (
                            (labirint[i][j] == '<') or (labirint[i][j] == ' ') or (self.lab[i][j] == 0)):
                        self.lab[i][j - 1] = self.count + 1
                    if (self.lab[i + 1][j] == ' ') and (
                            (labirint[i][j] == '/') or (labirint[i][j] == ' ') or (self.lab[i][j] == 0)):
                        self.lab[i + 1][j] = self.count + 1
                    if (self.lab[i - 1][j] == ' ') and (
                            (labirint[i][j] == '^') or (labirint[i][j] == ' ') or (self.lab[i][j] == 0)):
                        self.lab[i - 1][j] = self.count + 1
        self.count += 1

    def theend(self):
        boolean = (self.lab[self.finish[-1]][self.finish[-2] + 1] == self.count)
        boolean = boolean or (self.lab[self.finish[-1]][self.finish[-2] - 1] == self.count)
        boolean = boolean or (self.lab[self.finish[-1] + 1][self.finish[-2]] == self.count)
        boolean = boolean or (self.lab[self.finish[-1] - 1][self.finish[-2]] == self.count)
        return boolean

    def comeback(self, pos):
        self.count -= 1
        mark = '*'
        if not self.count: mark = 'S'
        for i in range(3):
            for j in range(3):
                if self.lab[pos[-1] + i - 1][pos[-2] + j - 1] == self.count:
                    self.lab[pos[-1] + i - 1][pos[-2] + j - 1] = mark
                    pos[-1] = pos[-1] + i - 1
                    pos[-2] = pos[-2] + j - 1
                    return  pos

    def numberdel(self):
        for i in range(len(self.lab)):
            for j in range(len(self.lab[i])):
                if self.lab[i][j] == '*':
                    labirint[i][j] = '*'

    def findkeys(self):
        alfabet = 'a'
        while alfabet[-1] < 'z':
            alfabet += chr(ord(alfabet[-1]) + 1)

        self.keys=[]
        for line in labirint:
            for element in line:
                if element in alfabet:
                    self.keys.append(element)

    def opendoor(self):
        alfabet = 'A'
        while alfabet[-1] < 'Z':
            alfabet += chr(ord(alfabet[-1]) + 1)
        self.findkeys()
        for key in self.keys:
            self.count = 0
            flag = 1
            door = chr(ord(key) - ord('a') + ord('A'))
            #Keys
            self.calculate_start_and_finish('S', key)
            labyritnh.transform_labirint()
            boolean = self.theend()
            ans = ''
            while not boolean:
                if not self.withoutways():
                    flag =0
                    break

                self.wave()
                boolean = self.theend()

            if flag:
                waytokey = self.count + 1
                self.count = 0
            print (waytokey, key, door, self.count)
            labyritnh.transform_labirint()
            # Door
            self.calculate_start_and_finish(key, door)
            boolean = self.theend()
            ans = ''
            while not boolean:
                if not self.withoutways():
                    flag = 0

                    break
                for l in self.lab:
                    prom = ''
                    for el in l:
                        prom += str(el)
                    prom += '\n'
                    ans += prom

                print(ans)
                self.wave()
                boolean = self.theend()
            print(self.count)
            if flag:
                self.lab[self.finish[-1]][self.finish[-2]] = self.count + waytokey

            for l in self.lab:
                prom = ''
                for el in l:
                    prom += str(el)
                prom += '\n'
                ans += prom

            print(ans)
            labyritnh.transform_labirint()
#Проверка на корректность входных данных
from TestInput_Output import TestIn
nfaila = input('Введите номер входного файла')
TestIn(nfaila)
#Начало работы алгоритма
file=open('Input/vhod' + nfaila + '.txt', 'r')
labirint=[]
for s in file:
    s=s[:-1]
    labirint.append(list(s))
file.close()
labyritnh = Labirint()
#labyritnh.opendoor()
labyritnh.calculate_start_and_finish('S', 'F')
labyritnh.transform_labirint()
boolean = labyritnh.theend()
ans = ''
while not boolean:
    if not labyritnh.withoutways():
        print ('Лабиринт невозможно пройти')
        ans+='Лабиринт невозможно пройти\n'
        break


    labyritnh.wave()
    boolean = labyritnh.theend()

pos=[]
for l in labyritnh.lab:
    if 'F' in l:
        coor1 = l.index('F')
        coor2 = labyritnh.lab.index(l)
        for x in range(-1, 2):
            for y in range(-1, 2):

                if ( not pos) and (labyritnh.lab[coor2 + y][coor1 + x] == labyritnh.count):
                    pos.extend((coor1 + x, coor2 + y))

if pos:
    labyritnh.lab[pos[-1]][pos[-2]] = '*'
    while labyritnh.count - 1:
        if pos:
            pos=labyritnh.comeback(pos)
        else: break

labyritnh.numberdel()
#Проверка на то, что в файл записывается корректный лабиринт
from TestInput_Output import TestOut
TestOut(ans, labirint, labyritnh.start)
#Запись в файл
for l in labirint:
    prom = ''
    for el in l:
        prom += str(el)
    prom += '\n'
    ans += prom

file=open('Output/vyhod' + nfaila + '.txt', 'w')
file.write(ans)
file.close()

