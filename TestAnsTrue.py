def TestAns(nfaila):
    fileOut = open('Output/vyhod' + nfaila + '.txt', 'r')
    fileAns = open('ExpectAnsw/vyhod' + nfaila + '.txt', 'r')

    for sOut in fileOut:
        sAns = fileAns.readline()
        i = 0
        for element in sOut:
            flag = False
            if not ((element == sAns[i]) or (sAns[i] == '*')):
                flag = True

            if flag:
                raise Exception('Задача решена неверно')

            i+=1

    print ('Был получен верный результат')