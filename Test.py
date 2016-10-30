#Проверка корректности введенных данных
def TestIn(nfaila):
    file=open('Input/vhod' + nfaila + '.txt', 'r')
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
    file = open('Output/vyhod' + nfaila + '.txt', 'r')
    labirint = []
    for s in file:
        s = s[:-1]
        labirint.append(list(s))
    file.close()
    #Проверям, считает ли программа, что из лабиринта возможен выход
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
        labirint = labirint[1 : ]

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
    fileOut = open('Output/vyhod' + nfaila + '.txt', 'r')
    fileAns = open('ExpectAnsw/vyhod' + nfaila + '.txt', 'r')
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

nfaila = input('Введите номер проверочного файла')
TestAns(nfaila)

if __name__ == '__main__':
    change = input('''Введите 0, если хотите проверить корректность входного файла,
                   введите 1, если хотите проверить корректность выходного файла''')
    if int(change):
        nfaila = input('Введите номер  файла, который нужно проверить')
        TestOut(nfaila)
        print('Введенный файл корректен')

    else:
        nfaila = input('Введите номер  файла, который нужно проверить')
        TestIn(nfaila)
        print('Введенный файл корректен')
	TestAns(nfaila)


