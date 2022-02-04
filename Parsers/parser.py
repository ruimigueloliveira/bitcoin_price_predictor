with open('../Dataset/unparsed_price.txt') as f:
    lines = f.readlines()


with open('../Dataset/btc_data.txt', 'w') as f:
    for line in lines[::-1]:
        # print(line.split('\t'))
        # print(line.split(',')[1].strip(), file=f)
        open_price = line.split('\t')[1].replace(',', '')
        print(open_price)
        print(open_price, file=f)
