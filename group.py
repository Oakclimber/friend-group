"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

class person:
    def __init__(self,name,age,job):
        self.name = name
        self.age = age
        self.job = []
        self.job.append(job)
        self.connect=[]
    def addconnect(self,connect):
        self.connect.append(connect)
    def printconnect(self):
        for i in range(len(self.connect)):
            if self.connect[i].name1 == self.name:
                print(self.connect[i].name2+' '+self.connect[i].connect)
            if self.connect[i].name2 == self.name:
                print(self.connect[i].name1+' '+self.connect[i].connect)

class connection:
    def __init__(self,name1,name2,connect):
        self.name1=name1
        self.name2=name2
        self.connect=connect

a = person("Jill", 26, "a biologist")
b = person("Zalika", 28, "an artist")
c = person("John", 27, "a writer")
d = person("Nash", 34, "a chef")

r1=connection("Jill","Zalika","friend")
r2=connection("Jill","John","partner")
r3=connection("Nash","John","cousin")
r4=connection("Nash","Zalika","landlord")

a.addconnect(r1)
a.addconnect(r2)
b.addconnect(r1)
c.addconnect(r2)
d.addconnect(r3)
d.addconnect(r4)

a.printconnect()
b.printconnect()
c.printconnect()
d.printconnect()

