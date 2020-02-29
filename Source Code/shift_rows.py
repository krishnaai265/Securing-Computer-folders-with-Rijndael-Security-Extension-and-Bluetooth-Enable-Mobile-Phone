a = [['63','EB','9F','A0'],['C0','2F','93','92'],['AB','30','AF','C7'],['20','CB','2B','A2']]

def shift_rows():
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

shift_rows()

for i in range(0,4):
    for j in range(0,4):
        print(a[i][j], end=",")
    print("\n")
