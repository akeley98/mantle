import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(8)
megawing.LED.on(1)

main = megawing.main()
I = main.SWITCH
O = main.LED[0]

rom = ROM8(128*[0,1])

rom(I)
wire(rom.O, O)


compile(sys.argv[1], main)

