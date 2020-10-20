class A:
    classVar1 = "I am the class Variable in calass A"
    def __init__(self):
        self.var1 = "I am in A's Constuctor"
        self.classVar1 =  "Instance var in Class A"
        self.special = "Special Variable"
class B(A):
    classVar2 = "I am the class Variable in class B"
    def __init__(self):
        super().__init__()
        self.var1 = "I am in B's Constructor"
        self.classVar1 = "Instance Var in B"

a = A()
b = B()

print(b.special)