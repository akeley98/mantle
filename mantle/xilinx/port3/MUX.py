from magma import *
from ..spartan3.CLB import *

__all__  = ['Mux2', 'Mux4', 'Mux8', 'Mux16']
__all__ += ['MuxN']
__all__ += ['DefineMux', 'Mux']

#
# C ? B : A
#
MUX2DATA = (~A2&A0)|(A2&A1)

def Mux2():
    """Construct a Mux with 2 1-bit inputs."""
    lut = _LUT3(INIT=lutinit(MUX2DATA,1<<3))
    return AnonymousCircuit("I",  array(lut.I0, lut.I1), 
                            "S",  lut.I2,
                            "O",  lut.O)


# """Construct a Mux with 4 1-bit inputs."""
class Mux4(Circuit):
    IO = ["I", In(Bits(4)), "S", In(Bits(2)), "O", Out(Bit) ]
            
    @classmethod
    def definition(mux4):

        mux0 = Mux2()
        mux1 = Mux2()
        mux = MUXF5()

        mux0(mux4.I[0:2],mux4.S[0]) 
        mux1(mux4.I[2:4],mux4.S[0])
        mux( mux0.O, mux1.O, mux4.S[1] )
        wire( mux.O, mux4.O )

# """Construct a Mux with 8 1-bit inputs."""
class Mux8(Circuit):
    IO = ["I", In(Array8), "S", In(Bits(3)), "O", Out(Bit) ]
            
    @classmethod
    def definition(mux8):

        mux0 = Mux4()
        mux1 = Mux4()
        mux = MUXF6()

        mux0(mux8.I[0:4], mux8.S[0:2]) 
        mux1(mux8.I[4:8], mux8.S[0:2])
        mux( mux0.O, mux1.O, mux8.S[2] )
        wire( mux.O, mux8.O )

# """Construct a Mux with 16 1-bit inputs."""
class Mux16(Circuit):
    IO = ["I", In(Array16), "S", In(Bits(4)), "O", Out(Bit) ]
            
    @classmethod
    def definition(mux16):

        mux0 = Mux8()
        mux1 = Mux8()
        mux = MUXF6()

        mux0(mux16.I[0:8],  mux16.S[0:3])
        mux1(mux16.I[8:16], mux16.S[0:3])
        mux(mux0.O, mux1.O, mux16.S[3])
        wire(mux.O, mux16.O)

def MuxN(height):

    assert height in [2, 4, 8, 16]

    if height == 2:
        return Mux2()
    elif height == 4:
        return Mux4()
    elif height == 8:
        return Mux8()
    elif height == 16:
        return Mux16()

# Mux Module name
def _MuxName(height, width):
    return 'Mux%dx%d' % (height, width)

def _MuxInterface(height, width):
    AW = In(Array(width,Bit))
    if   height == 2:
        args = ['I0', AW, 
                'I1', AW]
        args += ['S', In(Bit)]
    elif height == 4:
        args = ['I0', AW, 
                'I1', AW,
                'I2', AW,
                'I3', AW]
        args += ['S', In(Bits(2))]
    elif height == 8:
        args = ['I0', AW, 
                'I1', AW,
                'I2', AW,
                'I3', AW,
                'I4', AW,
                'I5', AW,
                'I6', AW,
                'I7', AW]
        args += ['S', In(Bits(3))]
    elif height == 16:
        args = ['I0',  AW, 
                'I1',  AW,
                'I2',  AW,
                'I3',  AW,
                'I4',  AW,
                'I5',  AW,
                'I6',  AW,
                'I7',  AW,
                'I8',  AW, 
                'I9',  AW,
                'I10', AW,
                'I11', AW,
                'I12', AW,
                'I13', AW,
                'I14', AW,
                'I15', AW]
        args += ['S', In(Bits(4))]

    args += ['O', Out(AW)]

    return args


def DefineMux(height, width):

    """
    Construct a Mux. Height inputs are width bits wide.
    """

    assert height in [2, 4, 8, 16]

    class _Mux(Circuit):
        name = _MuxName(height, width)
        IO = _MuxInterface(height, width)
        @classmethod
        def definition(Mux):
            def amux(y):
                return curry(MuxN(height), prefix='I')
            mux = braid(col(amux, width), forkargs=['S'])

            if   height == 2:  mux( Mux.I0, Mux.I1, Mux.S )
            elif height == 4:  mux( Mux.I0, Mux.I1, Mux.I2, Mux.I3, Mux.S )
            elif height == 8:  mux( Mux.I0, Mux.I1, Mux.I2, Mux.I3, 
                                    Mux.I4, Mux.I5, Mux.I6, Mux.I7, Mux.S )
            elif height == 16: mux( Mux.I0, Mux.I1, Mux.I2, Mux.I3, 
                                    Mux.I4, Mux.I5, Mux.I6, Mux.I7, 
                                    Mux.I8, Mux.I9, Mux.I10, Mux.I11, 
                                    Mux.I12, Mux.I13, Mux.I14, Mux.I15, Mux.S )
            wire( mux.O, Mux.O )
    return _Mux

def Mux(height, width):
    return DefineMux(height, width)()

