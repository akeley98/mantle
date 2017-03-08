import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
for i in range(6):
    icestick.J1[i].input().on()
icestick.J3[0].rename('D0').output().on()


main = icestick.main()

rom = ROM6(63*[0]+[1])
rom(main.J1)
wire(rom.O, main.D0)

compile(sys.argv[1], main)