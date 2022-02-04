from sklearn import preprocessing
import numpy as np

ls = []
with open('../Dataset/btc_data.txt') as f:
    for i in f.readlines():
        ls.append(float(i.strip()))


diff_ls = []
count = 1
for i in ls[:-1]:
    diff = round(ls[count] - i, 2)
    diff_ls.append(diff)
    count += 1


x_array = np.array(diff_ls)
normalized_arr = preprocessing.normalize([x_array])[0]
print(normalized_arr)


print(min(diff_ls))
print(max(diff_ls))
with open('../Dataset/btc_diff.txt', 'w') as f:
    for i in diff_ls:
        print(i, file=f)



# for i in ls2[:-(columns-1)]:
#     for j in range(columns):
#         if j == 0:
#             strr = str(ls2[count] / divider)
#         else:
#             strr = strr + ',' + str(ls2[count + j] / divider)
#         # print(strr)
#     count += 1
#     str_ls.append(strr)
#
training = round(len(normalized_arr) * 0.6)
validation = round(len(normalized_arr) * 0.2) + training


with open('../Dataset/training_diff.txt', 'w') as f:
    for i in normalized_arr[:training]:
        print(i, file=f)

with open('../Dataset/validation_diff.txt', 'w') as f:
    for i in normalized_arr[training:validation]:
        print(i, file=f)

with open('../Dataset/testing_diff.txt', 'w') as f:
    for i in normalized_arr[validation:]:
        print(i, file=f)
