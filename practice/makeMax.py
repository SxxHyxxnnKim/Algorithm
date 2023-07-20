answer = 0
numbers = [0,31,24,10,1,9]

numbers.sort() 
first = numbers[len(numbers)-1]
second = numbers[len(numbers)-2]

answer = first * second

print(answer)