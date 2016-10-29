import copy
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





