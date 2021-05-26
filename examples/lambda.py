# lambda expessions

# lambda param: action(param)

from functools import reduce

my_list = [1, 2, 3]

print(list(map(lambda item: item*2, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(reduce(lambda acc, item: acc+item, my_list))



#Square


my_list1 = [5, 4, 3]


new_list = list(map(lambda num: num**2, my_list1))

print(new_list)


#List Sorting

a = [(0,2), (4,3), (10,-1), (9,9)]

a.sort()

print(a)

a.sort(key=lambda x: x[1])

print(a)

a.sort(key=lambda x: x[0])

print(a)

FEAT = ["vibration", "emf", "environmental","accoustic"]

deviceid = "_deviceid_"
device_timestamp = "_device_timestamp_"

def filecheck(string):
	return string == 'emf'


file_name = lambda data_type, deviceid, device_timestamp: filecheck(data_type)
new_list = list(map(lambda data_type: file_name(data_type, deviceid, device_timestamp) , FEAT))

print(new_list)

# for data_type in ["vibration", "emf", "environmental","accoustic"]:
#     file_name = "project/okto/" + device_id + "/" + data_type + "/" + device_timestamp

