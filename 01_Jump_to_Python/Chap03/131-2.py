my_data=[1,1,1,2,3,44,6,8,6,8]
print(my_data)
unique_data = set(my_data)
print(unique_data)

for element in unique_data:
    print(element)


t_data=(1,4,5,3,77)
for element in t_data:
    print(element)

str_data="Hello world"
for element in str_data:
    print(element)

dic_data = {"�̸�":"��","����":55,"���":"��"}
for element in dic_data:
    print(element)
for key in dic_data:
    print(key+' '+str(dic_data)[key])

