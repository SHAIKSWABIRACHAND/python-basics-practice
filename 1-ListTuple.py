#Create a list and tuple in Python, and demonstrate how attempting to change an element works differently for each.

list = [1,2,3,4,5,6,7]
tuple = (1,2,3,4,5,6,7)
print("list:",list)
print("tuple:",tuple)
list[2] = 100
print("updated list:",list)
try:
    print(tuple(1))
    tuple[1] = 100
    print(tuple)
except:
    print("tuple is immutable, u cannot change it")
    
