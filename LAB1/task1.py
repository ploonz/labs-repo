from ipaddress import summarize_address_range
from types import NoneType

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
for i in range(len(numbers)):
    if numbers[i]==None :
        numbers[i]=0
        ind=i
numbers[ind]=sum(numbers)/len(numbers)

print("Измененный список:",numbers)
