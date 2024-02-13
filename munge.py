# Place code below to do the munging part of this assignment.

with open("/Users/brandongao/hw2/data/nasadata.txt", "r") as f:
    lines = f.readlines()
    print(lines)
with open("/Users/brandongao/hw2/data/output.txt","w") as w:
    count = 0
    for line in lines:
        if line.strip("\n").split(" ")[0] == "Year" and count == 0:
            w.write(line)
            count+=1
        try:
            int(line.strip("\n").split(" ")[0])
            w.write(line)
        except:
            continue

""" with open("output.txt","w") as wt:
    for line in wt.readlines():
        lst = line.strip("\n").split(" ")
        if "***" or "****" not in lst:
            wt.write(line) """