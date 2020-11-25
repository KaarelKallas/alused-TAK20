name = input("Sisesta oma nimi: ")
print("Tere, " + name + "!")
city = input("Kus on su elukoht: ")

if city.lower() == "kuressaare":
    print("Hei ma olen ka sealt!")
age = int(input("Kui vana sa oled: "))
if age < 18:
    print("Sa oled veel liiga noor, et autot juhtida!")
elif age > 18:
    print("Sa oled piisavalt vana, et autot juhtida!")
else:
    print("Palju õnne täisealiseks saamiseks!")
