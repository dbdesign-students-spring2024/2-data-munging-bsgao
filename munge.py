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
            parts = line.strip("\n").split()
                
            if "***" not in parts and "****" not in parts:
                processed_line = [parts[0]] + \
                                     [f"{float(value)/100/1.8:.2f}" 
                                      for i, value in enumerate(parts[1:-1], 1)] + \
                                     [parts[-1]]
                w.write(','.join(processed_line) + '\n')

        except:
            continue
        
with open("/Users/brandongao/hw2/data/output.txt", "r") as ro:
    output_lines = ro.readlines()

with open("/Users/brandongao/hw2/data/clean_data.csv", "w") as wo:
    for i in output_lines:
        wo.write(i)
