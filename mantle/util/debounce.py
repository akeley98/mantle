from magma import *
from mantle import *

def debounce(a, slow):
    CLK = getCurrentDefinition().CLK
    ffa = FF(ce=True)
    wire(slow, ffa.CE)
    wire(CLK, ffa.CLK)
    ffa(a)
    ffb = FF(ce=True)
    wire(slow, ffb.CE)
    wire(CLK, ffb.CLK)
    ffb(ffa.O)
    return And2()(ffa.O, ffb.O)