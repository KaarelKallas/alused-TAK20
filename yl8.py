num = int(input("Sisesta positiivne täisarv: "))
if (num % 4) == 0 and (num % 100) != 0:
    print("{0} On liigaasta number".format(num))
else:
    print("{0} On lihtaasta number".format(num))
