        #!/bin/env python
        """
        Demo standalone Connr Service Python FastCGI daemon using "flup" FastCGI->WSGI server behind Nginx.
        """
from flup.server.fcgi import WSGIServer
import time, os, sys
import optparse

import sys
sys.path.append('/usr/local/nginx/thrift/gen-py/')
from connr.rest.ttypes import *
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport

__usage__ = "%prog -n <num>"
__version__ = "1.0.0"

#FCGI_LISTEN_ADDRESS = ('localhost', 9000)
FCGI_SOCKET_DIR = '/tmp'
FCGI_SOCKET_UMASK = 0111

class test:
        

def thrift_details(thrift_bytes):
	transportIn = TTransport.TMemoryBuffer(thrift_bytes)
	protocolIn = TBinaryProtocol.TBinaryProtocol(transportIn)
	
	jaccount = connr_jaccount()
	jaccount.read(protocolIn)
	print jaccount.credentials 	
	return str(jaccount.credentials)



def myapp(environ, start_response):
    """Dummy response handler"""
    # SLEEP 100 ms to force a demostration of parallel threading performance
    time.sleep(0.1)
    #---------------------------------------------
    # A Dummy call to test the Thrift Object Transfer!
    
    start_response('200 OK', [('Content-Type', 'text/plain')])
    pretty_env = '\n'.join(['%s: %s' % (repr(k),repr(v)) for (k,v) in environ.items()])
    print "POST: "+repr(environ['wsgi.input'].read())
    msg = '''\
Connr Service Hello World!
Time: %s
PID %s\n
%s\n
POST-DATA: %s
Thrift: %s''' % (time.ctime(), os.getpid(), pretty_env, environ['wsgi.input'].readline(), environ['wsgi.input'].readline())
    return [msg]

def get_application():
    return myapp

def get_socketpath(name, server_number):
    return os.path.join(FCGI_SOCKET_DIR, 'fcgi-%s-%s.socket' % (name, server_number))

def main(args_in, app_name="hello"):
    p = optparse.OptionParser(description=__doc__, version=__version__)
    p.set_usage(__usage__)
    p.add_option("-v", action="store_true", dest="verbose", help="verbose logging")
    p.add_option("-n", type="int", dest="server_num", help="Server instance number")
    opt, args = p.parse_args(args_in)

    if not opt.server_num:
        print "ERROR: server number not specified"
        p.print_help()
        return

    socketfile = get_socketpath(app_name, opt.server_num)
    #app = get_application()

    try:
        WSGIServer(get_application(),
               bindAddress = socketfile,
               umask = FCGI_SOCKET_UMASK,
               multiplexed = True,
               ).run()
    finally:
        # Clean up server socket file
        os.unlink(socketfile)

if __name__ == '__main__':
    main(sys.argv[1:])


