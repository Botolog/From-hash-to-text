#HAX#
print('importing... wait a moment')
import time
import datetime
import itertools
import hashlib
import winsound
print("imported")
i = 1
c = 0
r = 0
LST = []
ANS = {}
stop = 0
D = []

num = int(input('how many hashes you want to crack: '))
print('suported types: md5, sha1, sha224, sha256, sha384, sha512')
for i in range(num):
    PH = input('Enter hash: ')
    if PH == '':
        break
    RB = open("Rainbow.txt", "r")
    RB = RB.read()
    if PH in RB:
        input('##########Pleas check the Rainbow.txt file##########')
        num = num - 1
        continue
    LST.append(PH)
    if len(PH) == 32:
        hashlib.e = hashlib.md5
    elif len(PH) == 64:
        hashlib.e = hashlib.sha256
    elif len(PH) == 40:
        hashlib.e = hashlib.sha1
    elif len(PH) == 56:
        hashlib.e = hashlib.sha224
    elif len(PH) == 96:
        hashlib.e = hashlib.sha384
    elif len(PH) == 128:
        hashlib.e = hashlib.sha512
    else:
        print('check you are copied all the symboles and this hash suported')
        quit()

OP = int(input('crack by word generator(1) or by file(2)?: '))

if OP == 1:
    T = input('nums(1), letters(2), nums and letters(3) or costume(Write here)?: ')
    if T == '1':
        All = "0123456789-_ "
    elif T == '2':
        All = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_ "
    elif T == '3':
        All = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_ "
    else:
        All = T
        
    i = input('start from: ')
    try:
        i = int(i)
    except:
        i = 1
        
    T1 = time.time()
    while True:            

        for subset in itertools.product(All, repeat=i):
            if stop == num:
                
                break
            Subset = ''.join(subset)
            digest = hashlib.e((Subset.encode('utf-8')).strip()).hexdigest()
            for q in range(len(LST)):
                if digest == LST[q]:
                    print(f'{digest}: {Subset}')
                    D.append(digest)
                    ANS[digest] = Subset
                    winsound.PlaySound('win-1', winsound.SND_FILENAME)
                    stop = stop + 1
                    if stop == num:
                        
                        break
                
                c = c + 1
        if stop == num:
            
            break
            
        
        winsound.Beep(1000, 100)
        print(f'Length of the password is more than {i}...')
        i = i + 1
        
    T2 = time.time()
    Atime = T2-T1
    rem = int(Atime)
    hours = int(rem / 3600)
    mins = int((rem % 3600) / 60)
    secs = rem % 60
    if hours > 0:
        Atime = '%d:%d:%d' % (hours, mins, secs)
        M = 'hours'
    elif mins > 0:
        if mins < 10:
            if secs < 10:
                Atime =  '0%d:0%d' % (mins, secs)
            else:
                Atime =  '0%d:%d' % (mins, secs)
        else:
            if secs < 10:
                Atime =  '%d:0%d' % (mins, secs)
            else:
                Atime =  '%d:%d' % (mins, secs)
        M = 'minutes'
    else:
        Atime = '%d' % secs
        M = 'seconds'
        
    print(f'{c} possible passwords was checked in {Atime} {M}')

    for j in range(len(LST)):
        word = ANS[D[j]]
        digest = D[j]
        i = 20 - len(word)
        for i in range(i):
            word = word + ' '
        f = open("Rainbow.txt", "a")
        f.write(f'{word}|{digest}\n')
        f.close()

elif OP == 2:
    File = input('File Name: ')
    try:
        PF = open (File, "r", encoding='utf-8')
    except:
        print('there is no file with this name\nmake sure the file is in the same folder of the code\n\nusing rockyou...')
        quit()

    T1 = time.time()
    print('starting...')
    winsound.Beep(1000, 100)
    G = 0
    for word in PF:
        c = c + 1
        Word = word[0:-1]
        enc_wrd = Word.encode('ANSI')
        digest = hashlib.e(enc_wrd.strip()).hexdigest()
        for q in range(len(LST)):
                if digest == LST[q]:
                    print(f'{digest}: {word}', end = '')
                    ANS[digest] = word
                    winsound.PlaySound('win-1', winsound.SND_FILENAME)
                    G += 1
                    if G == len(LST):
                        stop = True
                        break
        if stop:
            break

        i = i + 1
    T2 = time.time()
    if word == '~~~':
        word = None
        
    Atime = T2-T1
    rem = int(Atime)
    hours = int(rem / 3600)
    mins = int((rem % 3600) / 60)
    secs = rem % 60
    if hours > 0:
        Atime = '%d:%d:%d' % (hours, mins, secs)
        M = 'hours'
    elif mins > 0:
        if mins < 10:
            if secs < 10:
                Atime =  '0%d:0%d' % (mins, secs)
            else:
                Atime =  '0%d:%d' % (mins, secs)
        else:
            if secs < 10:
                Atime =  '%d:0%d' % (mins, secs)
            else:
                Atime =  '%d:%d' % (mins, secs)
        M = 'minutes'
    else:
        Atime = '%d' % secs
        M = 'seconds'
        
    print(f'{c} possible passwords was checked in {Atime} {M}')
    for j in range(len(LST)):
        word = ANS[digest][0:-1]
        i = 20 - len(word)
        for i in range(i):
            word = word + ' '
        f = open("Rainbow.txt", "a")
        f.write(f'{word}|{digest}\n')
        f.close()
input('press Enter to continue')


