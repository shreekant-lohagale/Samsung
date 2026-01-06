#Search Key 
keys = [24, 14, 13, 56, 45, 72, 90, 12, 67, 39]

#size of hash table 
n = 10

#create empty hash table
hash_table = [None] * n

#hash function
def hash_fuction(k):    
    return k % n

#insert keys using linear probing to handle collisions
for key in keys:
    index = hash_fuction(key)
    original_index = index
    steps = 0

    #hash Collision handling using linear probing
    while hash_table[index] is not None and steps < n:
        steps += 1
    if steps < n:
        hash_table[index] = key
        print(f"key: {key} stored at index: {index}")
    else:
        print(f"Hash table is full, cannot insert key: {key}")

# print("final hash table")
# for i in range(n):
#     print(f"Index {i}: {hash_table[i]}")

print(hash_table)