import hashlib
k = 1
with open('../input.txt', 'r') as file:
    key = file.read()
while True:
    if hashlib.md5((key+str(k)).encode()).hexdigest()[0:6] == "000000":
        break
    k += 1
print(k, "is the lowest number with wich combines the key to make an MD5 hash starting with 6 zeroes.")
