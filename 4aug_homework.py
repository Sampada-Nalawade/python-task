#Task 1 : Identity Card

print("-----My ID Card-----")
name = "Rahul"
print("Name = ",name)
age = 20
print("Age = ",age)
city = "Pune"
print("City = ",city)
dob = "22-1-2000"
print("Date of Birth = ",dob)
college = "TKA"
print("College = ",college)
blood_group = "A+"
print("Blood Group = ",blood_group)

# Output : 
# -----My ID Card-----
# Name =  Rahul
# Age =  20
# City =  Pune
# Date of Birth =  22-1-2000
# College =  TKA
# Blood Group =  A+

#Task 2 : Find data type

a = 25
print(type(a))
b = 25.5
print(type(b))
c = "Twenty Five"
print(type(c))
d = True
print(type(d))
e = 2 + 3j
print(type(e))

# Output :
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>
# <class 'complex'>

#Task 3 : Memory Detective

v1 = 100
print(id(v1))
v2 = 200
print(id(v2))
v3 = 100
print(id(v3))

# Output :
# 140721340010712
# 140721340013912
# 140721340010712