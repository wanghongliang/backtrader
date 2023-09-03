def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""

    # This requires a bit of explanation: the basic idea is to make a dummy
    # metaclass for one level of class instantiation that replaces itself with
    # the actual metaclass.

    class metaclass(meta):
        print('metaclass类要生成啦')

        def __new__(cls, name, this_bases, d):
            print('我是cls:', cls)
            print(name)

            for i in this_bases:
                print("--", type(i), i)
            print(this_bases, type(this_bases[0]))
            print(d)
            return meta(name, bases, d)
        # str('temporary_class2222') 指定类名。这将成为类的属性。__name__
        # type.__new__ 第一个参数必须是 type 的子类， 因为要用 type 类的 __new__方法
        # 第2个参数是类名
        # type.__new__ 和 type(name,parent,attr)
        # 区别是， type.__new__ 指定一个type类的__new__方法来调用，生成新的class

    return type.__new__(metaclass, str('temporary_class2222'), (), {})

class MetaBase(type):
    def doprenew(cls, *args, **kwargs):
        return cls, args, kwargs

    def donew(cls, *args, **kwargs):
        _obj = cls.__new__(cls, *args, **kwargs)
        return _obj, args, kwargs

    def dopreinit(cls, _obj, *args, **kwargs):
        return _obj, args, kwargs

    def doinit(cls, _obj, *args, **kwargs):
        _obj.__init__(*args, **kwargs)
        return _obj, args, kwargs

    def dopostinit(cls, _obj, *args, **kwargs):
        return _obj, args, kwargs


    #改写创建对象的初始化调用方式
    def __call__(cls, *args, **kwargs):
        cls, args, kwargs = cls.doprenew(*args, **kwargs)
        _obj, args, kwargs = cls.donew(*args, **kwargs)
        _obj, args, kwargs = cls.dopreinit(_obj, *args, **kwargs)
        _obj, args, kwargs = cls.doinit(_obj, *args, **kwargs)
        _obj, args, kwargs = cls.dopostinit(_obj, *args, **kwargs)
        return _obj


class mclass(type):
    def __new__(cls, name, *args, **kwargs):
        print('mclass元类要创造类啦,运行__new__函数')
        print(cls)
        print(name)
        print(args)     
        print(kwargs)
        return cls

    def __call__(self, *args, **kwargs):
        print('mclass的对象运行__call__函数啦')
        print(args)
        print(kwargs)
        return self

class mclass2(with_metaclass(mclass, mclass.__class__)):
    def __new__(cls, name, *args, **kwargs):
        print('mclass2元类要创造类啦,运行__new__函数')
        print(cls)
        print(name)
        print(args)
        print(kwargs)
        #cls = super(mclass2, meta).__new__(meta, name, args, kwargs)
        return cls

    def __call__(self, *args, **kwargs):
        print('mclass2的对象运行__call__函数啦')
        print(args)
        print(kwargs)
        return self
class mobject(object):
    name = 'mobject'
class example3(mclass2 ):
    print('准备创造example3类')
    def __new__(meta, name, *args, **kwargs):
        print('example3类要创造对象啦，运行__new__函数')
        print(name)

        cls = super(example3, meta).__new__(meta, name, args, kwargs)
        return meta
    
    def __init__(self, name, *args, **kwargs):
        print('example3的对象运行__init__函数啦')
        print(name)
    # def __call__(self, *args, **kwargs):
    #     print('example3的对象运行__call__函数啦')
    #     print(args)
    #     print(kwargs)
    #     return self

#t1 = with_metaclass(example3, object)
#print(t1,type(t1),'what type is t1?')
#class Cerebro(example3):
#class Cerebro(example3('Cerebro',(mobject),{})):

#t1 = with_metaclass(example3, object)
#t2 = example3('Cerebro',(mobject),{})


class Cerebro(with_metaclass(example3, mobject)):
    print('Cerebro类要生成啦')
    attrs = {'a':'a'}
    def __new__(cls, name):
        print(name)
        return cls

# c = Cerebro()
#
# print(c.__class__)
# print(c.__class__.__class__)
# print(c.__class__.__class__.__class__)
# print(c.__class__.__class__.__class__.__class__)