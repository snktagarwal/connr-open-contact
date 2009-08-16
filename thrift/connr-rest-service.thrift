#This is a .thrift file for the Connr RESTful Web Interface.
#It determines the data structures defining the 
#interface between Connr Client and Connr RESTful Web Server

namespace py connr.rest

/**
 * Struct: connr_timestamp
 * Description: A UTC compliant Time Stamp
 * date is in the format YYYYMMDD
 * time is in the format hhmmss
 */

struct connr_timestamp{
 1: i64 date,
 2: i64 time,
}


/**
 * Struct: connr_jaccount
 * Description: A representation of account node.
 * 'credentials': is a list of user login credentials
 * 'contacts': has a list of contacts, for each login credential
 */

struct connr_jaccount{
 1: list<string> credentials,
 2: list<list<string>> contacts,
}

/**
 * Struct: xmpp_account
 * Description: A description of a xmpp_account which will be stored on the xmpp server. Can be typedeffed to various
 *				structs for passing b/w services that the project implemented
 * username : username of the XMPP account
 * passwd   : password for the account
 * TODO : What else ? Timestamps, some other authentication string ?
 */

struct xmpp_account{
 1: string username,
 2: string passwd,
}

/**
 * Struct: connr_reg_response
 * Description: A structure which will be passed to the client on successful
 * creation of a Connr XMPP Account.
 */
struct connr_reg_response{
 1: string username,
 2: string passwd,
}

/**
 * Struct: connr_acc_req
 * Description : A request( from the Connr WEB Service ), asking the XMPP server to create a account
 */
 
struct connr_acc_req{
 1: string username,
 2: string passwd,
}

/**
 * Struct: connr_acc_del
 * Description : A request( from the Connr WEB Service ), asking the XMPP server to delete a account
 */
 
struct connr_acc_req{
 1: string username,
 2: string passwd,
}
