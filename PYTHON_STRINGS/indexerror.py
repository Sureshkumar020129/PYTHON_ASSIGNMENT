try:
    name="suresh kumar"
    num=int(input("Enter the index number: "))
    print(name[num])
except IndexError:
    print("Index is out of bounds")