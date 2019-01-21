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

# telnum.trb dosyası ve içinde olduğu klasör kontrol ediliyor
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
if not os.path.isfile(filename):
    try:
        index = str(0)
        kisikart = {}
        array1 = {}
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
        kisikart['time'] = '190117.0001'
        kisikart['user'] = '-1'

        array1[index] = kisikart
        with open(filename, "w") as f:

            f.write(json.dumps(array1))

            print(filename + ' dosyası oluştu.')
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise





def index_containing_substring(the_list, substring):
    lines = []
    idx = -1
    for i, s in enumerate(the_list):
        if substring in s.lower():
            if (i//11) > idx :
                idx = i//11

                lines.append(idx)


    return lines

def search(values, searchFor):
    sub = searchFor.lower()
    array2 = {}
    idx = -1
    lenk = len(values)
    lenks2 = '-1'

    for k in values:
        lenks = str(lenk-int(k)-1)
        array3 = values[lenks]

        # lenks ile tersten okumaya başlıyoruz
        for v in values[lenks]:
            y = values[lenks][v]
            if sub in y.lower():
                # lenks2 ile tekrar ekleme yapmasını engelliyoruz
                if lenks2 != lenks:
                    lenks2 = lenks
                    idx = idx + 1
                    arrayx = {}
                    arrayx['isim1'] = array3['isim1']
                    arrayx['kno'] = lenks
                    array2[idx] = arrayx


    return array2


def isimdenara(ad):
    with open(filename, 'r') as f:
        array1 = json.load(f)

    array2 = search(array1,ad)


    return array2


def idnodanara(index):
    with open(filename, 'r') as f:
        array1 = json.load(f)

    array3 = array1[index]
    lenks = str(len(array1))


    return array3, lenks



if __name__ == '__main__':
    array2 =isimdenara('YE')
    print(array2)
    print('-------------------------------')
    array3, lenks = idnodanara('0')
    print(array3, lenks)