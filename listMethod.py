a1 = ['a','b']

print(f"a1 ={a1},,len of a1 {len(a1)}")

print('-'*10)

a1.append('c')

print(f"a1 after append = {a1}, len of a1 ={len(a1)}")

a2 =  a1
print('-'*10)

print(f"a2 = a1 and then a2 = {a2} , len of a2 = {len(a2)}")
print('-'*10)

a2.clear()
print(f"a2  after clear = {a2} , len of a2 = {len(a2)}")
print(f"a1  after clear on a2 = {a1} , len of a1 = {len(a1)}")

print('now we init value ')

print()

a1 = ['arc','da25']
print(f"a1 ={a1},,len of a1 {len(a1)}")
print('-'*10)

a2 = a1.copy()
print(f"a2 ={a2},,len of a2 {len(a2)}")


a2.clear()
print(f"a2  after clear = {a2} , len of a2 = {len(a2)}")
print(f"a1  after clear on a2 = {a1} , len of a1 = {len(a1)}")

a2.append(['a','b'])
print('-'*10)

print(f"a2 after append [a,b] clear = {a2}, len of a2 = {len(a2)}")

a2.clear()
print(f"a2  after clear = {a2} , len of a2 = {len(a2)}")

a2.extend(['a','b'])

print(f"a2 afteer extend [a,b]= {a2}, len of a2 = {len(a2)}")


print()
# Count Method

num1 = [1,2,3,4,1]

a = num1.count(1)

print(a)

print()
print()
# index Methods

num1 = ['a','b','c','d','e','f']

a = num1.index("d")

print(a)

print()
print()


# insert Method
list =['nagpur','wardha','pune']
list.insert(2,'mumbai')
print(list)

# pop method

val = [10,12,24,30,46]
val1 = val.pop()


print(val)
print()
print(val1)

# pop method

val = [10,12,24,30,46]
val1 = val.pop(1)


print(val)
print()
print(val1)


# remove  Method
list =['nagpur','wardha','pune','mumbai']
list.remove('mumbai')
print(list)



# reverse Methods

a = ['a','b','c','d','e','f']

a.reverse()

print(a)

print()
print()



# sort Methods

a = ['d','f','a','c','b']

a.sort()

print(a)

print()
print()