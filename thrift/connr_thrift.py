#!/bin/env python

"""
Implementation of the basic functions required by the Connr Client to do the thrift talking!
"""

import sys

sys.path.append('/usr/local/nginx/thrift/gen-py/')

from connr.rest.ttypes import *
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport

class ConnrClientThriftInterface:

    def getObjectDump(self,thrift_obj):

        #Creates the bytes from the python-thrift object and returns them

        transportOut = TTransport.TMemoryBuffer()
        protocolOut  = TBinaryProtocol.TBinaryProtocol(transportOut)

        thrift_obj.write(protocolOut)

        return transportOut.getvalue()

    def getPyObject(self, thrift_bytes,saneObj):

        #Get python readable data types
        transportIn = TTransport.TMemoryBuffer(thrift_bytes)
        protocolIn = TBinaryProtocol.TBinaryProtocol(transportIn)
        print repr(thrift_bytes)
        try:
            saneObj.read(protocolIn)
        except:
            #Using wildcard exception because it throws an EOF error, which would lead to bad understanding
            #TODO: Add a wrapper to read, throwing an appropriate exception

            #Excepts exceptions thrown due to incorrectly thrift encoded objects

            saneObj = None #Let the server decide what to do!
