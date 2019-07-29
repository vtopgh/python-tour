# TASK 1
for value in range(1,21):
    print(value)

# TASK 2
nums = list(range(1, 1000000))
for num in nums:
    print(num)

# using list generators
nums = [num for num in range(1, 1000001)]
print(nums)

# TASK 3
nums2 = list(range(1, 1000001))
print("Min: " + str(min(nums2)))
print("Max: " + str(max(nums2)))
print("Sum: " + str(sum(nums2)))

# TASK 4
odd_nums = list(range(1, 21, 2))
for odd_num in odd_nums:
    print(odd_num)

# TASK 5
multiplesTo3 = list(range(3, 31, 3))
for num in multiplesTo3:
    print(num)

# TASK 6
cubes = list(range(1, 11))
for cube in cubes:
    cube = cube ** 3
    print(cube)

# using list-generators(comprehension)
cubes = [num ** 3 for num in range(1, 11)]
print(cubes)
