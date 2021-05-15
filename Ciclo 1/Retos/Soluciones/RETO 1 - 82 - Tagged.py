score = 0
comp = input("").upper()
if comp == "C1":
 score = score + 0
else:
   if comp == "C2":
    score = score + 0
   else:
    if comp == "C3":
     score = score + 1
    else:
      if comp == "C4":
       score = score + 2
ecg = input("").upper()
if ecg == "E1":
 score = score + 0
else:
   if ecg == "E2":
    score = score + 1
   else:
    if ecg == "E3":
     score = score + 2
    else:
      if ecg == "E4":
       score = score + 3
frm = input("").upper()
if frm == "F1":
 score = score + 0
else:
   if frm == "F2":
    score = score + 3
mgn = input("").upper()
if mgn == "M1":
    score = score + 0
else:
   if mgn == "M2":
    score = score +0
   else:
    if mgn == "M3":
     score = score + 2
    else:
      if mgn == "M4":
       score = score + 3
       
FE1 = input("")
if FE1 == "1":
    score = score +0
    

FE2 = input("")
if FE2 == "1":
    score = score +1

FE3 = input("")
if FE3 == "1":
    score = score +2

FE4 = input("")
if FE4 == 1:
    score = score +3

size = float(input())

if score <=1:
    print("benigno")
    print("no aaf")
if score ==2:
    print("no sospechoso")
    print("no aaf")
if score ==3 and size>=2.5:
    print("levemente sospechoso")
    print("aaf")           
if score ==3 and size<2.5:
    print("levemente sospechoso")
    print("seguimiento")            
if score>=4 and score<=6 and size >=1.5:
    print("moderadamente sospechoso")
    print("aaf")
if score>=4 and score<=6 and size <1.5:
    print("moderadamente sospechoso")
    print("seguimiento")
if score>=7 and size>=1:
    print("seguimiento")
    print("aaf")
if score>=7 and size<=1:
    print("seguimiento")
    print("altamente sospechoso")
