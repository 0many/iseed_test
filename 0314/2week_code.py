# 1
print("100")
print(100)
print(50+50)
print("50+50")

#2
print('%d / %d = %d' % (5,10, 5/10))

#3
print("%04d" % 876)
print("%5s" % "CookBook")
print("%1.1f" % 123.45)

#4
print("{2:d} {0:d} {1:d}".format(111,222,333))

#11-1
num_2 = "1011"
num_10 = 0
for i in range(len(num_2)):
    digit = int(num_2[i])
    power = len(num_2) - 1 - i
    num_10 += digit * (2 ** power)
print(num_10)

#11-2
num_16 = "1A"
num_10_2 = int(num_16, 16)
print(num_10_2)

#15
num=12345678
hex_num = hex(num)
oct_num = oct(num)
bin_num = bin(num)

print("10진수==>", num)
print("16진수==>", hex_num)
print(" 8진수==>", oct_num)
print(" 2진수==>", bin_num)








