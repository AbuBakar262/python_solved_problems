class A:
    pass


class B:
    pass


class C:
    pass


class E:
    pass


"""
    Single Inheritance
"""


class B(A):
    pass


"""
    Multiple Inheritance
"""


class C(A, B):
    pass


"""
    Multilevel Inheritance
"""


class B(A):
    pass


class C(B):
    pass


"""
    Hierarchical Inheritance
"""


class B(A):
    pass


class C(A):
    pass


class D(A):
    pass


"""
    Hybrid Inheritance
"""


class B(A, C):
    pass


class F(B, E):
    pass


class G(E):
    pass
