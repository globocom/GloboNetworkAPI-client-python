# -*- coding:utf-8 -*-
'''
Title: Infrastructure NetworkAPI
Author: globo.com / TQI
Copyright: ( c )  2009 globo.com todos os direitos reservados.
'''

from networkapiclient.GenericClient import GenericClient
from networkapiclient.utils import get_list_map, is_valid_int_param
from networkapiclient.exception import InvalidParameterError


class AmbienteLogico(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            AmbienteLogico,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def listar(self):
        """List all Logical Environment.

        :return: Dictionary with the following structure:

        ::

            {'logical_environment':
            [{'id': < id >,
            'nome': < nome >}, ...more Logical Environment...]}

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        code, map = self.submit(None, 'GET', 'logicalenvironment/all/')

        key = 'logical_environment'
        return get_list_map(self.response(code, map, [key]), key)

    def inserir(self, name):
        """Inserts a new Logical Environment and returns its identifier.

        :param name: Logical Environment name. String with a minimum 2 and maximum of 80 characters

        :return: Dictionary with the following structure:

        ::

            {'logical_environment': {'id': < id_logical_environment >}}

        :raise InvalidParameterError: Name is null and invalid.
        :raise NomeAmbienteLogicoDuplicadoError: There is already a registered Logical Environment with the value of name.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        logical_environment_map = dict()
        logical_environment_map['name'] = name

        code, xml = self.submit(
            {'logical_environment': logical_environment_map}, 'POST', 'logicalenvironment/')

        return self.response(code, xml)

    def alterar(self, id_logicalenvironment, name):
        """Change Logical Environment from by the identifier.

        :param id_logicalenvironment: Identifier of the Logical Environment. Integer value and greater than zero.
        :param name: Logical Environment name. String with a minimum 2 and maximum of 80 characters

        :return: None

        :raise InvalidParameterError: The identifier of Logical Environment or name is null and invalid.
        :raise NomeAmbienteLogicoDuplicadoError: There is already a registered Logical Environment with the value of name.
        :raise AmbienteLogicoNaoExisteError: Logical Environment not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_logicalenvironment):
            raise InvalidParameterError(
                u'The identifier of Logical Environment is invalid or was not informed.')

        url = 'logicalenvironment/' + str(id_logicalenvironment) + '/'

        logical_environment_map = dict()
        logical_environment_map['name'] = name

        code, xml = self.submit(
            {'logical_environment': logical_environment_map}, 'PUT', url)

        return self.response(code, xml)

    def remover(self, id_logicalenvironment):
        """Remove Logical Environment from by the identifier.

        :param id_logicalenvironment: Identifier of the Logical Environment. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: The identifier of Logical Environment is null and invalid.
        :raise AmbienteLogicoNaoExisteError: Logical Environment not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_logicalenvironment):
            raise InvalidParameterError(
                u'The identifier of Logical Environment is invalid or was not informed.')

        url = 'logicalenvironment/' + str(id_logicalenvironment) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)
