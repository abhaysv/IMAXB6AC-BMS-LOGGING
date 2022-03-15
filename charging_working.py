from struct import unpack, pack
from time import sleep
import time
from imax.b6mini import *
import csv

#-------------------------[CHARGING PARAMETERS]--------------------------------
#>>>>>>>>>[BATTERY OPERATING MODE]<<<<<<<<<
OPERATING_MODE = 2 # 1 FOR CHARGINF / 0 FOR DISCHARGE MODE
#>>>>>>>>>[FILENAME FOR LOGGING]<<<<<<<<<<<
filename = "LIPO"
#>>>>>>>>>[NUMBER OF CELLS]<<<<<<<<<<<<<<<<
NO_OF_CELLS = 1
#>>>>>>>>>[BATTERY TYPE]<<<<<<<<<<<<<<<<<<<
BAT_TYPE=BAT_LIFE
#>>>>>>>>>[CHARG/DISCH CURRENT (A)]<<<<<<<<
CURRENT_BATT = 0.7
#>>>>>>>>>[TARGET VOLTAGE]<<<<<<<<<<<<<<<<<
TARGET_VOLT_CHARG = 3.5
TARGET_VOLT_DISCH = 3.0
#------------------------------------------------------------------------------
filenamenew = filename+time.strftime("-%d-%m-%Y-%H_%M_%S")+'.csv'

def create_csv_file():
    timestr = time.strftime("-%d-%m-%Y-%H_%M_%S")
    row_list = [["SN", "Volatge", "Current", "mAH"]]
    with open(filenamenew, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)

dev = B6Mini()

def log_charge_info():
    create_csv_file()
    i = 0;
    while 1:
        dev.print_charge_info()
        charge_info = dev.get_charge_info()
        row_list = [[i, charge_info.voltage, charge_info.current, charge_info.mah]]
        with open(filenamenew, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(row_list)    
        time.sleep(0.5)
        i = i + 0.5
#dev.discharge(BAT_LIFE, 1, 0.3, 3.2)
if OPERATING_MODE == 1:
    dev.charge(BAT_LIFE, NO_OF_CELLS, CURRENT_BATT, TARGET_VOLT_CHARG)
    log_charge_info()
elif OPERATING_MODE == 2:
    log_charge_info()    
else:
    dev.discharge(BAT_LIFE, NO_OF_CELLS, CURRENT_BATT, TARGET_VOLT_DISCH)
    log_charge_info()


