
with open("nasadata.txt", "r") as f:
    lines = f.readlines()
    print(lines)
with open("output.txt","w") as w:
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
    

        
            

        

