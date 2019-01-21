#-*-coding:utf8-*-
import os
import json


if  os.name == 'nt':
    from pathlib import Path

    home = str(Path.home())


# linux ise dosya yolu değişecek
if os.name == 'posix':
    from pathlib import Path

    home = str(Path.home())


filename = home+"/telbook/telnum2.trj"


def isles(index,kisikart):
    import job4
    with open(filename, 'r') as f:
        array1 = json.load(f)

    len1 = len(array1)
    if int(index) < 0 :
        index = str(len1)
        kisikart['tel1'] = ''
        kisikart['isim1'] = '**yeni**'
        kisikart['aciklama1'] = ''
        kisikart['mail1'] = ''
        kisikart['faks1'] = ''
        kisikart['adres1'] = ''
        kisikart['tel2'] = ''
        kisikart['cep1'] = ''
        kisikart['tel3'] = ''
        kisikart['diger1'] = ''
        kisikart['ilgili1'] = ''
        kisikart['time'] = job4.timepul()
        kisikart['user'] = '-1'

    array1[index] = kisikart

    with open(filename, 'w') as file:
        file.write(json.dumps(array1))

    return index



if __name__ == '__main__':
    index = '-1'
    # kisikart = {}
    # print(isles(index, kisikart))

