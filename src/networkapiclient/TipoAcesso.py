# -*- coding:utf-8 -*-
'''
Title: Infrastructure NetworkAPI
Author: globo.com / TQI
Copyright: ( c )  2009 globo.com todos os direitos reservados.
'''

from networkapiclient.GenericClient import GenericClient
from networkapiclient.utils import get_list_map, is_valid_int_param
from networkapiclient.exception import InvalidParameterError

class TipoAcesso(GenericClient):
    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication. 
        """
        super(TipoAcesso, self).__init__(networkapi_url, user, password, user_ldap)
        
    def listar(self):
        """List all access types.

        :return: Dictionary with structure:

        ::

            {‘tipo_acesso’: [{‘id’: < id >, 
            ‘protocolo’: < protocolo >}, ... other access types ...]}   
        
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        code, map = self.submit(None, 'GET', 'tipoacesso/')
        
        key = 'tipo_acesso'
        return get_list_map(self.response(code, map, [key]), key) 
    
    def inserir(self, protocolo):
        """Insert new access type and returns its identifier.
        
        :param protocolo: Protocol.
        
        :return: Dictionary with structure: {‘tipo_acesso’: {‘id’: < id >}}

        :raise ProtocoloTipoAcessoDuplicadoError: Protocol already exists.
        :raise InvalidParameterError: Protocol value is invalid or none.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        tipo_acesso_map = dict()
        tipo_acesso_map['protocolo'] = protocolo
        
        code, xml = self.submit({'tipo_acesso':tipo_acesso_map}, 'POST', 'tipoacesso/')
        
        return self.response(code, xml) 

    
    def alterar(self, id_tipo_acesso, protocolo):
        """Edit access type by its identifier.
        
        :param id_tipo_acesso: Access type identifier.
        :param protocolo: Protocol.
        
        :return: None
        
        :raise ProtocoloTipoAcessoDuplicadoError: Protocol already exists.
        :raise InvalidParameterError: Protocol value is invalid or none.
        :raise TipoAcessoNaoExisteError: Access type doesn't exist.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_tipo_acesso):
            raise InvalidParameterError(u'Access type id is invalid or was not informed.')

        tipo_acesso_map = dict()
        tipo_acesso_map['protocolo'] = protocolo
        
        url = 'tipoacesso/' + str(id_tipo_acesso) + '/'
        
        code, xml = self.submit({'tipo_acesso':tipo_acesso_map}, 'PUT', url)
        
        return self.response(code, xml) 

    def remover(self, id_tipo_acesso):
        """Removes access type by its identifier.
        
        :param id_tipo_acesso: Access type identifier.

        :return: None
        
        :raise TipoAcessoError: Access type associated with equipment, cannot be removed.
        :raise InvalidParameterError: Protocol value is invalid or none.
        :raise TipoAcessoNaoExisteError: Access type doesn't exist.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_tipo_acesso):
            raise InvalidParameterError(u'Access type id is invalid or was not informed.')        

        url = 'tipoacesso/' + str(id_tipo_acesso) + '/'
        
        code, xml = self.submit(None, 'DELETE', url)
        
        return self.response(code, xml) 


