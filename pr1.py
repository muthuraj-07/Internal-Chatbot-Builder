def findgreatestelement(numbers):
    result=0
    n=len(numbers)
    for index in range(n):
        if numbers[index]>result:
            result=numbers[index]
    return result
numbers=[12,3,4,65,1,2,3]
result=findgreatestelement(numbers)
print("Greatest element is",result)

