a = [['63','EB','9F','A0'],['2F','93','92','C0'],['AF','C7','AB','30'],['A2','20','CB','2B']]
#func = [[0b10,0b11,0b1,0b1],[0b1,0b10,0b11,0b1],[0b1,0b1,0b10,0b11],[0b11,0b1,0b1,0b10]]
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

for i in range(0,4):
    for j in range(0,4):
        print(op[i][j], end=",")
    print("\n")
