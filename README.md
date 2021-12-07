# ProiectASC1
Echipa: UTF-8 abuser
Proiect ASC 2021 

Input si output sunt fisierele pentru encrypt.py
Intrare si output2 sunt fisierele pentru decript.py
-->innput=output2

Parola pe care am ales-o este introdusa in sistem prin environment variables din system properties.
Am folosit libraria os pentru a accesa parola fara a fi vizibila in cod.
Deoarece parola este in sistem, am folosit scriptul ca si cum ar avea transmisi 2 parametrii --> fisierul de intrare si cel de output.

Am folosit formaatul UTF-8 pentru a fi siguri ca toate caracterele pot fi interpretate si modificate.
Nota: Am pus in fisierul input numere in loc de text literal, am interpretat gresit termenul "lizibil"
Totusi, avand doar 10 cifre in loc de 26 de caractere, era mai simplu de rezolvat pentru cine ar fi trebuit sa sparga parola--> poate codul rula in timp util.

  Echipa Adversa1 : Lilled https://github.com/Federicis/Criptare-XOR
  
  Parola folosita: ETOTFILOZOFIE
  Pentru partea 1 am copiat din fisierul lor input o bucata de text de la inceput si o bucata de text din fisierul output si am facut o simpla xorare in python pentru a obtine parola (care se repeta)
  
  Pentru partea 2 o solutie ar fi incercarea spargerii parolei stiind ca este formata din litere si cifre (aprox. 36^15 combinatii din care am pastra pe cele unde intalnim in output cuvinte comune pentru un text literar: "de" "si"...), insa codul nu s-ar termina de rulat inainte sa se termine proiectul...
  
  Echipa Adversa2: Cei_sqrt(9)_musafiri https://github.com/DariaClem/ProiectASC
  Parola: Bw4dUHW7fqN1De
  
