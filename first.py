class test():
    def __init__(self):
        pass
    def add(self,a=35,b=95):
        c=a+b
        return c,a
z=test()
r=z.add(b=30,a=70)  
print(r)
