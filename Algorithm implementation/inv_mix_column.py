a = [['ba','84','e8','1b'],['75','a4','8d','40'],['f4','8d','6','7d'],['7a','32','e','5d']]
#func = [[0b10,0b11,0b1,0b1],[0b1,0b10,0b11,0b1],[0b1,0b1,0b10,0b11],[0b11,0b1,0b1,0b10]]
func = [[14,11,13,9],[9,14,11,13],[13,9,14,11],[11,13,9,14]]
my_list = []
# Final array
w, h = 4, 4;
op = [[0 for x in range(w)] for y in range(h)]

for k in range(0,4):
    for i in range(0,4):
        for j in range(0,4):
            x = int(a[j][k], 16)
#            print('a',a[j][k], bin(x))
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
#        print(hex(my_list[3])[2:])
        op[i][k] = hex(my_list[3])[2:]
        my_list = []

for i in range(0,4):
    for j in range(0,4):
        print(op[i][j], end=",")
    print("\n")
