import pytest
from magma import compile
from magma.testing import check_files_equal
from mantle.lattice.mantle40.halfadder import HalfAdder
import mantle
from mantle.lattice.mantle40.arith import \
    DefineAdd, DefineSub, DefineNegate
from fault.test_vectors import generate_function_test_vectors, \
    generate_simulator_test_vectors

width = 2
mask = 2**width-1
shift = 2

def sim(Test, TestFun):
    tvsim = generate_simulator_test_vectors(Test)
    tvfun = generate_function_test_vectors(Test, TestFun)
    assert tvsim == tvfun

def com(Test, name):
    name = 'test_{}'.format(name)
    build = 'build/' + name
    gold = 'gold/' + name
    compile(build, Test)
    assert check_files_equal(__file__, build+'.v', gold+'.v')


def test_ha():
    Test = HalfAdder
    com( Test, 'ha' )

def test_fa():
    Test = mantle.FullAdder
    assert mantle.FullAdder is mantle.lattice.mantle40.FullAdder
    # This is actually true since FullAdder is cached based on the name, so the
    # redefinition doesn't cause a problem here
    # assert mantle.FullAdder is not mantle.common.arith.FullAdder
    com( Test, 'fa' )

def test_add():
    Test = DefineAdd(width)
    sim( Test, lambda x, y: (x + y) & mask )
    com( Test, 'add{}'.format(width) )

def test_sub():
    Test = DefineSub(width)
    sim( Test, lambda x, y: (x - y) & mask )
    com( Test, 'sub{}'.format(width) )

def test_negate():
    Test = DefineNegate(width)
    sim( Test, lambda x: -x & mask )
    com( Test, 'negate{}'.format(width) )

