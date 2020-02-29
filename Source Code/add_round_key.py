a = [['ba','84','e8','1b'],['75','a4','8d','40'],['f4','8d','6','7d'],['7a','32','e','5d']]
b = [['E2','91','B1','D6'],['32','12','59','79'],['FC','91','E4','A2'],['F1','88','E6','93']]
# Final array
w, h = 4, 4;
c = [[0 for x in range(w)] for y in range(h)]

for i in range(0,4):
    for j in range(0,4):
        c[i][j] = int(a[i][j], 16) ^ int(b[i][j], 16)

for i in range(0,4):
    for j in range(0,4):
        print(hex(c[i][j])[2:], end=",")
    print("\n")
