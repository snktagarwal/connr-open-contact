# Author: Sanket Agarwal
# This file is meant to test the thrift objects for sanity, it uses thrift
# encoding and decoding protocols.



import sys

sys.path.append('./gen-py')

from connr.rest.ttypes import *
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport


def get_connr_jaccount_thrifted(credentials, contacts):

    #Create an object of connr_jaccount type with the input parameters

    acc = connr_jaccount()

    acc.credentials = credentials
    acc.contacts    = contacts

    return acc

def get_connr_timestamp_thrifted(yyyymmdd, hhmmss):

    #Create an object of connr_jaccount type with the input parameters

    tstamp = connr_timestamp()

    tstamp.date = yyyymmdd
    tstamp.time = hhmmss

    return tstamp

def get_thrift_bytes(thrift_obj):

    #Get the serialized form of data

    transportOut = TTransport.TMemoryBuffer()
    protocolOut  = TBinaryProtocol.TBinaryProtocol(transportOut)

    thrift_obj.write(protocolOut)

    return transportOut.getvalue()

def decode(thrift_bytes, sane_obj):

    #Get python readable data types

    transportIn = TTransport.TMemoryBuffer(thrift_bytes)
    protocolIn = TBinaryProtocol.TBinaryProtocol(transportIn)

    sane_obj.read(protocolIn)
    

    

if __name__ == '__main__':

    #First create some objects


    credentials = ['acc1','acc2','acc3']
    contacts    = [['acc1_con1','acc1_con2'],['acc2_con1'],['acc3_con1','acc3_con2','acc3_con3']]
    yyyymmdd    = 20090707
    hhmmss      = 101010

    timestamp = get_connr_timestamp_thrifted (yyyymmdd, hhmmss)
    jaccount  = get_connr_jaccount_thrifted  (credentials, contacts)

    
    print "Objects successfully written !\n\n"

    #Get the byte values of the objects, serialized data that is

    timestamp_bytes = get_thrift_bytes(timestamp)
    jaccount_bytes  = get_thrift_bytes(jaccount)

    print 'Timestamp: ', repr(timestamp_bytes), '\n\n\n\n','JAccount: ', repr(jaccount_bytes), '\n\n\n\n'

    print "Serialized data printed successfully !\n\n"

    #Deserialize the data

    timestamp_sane = connr_timestamp()
    decode(timestamp_bytes, timestamp_sane)

    print "Decoded timestamp: ",timestamp_sane.date," : ", timestamp_sane.time, '\n\n'

    jaccount_sane  = connr_jaccount()
    decode(jaccount_bytes, jaccount_sane)

    print "Decoded JAccount: \nCredentials: ",jaccount_sane.credentials,"\nContacts: ",jaccount_sane.contacts, '\n'
