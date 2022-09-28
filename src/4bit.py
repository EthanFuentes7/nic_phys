import pigpio

# so do we like ask if they want to send or receive or like what im confused what he means by library
# are we making a method named nic_send() and nic_recv()

def nic_send(): # would the take in be in the parenthesis like it is for java or do we ask them
	n = input("input a 4 bit value where 1 turns transmitter on and 0 turns transmitte off")
	first_bit = n[0]
	second_bit = n[1]
	third_bit = n[2]
	fourth_bit = n[3]
	
	if(int (first_bit) == 1)
		pi.write(27,1)
	if(int (first_bit) == 0)
		pi.write(27,0)
	if(int (second_bit) == 1)
		pi.write(25,1)
	if(int (first_bit) == 0)
		pi.write(25,0)
	if(int (third_bit) == 1)
		pi.write(23,1)
	if(int (first_bit) == 0)
		pi.write(23,0)
	if(int (fourth_bit) == 1)
		pi.write(21,1)
	if(int (first_bit) == 0)
		pi.write(21,0)

def nic_recv():
	first_bit = pi.read(26)
	second_bit = pi.read(24)
	third_bit = pi.read(22)
	fourth_bit = pi.read(20)
	final_bits = first_bit + second_bit + third_bit + fourth_bit
	print(final_bits)
