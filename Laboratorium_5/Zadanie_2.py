sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

print(sample_dict)

print(sample_dict.keys())

for k in sample_dict.keys():
    print(f"{k:<10} = {sample_dict[k]:>10}")

L = ['name', 'surname']
dict222 = {}
for key in L:
    print(key)
    if key in sample_dict:
        dict222[key] = sample_dict[key]

print(dict222)

d2 = {key:sample_dict[key] for key in L if key in sample_dict}
print(d2)
