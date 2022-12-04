#
values = [10, 20, 30]
keys = ["ten", "twenty", "thirty"]

dict = zip(keys, values)
print(list(dict))

# dict2 = dict(zip(keys, values))
# print(dict2)

dict1 = {}

for i in range(len(keys)):
    dict1[keys[i]] = values[i]
print(dict1)

dict2 = {'thirty':30, 'fourty':40, 'fifty':50}
print(dict2)

dict3 = dict1.copy();
print(dict3)
dict3.update(dict2)
print(dict3)

dict4 = {keys[i]:values[i] for i in range(len(keys))}
print(dict4)
