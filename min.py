first = int(input("Esimene arv: "))
second = int(input("Teine arv: "))
third = int(input("Kolmas arv: "))
if first < second and third:
    print(first)
elif second < first and third:
    print(second)
elif third < first and second:
    print(third)
