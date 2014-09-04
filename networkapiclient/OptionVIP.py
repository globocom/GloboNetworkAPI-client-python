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


class OptionVIP(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            OptionVIP,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def add(self, tipo_opcao, nome_opcao_txt):
        """Inserts a new Option VIP and returns its identifier.

        :param tipo_opcao: Type. String with a maximum of 50 characters and respect [a-zA-Z\_-]
        :param nome_opcao_txt: Name Option. String with a maximum of 50 characters and respect [a-zA-Z\_-]

        :return: Following dictionary:

        ::

            {'option_vip': {'id': < id >}}

        :raise InvalidParameterError: The value of tipo_opcao or nome_opcao_txt is invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        optionvip_map = dict()
        optionvip_map['tipo_opcao'] = tipo_opcao
        optionvip_map['nome_opcao_txt'] = nome_opcao_txt

        code, xml = self.submit(
            {'option_vip': optionvip_map}, 'POST', 'optionvip/')

        return self.response(code, xml)

    def alter(self, id_option_vip, tipo_opcao, nome_opcao_txt):
        """Change Option VIP from by the identifier.

        :param id_option_vip: Identifier of the Option VIP. Integer value and greater than zero.
        :param tipo_opcao: Type. String with a maximum of 50 characters and respect [a-zA-Z\_-]
        :param nome_opcao_txt: Name Option. String with a maximum of 50 characters and respect [a-zA-Z\_-]

        :return: None

        :raise InvalidParameterError: Option VIP identifier is null and invalid.
        :raise InvalidParameterError: The value of tipo_opcao or nome_opcao_txt is invalid.
        :raise OptionVipNotFoundError: Option VIP not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_option_vip):
            raise InvalidParameterError(
                u'The identifier of Option VIP is invalid or was not informed.')

        optionvip_map = dict()
        optionvip_map['tipo_opcao'] = tipo_opcao
        optionvip_map['nome_opcao_txt'] = nome_opcao_txt

        url = 'optionvip/' + str(id_option_vip) + '/'

        code, xml = self.submit({'option_vip': optionvip_map}, 'PUT', url)

        return self.response(code, xml)

    def remove(self, id_option_vip):
        """Remove Option VIP from by the identifier.

        :param id_option_vip: Identifier of the Option VIP. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: Option VIP identifier is null and invalid.
        :raise OptionVipNotFoundError: Option VIP not registered.
        :raise OptionVipError: Option VIP  associated with environment vip.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_option_vip):
            raise InvalidParameterError(
                u'The identifier of Option VIP is invalid or was not informed.')

        url = 'optionvip/' + str(id_option_vip) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def search(self, id_option_vip):
        """Search Option VIP from by the identifier.

        :param id_option_vip: Identifier of the Option VIP. Integer value and greater than zero.

        :return: Following dictionary:

        ::

            {‘option_vip’: {‘id’: < id_option_vip >,
            ‘tipo_opcao’: < tipo_opcao >,
            ‘nome_opcao_txt’: < nome_opcao_txt >} }

        :raise InvalidParameterError: Option VIP identifier is null and invalid.
        :raise OptionVipNotFoundError: Option VIP not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_option_vip):
            raise InvalidParameterError(
                u'The identifier of Option VIP is invalid or was not informed.')

        url = 'optionvip/' + str(id_option_vip) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def get_all(self):
        """Get all Option VIP.

        :return: Dictionary with the following structure:

        ::

            {‘option_vip’: [{‘id’: < id >,
            ‘tipo_opcao’: < tipo_opcao >,
            ‘nome_opcao_txt’: < nome_opcao_txt >}, ... other option vips ...] }

        :raise OptionVipNotFoundError: Option VIP not registered.
        :raise DataBaseError: Can't connect to networkapi database.
        :raise XMLError: Failed to generate the XML response.
        """

        url = 'optionvip/all/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def get_option_vip(self, id_environment_vip):
        """Get all Option VIP by Environment Vip.

        :return: Dictionary with the following structure:

        ::

            {‘option_vip’: [{‘id’: < id >,
            ‘tipo_opcao’: < tipo_opcao >,
            ‘nome_opcao_txt’: < nome_opcao_txt >}, ... too option vips ...] }

        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise DataBaseError: Can't connect to networkapi database.
        :raise XMLError: Failed to generate the XML response.
        """

        url = 'optionvip/environmentvip/' + str(id_environment_vip) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml, ['option_vip'])

    def associate(self, id_option_vip, id_environment_vip):
        """Create a relationship of OptionVip with EnvironmentVip.

        :param id_option_vip: Identifier of the Option VIP. Integer value and greater than zero.
        :param id_environment_vip: Identifier of the Environment VIP. Integer value and greater than zero.

        :return: Following dictionary

        ::

            {'opcoesvip_ambiente_xref': {'id': < id_opcoesvip_ambiente_xref >} }

        :raise InvalidParameterError: Option VIP/Environment VIP identifier is null and/or invalid.
        :raise OptionVipNotFoundError: Option VIP not registered.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise OptionVipError: Option vip is already associated with the environment vip.
        :raise UserNotAuthorizedError: User does not have authorization to make this association.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_option_vip):
            raise InvalidParameterError(
                u'The identifier of Option VIP is invalid or was not informed.')

        if not is_valid_int_param(id_environment_vip):
            raise InvalidParameterError(
                u'The identifier of Environment VIP is invalid or was not informed.')

        url = 'optionvip/' + \
            str(id_option_vip) + '/environmentvip/' + str(id_environment_vip) + '/'

        code, xml = self.submit(None, 'PUT', url)

        return self.response(code, xml)

    def disassociate(self, id_option_vip, id_environment_vip):
        """Remove a relationship of OptionVip with EnvironmentVip.

        :param id_option_vip: Identifier of the Option VIP. Integer value and greater than zero.
        :param id_environment_vip: Identifier of the Environment VIP. Integer value and greater than zero.

        :return: Nothing

        :raise InvalidParameterError: Option VIP/Environment VIP identifier is null and/or invalid.
        :raise OptionVipNotFoundError: Option VIP not registered.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise OptionVipError: Option vip is not associated with the environment vip
        :raise UserNotAuthorizedError: User does not have authorization to make this association.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_option_vip):
            raise InvalidParameterError(
                u'The identifier of Option VIP is invalid or was not informed.')

        if not is_valid_int_param(id_environment_vip):
            raise InvalidParameterError(
                u'The identifier of Environment VIP is invalid or was not informed.')

        url = 'optionvip/' + \
            str(id_option_vip) + '/environmentvip/' + str(id_environment_vip) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def buscar_timeout_opcvip(self, id_ambiente_vip):
        """Buscar nome_opcao_txt das Opcoes VIp quando tipo_opcao = 'Timeout' pelo environmentvip_id

        :return: Dictionary with the following structure:

        ::
            {‘timeout_opt’: ‘timeout_opt’: <'nome_opcao_txt'>}

        :raise InvalidParameterError: Environment VIP identifier is null and invalid.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise InvalidParameterError: finalidade_txt and cliente_txt is null and invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_ambiente_vip):
            raise InvalidParameterError(
                u'The identifier of environment-vip is invalid or was not informed.')

        url = 'environment-vip/get/timeout/' + str(id_ambiente_vip) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def buscar_grupo_cache_opcvip(self, id_ambiente_vip):
        """Search nome_opcao_txt of Option VIP when tipo_opcao = 'Grupo de Caches' ​​by environmentvip_id


        :return: Dictionary with the following structure:

        ::

            {‘grupocache_opt’: ‘grupocache_opt’: <'nome_opcao_txt'>}

        :raise EnvironmentVipNotFoundError: Ambiente VIP não encontrado
        :raise OptionVipError: Falha na requisição.
        :raise EnvironmentVipError: Falha na requisição.
        :raise InvalidParameterError: O identificador da requisição de VIP é inválido ou nulo.
        :raise ScriptError: Falha ao executar o script.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """

        if not is_valid_int_param(id_ambiente_vip):
            raise InvalidParameterError(
                u'The identifier of environment-vip is invalid or was not informed.')

        url = 'environment-vip/get/grupo-cache/' + str(id_ambiente_vip) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def buscar_balanceamento_opcvip(self, id_ambiente_vip):
        """Search nome_opcao_txt of Option VIP when tipo_opcao = 'Balanceamento' ​​by environmentvip_id

        :return: Dictionary with the following structure:

        ::

            {‘balanceamento_opt’: ‘balanceamento_opt’: <'nome_opcao_txt'>}

        :raise InvalidParameterError: Environment VIP identifier is null and invalid.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise InvalidParameterError: finalidade_txt and cliente_txt is null and invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_ambiente_vip):
            raise InvalidParameterError(
                u'The identifier of environment-vip is invalid or was not informed.')

        url = 'environment-vip/get/balanceamento/' + str(id_ambiente_vip) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def buscar_persistencia_opcvip(self, id_ambiente_vip):
        """Search nome_opcao_txt of Option VIP when tipo_opcao = 'Persistencia' ​​by environmentvip_id

        :return: Dictionary with the following structure:

        ::

            {‘persistencia_opt’: ‘persistencia_opt’: <'nome_opcao_txt'>}

        :raise InvalidParameterError: Environment VIP identifier is null and invalid.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise InvalidParameterError: finalidade_txt and cliente_txt is null and invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_ambiente_vip):
            raise InvalidParameterError(
                u'The identifier of environment-vip is invalid or was not informed.')

        url = 'environment-vip/get/persistencia/' + str(id_ambiente_vip) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def buscar_rules(self, id_ambiente_vip, id_vip=''):
        """Search rules ​by environmentvip_id

        :return: Dictionary with the following structure:

        ::

            {'name_rule_opt': [{'name_rule_opt': <name>, 'id': <id>}, ...]}

        :raise InvalidParameterError: Environment VIP identifier is null and invalid.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise InvalidParameterError: finalidade_txt and cliente_txt is null and invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        url = 'environment-vip/get/rules/' + \
            str(id_ambiente_vip) + '/' + str(id_vip)

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def buscar_healthchecks(self, id_ambiente_vip):
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

        url = 'environment-vip/get/healthcheck/' + str(id_ambiente_vip)

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml, ['healthcheck_opt'])
