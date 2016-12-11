import sys
#Проверка корректности введенных данных
def TestIn(nfaila):
    file=open('Input/' + nfaila + '.txt', 'r')
    s = file.readline()
    s = s[:-1]
    length = 0
    #Считываем первую строчку, проверяем, что лабиринт ограничен сверху
    for element in s:
        length = len(s)
        if not ((element == '-') or (element == '|')):
            raise Exception('Лабиринт неограничен')

    #Создаем алфавит допустимых букв в лабиринте
    alfabet = 'a'
    while alfabet[-1] < 'z':
        alfabet += chr(ord(alfabet[-1]) + 1)

    for letter in alfabet:
        alfabet+=(chr(ord(letter) - ord('a') + ord('A')))

    #Проверяем допустимость символов и ограниченность лабиринта по бокам
    for s in file:
        s=s[:-1]
        if not (length == len(s)):
            raise Exception('Строки в либиринте имеют разную длину')

        if not (((s[0] == '|') or  (s[0] == '-')) and ((s[-1] == '|') or (s[-1] == '-'))) :
            raise Exception('Лабиринт неограничен')

        for element in s:
            boolean = (element == '<') or (element == '>')  or (element == '/')  or (element == '^')
            boolean = boolean or (element == ' ') or (element in alfabet)
            boolean = boolean or (element == '-') or (element == '|') or (element == '\n')
            if not boolean:
                print(element)
                raise Exception('Некорректный символ в файле')

    #Проверяем ограниченность лабиринта снизу
    for element in s:
        if not ((element == '-') or (element == '|')):
            raise Exception('Лабиринт неограничен')

    file.close()

import copy
#Проверка корректности выходных данных
def TestOut(nfaila):
    file = open('Output/' + nfaila + '.txt', 'r')
    labirint = []
    for s in file:
        if s == '\n':
            labirint = []

        else:
            s = s[:-1]
            labirint.append(list(s))
    #Проверям, считает ли программа, что из лабиринта возможен выход
    if labirint:
        start = []
        if labirint[0][1] == '-':
            ans = ''
            for l in labirint:
                try:
                    start.append(l.index(str('S')))
                    start.append(labirint.index(l))
                except:
                    pass

        else:
            ans = str(labirint[0])
            labirint = '-'

        #Проверяем ограниченность лабиринта сверху
        for element in labirint[0]:
            if not ((element == '-') or (element == '|')):
                raise Exception('Выходной лабиринт неограничен')

        #Проверяем ограниченность лабиринта снизу
        for element in labirint[-1]:
            if not ((element == '-') or (element == '|')):
                raise Exception('Выходной лабиринт неограничен')

        alfabet = 'a'
        while alfabet[-1] < 'z':
            alfabet += chr(ord(alfabet[-1]) + 1)

        for letter in alfabet:
            alfabet += (chr(ord(letter) - ord('a') + ord('A')))

        alfabet += '*#$%'
        length = len(labirint[0])
        #Проверка на ограниченность лабиринта по бокам и корректность символов внутри
        for line in labirint:
            if not (length == len(line)):
                raise Exception('Строки в либиринте имеют разную длину')

            if not (((line[0] == '|') or  (line[0] == '-')) and ((line[-1] == '|') or (line[-1] == '-'))) :
                raise Exception('Лабиринт неограничен')

            for element in line:
                boolean = (element == '<') or (element == '>')  or (element == '/')  or (element == '^')
                boolean = boolean or (element == ' ') or (element in alfabet)
                boolean = boolean or (element == '-') or (element == '|')
                if not boolean:
                    print(element)
                    raise Exception('Некорректный символ в файле')

        #Если лабиринт возможно пройти, проверяем есть ли путь, соединяющий старт и финиш
        if not ans:
            currentstars = {'S' : start}
            nextstars = {}
            alfabet = '*#$'
            lab = copy.deepcopy(labirint)
            while not ('F' in currentstars):
                count = 0
                for key in currentstars.keys():
                    lab[currentstars[key][1]][currentstars[key][0]] = ' '
                    for i in range(3):
                        for j in range(3):
                            if lab[currentstars[key][1] + j - 1][currentstars[key][0] + i - 1] in alfabet:
                                nextstars['*' + str(count)] = [currentstars[key][0] + i - 1, currentstars[key][1] + j - 1]
                                count += 1

                            if lab[currentstars[key][1] + j - 1][currentstars[key][0] + i - 1] == 'F':
                                nextstars['F'] = [currentstars[key][0] + i - 1, currentstars[key][1] + j - 1]
                                count += 1

                if count == 0:
                    raise Exception ('Нет пути, соединяющего старт и финиш')

                currentstars = copy.deepcopy(nextstars)
                nextstars = {}

