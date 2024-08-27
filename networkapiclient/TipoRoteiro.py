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


class TipoRoteiro(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            TipoRoteiro,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def listar(self):
        """List all Script Type.

        :return: Dictionary with the following structure:

        ::

            {‘script_type’: [{‘id’: < id >,
            ‘tipo’: < tipo >,
            ‘descricao’: < descricao >}, ...more Script Type...]}

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        code, map = self.submit(None, 'GET', 'scripttype/all/')

        key = 'script_type'
        return get_list_map(self.response(code, map, [key]), key)

    def inserir(self, type, description):
        """Inserts a new Script Type and returns its identifier.

        :param type: Script Type type. String with a minimum 3 and maximum of 40 characters
        :param description: Script Type description. String with a minimum 3 and maximum of 100 characters

        :return: Dictionary with the following structure:

        ::

            {'script_type': {'id': < id_script_type >}}

        :raise InvalidParameterError: Type or description is null and invalid.
        :raise NomeTipoRoteiroDuplicadoError: Type script already registered with informed.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        script_type_map = dict()
        script_type_map['type'] = type
        script_type_map['description'] = description

        code, xml = self.submit(
            {'script_type': script_type_map}, 'POST', 'scripttype/')

        return self.response(code, xml)

    def alterar(self, id_script_type, type, description):
        """Change Script Type from by the identifier.

        :param id_script_type: Identifier of the Script Type. Integer value and greater than zero.
        :param type: Script Type type. String with a minimum 3 and maximum of 40 characters
        :param description: Script Type description. String with a minimum 3 and maximum of 100 characters

        :return: None

        :raise InvalidParameterError: The identifier of Script Type, type or description is null and invalid.
        :raise TipoRoteiroNaoExisteError: Script Type not registered.
        :raise NomeTipoRoteiroDuplicadoError: Type script already registered with informed.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_script_type):
            raise InvalidParameterError(
                'The identifier of Script Type is invalid or was not informed.')

        script_type_map = dict()
        script_type_map['type'] = type
        script_type_map['description'] = description

        url = 'scripttype/' + str(id_script_type) + '/'

        code, xml = self.submit({'script_type': script_type_map}, 'PUT', url)

        return self.response(code, xml)

    def remover(self, id_script_type):
        """Remove Script Type from by the identifier.

        :param id_script_type: Identifier of the Script Type. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: The identifier of Script Type is null and invalid.
        :raise TipoRoteiroNaoExisteError: Script Type not registered.
        :raise TipoRoteiroError: Script type is associated with a script.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_script_type):
            raise InvalidParameterError(
                'The identifier of Script Type is invalid or was not informed.')

        url = 'scripttype/' + str(id_script_type) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)
