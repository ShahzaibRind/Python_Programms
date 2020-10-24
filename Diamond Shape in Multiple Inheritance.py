class A:
    def met(self):
        print("This is a Method from A")

class B(A):
    def met(self):
        print("This is a Method from B")

class C(A):
    def met(self):
        print("This is a Method from C")

class D(B, C):
    # def met(self):
        # print("This is a Method from D")
        pass

a = A()
b = B()
c = C()
d = D()

d.met()