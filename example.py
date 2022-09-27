class A:

    def functionality1(self):
        print("func 1")

    def functionality2(self):
        print("func 2")

class B(A):
    pass

b = B()

b.functionality1()
b.functionality2()
    
