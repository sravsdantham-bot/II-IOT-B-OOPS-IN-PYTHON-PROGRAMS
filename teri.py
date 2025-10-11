class emp:
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal
class empchild(emp):
    def __init__(self,name,age,sal,idno):
        self.name=name
        self.sal=sal
        self.idno=idno
#driver code
e=emp("iot",23,50000)
print("emp name=",e.name)
el = empchild('iot-AB',23,5000,22)
print(el.name)
 
