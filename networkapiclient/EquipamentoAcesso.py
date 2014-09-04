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


class EquipamentoAcesso(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            EquipamentoAcesso,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def get_access(self, id_access):
        """Get Equipment Access by id.

        :return: Dictionary with following:

        ::

            {'equipamento_acesso':
            {'id_equipamento': < id_equipamento >,
            'fqdn': < fqdn >,
            'user': < user >,
            'pass': < pass >,
            'id_tipo_acesso': < id_tipo_acesso >,
            'enable_pass': < enable_pass >}}
        """

        if not is_valid_int_param(id_access):
            raise InvalidParameterError(u'Equipment Access ID is invalid.')

        url = 'equipamentoacesso/id/' + str(id_access) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def listar(self):
        """List Equipment Access relationships.

        Return only the relationships from equipments the user have write permissions
        in one of the equipment groups

        :return: Dictionary with the following:

        ::

            {'equipamento_acesso':
            [{'id_equipamento': < id_equipamento >,
            'fqdn': < fqdn >,
            'user': < user >,
            'pass': < pass >,
            'id_tipo_acesso': < id_tipo_acesso >,
            'enable_pass': < enable_pass >,
            'protocolo_tipo_acesso': < protocol_tipo_acesso >},
            ... other equipment_access ....]}

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        code, map = self.submit(None, 'GET', 'equipamentoacesso/')

        key = 'equipamento_acesso'
        return get_list_map(self.response(code, map, [key]), key)

    def list_by_equip(self, name):
        """
        List all equipment access by equipment name

        :return: Dictionary with the following structure:

        ::

            {‘equipamento_acesso’:[ {'id': <id_equiptos_access>,
            'equipamento': <id_equip>,
            'fqdn': <fqdn>,
            'user': <user>,
            'password': <pass>
            'tipo_acesso': <id_tipo_acesso>,
            'enable_pass': <enable_pass> }]}

        :raise InvalidValueError: Invalid parameter.
        :raise EquipamentoNotFoundError: Equipment name not found in database.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        equip_access_map = dict()
        equip_access_map['name'] = name

        code, xml = self.submit(
            {"equipamento_acesso": equip_access_map}, 'POST', 'equipamentoacesso/name/')

        key = 'equipamento_acesso'
        return get_list_map(self.response(code, xml, [key]), key)

    def inserir(
            self,
            id_equipamento,
            fqdn,
            user,
            password,
            id_tipo_acesso,
            enable_pass):
        """Add new relationship between equipment and access type and returns its id.

        :param id_equipamento: Equipment identifier.
        :param fqdn: Equipment FQDN.
        :param user: User.
        :param password: Password.
        :param id_tipo_acesso: Access Type identifier.
        :param enable_pass: Enable access.

        :return: Dictionary with the following: {‘equipamento_acesso’: {‘id’: < id >}}

        :raise EquipamentoNaoExisteError: Equipment doesn't exist.
        :raise TipoAcessoNaoExisteError: Access Type doesn't exist.
        :raise EquipamentoAcessoError:  Equipment and access type already associated.
        :raise InvalidParameterError: The parameters equipment id, fqdn, user, password or
            access type id are invalid or none.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        equipamento_acesso_map = dict()
        equipamento_acesso_map['id_equipamento'] = id_equipamento
        equipamento_acesso_map['fqdn'] = fqdn
        equipamento_acesso_map['user'] = user
        equipamento_acesso_map['pass'] = password
        equipamento_acesso_map['id_tipo_acesso'] = id_tipo_acesso
        equipamento_acesso_map['enable_pass'] = enable_pass

        code, xml = self.submit(
            {'equipamento_acesso': equipamento_acesso_map}, 'POST', 'equipamentoacesso/')

        return self.response(code, xml)

    def edit_by_id(
            self,
            id_equip_acesso,
            id_tipo_acesso,
            fqdn,
            user,
            password,
            enable_pass):
        """Edit access type, fqdn, user, password and enable_pass of the relationship of
        equipment and access type.

        :param id_tipo_acesso: Access type identifier.
        :param id_equip_acesso: Equipment identifier.
        :param fqdn: Equipment FQDN.
        :param user: User.
        :param password: Password.
        :param enable_pass: Enable access.

        :return: None

        :raise InvalidParameterError: The parameters fqdn, user, password or
            access type id are invalid or none.
        :raise EquipamentoAcessoNaoExisteError: Equipment access type relationship doesn't exist.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_tipo_acesso):
            raise InvalidParameterError(
                u'Access type id is invalid or not informed.')

        equipamento_acesso_map = dict()
        equipamento_acesso_map['fqdn'] = fqdn
        equipamento_acesso_map['user'] = user
        equipamento_acesso_map['pass'] = password
        equipamento_acesso_map['enable_pass'] = enable_pass
        equipamento_acesso_map['id_tipo_acesso'] = id_tipo_acesso
        equipamento_acesso_map['id_equip_acesso'] = id_equip_acesso

        url = 'equipamentoacesso/edit/'

        code, xml = self.submit(
            {'equipamento_acesso': equipamento_acesso_map}, 'POST', url)

        return self.response(code, xml)

    def remover(self, id_tipo_acesso, id_equipamento):
        """Removes relationship between equipment and access type.

        :param id_equipamento: Equipment identifier.
        :param id_tipo_acesso: Access type identifier.

        :return: None

        :raise EquipamentoNaoExisteError: Equipment doesn't exist.
        :raise EquipamentoAcessoNaoExisteError: Relationship between equipment and access type doesn't exist.
        :raise InvalidParameterError: Equipment and/or access type id is/are invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_tipo_acesso):
            raise InvalidParameterError(u'Access type id is invalid.')

        if not is_valid_int_param(id_equipamento):
            raise InvalidParameterError(u'Equipment id is invalid.')

        url = 'equipamentoacesso/' + \
            str(id_equipamento) + '/' + str(id_tipo_acesso) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)
