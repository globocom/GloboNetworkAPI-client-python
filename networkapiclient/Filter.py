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
from networkapiclient.utils import is_valid_int_param, get_list_map


class Filter(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(Filter, self).__init__(networkapi_url, user, password, user_ldap)

    def list_all(self):
        """
        List all filters

        :return: Following dictionary:

        ::

            {'filter': [{'id': <id>,
            'name': <name>,
            'description': <description>,
            'equip_types': [<TipoEquipamento>,
            {...demais TipoEquipamento's...}]}
            {... demais filters ...}] }

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        url = 'filter/all/'

        code, xml = self.submit(None, 'GET', url)

        key = 'filter'

        return get_list_map(self.response(code, xml, [key]), key)

    def add(self, name, description):
        """Inserts a new Filter and returns its identifier.

        :param name: Name. String with a maximum of 100 characters and respect [a-zA-Z\_-]
        :param description: Description. String with a maximum of 200 characters and respect [a-zA-Z\_-]

        :return: Following dictionary:

        ::

            {'filter': {'id': < id >}}

        :raise InvalidParameterError: The value of name or description is invalid.
        :raise FilterDuplicateError: A filter named by name already exists.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        filter_map = dict()
        filter_map['name'] = name
        filter_map['description'] = description

        code, xml = self.submit({'filter': filter_map}, 'POST', 'filter/')

        return self.response(code, xml)

    def alter(self, id_filter, name, description):
        """Change Filter by the identifier.

        :param id_filter: Identifier of the Filter. Integer value and greater than zero.
        :param name: Name. String with a maximum of 50 characters and respect [a-zA-Z\_-]
        :param description: Description. String with a maximum of 50 characters and respect [a-zA-Z\_-]

        :return: None

        :raise InvalidParameterError: Filter identifier is null and invalid.
        :raise InvalidParameterError: The value of name or description is invalid.
        :raise FilterNotFoundError: Filter not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_filter):
            raise InvalidParameterError(
                'The identifier of Filter is invalid or was not informed.')

        filter_map = dict()
        filter_map['name'] = name
        filter_map['description'] = description

        url = 'filter/' + str(id_filter) + '/'

        code, xml = self.submit({'filter': filter_map}, 'PUT', url)

        return self.response(code, xml)

    def remove(self, id_filter):
        """Remove Filter by the identifier.

        :param id_filter: Identifier of the Filter. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: Filter identifier is null and invalid.
        :raise FilterNotFoundError: Filter not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_filter):
            raise InvalidParameterError(
                'The identifier of Filter is invalid or was not informed.')

        url = 'filter/' + str(id_filter) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def get(self, id_filter):
        """Get filter by id.

        :param id_filter: Identifier of the Filter. Integer value and greater than zero.

        :return: Following dictionary:

        ::

            {‘filter’: {‘id’: < id >,
            ‘name’: < name >,
            ‘description’: < description >}}

        :raise InvalidParameterError: The value of id_filter is invalid.
        :raise FilterNotFoundError: Filter not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        url = 'filter/get/' + str(id_filter) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def associate(self, et_id, id_filter):
        """Create a relationship between Filter and TipoEquipamento.

        :param et_id: Identifier of TipoEquipamento. Integer value and greater than zero.
        :param id_filter: Identifier of Filter. Integer value and greater than zero.

        :return: Following dictionary:

        ::

            {'equiptype_filter_xref': {'id': < id_equiptype_filter_xref >} }

        :raise InvalidParameterError: TipoEquipamento/Filter identifier is null and/or invalid.
        :raise TipoEquipamentoNaoExisteError: TipoEquipamento not registered.
        :raise FilterNotFoundError: Filter not registered.
        :raise FilterEqTypeAssociationError: TipoEquipamento and Filter already associated.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(et_id):
            raise InvalidParameterError(
                'The identifier of TipoEquipamento is invalid or was not informed.')

        if not is_valid_int_param(id_filter):
            raise InvalidParameterError(
                'The identifier of Filter is invalid or was not informed.')

        url = 'filter/' + str(id_filter) + '/equiptype/' + str(et_id) + '/'

        code, xml = self.submit(None, 'PUT', url)

        return self.response(code, xml)

    def dissociate(self, id_filter, id_eq_type):
        """Removes relationship between Filter and TipoEquipamento.

        :param id_filter: Identifier of Filter. Integer value and greater than zero.
        :param id_eq_type: Identifier of TipoEquipamento. Integer value, greater than zero.

        :return: None

        :raise FilterNotFoundError: Filter not registered.
        :raise TipoEquipamentoNotFoundError: TipoEquipamento not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_filter):
            raise InvalidParameterError(
                'The identifier of Filter is invalid or was not informed.')

        if not is_valid_int_param(id_eq_type):
            raise InvalidParameterError(
                'The identifier of TipoEquipamento is invalid or was not informed.')

        url = 'filter/' + \
            str(id_filter) + '/dissociate/' + str(id_eq_type) + '/'

        code, xml = self.submit(None, 'PUT', url)

        return self.response(code, xml)
