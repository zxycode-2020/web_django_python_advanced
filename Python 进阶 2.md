Python 进阶
===========

1. PEP8 编码规范, 以及开发中的一些惯例和建议
    * 代码编排: 缩进 4 个空格, 行长 80, 空行(函数间, 函数内, 文件结尾)
    * import: import 顺序; 单行不要 import 多个库; 模块内用不到的不要去 import
    * 空格
    * 注释
        - 行注释
        - 块注释
        - 引入外来算法或者配置时须在注释中添加源连接，标明出处
    * 函数和类尽可能添加 `__doc__`
    * 命名
        - 包名、模块名、函数名、方法名全部使用小写, 单词间用下划线连接
        - 类名、异常名使用CapWords的方式, 异常名结尾加 `Error` 或 `Wraning` 后缀
        - 全局变量尽量使用大写, 一组同类型的全局变量要加上统一前缀
        - 常量全部使用大写, 单词用下划线连接
    * 字符串拼接尽量使用 `join` 方式
    * 语意明确、直白
        - `not xx in yy` vs `xx not in yy`
        - `a not is b` vs `a is not b`
    * 一个函数只做一件事情, 并把这件事做好, 大的功能用小函数之间灵活组合来完成
    * 函数名必须有动词, 最好是 do_something 的句式, 或者 somebody_do_something 句式
    * 自定义的变量名、函数名不要与标准库中的名字冲突
    * pip install pep8
    * 练习: 规范化这段代码

            from django.conf import settings
            import sys, os
            MOD=0xffffffff
            def foo ( a , b = 123 ) :
                c = { 'x' : 111 , 'y' : 222 }#定义一个字典
                d = [ 1, 3 , 5 ]
                return a , b , c
            def bar(x):
                if x%2 ==0: return true

2. Python 的赋值和引用
    * `==, is`
    * `copy, deepcopy`
    * 练习1: 说出执行结果

            def extendList(val, list=[]):
                list.append(val)
                return list

            list1 = extendList(10)
            list2 = extendList(123,[])
            list3 = extendList('a')

    * 练习2: 说出下面执行结果

            from copy import copy, deepcopy
            from pickle import dumps, loads

            a = [1, 2, 3]
            b = [a] * 3
            c = copy(b)
            d = deepcopy(b)
            e = loads(dumps(b, 4))

            b[1].append(999)
            c[1].append(999)
            d[1].append(999)
            e[1].append(999)

    * 自定义 deepcopy: `my_deepcopy = lambda item: loads(dumps(item, 4))`

3. 迭代器, 生成器, itertools, yield, 列表/字典/集合的推导
    * iterator: 任何实现了 `__iter__` 和 `__next__` (python2中实现next()) 方法的对象都是迭代器.
        - `__iter__`返回迭代器自身，
        - `__next__` 返回容器中的下一个值
        - 如果容器中没有更多元素，则抛出StopIteration异常

    * generator: 生成器其实是一种特殊的迭代器, 不需要自定义 `__iter__` 和 `__next__`
        - 生成器函数 (yield)
        - 生成器表达式

    * 练习1: 自定义一个迭代器, 实现斐波那契数列

            class Fib(object):
                def __init__(self, max):
                    self.x = 0
                    self.y = 1
                    self.max = max

                def __iter__(self):
                    return self

                def __next__(self):
                    n_next = self.y
                    self.x, self.y = self.y, self.x + self.y
                    if self.max > self.x:
                        return n_next
                    else:
                        raise StopIteration()

    * 练习2: 自定义一个生成器函数, 实现斐波那契数列

            def fib(max):
                x = 0
                y = 1
                while y < max:
                    yield y
                    x, y = y, x + y

    * 迭代器、生成器有什么好处？
        - 节省内存
        - 惰性求值

4. `method`, `classmethod` 和 `staticmethod`
    * `method`: 通过实例调用时，可以引用类内部的任何属性和方法
    * `classmethod`: 无需实例化, 可以调用类属性和类方法，无法取到普通的成员属性和方法
    * `staticmethod`: 无论用类调用还是用实例调用，都无法取到类内部的属性和方法, 完全独立的一个方法

    * 练习: 说出下面代码的运行结果

            class Test(object):
                x = 123

                def __init__(self):
                    self.y = 456

                def bar1(self):
                    print('Hello world')

                @classmethod
                def bar2(cls):
                    print('Bad world')

                def foo1(self):
                    print(self.x)
                    print(self.y)
                    self.bar1()
                    self.bar2()

                @classmethod
                def foo2(cls):
                    print(cls.x)
                    cls.bar1()
                    cls.bar2()

                @staticmethod
                def foo3(obj):
                    print(obj.x)
                    print(obj.y)

                        t = Test()
                        t.foo1()
                        t.foo2()
                        t.foo3()

