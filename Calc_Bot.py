from math import *
from numpy import *

def Calc_Bot(self,msg):
	input_calc = msg['text']
	input_calc = " ".join(filter(lambda x:x[0]!='/', input_calc.split()))
	output = eval(input_calc)
	self.sender.sendMessage("%s" % (output))

__commands__ = {
	"/calc" : Calc_Bot

}
