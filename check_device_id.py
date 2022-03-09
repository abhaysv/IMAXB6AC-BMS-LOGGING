import usb.core

dev = usb.core.find(idVendor=0x0000, idProduct=0x0001)
if dev is None:
    raise ValueError('Device not found')
dev.set_configuration()
print("Read: ", dev.read(0x81, 7))
print("Write: ", dev.write(1, '0xB1')) 
