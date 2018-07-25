class dogs:
    
    tricks=[]
    cnt=0

    def __init__(self,name,trick):
        self.name=name
        self.tricks.append(trick)

    def print_tricks(self):
        print(self.tricks)

    def print_name(self):
        print(self.name)


d1=dogs("hector","roll")
d2=dogs("bubi","jump")
d3=dogs("kutya","bark")

objs=[]
objs.append(d1)
objs.append(d2)
objs.append(d3)

for i in range(len(objs)):
    objs[i].print_tricks()


print(dogs.cnt)
