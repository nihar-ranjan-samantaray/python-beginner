from functools import reduce
nums = [2,3,4,7,8,13,16,25,32]
evens = list(filter(lambda n : n%2 == 0,nums))
doubles = list(map(lambda n : n * 2,evens))
add = reduce(lambda a,b : a + b,doubles)
print(nums)
print(evens)
print(doubles)
print(add)
