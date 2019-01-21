import json
import trjara


def tolist(array2):
    lines3 = []
    for k in array2:
        lines3.append(array2[k]['isim1'])



    return lines3



def timepul():
    import time
    ts = time.time()
    import datetime
    tpul = datetime.datetime.fromtimestamp(ts).strftime('%y%m%d.%H%M%S')

    return tpul



if __name__ == '__main__':

    tpul = timepul()
    print(tpul)
