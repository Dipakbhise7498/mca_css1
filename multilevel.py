class A:
    def__init__(self):
    #def feature1(self):#
        print("__init__of class A constructor")    
    def feature2(self):
        print("feature 2 is working")  
                
class B(A):
    def feature3(self):
        print("feature 3 is working")
        
    def feature4(self):
        print("feature 4 is working")
            
a=A()
a.feature2()
b=B()
b.feature2()
    