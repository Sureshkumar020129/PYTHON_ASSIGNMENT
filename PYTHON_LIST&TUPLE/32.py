print("32.	Create a tuple of numbers and find the largest and smallest values.")
t1=(1,2,3,4,5,6,7,8,9,10)
lar=0
for x in t1:
    if x>lar:
        lar=x
print(lar)
for y in t1:
    if y<lar:
        lar=y
print(lar)        