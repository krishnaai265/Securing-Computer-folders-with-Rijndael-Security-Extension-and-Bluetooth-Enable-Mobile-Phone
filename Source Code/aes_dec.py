a = [['ba','84','e8','1b'],['75','a4','8d','40'],['f4','8d','6','7d'],['7a','32','e','5d']]
key = [['01','00','00','00'],['00','01','00','00'],['00','00','01','00'],['00','00','00','01']]

inv_s_box = [['52', '09', '6a', 'd5', '30', '36', 'a5', '38', 'bf', '40', 'a3', '9e', '81', 'f3', 'd7', 'fb'], ['7c', 'e3', '39', '82', '9b', '2f', 'ff', '87', '34', '8e', '43', '44', 'c4', 'de', 'e9', 'cb'], ['54', '7b', '94', '32', 'a6', 'c2', '23', '3d', 'ee', '4c', '95', '0b', '42', 'fa', 'c3', '4e'], ['08', '2e', 'a1', '66', '28', 'd9', '24', 'b2', '76', '5b', 'a2', '49', '6d', '8b', 'd1', '25'], ['72', 'f8', 'f6', '64', '86', '68', '98', '16', 'd4', 'a4', '5c', 'cc', '5d', '65', 'b6', '92'], ['6c', '70', '48', '50', 'fd', 'ed', 'b9', 'da', '5e', '15', '46', '57', 'a7', '8d', '9d', '84'], ['90', 'd8', 'ab', '00', '8c', 'bc', 'd3', '0a', 'f7', 'e4', '58', '05', 'b8', 'b3', '45', '06'], ['d0', '2c', '1e', '8f', 'ca', '3f', '0f', '02', 'c1', 'af', 'bd', '03', '01', '13', '8a', '6b'], ['3a', '91', '11', '41', '4f', '67', 'dc', 'ea', '97', 'f2', 'cf', 'ce', 'f0', 'b4', 'e6', '73'], ['96', 'ac', '74', '22', 'e7', 'ad', '35', '85', 'e2', 'f9', '37', 'e8', '1c', '75', 'df', '6e'], ['47', 'f1', '1a', '71', '1d', '29', 'c5', '89', '6f', 'b7', '62', '0e', 'aa', '18', 'be', '1b'], ['fc', '56', '3e', '4b', 'c6', 'd2', '79', '20', '9a', 'db', 'c0', 'fe', '78', 'cd', '5a', 'f4'], ['1f', 'dd', 'a8', '33', '88', '07', 'c7', '31', 'b1', '12', '10', '59', '27', '80', 'ec', '5f'], ['60', '51', '7f', 'a9', '19', 'b5', '4a', '0d', '2d', 'e5', '7a', '9f', '93', 'c9', '9c', 'ef'], ['a0', 'e0', '3b', '4d', 'ae', '2a', 'f5', 'b0', 'c8', 'eb', 'bb', '3c', '83', '53', '99', '61'], ['17', '2b', '04', '7e', 'ba', '77', 'd6', '26', 'e1', '69', '14', '63', '55', '21', '0c', '7d']]


def inv_add_round_key():
    w, h = 4, 4;
    c = [[0 for x in range(w)] for y in range(h)]

    for i in range(0,4):
        for j in range(0,4):
            c[i][j] = int(a[i][j], 16) ^ int(key[i][j], 16)
    a = c

def inv_substitution_box():
    for i in range(4):
        for j in range(4):

            l = list(X[i][j])
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

            X[i][j]=s_box[int(l[0])][int(l[1])]
    a = X

def inv_shift_rows():
    x = a[1][3]
    x1 = a[2][2]
    x2 = a[2][3]
    x3 = a[3][0]
    for i in range(1,4):

        for j in reversed(range(0,4)):
            if i == 1 and j>0:
                a[i][j] = a[i][j-1]

            if i == 2 and j > 1:
                a[i][j] = a[i][j-2]

        for j in range(0,3):
            if i == 3 and j < 3:
                a[i][j] = a[i][j+1]

    a[1][0] = x
    a[2][0] = x1
    a[2][1] = x2
    a[3][3] = x3

def inv_mix_column():
    func = [[14,11,13,9],[9,14,11,13],[13,9,14,11],[11,13,9,14]]
    my_list = []
    # Final array
    w, h = 4, 4;
    op = [[0 for x in range(w)] for y in range(h)]

    for k in range(0,4):
        for i in range(0,4):
            for j in range(0,4):
                x = int(a[j][k], 16)
                print('a',a[j][k], bin(x))
                if func[i][j] == 9:
                    y = x*2
                    if y > 255:
                        y = y - 256
                        y = y ^ 27
                    y = y*2
                    if y > 255:
                        y = y - 256
                        y = y ^ 27
                    y = y*2
                    if y > 255:
                        y = y - 256
                        y = y ^ 27
                    y = y ^ x

                if func[i][j] == 11:
                    y = x*2
                    if y > 255:
                        y = y - 256
                        y = y ^ 27
                    y = y*2
                    if y > 255:
                        y = y - 256
                        y = y ^ 27
                    y = y ^ x
                    y = y*2
                    if y > 255:
                        y = y - 256
                        y = y ^ 27
                    y = y ^ x

                if func[i][j] == 13:
                    y = x*2
                    if y > 255:
                        y = y - 256
                        y = y ^ 27
                    y = y ^ x
                    y = y*2
                    if y > 255:
                        y = y - 256
                        y = y ^ 27
                    y = y*2
                    if y > 255:
                        y = y - 256
                        y = y ^ 27
                    y = y ^ x

                if func[i][j] == 14:
                    y = x*2
                    if y > 255:
                        y = y - 256
                        y = y ^ 27
                    y = y ^ x
                    y = y*2
                    if y > 255:
                        y = y - 256
                        y = y ^ 27
                    y = y ^ x
                    y = y*2
                    if y > 255:
                        y = y - 256
                        y = y ^ 27

                my_list.append(y)
            for l in range(0,3):
                my_list[l+1] = my_list[l] ^ my_list[l+1]
            print(hex(my_list[3])[2:])
            op[i][k] = hex(my_list[3])[2:]
            my_list = []
    a = op

def decrypt():
    inv_add_round_key()
    for i in range(0, 9):
        inv_shift_rows()
        inv_substitution_box()
        inv_add_round_key()
        inv_mix_column()
    inv_shift_rows()
    inv_substitution_box()
    inv_add_round_key()

def show_output():
    for i in range(0,4):
        for j in range(0,4):
            print(a[i][j], end=",")
        print("\n")
