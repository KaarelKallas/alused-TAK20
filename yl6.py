e = int(input("Esimene arv: "))
t = int(input("Teine arv: "))
k = int (input("Kolmas arv: "))
if e > t and e > k:
    print(e)
elif t > k:
    print(t)
else:
    print(k)
