# -*- coding:utf-8 -*-

from networkapiclient.GenericClient import GenericClient

class BlockRule(GenericClient):
    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication. 
        """
        super(BlockRule, self).__init__(networkapi_url, user, password, user_ldap);

    def get_rule_by_id(self, rule_id):
        
        """Get rule by indentifier.
        
        :param rule_id: Rule identifier
        
        :return: Dictionary with the following structure:

        ::

            {'rule': {'environment': < environment_id >,
            'content': < content >,
            'custom': < custom >,
            'id': < id >,
            'name': < name >}}
        
        :raise UserNotAuthorizedError: User dont have permition.
        :raise InvalidParameterError: RULE identifier is null or invalid.
        :raise DataBaseError: Can't connect to networkapi database.
        """
        
        url = "rule/get_by_id/" + str(rule_id)
        
        code, xml = self.submit(None, 'GET', url)
        
        return self.response(code, xml, ['rule_contents', 'rule_blocks'])
    