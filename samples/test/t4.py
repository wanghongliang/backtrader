class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


myclass = MyClass()
myclass.i = 2345
print( myclass.i )
MyClass.i  = 1
myclass2 = MyClass()
myclass2.i =2
print( myclass2.i )

print( MyClass.i )
print( myclass.i )