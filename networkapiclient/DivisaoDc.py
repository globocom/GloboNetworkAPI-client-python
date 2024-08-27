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


class DivisaoDc(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            DivisaoDc,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def listar(self):
        """List all Division Dc.

        :return: Dictionary with the following structure:

        ::

            {'division_dc':
            [{'id': < id >,
            'name': < name >}, ...more Division Dc...]}

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        code, map = self.submit(None, 'GET', 'divisiondc/all/')

        key = 'division_dc'
        return get_list_map(self.response(code, map, [key]), key)

    def inserir(self, name):
        """Inserts a new Division Dc and returns its identifier.

        :param name: Division Dc name. String with a minimum 2 and maximum of 80 characters

        :return: Dictionary with the following structure:

        ::

            {'division_dc': {'id': < id_division_dc >}}

        :raise InvalidParameterError: Name is null and invalid.
        :raise NomeDivisaoDcDuplicadoError: There is already a registered Division Dc with the value of name.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        division_dc_map = dict()
        division_dc_map['name'] = name

        code, xml = self.submit(
            {'division_dc': division_dc_map}, 'POST', 'divisiondc/')

        return self.response(code, xml)

    def alterar(self, id_divisiondc, name):
        """Change Division Dc from by the identifier.

        :param id_divisiondc: Identifier of the Division Dc. Integer value and greater than zero.
        :param name: Division Dc name. String with a minimum 2 and maximum of 80 characters

        :return: None

        :raise InvalidParameterError: The identifier of Division Dc or name is null and invalid.
        :raise NomeDivisaoDcDuplicadoError: There is already a registered Division Dc with the value of name.
        :raise DivisaoDcNaoExisteError: Division Dc not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_divisiondc):
            raise InvalidParameterError(
                'The identifier of Division Dc is invalid or was not informed.')

        url = 'divisiondc/' + str(id_divisiondc) + '/'

        division_dc_map = dict()
        division_dc_map['name'] = name

        code, xml = self.submit({'division_dc': division_dc_map}, 'PUT', url)

        return self.response(code, xml)

    def remover(self, id_divisiondc):
        """Remove Division Dc from by the identifier.

        :param id_divisiondc: Identifier of the Division Dc. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: The identifier of Division Dc is null and invalid.
        :raise DivisaoDcNaoExisteError: Division Dc not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_divisiondc):
            raise InvalidParameterError(
                'The identifier of Division Dc is invalid or was not informed.')

        url = 'divisiondc/' + str(id_divisiondc) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)
