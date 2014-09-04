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


class GrupoL3(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            GrupoL3,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def listar(self):
        """List all Group L3.

        :return: Dictionary with the following structure:

        ::

            {'group_l3': [{'id': < id >,
            'name': < name >},
            ...more Group L3...]}

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        code, map = self.submit(None, 'GET', 'groupl3/all/')

        key = 'group_l3'
        return get_list_map(self.response(code, map, [key]), key)

    def inserir(self, name):
        """Inserts a new Group L3 and returns its identifier.

        :param name: Group L3 name. String with a minimum 2 and maximum of 80 characters

        :return: Dictionary with the following structure:

        ::

            {'group_l3': {'id': < id_group_l3 >}}

        :raise InvalidParameterError: Name is null and invalid.
        :raise NomeGrupoL3DuplicadoError: There is already a registered Group L3 with the value of name.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        group_l3_map = dict()
        group_l3_map['name'] = name

        code, xml = self.submit({'group_l3': group_l3_map}, 'POST', 'groupl3/')

        return self.response(code, xml)

    def alterar(self, id_groupl3, name):
        """Change Group L3 from by the identifier.

        :param id_groupl3: Identifier of the Group L3. Integer value and greater than zero.
        :param name: Group L3 name. String with a minimum 2 and maximum of 80 characters

        :return: None

        :raise InvalidParameterError: The identifier of Group L3 or name is null and invalid.
        :raise NomeGrupoL3DuplicadoError: There is already a registered Group L3 with the value of name.
        :raise GrupoL3NaoExisteError: Group L3 not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_groupl3):
            raise InvalidParameterError(
                u'The identifier of Group L3 is invalid or was not informed.')

        url = 'groupl3/' + str(id_groupl3) + '/'

        group_l3_map = dict()
        group_l3_map['name'] = name

        code, xml = self.submit({'groupl3': group_l3_map}, 'PUT', url)

        return self.response(code, xml)

    def remover(self, id_groupl3):
        """Remove Group L3 from by the identifier.

        :param id_groupl3: Identifier of the Group L3. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: The identifier of Group L3 is null and invalid.
        :raise GrupoL3NaoExisteError: Group L3 not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_groupl3):
            raise InvalidParameterError(
                u'The identifier of Group L3 is invalid or was not informed.')

        url = 'groupl3/' + str(id_groupl3) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)