3. Python 魔术方法
    1. `__str__`, `__repr__`
    2. `__init__` 和 `__new__`
        - `__new__` 返回一个 对象的实例, `__init__` 无返回值
        - `__new__` 是一个类方法
            1. 先生成实例 `obj`
            2. 通过实例去掉用 `obj.__init__`

                    class A(object):
                        def __new__(cls, *args, **kwargs):
                            obj = object.__new__(cls)
                            obj.__init__(*args, **kwargs)
                            return obj
                        def __init__(self, x):
                            self.x = x

    3. 比较运算、数学运算
        - 比较运算符的重载: `__eq__, __ge__, __le__, __gt__, __gt__, __ne__`
        - 练习: 完成一个类，实现负无穷的概念

                class A(object):
                    def __le__(self, other):
                        return True
                    def __lt__(self, other):
                        return True
                    def __eq__(self, other):
                        return False
                    def __ge__(self, other):
                        return False
                    def __gt__(self, other):
                        return False

        - 运算符重载: `__add__, __sub__, __mul__, __div__, __mod__`

    4. 容器方法
        - `__len__, __iter__, __next__, __contains__`
        - `__getitem__, __setitem__, __missing__`
    5. 可执行对象: `__call__`
    6. with: `__enter__, __exit__`
    7. `__setattr__, __getattr__, __getattribute__, __dict__`
    8. 描述器: `__set__, __get__`
    9. `__slots__` 和内存优化

4. Python 性能之困
    0. 计算密集型，I/O 密集型
    1. Profile, timeit
    2. GIL 全局解释器锁
    3. 瓶颈在哪里：
        - 计算密集型: 用 C 语言补充
        - I/O 密集型: 多线程 / 多进程 / 协程, 阻塞 -> 非阻塞, 同步 -> 异步
    4. 什么是同步、异步、阻塞、非阻塞？
    5. 什么是进程、线程、协程？
        - 进程: 资源消耗大, 系统整体开销大, 数据通信不方便
        - 线程: 资源消耗小, 可共享数据。上下文开销大。按时间片强制切换, 不够灵活
        - 协程: 上下文切换开销更小, 内存开销更小。可根据事件切换, 更加有效的利用 CPU
    6. 事件驱动 + 多路复用
        - 轮询: select, poll
        - 事件驱动: epoll 有效轮询
    7. Greenlets / gevent | tornado / asyncio
    8. 线程安全, 锁
        - 获得锁之后, 一定要释放, 避免死锁
        - 获得锁之后, 执行的语句, 只跟被锁资源有关
    9. gevent
        - monkey.patch
        - gevent.sleep 非阻塞式等待
        - Queue 协程间数据交互, 避免竞争

5. 装饰器
    * 检查、预处理
        - 练习：写一个计数器的装饰器，被装饰函数每执行一次，计数器加一，并打印出当前执行次数
    * 缓存
    * 其他
    * 闭包

            local namespace
                |
                V
            global namespace
                |
                V
            builtin namespace

6. 一些技巧和误区
    1. 格式化打印 json
    2. 确保能取到有效值
        - `x.get(k, default)`
        - `d.setdefault`
        - `defaultdict`
        - `a or b`
    3. try...except... 的滥用
        - 不要把所有东西全都包住，程序错误需要报出来
        - 使用 try...except 要指明具体错误, try 结构不是用来隐藏错误的，而是用来有方向的处理错误的
    4. 利用 dict 做模式匹配

            mod = random.randint(1, 4)

            def do1():
                print('i am do1')

            def do2():
                print('i am do2')

            def do3():
                print('i am do3')

            def do4():
                print('i am do4')

            func = {1: do1, 2: do2, 3: do3, 4: do4}[mod]
            func()

    5. `inf, -inf, nan`
    6. `*args`, `**kwargs`, `foo(x, y, *, z, **kwargs)`, 强制显式参数 *
    7. pyenv, venv, 命名空间
        - pyenv: 管理 Python 版本
        - venv: 创建虚拟环境, 做环境隔离, venv 目录直接放到项目的目录里
    8. property: 把一个方法属性化
    9. 要批量修改、存取, 避免循环内单步获取：`for range(): db.get()` vs  `db.mget()`
    10. 三元运算: x = a if foo() else b
    11. else 字句: if, for, while, try
    12. foo(a, b=[])
    13. collections
        - defaultdict
        - namedtuple
        - Counter

7. 项目中的代码管理
    1. venv
    2. 代码结构管理, 目录树
    3. git
        - clone
        - status
        - add
        - commit
        - push
        - pull
        - merg
        - checkout
        - branch

8. 补充
    * 分享一些图书
    * Django -> json
