#Проверка корректности введенных данных
def Test(nfaila):
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




