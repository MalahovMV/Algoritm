#Проверка корректности введенных данных
def TestIn(nfaila):
    file=open('Input/vhod' + nfaila + '.txt', 'r')
    s = file.readline()
    s = s[:-1]
    length = 0
    for element in s:
        length = len(s)
        if not ((element == '-') or (element == '|')):
            raise Exception('Лабиринт неограничен')

    alfabet = 'a'
    while alfabet[-1] < 'z':
        alfabet += chr(ord(alfabet[-1]) + 1)

    for letter in alfabet:
        alfabet+=(chr(ord(letter) - ord('a') + ord('A')))

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

    for element in s:
        if not ((element == '-') or (element == '|')):
            raise Exception('Лабиринт неограничен')

    file.close()

import copy
#Проверка корректности выходных данных
def TestOut(ans, labirint, start):
    for element in labirint[0]:
        if not ((element == '-') or (element == '|')):
            raise Exception('Выходной лабиринт неограничен')

    for element in labirint[-1]:
        if not ((element == '-') or (element == '|')):
            raise Exception('Выходной лабиринт неограничен')

    alfabet = 'a'
    while alfabet[-1] < 'z':
        alfabet += chr(ord(alfabet[-1]) + 1)

    for letter in alfabet:
        alfabet += (chr(ord(letter) - ord('a') + ord('A')))

    alfabet += '*'
    length = len(labirint[0])
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

    if not ans:
        currentstars = {'S' : start}
        nextstars = {}
        lab = copy.deepcopy(labirint)
        while not ('F' in currentstars):
            count = 0
            for key in currentstars.keys():
                lab[currentstars[key][1]][currentstars[key][0]] = ' '
                for i in range(3):
                    for j in range(3):
                        if lab[currentstars[key][1] + j - 1][currentstars[key][0] + i - 1] == '*':
                            nextstars['*' + str(count)] = [currentstars[key][0] + i - 1, currentstars[key][1] + j - 1]
                            count += 1

                        if lab[currentstars[key][1] + j - 1][currentstars[key][0] + i - 1] == 'F':
                            nextstars['F'] = [currentstars[key][0] + i - 1, currentstars[key][1] + j - 1]
                            count += 1

            if count == 0:
                raise Exception ('Нет пути, соединяющего старт и финиш')

            currentstars = copy.deepcopy(nextstars)
            nextstars = {}

if __name__ == '__main__':
    nfailain = input('Введите номер входного файла, который нужно проверить')
    TestIn(nfailain)
    print('Введенный файл корректен')


