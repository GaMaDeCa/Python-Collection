array=[0,1,2,3,4,5,6,7,8,9,2,4,1,3,1,4,3,9,1,0,9,8,7,4,2,4,5,6,7,8,2,2]
print(array)

remdup=[array[0]]
print(array[0],array.count(array[0]))
for i in range(1,len(array)):
    if not array[i] in remdup:
        remdup.append(array[i])
        print(array[i],array.count(array[i]))

print(remdup)
