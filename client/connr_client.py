#!/bin/evn python

"""
A simple implementation of the Connr Client
"""

import sys
sys.path.append('../thrift/gen-py')
import connr.rest
import connr.rest.ttypes
from connr.rest.ttypes import *

from connr_client_thrift import ConnrClientThriftInterface as ThriftInterface
from connr_client_transport import ConnrWEBServiceTransport as Transport

class TestClient:

    def createObject(self, type=None):

        #Creates a datatype based on the type defined, type(type) should be str

        assert ( type(type) == 'int' )

        if type == 1:

            #create a connr_jaccount node

            jaccount = createConnrJaccount()

        elif type == 2:

            #create a connr_timestamp node

            timestamp = createConnrTimestamp()


    def createConnrJaccount(self):

        #first create a timestamp node

        print "Input a comma list of credentials( Example: \"cred1,cred2,cred3\" ): "
        
        cred_raw = raw_input()
        cred_list = cred_raw.split(',')
        contact_list = []
        
        for i in range(len(cred_list)):

            #For each credential input the contacts

            print "Contacts for "+cred_list[i]+" ( Same format as credentials ): "

            cred_raw_contacts = raw_input()
            contact_list.append(cred_raw_contacts.split(','))

        jaccount = connr_jaccount()
        
        jaccount.contacts = contact_list
        jaccount.credentials = cred_list

        return jaccount

    def createConnrTimestamp(self):

        print "Input date in the format,YYYYMMDD Ex: 19891009: "

        raw_date = input()
        assert len(str(raw_date)) == 8

        print "Input time in the format,hhmmss Ex: 121212: "

        raw_time = input()
        assert len(str(raw_time)) == 6

        timestamp = connr_timestamp()
        timestamp.date = raw_date
        timestamp.time = raw_time

        return timestamp

    def sendThriftObject(self, object):
            
        transport = Transport()
        thrift_interface = ThriftInterface()

        object_bytes = thrift_interface.getObjectDump(object)

        return transport.sendData('http://localhost/fcgi-bin/hello/','thrift-x/application','POST',object_bytes)
        

             

if __name__ == '__main__':

    #Perform some simple object creation

    test_client = TestClient()

    jaccount = test_client.createConnrJaccount()

    print test_client.sendThriftObject(jaccount)

    # A clumsy-ugly test case -- Please please delete it asap :P

    #transport = Transport()
    #thrift_interface = ThriftInterface()
    #create_acc = connr_acc_req()
    #create_acc.username = 'testclient1'
    #create_acc.passwd       = 'testclientpass1'
    #object_bytes = thrift_interface.getObjectDump(create_acc)
    #reply = transport.sendData('http://localhost/xmpp-service/','thrift-x/application','POST',object_bytes)
