#list - data structure which can hold multiple values of multiple type
#arrary - data structure which can hold multiple values of same type

list_of_cloud = ["aws","azure","gcp","digital-ocean","oracle"]

print(list_of_cloud)

list_of_cloud.append("SALESFORCE") #add element to the end of the list
list_of_cloud.append("IBM")

print(list_of_cloud)

list_of_cloud.insert(2,"Heroku") #adds element to at specific location "2"

print(list_of_cloud)

print(len(list_of_cloud))

list_of_cloud.insert(0, "Mycloud")

print(list_of_cloud)

for cloud in list_of_cloud: #iteration of a list
    print(" ")
    print(cloud)

for i in range(1,11):
    print(i)

