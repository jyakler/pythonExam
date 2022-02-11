import os

path = "C:\BigData\WEBCLIENTexam\htmlexam\images"
files = os.listdir(path)
for f in files:
    if (f.find("_") != -1 and f.endswith(".png")):
        name = f[0:-4]
        ext = f[-4:]
        part = name.split("_")
        newname = part[1].strip() + "-" + part[0].strip()+"-new" + ext
        print(newname)
