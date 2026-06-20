#clearing web artifacts and writing into the new file

text = []

with open(("C:/.../ST_raw.txt"), "r", encoding="utf-8") as c:
    for line in c:
        if (line[0]!="["):
            text.append(line.strip())

with open("C:/.../ST.txt", "w", encoding="utf-8") as f:
    for i in text:
        f.write(i+"\n")



#checking for more web artifacts

ST = ["PP", "PS", "SS", "TP"]

for i in ST:
    with open(("C:/Users/Win10/.ANDRIJA/Skolastika/Summa T/ST_"+i+".txt"), "r", encoding="utf-8") as c:
        for line in c:
            if ((line).strip()=="INDEX" or (line).strip()=="age retro   age ultra"):
                print("error in "+i)



#printing the question location given question index (0-511) i

for i in range(len(q)):
    if (i>421):
        print("TP "+str(i-421)+"\t"+str(q[i]))
    elif (i>232):
        print("SS "+str(i-232)+"\t"+str(q[i]))
    elif (i>118):
        print("PS "+str(i-118)+"\t"+str(q[i]))
    else:
        print("PP "+str(i+1)+"\t"+str(q[i]))
