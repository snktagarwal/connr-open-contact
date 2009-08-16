#!/bin/env python

"""
Implementation of the basic functions required by the Connr Client to do the thrift talking!
"""

import sys

sys.path.append('../thrift/gen-py')

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
