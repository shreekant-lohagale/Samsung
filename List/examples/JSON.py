import json 
data = '{ "Title": "List", "Author": "Guido van Rossum", "Year": 1991, "Genres": ["Programming", "Technology", "Education"] }'
parsed_data = json.loads(data)
print(type(parsed_data))
print("Title:", parsed_data["Title"])

# print(open('books.json','w'))
# with open('books.json', 'w') as file:
#     json.dump(parsed_data, file, indent = '\t')

lst = [1, 2, 3, 4, 5]
print('before pop(0): ', lst)
print('before pop(0) lst[1] =', lst[1])
lst.pop(0)
print('after pop(0):', lst)
print('after pop(0) lst[1] =', lst[1])
print('----------------------------------')