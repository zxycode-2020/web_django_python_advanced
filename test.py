#!/usr/bin/env python
# coding: utf-8


def check_result(function):
    '''检查被装饰函数的返回值，确保不大于 1000'''
    def wrap(*args, **kwargs):
        result = function(*args, **kwargs)
        if result > 1000:
            return 0
        else:
            return result
    return wrap


@check_result
def foo(x, y):
    return x ** y


if __name__ == '__main__':
    # check_result -> wrap -> foo
    ww = check_result(foo)
    res = ww(3, 2)
    print(res)




