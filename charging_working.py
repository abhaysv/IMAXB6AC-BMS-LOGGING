from struct import unpack, pack
from time import sleep
import time

from imax.b6mini import *

dev = B6Mini()

dev.print_charge_info()
dev.stop()

dev.charge(BAT_LIFE, 1, 0.1, 3.5)
while 1:
    dev.print_charge_info()
    time.sleep(2)
#dev.discharge(BAT_LIFE, 1, 0.3, 3.2)
