# -*- coding:utf-8 -*-
'''
Title: Infrastructure NetworkAPI
Author: masilva / s2it
Copyright: ( c )  2012 globo.com todos os direitos reservados.
'''

from networkapiclient.GenericClient import GenericClient
from networkapiclient.utils import get_list_map

class Permission(GenericClient):
    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication. 
        """
        super(Permission, self).__init__(networkapi_url, user, password, user_ldap)
        
    def list_all(self):
        """List all Permission.
        
        :return: Dictionary with the following structure:

        ::

            {'perms': [{ 'function' < function >, 'id': < id > }, ... more permissions ...]} 

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response. 
        """
        code, map = self.submit(None, 'GET', 'perms/all/')
        
        key = 'perms'
        return get_list_map(self.response(code, map, [key]), key)

