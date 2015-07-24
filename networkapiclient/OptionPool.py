# -*- coding:utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from networkapiclient.GenericClient import GenericClient
from networkapiclient.exception import InvalidParameterError
from networkapiclient.utils import is_valid_int_param


class OptionPool(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            OptionPool,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def add(self, tipo_opcao, nome_opcao_txt):
        """Inserts a new Option Pool and returns its identifier.

        :param tipo_opcao: Type. String with a maximum of 50 characters and respect [a-zA-Z\_-]
        :param nome_opcao_txt: Name Option. String with a maximum of 50 characters and respect [a-zA-Z\_-]

        :return: Following dictionary:

        ::

            {'option_pool': {'id': < id >}}

        :raise InvalidParameterError: The value of tipo_opcao or nome_opcao_txt is invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        optionpool_map = dict()
        optionpool_map['type'] = tipo_opcao
        optionpool_map['name'] = nome_opcao_txt

        code, xml = self.submit(
            {'option_pool': optionpool_map}, 'POST', 'optionpool/')

        return self.response(code, xml)

    def alter(self, id_option_pool, tipo_opcao, nome_opcao_txt):
        """Change Option Pool from by the identifier.

        :param id_option_pool: Identifier of the Option VIP. Integer value and greater than zero.
        :param tipo_opcao: Type. String with a maximum of 50 characters and respect [a-zA-Z\_-]
        :param nome_opcao_txt: Name Option. String with a maximum of 50 characters and respect [a-zA-Z\_-]

        :return: None

        :raise InvalidParameterError: Option VIP identifier is null and invalid.
        :raise InvalidParameterError: The value of tipo_opcao or nome_opcao_txt is invalid.
        :raise optionpoolNotFoundError: Option VIP not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_option_pool):
            raise InvalidParameterError(
                u'The identifier of Option Pool is invalid or was not informed.')

        optionpool_map = dict()
        optionpool_map['type'] = tipo_opcao
        optionpool_map['name'] = nome_opcao_txt

        url = 'optionpool/' + str(id_option_pool) + '/'

        code, xml = self.submit({'option_pool': optionpool_map}, 'PUT', url)

        return self.response(code, xml)

    def remove(self, id_option_pool):
        """Remove Option VIP from by the identifier.

        :param id_option_pool: Identifier of the Option VIP. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: Option VIP identifier is null and invalid.
        :raise optionpoolNotFoundError: Option VIP not registered.
        :raise optionpoolError: Option VIP  associated with environment vip.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_option_pool):
            raise InvalidParameterError(
                u'The identifier of Option Pool is invalid or was not informed.')

        url = 'optionpool/' + str(id_option_pool) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def search(self, id_option_pool):
        """Search Option Pool from by the identifier.

        :param id_option_pool: Identifier of the Option Pool. Integer value and greater than zero.

        :return: Following dictionary:

        ::

            {‘option_pool’: {‘id’: < id_option_pool >,
            ‘type’: < tipo_opcao >,
            ‘name’: < nome_opcao_txt >} }

        :raise InvalidParameterError: Option Pool identifier is null and invalid.
        :raise optionpoolNotFoundError: Option Pool not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_option_pool):
            raise InvalidParameterError(
                u'The identifier of Option Pool is invalid or was not informed.')

        url = 'optionpool/' + str(id_option_pool) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def get_all(self):
        """Get all Option Pool.

        :return: Dictionary with the following structure:

        ::

            {‘option_pool’: [{‘id’: < id >,
            ‘type’: < tipo_opcao >,
            ‘name’: < nome_opcao_txt >}, ... other option pool ...] }

        :raise optionpoolNotFoundError: Option Pool not registered.
        :raise DataBaseError: Can't connect to networkapi database.
        :raise XMLError: Failed to generate the XML response.
        """

        url = 'optionpool/all/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def get_option_pool(self, id_environment):
        """Get all Option VIP by Environment .

        :return: Dictionary with the following structure:

        ::

            {‘option_pool’: [{‘id’: < id >,
            ‘type’: < tipo_opcao >,
            ‘name’: < nome_opcao_txt >}, ... too option vips ...] }

        :raise EnvironmentVipNotFoundError: Environment Pool not registered.
        :raise DataBaseError: Can't connect to networkapi database.
        :raise XMLError: Failed to generate the XML response.
        """

        url = 'optionpool/environmentvip/' + str(id_environment) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml, ['option_pool'])

    def associate(self, id_option_pool, id_environment):
        """Create a relationship of optionpool with Environment.

        :param id_option_pool: Identifier of the Option Pool. Integer value and greater than zero.
        :param id_environment: Identifier of the Environment Pool. Integer value and greater than zero.

        :return: Following dictionary

        ::

            {'opcoespool_ambiente_xref': {'id': < id_opcoespool_ambiente_xref >} }

        :raise InvalidParameterError: Option Pool/Environment Pool identifier is null and/or invalid.
        :raise optionpoolNotFoundError: Option Pool not registered.
        :raise EnvironmentVipNotFoundError: Environment Pool not registered.
        :raise optionpoolError: Option Pool is already associated with the environment pool.
        :raise UserNotAuthorizedError: User does not have authorization to make this association.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_option_pool):
            raise InvalidParameterError(
                u'The identifier of Option Pool is invalid or was not informed.')

        if not is_valid_int_param(id_environment):
            raise InvalidParameterError(
                u'The identifier of Environment Pool is invalid or was not informed.')

        url = 'optionpool/' + \
            str(id_option_pool) + '/environmentpool/' + str(id_environment) + '/'

        code, xml = self.submit(None, 'PUT', url)

        return self.response(code, xml)

    def disassociate(self, id_option_pool, id_environment):
        """Remove a relationship of optionpool with Environment.

        :param id_option_pool: Identifier of the Option Pool. Integer value and greater than zero.
        :param id_environment: Identifier of the Environment Pool. Integer value and greater than zero.

        :return: Nothing

        :raise InvalidParameterError: Option Pool/Environment Pool identifier is null and/or invalid.
        :raise optionpoolNotFoundError: Option Pool not registered.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise optionpoolError: Option pool is not associated with the environment pool
        :raise UserNotAuthorizedError: User does not have authorization to make this association.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_option_pool):
            raise InvalidParameterError(
                u'The identifier of Option Pool is invalid or was not informed.')

        if not is_valid_int_param(id_environment):
            raise InvalidParameterError(
                u'The identifier of Environment Pool is invalid or was not informed.')

        url = 'optionpool/' + \
            str(id_option_pool) + '/environmentpool/' + str(id_environment) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)


    def buscar_servicedownaction_opcpool(self, id_ambiente):
        """Search name of Option Pool when type = 'ServiceDownAction' ​​by environmentvip_id

        :return: Dictionary with the following structure:

        ::

            {‘servicedownaction_opt’: ‘servicedownaction_opt’: <'nome_opcao_txt'>}

        :raise InvalidParameterError: Environment VIP identifier is null and invalid.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise InvalidParameterError: finalidade_txt and cliente_txt is null and invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_ambiente):
            raise InvalidParameterError(
                u'The identifier of environment-pool is invalid or was not informed.')

        url = 'environment-pool/get/servicedownaction/' + str(id_ambiente) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)


    def buscar_healthchecks(self, id_ambiente):
        """Search healthcheck ​by environmentvip_id

        :return: Dictionary with the following structure:

        ::

            {'healthcheck_opt': [{'name': <name>, 'id': <id>},...]}

        :raise InvalidParameterError: Environment VIP identifier is null and invalid.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise InvalidParameterError: id_ambiente_vip is null and invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        url = 'environment-pool/get/healthcheck/' + str(id_ambiente)

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml, ['healthcheck_opt'])
