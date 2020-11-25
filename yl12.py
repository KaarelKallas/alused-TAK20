list = ["mandariin", "virsik", "õun"]
print(list)
print(list[0])
list.append("banaan")
print(list[3])
list[0] = "sidrun"
print(list)
if "õun" in list:
  print("Jah, 'õun' on listis")
print(len(list))
list.remove("banaan")
print(list)
list.reverse()
print(list)
list.sort()
print(list)
