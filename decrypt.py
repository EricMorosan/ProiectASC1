import os
import sys
import io


if len(sys.argv) > 3:

    sys.exit()

if len(sys.argv) < 3:
    sys.exit()

fisieroutput = sys.argv[1]
fisierinput = sys.argv[2]

parola = os.environ.get("parolaASC1")
k = parola
f = open(fisieroutput, "w", encoding="utf-8")
g = open(fisierinput)
s = g.readline()
while s != "":
	v = s
	for i in range(0,len(v)-1):
   	 	x = ord(v[i])
   	 	y = ord(k[i % len(k)])
   	 	x = x ^ y
   	 	f.write(chr(x))
	f.write("\n")
	s = g.readline()
f.close()
g.close()