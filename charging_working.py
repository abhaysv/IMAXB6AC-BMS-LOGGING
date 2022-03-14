from struct import unpack, pack
from time import sleep
import time

from imax.b6mini import *

import csv

def create_csv_file():
    row_list = [["SN", "Volatge", "Current"]]
    with open('protagonist.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)

dev = B6Mini()

def log_charge_info():
    create_csv_file()
    i = 0;
    while 1:
        dev.print_charge_info()
        charge_info = dev.get_charge_info()
        row_list = [[i, charge_info.voltage, charge_info.current]]
        with open('protagonist.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(row_list)
        time.sleep(2)
#dev.discharge(BAT_LIFE, 1, 0.3, 3.2)

dev.charge(BAT_LIFE, 1, 0.1, 3.5)
log_charge_info()


