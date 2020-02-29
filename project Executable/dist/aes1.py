#path = 'D:/FORM - Copy/abc.txt'
#im_file = open(path,'r')
#for ch in im_file:
#    ch1  = ch.read(8)
#    print(ch1)

a = [['ba','84','e8','1b'],['75','a4','8d','40'],['f4','8d','6','7d'],['7a','32','e','5d']]
key = [['01','00','00','00'],['00','01','00','00'],['00','00','01','00'],['00','00','00','01']]

s_box = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'], ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'], ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'], ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'], ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'], ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'], ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'], ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'], ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'], ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'], ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'], ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'], ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'], ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'], ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'], ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]

def add_round_key():
    global a, key, s_box
    w, h = 4, 4;
    c = [[0 for x in range(w)] for y in range(h)]

    for i in range(0,4):
        for j in range(0,4):
            c[i][j] = int(a[i][j], 16) ^ int(key[i][j], 16)
    a = c

def substitution_box():
    global a, key, s_box
    for i in range(4):
        for j in range(4):

            l = list(a[i][j])
            if l[0]=='a':
            	l[0]=10
            if l[1]=='a':
            	l[1]=10
            if l[0]=='b':
            	l[0]=11
            if l[1]=='b':
            	l[1]=11
            if l[0]=='c':
            	l[0]=12
            if l[1]=='c':
            	l[1]=12
            if l[0]=='d':
            	l[0]=13
            if l[1]=='d':
            	l[1]=13
            if l[0]=='e':
            	l[0]=14
            if l[1]=='e':
            	l[1]=14
            if l[0]=='f':
            	l[0]=15
            if l[1]=='f':
            	l[1]=15

            a[i][j]=s_box[int(l[0])][int(l[1])]


def shift_rows():
    global a, key, s_box
    x = a[1][0]
    x1 = a[2][0]
    x2 = a[2][1]
    x3 = a[3][3]
    for i in range(1,4):
        for j in range(0,3):
            if i == 1 and j < 3:
                a[i][j] = a[i][j+1]

            if i == 2 and j < 2:
                a[i][j] = a[i][j+2]

        for j in reversed(range(0,4)):
            if i == 3 and j>0:
                a[i][j] = a[i][j-1]

    a[1][3] = x
    a[2][2] = x1
    a[2][3] = x2
    a[3][0] = x3


def mix_column():
    global a, key, s_box
    func = [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
    my_list = []
    # Final array
    w, h = 4, 4;
    op = [[0 for x in range(w)] for y in range(h)]

    for k in range(0,4):
        for i in range(0,4):
            for j in range(0,4):
                x = int(a[j][k], 16)
                print('a',a[j][k], bin(x))
                if func[i][j] == 3:
                    y = x*2
                    print('b',bin(x))
                    x = y ^ x
                    if x > 511:
                        x = x - 512
                    if x > 255:
                        x = x - 256
                        x = x ^ 27
                    #x = '{0:b}'.format(y)
                    print('c',bin(x))
                else:
                    x = x* func[i][j]
                    if x > 511:
                        x = x - 512
                    if x > 255:
                        x = x - 256
                        x = x ^ 27

                    print(bin(x))
                my_list.append(x)
            for l in range(0,3):
                my_list[l+1] = my_list[l] ^ my_list[l+1]
            print(hex(my_list[3])[2:])
            op[i][k] = hex(my_list[3])[2:]
            my_list = []
    a = op

def encrypt():
    add_round_key()
    for i in range(0, 9):
        substitution_box()
        shift_rows()
        mix_column()
        add_round_key()
    substitution_box()
    shift_rows()
    mix_column()

encrypt()

def show_output():
    for i in range(0,4):
        for j in range(0,4):
            print(a[i][j], end=",")
        print("\n")
