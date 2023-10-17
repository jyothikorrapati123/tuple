#remove
attendees=["jyothi","sumathi","venky"]
attendees.remove("jyothi")
print(attendees)
#pop with index
attendees=["jyothi","sumathi","venky"]
attendees.pop(0)
print(attendees)
#pop without index
attendees=["jyothi","sumathi","venky"]
attendees.pop()
attendees.pop()
print(attendees)
#clear
a=["jyothi","sumathi","venky"]
print(a.clear())
print(type(a))
print(a)
#delete
a=["jyothi","sumathi","venky"]
del a[0]
print(a)
del a
#print(a)
#
a=input("enter a value:")
b=input("enter  b value:")
c=input("enter  c value:")
attendees=[]
attendees.append(a)
attendees.append(b)
attendees.append(c)
print(attendees)


