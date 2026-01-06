#Search Key 
keys = [24, 18, 13, 56, 45, 72, 90, 11, 67, 39]

#size of hash table 
n = 10

#create empty hash table
hash_table = [None] * n

#hash function
def hash_fuction(k):
    return k % n

#insert keys into hash table 
for key in keys:
    index = hash_fuction(key)
    print(f"key: {key} stored at index: {index}")