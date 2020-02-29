import os
import os.path
from os import listdir
from os.path import isfile, join

def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(self, message, key, key_size=256):
    message = self.pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)

def encrypt_file(self, file_name):
    print("enc"+file_name)
    try:
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(file_name)
    except Exception as e:
        print(e)

def decrypt(self, ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def decrypt_file(self, file_name):
    print("dec"+file_name)
    try:
        if ".enc" != file_name[-4:]:
            # sa = sa + ".enc"
            file_name = file_name +".enc"
            print("If Encryption working"+file_name)
            with open(file_name, 'rb') as fo:
                ciphertext = fo.read()
            dec = self.decrypt(ciphertext, self.key)
            with open(file_name[:-4], 'wb') as fo:
                fo.write(dec)
            os.remove(file_name)
        else:
            print("Else Encryption working"+file_name)
            with open(file_name, 'rb') as fo:
                ciphertext = fo.read()
            dec = self.decrypt(ciphertext, self.key)
            with open(file_name[:-4], 'wb') as fo:
                fo.write(dec)
            os.remove(file_name)
    except Exception as e:
        print(e)


def getAllFiles(self, line):
    dir_path = line
    dirs = []
    for dirName, subdirList, fileList in os.walk(dir_path):
        for fname in fileList:
            if (fname != 'script.py' and fname != 'data.txt.enc'):
                dirs.append(dirName + "\\" + fname)
    return dirs

def encrypt_all_files(self, line):
    dirs = self.getAllFiles(line)
    for file_name in dirs:
        self.encrypt_file(file_name)

def decrypt_all_files(self, line):
    dirs = self.getAllFiles(line)
    for file_name in dirs:
        self.decrypt_file(file_name)

file = "F:\\abc\\ezgif.com-video-to-gif.gif"+"\n"+"F:\\abc\\computer science.pdf"+"\n"+"F:\\abc\\Computer Programming.pdf"
for line in file.split("\n"):
    print(line[8:], '   ', line[0:8])
    if line[0:8] == 'file:///':
        line = line[8:]
        print(a+line)
    print(line)
    if os.path.isdir(line):
        print(a+line)
        print("Folder")
        enc.decrypt_all_files(line)
    elif os.path.isfile(line):
        print(a+line)
        enc.decrypt_file(line+".enc")
        print("File")
    else:
        print("headache")

    # print("Wrong mac")
    # # file = self.plainTextEdit_2.toPlainText()
    # file = t_f
    # for line in file.split("\n"):
    #     print(line[8:], '   ', line[0:8])
    #     if line[0:8] == 'file:///':
    #         line = line[8:]
    #     if os.path.isdir(line):
    #         print("Folder")
    #         enc.encrypt_all_files(line)
    #     elif os.path.isfile(line):
    #         enc.encrypt_file(line)
    #         print("File")
    # 