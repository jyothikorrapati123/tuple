#implicit
a=(1,2,3)
print(type(a))
#explicit
a=tuple((1,2,3))
print(type(a))
#datatype/variable annotation
a:tuple=((1,2,3))
print(type(a))
#tuple methods

#count
a=tuple((1,2,3,4,5,6,7,7,7))
print(a.count(7))
#index
a=tuple(("jyo","sagar","sumathi"))
print(a.index("sagar"))
#tuple in list
a=tuple((1,2,3,4,5))
a=list(a)
print(type(a))