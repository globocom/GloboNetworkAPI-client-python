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
from networkapiclient.utils import get_list_map


class TipoEquipamento(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            TipoEquipamento,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def listar(self):
        """List all Equipment Type.

        :return: Dictionary with the following structure:

        ::

            {‘equipment_type’ : [{‘id’: < id >,
            ‘nome’: < name >}, ... too Equipment Type ...] }

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response
        """
        code, map = self.submit(None, 'GET', 'equipmenttype/all/')

        key = 'equipment_type'
        return get_list_map(self.response(code, map, [key]), key)

    def inserir(self, name):
        """Inserts a new Equipment Type and returns its identifier

        :param name: Equipment Type name. String with a minimum 3 and maximum of 100 characters

        :return: Dictionary with the following structure:

        ::

            {'tipo_equipamento': {'id': < id_equipment_ype >}}

        :raise InvalidParameterError: Name is null and invalid.
        :raise EquipamentoError: There is already a registered Equipment Type with the value of name.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response
        """
        equipment_type_map = dict()
        equipment_type_map['name'] = name

        url = 'equipmenttype/'

        code, xml = self.submit(
            {'equipment_type': equipment_type_map}, 'POST', url)

        return self.response(code, xml)
