k1 = int(input("Esimene külg: "))
k2 = int(input("Teine külg: "))
k3 = int(input("Kolmas külg: "))
if k1 + k2 < k3:
    print("Võimatu")
elif k1 + k3 < k2:
    print("Võimatu")
elif k2 + k3 < k1:
    print("Võimatu")
elif k1 == k2 == k3:
    print("Võrdkülgne kolnurk")
elif k1 == k3:
    print("Võrdhaarne kolmnurk")
elif k2 == k3:
    print("Võrdhaarne kolmnurk")
elif k1 == k2:
    print("Võrdhaarne kolmnurk")
elif k1 != k2 != k3:
    print("Erikülgne kolmnurk")
