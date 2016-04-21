from math import *
from numpy import *

def Calc_Bot(self,msg):
	input_calc = msg['text']
	input_calc = input_calc.replace("/calc ","",1)
	output = eval(input_calc)
	self.sender.sendMessage("%s" % (output))

__commands__ = {
	"/calc" : Calc_Bot

}
