a = {'key1':'value1','key2':'value2'}
print(a) #{'key1': 'value1', 'key2': 'value2'}
print(a['key1']) #value1
b = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print(b['key3']) #['item0', 'item1', 'item2']
print(b['key3'][0]) #item0
print(b['key3'][0].upper()) #ITEM0
b['key1'] = 1
print(b['key1']) #1
c = {}
c['animal'] = 'dog'
c['answer'] = 42
print(c) #{'animal': 'dog', 'answer': 42}

print("\n Nesting")
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(d['key1']['nestkey']['subnestkey']) #value

print("\n Method")
e = {'key1':1,'key2':2,'key3':3}
print(e.keys()) #dict_keys(['key1', 'key2', 'key3'])
print(e.items()) #dict_items([('key1', 1), ('key2', 2), ('key3', 3)])

print("\n Sort and list")
f = {'key2':2,'key1':1,'key3':3}
print(sorted(f.values())) #[1,2,3]
print(list(f.keys())) #['key2', 'key1', 'key3']
print(sorted(f.keys())) #['key1', 'key2', 'key3']

