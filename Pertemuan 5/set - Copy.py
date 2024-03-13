print("\033c")

# PART 1
# Constructing a Set (there are two methods)
Set_1 = {"Toyota", "Daihatsu", "Honda"}
Set_2 = set(("Toyota", "Daihatsu", "Honda"))

print("Tipe data Set 1 adalah ", type(Set_1))
print("Tipe data Set 2 adalah ", type(Set_2))

print("Data Set_1: ", Set_1)
print("Data Set_2: ", Set_2)
print("---")

# Print every item of Set_1
for x in Set_1:
    print(x)

print("---")

# Check the length of the set
print(len(Set_1))

# Check if a key exists
if "Daihatsu" in Set_1:
    print("Yes, 'Daihatsu' is an item in Set_1.")

# Add an item
Set_1.add("Mitsubishi")
print(Set_1)

# Add multiple items
Set_1.update(["Suzuki", "Mazda", "Nissan"])
print(Set_1)
