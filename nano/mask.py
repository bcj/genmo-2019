import struct
R=open("i.bmp","rb").read
R(18)
w,h,b=struct.unpack("<iixxh",R(12))
R(24)
m=[any(R(b//8)[:3]) for _ in range(w*-h)]
L=lambda n:open(n).read().split()
for i,o in enumerate(zip(L("a.txt"),L("b.txt"))):
 print(o[m[i%(w*-h)]],end=" \n"[w-1==i%w])