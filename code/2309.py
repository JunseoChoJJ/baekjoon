dwarf =[]
for i in range(9):
    dwarf.append(int(input()))
    
num = sum(dwarf) - 100
two = []
for i in range(9):
    for j in range(i+1 , 9):
        if (dwarf[i] + dwarf[j]) == num:
            two.append(dwarf[i])
            two.append(dwarf[j])
            break
            
dwarf.remove(two[0])
dwarf.remove(two[1])

dwarf.sort()
for k in dwarf:
    print(k)
