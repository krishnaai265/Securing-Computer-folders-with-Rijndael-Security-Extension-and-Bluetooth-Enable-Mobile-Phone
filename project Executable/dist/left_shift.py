#left shift
no = 3
b = "00011011"
x=int('d4', 16)
y = x<<1
'''
print(y)
z = format(y, '02x')
print(z)
'''
# If extra one in left the add 1b
if y >= 254:
    y = y - 128  # remove extra one from left
    z = y ^ int(b,2)
    z = '{0:b}'.format(z)
    print(z)
'''
print(z[0])
print(z[1:])
i = bin(int(z[1:], 16)).replace("0b","")
print(i)
#print(format(i, '02x'))
if z[0] == '1':
    #XOR
    a = bin(int(z[1:], 16)).replace("0b","")
    b = "00011011"
    y = int(a,2) ^ int(b,2)
    y = '{0:b}'.format(y)
    print()
else:
    print(bin(int(z[1:], 16)).replace("0b",""))
'''
