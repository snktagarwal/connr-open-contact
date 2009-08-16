#!/bin/env python
""" This module will provide a WEB interface to the XMPP Server API.
    This service shall be partially RESTful using Thrift as a serialization
    technique. The following objectives are to be satisfied:

    1. Request to make a new account on the XMPP server. Appropriate reply
    2. Delete a specific account from the server.
    3. Query information about a user. TODO# Impl it in the API first!
"""

# Add the thrift generated code for python
import sys
sys.path.append('/usr/local/nginx/thrift/gen-py/')
sys.path.append('/usr/local/nginx/thrift/')


from flup.server.fcgi import WSGIServer   #WSGI: http://www.python.org/dev/peps/pep-0333/
import time, os, sys
import optparse

# Thrift API
from connr.rest.ttypes import * #TODO: Remove this module after testing!
from connr.rest.ttypes import *
from connr_thrift import ThriftInterface

# Server API
from prosody_api import XMPPApi 

accepted_http_req = ['GET','POST','DELETE']

class XMPPServer:
    fcgi_socket_umask = 0111
    fcgi_socket_dir = '/tmp'
    host                = 'localhost'
    
    def __init__(self):
        
        self.thrift_interface    = ThriftInterface()
        self.xmpp                = XMPPApi()


    def getSocketPath(self, name, server_number):
        return os.path.join(self.fcgi_socket_dir,  '%s-%s.socket' % (name, server_number))

    def authHeaderOr404(self,environ, start_response):

        http_request_type = environ['REQUEST_METHOD']
        
        if not http_request_type in accepted_http_req:

            start_response('404 Not Found', [('Content-Type', 'text/plain')])
        
        else:

            start_response('200 OK', [('Content-Type', 'text/plain')])


    def handleRequest(self, environ, start_response):

        # Get the request method of the query
        http_request_type = environ['REQUEST_METHOD']

        # Start the response header by checking the Request type
        if not http_request_type in accepted_http_req:
            start_response('404 Not Found', [('Content-Type', 'text/plain')])

        # TODO: Some sort of authentication of the requesting entity ?
        # Decide on the basis of Request Method what to do
        
        if http_request_type == accepted_http_req[0]:

            # GET
            # TODO: Implement this
            # The functionality should preferably return account information
            start_response('200 OK', [('Content-Type', 'text/plain')])
        
        elif http_request_type == accepted_http_req[1]:

            # POST
            # Create the Account on the server.
            
            acc = connr_acc_req()
            self.thrift_interface.getPyObject(environ['wsgi.input'].read(), acc)
            
            print acc.username, acc.passwd
            
            success = self.xmpp.createUser(acc.username, acc.passwd, 'localhost')

            # Return success, but how ? Some tokens

            if success == true:
                # Return a Success string to the Connr Web Service regarding
                # the creation of the account.
                start_response('201 Created', [('Content-Type', 'text/plain')])
                return ""
                
            
            else:
                # Return a Faliure string to the Connr Web Service regarding
                # the faliure of account creation
                start_response('500 Internal Server Error', [('Content-Type', 'text/plain')])
                return 
                    
                
            

        elif http_request_type == accepted_http_req[2]:
            
            # DELETE
            # Delete a specified account from the server

            acc = connr_acc_del()
            self.thrift_interface.getPyObject(environ['wsgi.input'].read(), acc)
            self.xmpp.deleteUser(acc.username, acc.passwd)

        else:

            # This should really not happen, maybe some bug ?
            return "Method not supported\n"


if __name__ == '__main__':

    # Start the server

    args_in = sys.argv[1:]
    __usage__ = "%prog -n <num>"
    __version__ = "1.0.0"    


    xmpp_server = XMPPServer()
    xmpp_server.xmpp.createUser('testaaa','testbbb','localhost')
    
    p = optparse.OptionParser(description=__doc__, version=__version__)
    p.set_usage(__usage__)
    p.add_option("-v", action="store_true", dest="verbose", help="verbose logging")
    p.add_option("-n", type="int", dest="server_num", help="Server instance number")
    opt, args = p.parse_args(args_in)

    if not opt.server_num:
        print "ERROR: server number not specified"
        p.print_help()
        exit()

    socketfile = xmpp_server.getSocketPath('xmpp_service', opt.server_num)

    try:
        WSGIServer(xmpp_server.handleRequest,
               bindAddress = socketfile,
               umask = xmpp_server.fcgi_socket_umask,
               multiplexed = True,
               ).run()
        
    finally:
        # Clean up server socket file
        os.unlink(socketfile)


        

    

    