#Проверка правильности ответа к тестирующему входу.
def TestAns(nfaila):
    fileOut = open('Output/' + nfaila + '.txt', 'r')
    fileAns = open('ExpectAnsw/' + nfaila + '.txt', 'r')
    #Сверяем полученный файл и ожидаемый
    for sOut in fileOut:
        sAns = fileAns.readline()
        i = 0
        for element in sOut:
            flag = False
            if not (element == sAns[i]):
                flag = True

            if flag:
                raise Exception('Задача решена неверно')

            i+=1

    print ('Был получен верный результат')

from WithDoor import Labirint
import unittest

class Labirint_Test(unittest.TestCase):
    def setUp(self):
        global all
        all = []
        for i in range(6):
            file = open('Test/' + str(i) + '.txt', 'r')
            lab = []
            for s in file:
                s = s[:-1]
                lab.append(list(s))
            file.close()
            all.append(lab)

        self.good1 = Labirint(all[0])
        self.good2 = Labirint(all[1])
        self.worst1 = Labirint(all[2])
        self.worst2 = Labirint(all[3])
        self.oi_oi_oi1 = Labirint(all[4])
        self.oi_oi_oi2 = Labirint(all[5])

    def test_init(self):
        global al
        al = []
        for i in range(6):
            file = open('Test/' + str(i) + 'lab.txt', 'r')
            lab = []
            for s in file:
                s = list(s)
                for j in range(len(s)):
                    if s[j] == '0':
                        s[j] = 0

                s = s[:-1]
                lab.append(list(s))

            file.close()
            al.append(lab)

        self.assertEqual((self.good1.count, self.good1.new_doors,
                          self.good1.keys, self.good1.doors, self.good1.lab), (0, [], ['f', 0], ['F', -1], al[0]))

        self.assertEqual((self.good2.count, self.good2.new_doors,
                          self.good2.keys, self.good2.doors, self.good2.lab), (0, [], ['f', 0], ['F', -1], al[1]))

        self.assertEqual((self.worst1.count, self.worst1.new_doors,
                          self.worst1.keys, self.worst1.doors, self.worst1.lab), (0, [], ['a', -1, 'f', 0], ['A', -1,'F', -1], al[2]))

        self.assertEqual((self.worst2.count, self.worst2.new_doors,
                          self.worst2.keys, self.worst2.doors, self.worst2.lab), (0, [], ['a', -1,'f', 0], ['A', -1,'F', -1], al[3]))

        self.assertEqual((self.oi_oi_oi1.count, self.oi_oi_oi1.new_doors,
                          self.oi_oi_oi1.keys, self.oi_oi_oi1.doors, self.oi_oi_oi1.lab), (0, [], ['a', -1, 'b', -1,'f', 0], ['B', -1, 'A',-1,'F', -1], al[4]))

        self.assertEqual((self.oi_oi_oi2.count, self.oi_oi_oi2.new_doors,
                          self.oi_oi_oi2.keys, self.oi_oi_oi2.doors, self.oi_oi_oi2.lab), (0, [], ['a', -1, 'b', -1,'f', 0], ['B', -1, 'A',-1,'F', -1], al[5]))


    def test_calculate_keys(self):
        self.good1.calculate_keys_way(all[0])
        self.assertEqual(self.good1.keys, ['f', 0])
        self.good2.calculate_keys_way(all[1])
        self.assertEqual(self.good2.keys, ['f', 0])
        self.worst1.calculate_keys_way(all[2])
        self.assertEqual(self.worst1.keys, ['a', 10, 'f', 0])
        self.worst2.calculate_keys_way(all[3])
        self.assertEqual(self.worst2.keys, ['a', 16, 'f', 0])
        self.oi_oi_oi1.calculate_keys_way(all[4])
        self.assertEqual(self.oi_oi_oi1.keys, ['a', 10, 'b', 15,'f', 0])
        self.oi_oi_oi2.calculate_keys_way(all[5])
        self.assertEqual(self.oi_oi_oi2.keys, ['a', 16, 'b', 24, 'f', 0])

    def test_number_del(self):
        self.good1.number_del(all[0])
        self.assertEqual(self.good1.lab, al[0])
        self.good2.number_del(all[1])
        self.assertEqual(self.good2.lab, al[1])
        self.worst1.number_del(all[2])
        self.assertEqual(self.worst1.lab, al[2])
        self.worst2.number_del(all[3])
        self.assertEqual(self.worst2.lab, al[3])
        self.oi_oi_oi1.number_del(all[4])
        self.assertEqual(self.oi_oi_oi1.lab, al[4])
        self.oi_oi_oi2.number_del(all[5])
        self.assertEqual(self.oi_oi_oi2.lab, al[5])

    def test_set_count(self):
        self.good1.set_count(131)
        self.assertEqual(self.good1.count, 131)
        self.worst2.set_count(-76)
        self.assertEqual(self.worst2.count, -76)

    def test_dif_way(self):
        self.good1.calculate_keys_way(all[0])
        self.good1.number_del(all[0])
        self.good1.calculate_dif_way(all[0])
        self.assertEqual(self.good1.new_doors, [])
        self.worst1.calculate_keys_way(all[2])
        self.worst1.number_del(all[2])
        self.worst1.calculate_dif_way(all[2])
        self.assertEqual(self.worst1.new_doors, [['a', 10, 'A', 22]])
        self.worst2.calculate_keys_way(all[3])
        self.worst2.number_del(all[3])
        self.worst2.calculate_dif_way(all[3])
        self.assertEqual(self.worst2.new_doors, [['a', 16, 'A', 37]])
        self.oi_oi_oi1.calculate_keys_way(all[4])
        self.oi_oi_oi1.number_del(all[4])
        self.oi_oi_oi1.calculate_dif_way(all[4])
        self.assertEqual(self.oi_oi_oi1.new_doors,
                         [['a', 10, 'B', 47, 'a', 36, 'A', 19], ['b', 15, 'B', 35, 'A', 37, 'b', 31]])
        self.oi_oi_oi2.calculate_keys_way(all[5])
        self.oi_oi_oi2.number_del(all[5])
        self.oi_oi_oi2.calculate_dif_way(all[5])
        self.assertEqual(self.oi_oi_oi2.new_doors,
                         [['a', 16, 'B', -1, 'a', 44, 'A', 30], ['b', 24, 'B', -1, 'A', 44, 'b', 36]])

    def test_kill_key(self):
        global kil
        kil = []
        for i in ['2', '3', '4', '5']:
            file = open('Test/' + str(i) + 'kil.txt', 'r')
            lab = []
            for s in file:
                s = list(s)
                for j in range(len(s)):
                    if s[j] == '0':
                        s[j] = 0

                s = s[:-1]
                lab.append(list(s))

            file.close()
            kil.append(lab)

        self.worst1.kill_key('a')
        self.assertEqual(self.worst1.lab, kil[0])
        self.oi_oi_oi1.kill_key('a')
        self.assertEqual(self.oi_oi_oi1.lab, kil[2])
        self.oi_oi_oi2.kill_key('b')
        self.assertEqual(self.oi_oi_oi2.lab, kil[3])

    def test_door_way(self):
        self.good1.calculate_keys_way(all[0])
        self.good1.number_del(all[0])
        self.good1.calculate_dif_way(all[0])
        self.good1.number_del(all[0])
        self.good1.set_count(0)
        self.good1.kill_key('f')
        self.good1.calculate_door_ways(all[0], 'F', 'f')
        self.assertEqual(self.good1.doors, ['F', 39])
        self.good2.calculate_keys_way(all[1])
        self.good2.number_del(all[1])
        self.good2.calculate_dif_way(all[1])
        self.good2.number_del(all[1])
        self.good2.set_count(0)
        self.good2.kill_key('f')
        self.good2.calculate_door_ways(all[1], 'F', 'f')
        self.assertEqual(self.good2.doors, ['F', 54])
        self.worst1.calculate_keys_way(all[2])
        self.worst1.number_del(all[2])
        self.worst1.calculate_dif_way(all[2])
        self.worst1.number_del(all[2])
        self.worst1.set_count(10)
        self.worst1.kill_key('a')
        self.worst1.calculate_door_ways(all[2], 'A', 'a')
        self.assertEqual(self.worst1.doors, ['A', 22, 'F', -1])
        self.worst1.number_del(all[2])
        self.worst1.calculate_dif_way(all[2])
        self.worst1.number_del(all[2])
        self.worst1.set_count(0)
        self.worst1.kill_key('f')
        self.worst1.calculate_door_ways(all[2], 'F', 'f')
        self.assertEqual(self.worst1.doors, ['A', 22, 'F', 31])
        self.worst2.calculate_keys_way(all[3])
        self.worst2.number_del(all[3])
        self.worst2.calculate_dif_way(all[3])
        self.worst2.number_del(all[3])
        self.worst2.set_count(16)
        self.worst2.kill_key('a')
        self.worst2.calculate_door_ways(all[3], 'A', 'a')
        self.assertEqual(self.worst2.doors, ['A', 37, 'F', -1])
        self.oi_oi_oi1.calculate_keys_way(all[4])
        self.oi_oi_oi1.number_del(all[4])
        self.oi_oi_oi1.calculate_dif_way(all[4])
        self.oi_oi_oi1.number_del(all[4])
        self.oi_oi_oi1.set_count(10)
        self.oi_oi_oi1.kill_key('a')
        self.oi_oi_oi1.calculate_door_ways(all[4], 'A', 'a')
        self.assertEqual(self.oi_oi_oi1.doors, ['B', -1, 'A', 19, 'F', -1])
        self.oi_oi_oi2.calculate_keys_way(all[5])
        self.oi_oi_oi2.number_del(all[5])
        self.oi_oi_oi2.calculate_dif_way(all[5])
        self.oi_oi_oi2.number_del(all[5])
        self.oi_oi_oi2.set_count(24)
        self.oi_oi_oi2.kill_key('b')
        self.oi_oi_oi2.calculate_door_ways(all[5], 'B', 'b')
        self.assertEqual(self.oi_oi_oi2.doors, ['B', 47, 'A', -1, 'F', -1])
        self.oi_oi_oi2.number_del(all[5])
        self.oi_oi_oi2.calculate_dif_way(all[5])
        self.oi_oi_oi2.number_del(all[5])
        self.oi_oi_oi2.set_count(16)
        self.oi_oi_oi2.kill_key('a')
        self.oi_oi_oi2.calculate_door_ways(all[5], 'A', 'a')
        self.assertEqual(self.oi_oi_oi2.doors, ['B', 47, 'A', 30, 'F', -1])
        self.oi_oi_oi2.number_del(all[5])
        self.oi_oi_oi2.calculate_dif_way(all[5])
        self.oi_oi_oi2.number_del(all[5])
        self.oi_oi_oi2.set_count(0)
        self.oi_oi_oi2.kill_key('f')
        self.oi_oi_oi2.calculate_door_ways(all[5], 'F', 'f')
        self.assertEqual(self.oi_oi_oi2.doors, ['B', 47, 'A', 30, 'F', 50])

    def test_come_back(self):
        self.good1.calculate_keys_way(all[0])
        self.good1.number_del(all[0])
        self.good1.calculate_dif_way(all[0])
        self.good1.number_del(all[0])
        self.good1.set_count(0)
        self.good1.kill_key('f')
        self.good1.calculate_door_ways(all[0], 'F', 'f')
        self.good1.number_del(all[0])
        self.good1.set_count(39)
        self.assertEqual(self.good1.come_back(all[0],'F'), ('f',0))
        #Протестировал еще сложный вариант, чтобы все не копировать
        self.oi_oi_oi2.calculate_keys_way(all[5])
        self.oi_oi_oi2.number_del(all[5])
        self.oi_oi_oi2.calculate_dif_way(all[5])
        self.oi_oi_oi2.number_del(all[5])
        self.oi_oi_oi2.set_count(24)
        self.oi_oi_oi2.kill_key('b')
        self.oi_oi_oi2.calculate_door_ways(all[5], 'B', 'b')
        self.oi_oi_oi2.number_del(all[5])
        self.oi_oi_oi2.calculate_dif_way(all[5])
        self.oi_oi_oi2.number_del(all[5])
        self.oi_oi_oi2.set_count(16)
        self.oi_oi_oi2.kill_key('a')
        self.oi_oi_oi2.calculate_door_ways(all[5], 'A', 'a')
        self.oi_oi_oi2.number_del(all[5])
        self.oi_oi_oi2.calculate_dif_way(all[5])
        self.oi_oi_oi2.number_del(all[5])
        self.oi_oi_oi2.set_count(0)
        self.oi_oi_oi2.kill_key('f')
        self.oi_oi_oi2.calculate_door_ways(all[5], 'F', 'f')
        self.oi_oi_oi2.number_del(all[5])
        self.oi_oi_oi2.set_count(50)
        self.assertEqual(self.oi_oi_oi2.come_back(all[5], 'F'), ('B', 47))
        self.oi_oi_oi2.number_del(all[5])
        self.oi_oi_oi2.set_count(47)
        self.assertEqual(self.oi_oi_oi2.come_back(all[5], 'B'), ('A', 44))
        self.oi_oi_oi2.number_del(all[5])
        self.oi_oi_oi2.set_count(44)
        self.assertEqual(self.oi_oi_oi2.come_back(all[5], 'A'), ('b', 36))
        self.oi_oi_oi2.number_del(all[5])
        self.oi_oi_oi2.set_count(36)
        self.assertEqual(self.oi_oi_oi2.come_back(all[5], 'b'), ('a', 16))
        self.oi_oi_oi2.number_del(all[5])
        self.oi_oi_oi2.set_count(16)
        self.assertEqual(self.oi_oi_oi2.come_back(all[5], 'a'), ('f', 0))

    def test_paint_way(self):
        ans = []
        for i in ['0', '5', '51', '52', '53', '54']:
            file = open('Test/' + str(i) + 'ans.txt', 'r')
            lab = []
            for s in file:
                s = list(s)
                s = s[:-1]
                lab.append(list(s))

            file.close()
            ans.append(lab)

        self.good1.paint_way(0,'F', 39, all[0])
        self.assertEqual(self.good1.lab, ans[0])
        self.oi_oi_oi2.paint_way(0, 'a', 16, all[5])
        self.assertEqual(self.oi_oi_oi2.lab, ans[1])
        self.oi_oi_oi2.number_del(all[5])
        for k in range(len(self.oi_oi_oi2.lab)):
            for j in range(len(self.oi_oi_oi2.lab[k])):
                if self.oi_oi_oi2.lab[k][j] == 'a':
                    self.oi_oi_oi2.lab[k][j] = 16

        self.oi_oi_oi2.set_count(16)
        self.oi_oi_oi2.paint_way(16, 'b', 36, all[5])
        self.assertEqual(self.oi_oi_oi2.lab, ans[2])
        self.oi_oi_oi2.number_del(all[5])
        for k in range(len(self.oi_oi_oi2.lab)):
            for j in range(len(self.oi_oi_oi2.lab[k])):
                if self.oi_oi_oi2.lab[k][j] == 'b':
                    self.oi_oi_oi2.lab[k][j] = 36

        self.oi_oi_oi2.set_count(36)
        self.oi_oi_oi2.paint_way(36, 'A', 44, all[5])
        self.assertEqual(self.oi_oi_oi2.lab, ans[3])

        self.oi_oi_oi2.number_del(all[5])
        for k in range(len(self.oi_oi_oi2.lab)):
            for j in range(len(self.oi_oi_oi2.lab[k])):
                if self.oi_oi_oi2.lab[k][j] == 'A':
                    self.oi_oi_oi2.lab[k][j] = 44

        self.oi_oi_oi2.set_count(44)
        self.oi_oi_oi2.paint_way(44, 'B', 47, all[5])
        self.assertEqual(self.oi_oi_oi2.lab, ans[4])

        self.oi_oi_oi2.number_del(all[5])
        for k in range(len(self.oi_oi_oi2.lab)):
            for j in range(len(self.oi_oi_oi2.lab[k])):
                if self.oi_oi_oi2.lab[k][j] == 'B':
                    self.oi_oi_oi2.lab[k][j] = 47

        self.oi_oi_oi2.set_count(47)
        self.oi_oi_oi2.paint_way(47, 'F', 50, all[5])
        self.assertEqual(self.oi_oi_oi2.lab, ans[5])


if __name__ == '__main__':
    try:
        param1 = sys.argv[1]
        param2 = sys.argv[2]

    except:
        param1 = param2 =''
        unittest.main()

    if param1 == 'i':
        TestIn(param2)
        print('Ok')

    elif param1 == 'o':
        TestOut(param2)
        print('Ok')

    elif param1 == 'ans':
        TestAns(param2)





