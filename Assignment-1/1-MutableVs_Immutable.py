# 6. Write a function to demonstrate the behavior of mutable and immutable arguments.
def IsMutable(a,b):
    return (a == b)
def function(Int,List):
    before_Int_id = id(Int)
    print(f"Value of Int variable is {Int} and it's address before update is {before_Int_id }")
    Int = Int+10
    after_Int_id  = id(Int)
    print(f"Value of Int variable is {Int} and it's address after update is {after_Int_id }")
    
    before_List_id = id(List)
    print(f"Value of Int variable is {List} and it's address before update is {before_List_id }")
    List.append(10)
    after_List_id = id(List)
    print(f"Value of Int variable is {List} and it's address after update is {after_List_id }")
    IsMutable_Int = "mutable" if IsMutable(before_Int_id, after_Int_id) else "immutable"
    IsMutable_List = "mutable" if IsMutable(before_List_id, after_List_id) else "immutable"

    print("int is",IsMutable_Int)
    print("list is",IsMutable_List)
function(10,[12,100])
    
