data = open('CupcakeInvoices.csv')


#3
for info in data:
    print(info)

#4
for line in data:
    line = line.strip()
    values = line.split(',')
    print(values[2])


#5 
answer = []
for info in data:
    info = info.strip()
    values = info.split(',')
    total = round(int(values[3]) * float(values[4]), 2)
    answer.append(total)

print(answer)

#6
print(sum(answer))






#7
data.close()