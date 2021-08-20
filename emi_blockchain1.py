blockchain = [[1]]

def getLastValue():
    return blockchain[-1]

def transaction(last_value, currentValue):
    blockchain.append([last_value,currentValue])
    print(f"${last_value},${currentValue}")
12
print("Emi - Blockchain world")
while True:
    i = input(">>crate transaction ammount>>$")
    transaction(getLastValue(),i)
    if i == -1:
        break
    elif i == "bal":
        print(blockchain)

print("Blockchain end>> ")