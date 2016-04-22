#!/usr/bin/env python

import logging, sys, json
import time
import stomp
#import pprint
import config
import yaml

NETWORK_RAIL_AUTH = (config.NR_USER, config.NR_PASSWORD)
feed = config.NR_TMVT_FEED_ID

locations = yaml.load(open("Location_Info.dat","rb"))

#pretty = pprint.PrettyPrinter(indent=4)

# Sourced from http://nrodwiki.rockshore.net/index.php/Python_Examples

class Listener(object):
    msg_list = []
    #output_string = None
    def __init__(self, mq):
        self._mq = mq
        self.msg_list = []

    def on_message(self, headers, message):
        self._mq.ack(id=headers['message-id'], subscription=headers['subscription'])
        self.msg_list.append(message) 
def Get_Feed_Info(self,feed):
    if feed == '':
        print("ERROR: Feed ID not provided")
        sys.exit()
    mq = stomp.Connection(host_and_ports=[('datafeeds.networkrail.co.uk', 61618)],
                          keepalive=True,
                          vhost='datafeeds.networkrail.co.uk',
                          heartbeats=(10000, 5000))

    listener = Listener(mq)
    mq.set_listener('', listener)

    mq.start()
    mq.connect(username=NETWORK_RAIL_AUTH[0],
               passcode=NETWORK_RAIL_AUTH[1],
               wait=True)

    mq.subscribe('/topic/%s' % feed, 'test-LM', ack='client-individual')
    while listener.msg_list == []:
	    time.sleep(2)
    return listener.msg_list

class TOC_Feed:
    def __init__(self,feedid):
        self.Train_Info = {}
        self.feed_id = feedid
    def getInfo(self):

        message_array = Get_Feed_Info(self,self.feed_id)
        message_list = json.loads(message_array[0])
        for i in range(0,len(message_list)):
            message_dict = message_list[i]
            for key in message_dict:
                skey = 'loc_stanox'
			#print pretty.pprint(message_dict)
                if skey in message_dict[key]:
                    self.Train_Info[message_dict[key]['train_id']] = {'Time': time.ctime((int(message_dict[key]['actual_timestamp'])-60*60*1000)/1E3),'Location ID': message_dict[key]['loc_stanox']}
	
    def getLastLocation(self, train_id):
	   
	    area = ''	
	    for i in range(0,len(locations)):
		    if int(locations[i]['STANOX']) == int(train_id):
			    area = locations[i]['STANME']
	    return area

    def getTime(self, key):
	    return self.Train_Info[key]['Time']

def NetRailBot(self,msg):
    self.sender.sendMessage("Accessing Feeds Please Wait...")
    LM_Feed = TOC_Feed(feed)
    LM_Feed.getInfo()
    Res_dict = LM_Feed.Train_Info
    out_string = ''
    for key in Res_dict:
        out_string += "Time: %s \t \nID: %s \t \nLast Location: %s \n-------------------\n" % (LM_Feed.getTime(key),key,LM_Feed.getLastLocation(Res_dict[key]['Location ID']))
    self.sender.sendMessage( 
".                               \n"
"            		    ___\n"+
"		       _____\   \______\n"+
"		      |_____     _____|\n"
"		       _____/   /______\n"+
"		      |_____     _____|\n"+
"		                \__\ \n\n"+

"	   NETWORK RAIL TRAIN MOVEMENT\n"
"		 REGION: LONDONMIDLAND\n\n%s" % (out_string))

__commands__ = {
        "/railstatus": NetRailBot 
}
