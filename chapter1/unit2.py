list = [11,3,23,7]
list.append(17)
print(list)
list.pop(4)
print(list)

# Adding to list or removing is O(1) on the right end 
# Adding to list or removing is O(n) on the left end 
list.insert(1,'Hi')
print(list)