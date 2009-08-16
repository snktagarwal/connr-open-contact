# This is a simple interface to the prosody XMPP server and presently takes care of simple use cases like
# creation, deletion of accounts. It should be used in further development to change the server if required!

# Note that this script should be run with privellages that can allow prosody databases to be accessed.
# If you are not sure enough, use sudo/root privellages( is that a stiable idea ? )

# Import the Lunatic Python, Lua-Python, interpolability module
import lua

# Import the Lua side of API
lua.require('prosody_api')

# Import types module for assertion reasoning
import types

class XMPPApi:

	def isUser(self, uname, host):
	
		# Check if we have got valid strings
		
		assert ( type(uname) == types.StringType ) and ( type(host) == types.StringType )
		
		# Evaluate the function from the prosody API
		
		pro_isUser = 'isUser("'+uname+'","'+host+'")'
		
		return lua.eval(pro_isUser)
		
	def createUser(self, uname, passwd, host):
	
		# Check if we got valid strings
		assert ( type(uname) == types.StringType ) and ( type(host) == types.StringType ) and ( type(passwd) == types.StringType )
		
		# Evaluate the function from the prosody API		
		pro_createUser = 'createUser("'+uname+'","'+passwd+'","'+host+'")'
		lua.eval(pro_createUser)

	def deleteUser(self, uname, host):
		
		# Check if we got valid strings
		assert ( type(uname) == types.StringType ) and ( type(host) == types.StringType )
		
		# Evaluate the function from the prosody API
		pro_deleteUser = 'deleteUser("'+uname+'","'+host+'")'
		lua.eval(pro_deleteUser)
		

if __name__ == '__main__':
	
		# Do some unit testing!
		xmpp_server = XMPPApi()
		for i in range(1000):
			xmpp_server.createUser("orkut","mypass","localhost")
			print xmpp_server.isUser("orkut","localhost")
			xmpp_server.deleteUser("orkut",  "localhost")		
			print xmpp_server.isUser("orkut", "localhost")
	
		

