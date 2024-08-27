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
from networkapiclient.utils import get_list_map, is_valid_int_param
from networkapiclient.exception import InvalidParameterError


class TipoRede(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            TipoRede,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def listar(self):
        """List all network types.

        :return: Following dictionary:

        ::

            {'net_type': [{'id': < id_tipo_rede >,
            'name': < nome_tipo_rede >}, ... other network types ...]}

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        code, xml = self.submit(None, 'GET', 'net_type/')

        key = 'net_type'
        return get_list_map(self.response(code, xml, [key]), key)

    def inserir(self, name):
        """Insert new network type and return its identifier.

        :param name: Network type name.

        :return: Following dictionary: {'net_type': {'id': < id >}}

        :raise InvalidParameterError: Network type is none or invalid.
        :raise NomeTipoRedeDuplicadoError: A network type with this name already exists.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        net_type_map = dict()
        net_type_map['name'] = name

        code, xml = self.submit(
            {'net_type': net_type_map}, 'POST', 'net_type/')

        return self.response(code, xml)

    def alterar(self, id_net_type, name):
        """Edit network type by its identifier.

        :param id_net_type: Network type identifier.
        :param name: Network type name.

        :return: None

        :raise InvalidParameterError: Network type identifier and/or name is(are) none or invalid.
        :raise TipoRedeNaoExisteError: Network type does not exist.
        :raise NomeTipoRedeDuplicadoError: Network type name already exists.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_net_type):
            raise InvalidParameterError(
                'Network type is invalid or was not informed.')

        url = 'net_type/' + str(id_net_type) + '/'

        net_type_map = dict()
        net_type_map['name'] = name

        code, xml = self.submit({'net_type': net_type_map}, 'PUT', url)

        return self.response(code, xml)

    def remover(self, id_net_type):
        """Remove network type by its identifier.

        :param id_net_type: Network type identifier.

        :return: None

        :raise TipoRedeNaoExisteError: Network type does not exist.
        :raise TipoRedeError: Network type is associated with network.
        :raise InvalidParameterError: Network type is none or invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_net_type):
            raise InvalidParameterError(
                'Network type is invalid or was not informed.')

        url = 'net_type/' + str(id_net_type) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)
