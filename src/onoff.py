import pigpio

pi = pigpio.pi()
pi.set_mode(21, pigpio.OUTPUT)
pi.set_mode(23, pigpio.OUTPUT)
pi.set_mode(25, pigpio.OUTPUT)
pi.set_mode(27, pigpio.OUTPUT)
pi.set_mode(20, pigpio.INPUT) # dont actually know what to do with these
pi.set_mode(22, pigpio.INPUT)
pi.set_mode(24, pigpio.INPUT)
pi.set_mode(26, pigpio.INPUT)

q = input("choose 1 to enter 0 to exit")

while n != 0 && q != 0:
	n = input("choose a port 1-4 or 0 to exit")
	m = input("choose 1 to turn on/off transmitter or 2 to get state of receiver")

	if(int (n) == 1 && pi.read(27) == 0 && int (m) == 1):
		pi.write(27,1)
	if(int (n) == 1 && pi.read(27) == 1 && int (m) == 1):
		pi.write(27,0)
	if(int (m) == 2 && int (n) == 1)
		print(pi.read(26))
	if(int (n) == 2 && pi.read(25) == 0 && int (m) == 2):
		pi.write(25,1)
	if(int (n) == 2 && pi.read(25) == 1 && int (m) == 2):
		pi.write(25,0)
	if(int (m) == 2 && int (n) == 2)
		print(pi.read(24))
	if(int (n) == 3 && pi.read(23) == 0 && int (m) == 3):
		pi.write(23,1)
	if(int (n) == 3 && pi.read(23) == 1 && int (m) == 3):
		pi.write(23,0)
	if(int (m) == 2 && int (n) == 3)
		print(pi.read(22))
	if(int (n) == 4 && pi.read(21) == 0 && int (m) == 4):
		pi.write(21,1)
	if(int (n) == 4 && pi.read(21) == 1 && int (m) == 4):
		pi.write(21,0)
	if(int (m) == 2 && int (n) == 4)
		print(pi.read(20))
	else:
		print ("input a valid number")
