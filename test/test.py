def recurse_factorial(n):
    if n == 0:
        return 1
    return n * recurse_factorial(n-1)

print(recurse_factorial(6))

def iter_factorial(n):
    answer = 1
    for i in range(n, 0, -1):
        answer *= i
    return answer

print(iter_factorial(8))

[]
x = 0
y = 0

while 0 is less length of an array and 0 is less then length of another one

if first array first position <= 2nd array first position
put first array into empty array and x + 1

or else put the second array into the empty array and y + 1

[2, 6, 8, 9, 1]

[2, 6, 8] [9, 1]

0 < 3 and 0 < 2
   if [(2), 6, 8] <= [(9), 1]
        [2]
    if [6, 8] <= [9, 1]
    

helper function for merge sort:
declare an empty array and two varibles for two arrays indexes starting at 0
while the length of each array is greater then it's index you should
compare the first(0) index of both arrays, take the smaller number
and place it in the empty array. Add 1 to the index of the array you took the 
integer from.
Declare this same function again but individualy for each array to deal with 
when there is just 1 integer left in each array.
return your merged array

to sort: base case = length of array is less then 2 (1) return the array
find the middle via math floor length of array divided by two
declare left array is index 0 to middle
right array is middle to end or array (len(array))
call your sort function recursively and stick it inside your 
helper function

