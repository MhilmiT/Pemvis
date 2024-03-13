#PART 3
#Case 5
print("Case 5")
#Variabel yang kosong memiliki nilai Boolean False
a = 0
b = ""
C = ()
d = []
e = {}
#integer null
#string kosong
#tuple kosong
#list kosong
#dictionary/set kosong
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print("===============")
#Case 6
print("Case 6")
#Variabel yang panjangnya nol memiliki nilai Boolean False
class myclass():
 def __len__(self):
  return 0
print (bool (myclass()))
print("================")