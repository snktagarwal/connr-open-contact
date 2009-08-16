#!/bin/env python

"""
The transport layer for clients.

Presently Implementing simply the Connr WEB Service Protocol
"""

import httplib2 as httplib

class ConnrWEBServiceTransport:

    h = httplib.Http("/tmp/.cache")

    def sendData(self,url,content_type,method='POST',body_data=None):

        if not body_data:

            #No HTTP Data, only headers

            resp, content = self.h.request(url,method,headers={'Content-Type':content_type})

        else:

            #Some HTTP Data, hmmm

            resp, content = self.h.request(url,method,body = body_data,headers={'Content-Type':content_type})


        return [resp,content]    
    
