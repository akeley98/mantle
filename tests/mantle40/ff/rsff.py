import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].rename('I0').input().on()
icestick.J1[1].rename('I1').input().on()
icestick.D5.on()

main = icestick.main()

rsff = RSFF()

rsff(main.I0, main.I1)

wire(rsff, main.D5)

compile(sys.argv[1], main)