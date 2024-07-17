"""
Understanding Big O(n) complexities 
"""
Sample Code 1 
def print_items(n):
    for i in range(n):
        print(i)
    # Bit 1 
    for j in range(n):
        print(j)

print_items(10)

def print_items(n,y):
    for i in range(n):
        for j in range(n):
            print(i,j)
    
    #Bit 2 
    for k in range(y):
        print(k)

def add_items(n):
    return n + n 

add = lambda x : x + x 
result = add(5)

print(result)
add_items(2)
print_items(10,90)           