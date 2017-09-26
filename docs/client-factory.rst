.. _client-factory:

Get Client Factory Instance
###########################

For use V3 or V4 functions of GloboNetworkAPI client, you first need to instantiate the Client Factory.

First import ClientFactory class doing:

from networkapiclient.ClientFactory import ClientFactory

After it instantiate ClientFactory passing to it 5 (five) parameters in this order:

   networkapi_url - string representing URL that points to where GloboNetworkAPI service is running.
   user - string representing the name of the user that wants to access some GloboNetworkAPI functionality. Example: "networkapi_test".
   password - string representing the password of the user above specified that wants to access some GloboNetworkAPI functionality. Example: "networkapi_pwd".
   user_ldap - string representing the LDAP user of the registered user at GloboNetworkAPI Service. It's optional.
   log_level - string representing how client will manage LOG's. You can pass "ERROR", "WARN", "INFO", "DEBUG" or "TRACE". It's optional, if you don't pass anything the standard value will be "INFO".

Example:
   client = ClientFactory("http://localhost:8000/", "networkapi_user", "networkapi_pwd", "networkapi_user", "DEBUG")

