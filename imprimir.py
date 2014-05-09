# encoding: utf-8
from escpos import *
import usb
busses = usb.busses()
for bus in busses:
	for dev in bus.devices:
		try:
			a = (int(hex(dev.idVendor), 16))
			b = (int(hex(dev.idProduct), 16))
			OO = printer.Usb(a, b)
			OO.text("Impresión con Ticketera USB\n")
			OO.text("===========================\n")
			# OO.image("logo.gif")
			# OO.barcode
			# OO.barcode('1324354657687','EAN13',64,2,'','')
			OO.text("\n")
			OO.text("\n")
			OO.cut()
		except Exception, e:
			pass