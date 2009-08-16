#A simple testbed Application to test Bootstraping

import sys
sys.path.append('/usr/local/nginx/thrift/')
sys.path.append('/usr/local/nginx/server/')
sys.path.append('/usr/local/nginx/client/')
sys.path.append('/usr/local/nginx/prosody/')

import connr_server
import connr_client
import connr_thrift
import connr_db
from connr_server_utils import ServerUtils


class BootStrap:

    def __init__(self):
        self._client_handle         = connr_client.TestClient()
        self._thrift_handle  = connr_thrift.ConnrThriftInterface()
        self._server_handle         = connr_server.ConnrServer()

    
    def sendThriftDataToServer(self):

        jaccount = self._client_handle.createConnrJaccount()
        jaccount_bytes = self._thrift_handle.getObjectDump(jaccount)

        self._server_handle.testHandleThriftData(jaccount_bytes)

    def convertThriftObjToClientIDDoc(self):

        #CLIENT
        
        # Create a test jaccount on client
        
        jaccount = self._client_handle.createConnrJaccount()

        # Data sent over to server, server recieves it and decodes it

        # Convert data to client ID Document

        doc = self._thrift_handle.thriftObjToClientIDDoc(jaccount)

        return doc
        


if __name__ == '__main__':

    bs              = BootStrap()
    #bs.sendThriftDataToServer()
    doc             = bs.convertThriftObjToClientIDDoc()
    server_handle   = connr_db.ConnrDBServer().getDBServerHandle()
    db_handle       = connr_db.ConnrDBDatabase(server_handle, 'test-1')
    print db_handle.saveNewDocToDB(doc)
    server_utils = ServerUtils()
    print server_utils.passwd_gen(12, True)    
    
        

        
