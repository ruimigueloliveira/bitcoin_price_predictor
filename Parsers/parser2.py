import sys

if len(sys.argv) != 2:
    print("Please insert number of columns")

ls = []
with open('../Dataset/btc_data.txt') as f:
    for i in f.readlines():
        ls.append(i.strip())

ls2 = []
for i in ls:
    ls2.append(float(i))

columns = 3
try:
    columns = int(sys.argv[1])
except:
    print()
count = 0
strr = ''
str_ls = []

max_num = int(max(ls2))
divider = 0
if max_num % 10000 == 0:
    divider = max_num
else:
    divider = 10000 - (max_num % 10000) + max_num

for i in ls2[:-(columns-1)]:
    for j in range(columns):
        if j == 0:
            strr = str(ls2[count] / divider)
        else:
            strr = strr + ',' + str(ls2[count + j] / divider)
        # print(strr)
    count += 1
    str_ls.append(strr)

training = round(len(str_ls) * 0.6)
validation = round(len(str_ls) * 0.2) + training

with open('../Dataset/training_data.txt', 'w') as f:
    for i in str_ls[:training]:
        print(i, file=f)

with open('../Dataset/validation_data.txt', 'w') as f:
    for i in str_ls[training:validation]:
        print(i, file=f)

with open('../Dataset/testing_data.txt', 'w') as f:
    for i in str_ls[validation:]:
        print(i, file=f)
