count = 0
ArpgR2_01_Arr = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR2_01)):
            if ArpgR2_01[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count += 1
                else:
                    count += -1/(last - j + 1)
if count != 0:                    
    count = count / len(ArpgR2_01)
print ("Arpg for Room with 2 tun. and act. 1, divid. by tot. numb. memb.: " + str(count))

count = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR2_02)):
            if ArpgR2_02[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count += 1
                else:
                    count += -1/(last - j + 1)
if count != 0:                    
    count = count / len(ArpgR2_02)
print ("Arpg for Room with 2 tun. and act. 2, divid. by tot. numb. memb.: " + str(count))
    
count = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR2_03)):
            if ArpgR2_03[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count += 1
                else:
                    count += -1/(last - j + 1)
if count != 0:                    
    count = count / len(ArpgR2_03)
print ("Arpg for Room with 2 tun. and act. 3, divid. by tot. numb. memb.: " + str(count))
    
count = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR2_04)):
            if ArpgR2_04[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count += 1
                else:
                    count += -1/(last - j + 1)
if count != 0:                    
    count = count / len(ArpgR2_04)
print ("Arpg for Room with 2 tun. and act. 4, divid. by tot. numb. memb.: " + str(count))

count = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR2_05)):
            if ArpgR2_05[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count += 1
                else:
                    count += -1/(last - j + 1)
if count != 0:                    
    count = count / len(ArpgR2_05)
print ("Arpg for Room with 2 tun. and act. 5, divid. by tot. numb. memb.: " + str(count))

count = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR2_06)):
            if ArpgR2_06[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count += 1
                else:
                    count += -1/(last - j + 1)
if count != 0:                    
    count = count / len(ArpgR2_06)
print ("Arpg for Room with 2 tun. and act. 6, divid. by tot. numb. memb.: " + str(count))

print ("")

count = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR6_00)):
            if ArpgR6_00[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count += 1
                else:
                    count += -1/(last - j + 1)
if count != 0:                    
    count = count / len(ArpgR6_00)
print ("Arpg for Room with 6 tun. and act. 0, divid. by tot. numb. memb.: " + str(count))

count = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR6_01)):
            if ArpgR6_01[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count += 1
                else:
                    count += -1/(last - j + 1)
if count != 0:                    
    count = count / len(ArpgR6_01)
print ("Arpg for Room with 6 tun. and act. 1, divid. by tot. numb. memb.: " + str(count))

count = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR6_02)):
            if ArpgR6_02[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count += 1
                else:
                    count += -1/(last - j + 1)
if count != 0:                    
    count = count / len(ArpgR6_02)
print ("Arpg for Room with 6 tun. and act. 2, divid. by tot. numb. memb.: " + str(count))

count = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR6_03)):
            if ArpgR6_03[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count += 1
                else:
                    count += -1/(last - j + 1)
if count != 0:                    
    count = count / len(ArpgR6_03)
print ("Arpg for Room with 6 tun. and act. 3, divid. by tot. numb. memb.: " + str(count))

count = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR6_04)):
            if ArpgR6_04[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count += 1
                else:
                    count += -1/(last - j + 1)
if count != 0:                    
    count = count / len(ArpgR6_04)
print ("Arpg for Room with 6 tun. and act. 4, divid. by tot. numb. memb.: " + str(count))

count = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR6_05)):
            if ArpgR6_05[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count += 1
                else:
                    count += -1/(last - j + 1)
if count != 0:                    
    count = count / len(ArpgR6_05)
print ("Arpg for Room with 6 tun. and act. 5, divid. by tot. numb. memb.: " + str(count))

count = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(ArpgR6_06)):
            if ArpgR6_06[k] == arr[i][j]:
                last = findLast(arr[i])
                if arr[i][last] == '0':
                    count += 1
                else:
                    count += -1/(last - j + 1)
if count != 0:                    
    count = count / len(ArpgR6_06)
print ("Arpg for Room with 6 tun. and act. 6, divid. by tot. numb. memb.: " + str(count))

#
#
#
#


    
    
    