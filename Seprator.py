import os,shutil
path = input("Enter your Path :- ")
os.chdir(path)
ext = []
for i in os.listdir():
    ext.append(i[::-1].split('.')[0][::-1])
ext = list(set(ext))
for i in ext:
    if os.path.exists(i) == False:
        os.mkdir(i)
for i in os.listdir():
    shutil.move(i,i[::-1].split('.')[0][::-1])