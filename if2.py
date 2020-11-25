tmp = int(input("Temp: "))

if tmp < -50:
    print("liiga külm")
elif tmp < -25:
    print("külm")
elif tmp < -10:
    print("jahe")
elif tmp > 0:
    print("normaalne")
elif tmp > 15:
    print("soe")
elif tmp > 25:
    print("palav")
else:
    print("kuum")
