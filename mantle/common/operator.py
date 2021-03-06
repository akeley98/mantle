from functools import wraps

import magma as m
from magma.bitutils import seq2int
from mantle import And, NAnd, Or, NOr, XOr, NXOr, LSL, LSR, Not, Invert
from mantle import ASR
from mantle import EQ, NE, ULT, ULE, UGT, UGE, SLT, SLE, SGT, SGE
from mantle import Mux
from .arith import Add, Sub, Negate

__all__ = []


def get_length(value):
    if isinstance(value, m._BitType):
        return None
    elif isinstance(value, m.ArrayType):
        return len(value)
    else:
        raise NotImplementedError(f"Cannot get_length of {type(value)}")


def check_operator_args(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        if len(args) < 2:
            raise RuntimeError(
                f"{fn.__name__} requires at least 2 arguments")
        width = get_length(args[0])
        if not all(get_length(x) == width for x in args):
            raise ValueError(
                f"All arguments should have the same length: {args}")
        T = type(args[0])
        if not (all(issubclass(type(x).__class__, T.__class__) for x in args) or (
                all(issubclass(T.__class__, type(x).__class__) for x in args))):
            raise TypeError(
                "Currently Arguments to operators must be of the same type")
        return fn(width, *args, **kwargs)
    return wrapped


operators = {}


def _pass_closure_vars_as_args(*closure_args):
    def _wrapped(fn):
        @wraps(fn)
        def _wrapped_inner(*args, **kwargs):
            return fn(*closure_args, *args, **kwargs)
        return _wrapped_inner
    return _wrapped


def export(fn):
    global __all__
    __all__ += [fn.__name__]
    return fn


def preserve_type(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        retval = fn(*args, **kwargs)
        T = type(args[0])
        if isinstance(T, m.UIntKind):
            return m.uint(retval)
        elif isinstance(T, m.SIntKind):
            return m.sint(retval)
        return retval
    return wrapper


for _operator_name, _Circuit in (
    ("and_", And),
    ("nand", NAnd),
    ("or_", Or),
    ("nor", NOr),
    ("xor", XOr),
    ("nxor", NXOr),
    ("add", Add),
    ("sub", Sub),
    # TODO: These lack implementations
    # ("mul", Mul),
    # ("div", Div)
):
    __all__ += [_operator_name]

    # Because Python uses dynamic scoping, the closures will use the
    # last value of _Circuit rather than capturing the lexical value.
    # Hacky workaround is to pass _Circuit as an argument to a
    # decorator so the "lexical" value is captured.
    @preserve_type
    @check_operator_args
    @_pass_closure_vars_as_args(_Circuit, _operator_name)
    def operator(circuit, name, width, *args, **kwargs):
        if name in ["add", "sub"]:
            # These don't have a height
            if len(args) > 2:
                raise Exception(f"{name} operator expects 2 arguments")
            return circuit(width, **kwargs)(*args)
        else:
            return circuit(len(args), width, **kwargs)(*args)
    operator.__name__ = _operator_name
    operator.__qualname__ = _operator_name
    operators[_operator_name] = operator
    exec(f"{_operator_name} = operator")


@export
@preserve_type
def lsl(I0, I1, **kwargs):
    width = get_length(I0)
    return LSL(width, **kwargs)(I0, I1)


@export
@preserve_type
def lsr(I0, I1, **kwargs):
    width = get_length(I0)
    return LSR(width, **kwargs)(I0, I1)


@export
@preserve_type
def asr(I0, I1, **kwargs):
    width = get_length(I0)
    return ASR(width, **kwargs)(I0, I1)


@export
@preserve_type
def not_(arg, **kwargs):
    return Not(**kwargs)(arg)


@export
@preserve_type
def invert(arg, **kwargs):
    width = get_length(arg)
    if width is None:
        return Not(**kwargs)(arg)
    else:
        return Invert(width, **kwargs)(arg)


@export
@preserve_type
def neg(arg, **kwargs):
    if isinstance(arg, int):
        return -arg
    return Negate(get_length(arg), **kwargs)(arg)


bitwise_ops = [
    ("__and__", and_),
    ("__or__", or_),
    ("__xor__", xor),
    ("__invert__", invert),
    ("__lshift__", lsl),
    ("__rshift__", lsr),
]

for method, op in bitwise_ops:
    if op not in (lsl, lsr):
        setattr(m.BitType, method, op)
    setattr(m.BitsType, method, op)

arithmetic_ops = [
    ("__neg__", neg),
    ("__add__", add),
    ("__sub__", sub),
    # ("__mul__", mul),
    # ("__div__", div)
]


@export
@check_operator_args
def lt(width, I0, I1, **kwargs):
    if isinstance(I0, m.SIntType):
        return SLT(width, **kwargs)(I0, I1)
    else:
        return ULT(width, **kwargs)(I0, I1)


@export
@check_operator_args
def le(width, I0, I1, **kwargs):
    if isinstance(I0, m.SIntType):
        return SLE(width, **kwargs)(I0, I1)
    else:
        return ULE(width, **kwargs)(I0, I1)


@export
@check_operator_args
def gt(width, I0, I1, **kwargs):
    if isinstance(I0, m.SIntType):
        return SGT(width, **kwargs)(I0, I1)
    else:
        return UGT(width, **kwargs)(I0, I1)


@export
@check_operator_args
def ge(width, I0, I1, **kwargs):
    if isinstance(I0, m.SIntType):
        return SGE(width, **kwargs)(I0, I1)
    else:
        return UGE(width, **kwargs)(I0, I1)


@export
@check_operator_args
def eq(width, I0, I1, **kwargs):
    return EQ(width, **kwargs)(I0, I1)


@export
@check_operator_args
def ne(width, I0, I1, **kwargs):
    return NE(width, **kwargs)(I0, I1)


relational_ops = [
    ("__lt__", lt),
    ("__le__", le),
    ("__gt__", gt),
    ("__ge__", ge),
]

for method, op in arithmetic_ops + relational_ops:
    setattr(m.SIntType, method, op)
    setattr(m.UIntType, method, op)

for type_ in (m._BitType, m.ArrayType):
    setattr(type_, "__eq__", eq)
    setattr(type_, "__neq__", ne)


@export
@preserve_type
def mux(I, S):
    if isinstance(S, int):
        return I[S]
    elif S.const():
        return I[seq2int(S.bits())]
    return Mux(len(I), get_length(I[0]))(*I, S)
