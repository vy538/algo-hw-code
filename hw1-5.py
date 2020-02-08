def print_duplicates(line):
    for i in range(0,len(line)):
        for j in range(i+1,len(line)):
            if line[i] == line[j]:
                # print(i,"is same as",j)
                print(line[i])

print_duplicates("babcda")