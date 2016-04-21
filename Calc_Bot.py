from math import *

def Calc_Bot(self,msg):
	input_calc = msg['text']
	input_calc = input_calc.replace("/calc","",1)
	print(input_calc)
	output = eval(input_calc)
	self.sender.sendMessage("%s = %s" % (input_calc,output))

__commands__ = {
	"/calc" : Calc_Bot

}
