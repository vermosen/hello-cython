

cpdef str hello(str arg):
    """
    Prints back 'Hello <param>', for example example: hello.hello('you')
    """
    return "Hello, %s!\n" % arg

cpdef double invoke(object func, double x):
    """
    execute the callback
    """
    return func(x)

cdef class math:
    cpdef double square(self, double x):
        return x * x

cpdef double callee(double x):
    return x + 1

cpdef double caller(object func, double x):
    cdef double tmp = func(x)
    return tmp * tmp


