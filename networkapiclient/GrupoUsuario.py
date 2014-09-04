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


class GrupoUsuario(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            GrupoUsuario,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def search(self, id_ugroup):
        """Search Group User by its identifier.

        :param id_ugroup: Identifier of the Group User. Integer value and greater than zero.

        :return: Following dictionary:

        ::

            {‘user_group’: {'escrita': < escrita >,
            'nome': < nome >,
            'exclusao': < exclusao >,
            'edicao': < edicao >,
            'id': < id >,
            'leitura': < leitura >}}

        :raise InvalidParameterError: Group User identifier is none or invalid.
        :raise GrupoUsuarioNaoExisteError: Group User not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_ugroup):
            raise InvalidParameterError(
                u'The identifier of Group User is invalid or was not informed.')

        url = 'ugroup/get/' + str(id_ugroup) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def listar(self):
        """List all user groups.

        :return: Dictionary with structure:

        ::

            {'user_group':  [{'escrita': < escrita >,
            'nome': < nome >,
            'exclusao': < exclusao >,
            'edicao': < edicao >,
            'id': < id >,
            'leitura': < leitura >},
            ... other groups ...]}

        :raise DataBaseError: Networkapi failed to access database.
        :raise XMLError: Networkapi fails generating response XML.
        """
        code, map = self.submit(None, 'GET', 'ugroup/all/')

        key = 'user_group'
        return get_list_map(self.response(code, map, [key]), key)

    def inserir(self, name, read, write, edit, remove):
        """Insert new user group and returns its identifier.

        :param name: User group's name.
        :param read: If user group has read permission ('S' ou 'N').
        :param write: If user group has write permission ('S' ou 'N').
        :param edit: If user group has edit permission ('S' ou 'N').
        :param remove: If user group has remove permission ('S' ou 'N').

        :return: Dictionary with structure: {'user_group': {'id': < id >}}

        :raise InvalidParameterError: At least one of the parameters is invalid or none..
        :raise NomeGrupoUsuarioDuplicadoError: User group name already exists.
        :raise ValorIndicacaoPermissaoInvalidoError: Read, write, edit or remove value is invalid.
        :raise DataBaseError: Networkapi failed to access database.
        :raise XMLError: Networkapi fails generating response XML.
        """
        ugroup_map = dict()
        ugroup_map['nome'] = name
        ugroup_map['leitura'] = read
        ugroup_map['escrita'] = write
        ugroup_map['edicao'] = edit
        ugroup_map['exclusao'] = remove

        code, xml = self.submit({'user_group': ugroup_map}, 'POST', 'ugroup/')

        return self.response(code, xml)

    def alterar(self, id_user_group, name, read, write, edit, remove):
        """Edit user group data from its identifier.

        :param id_user_group: User group id.
        :param name: User group name.
        :param read: If user group has read permission ('S' ou 'N').
        :param write: If user group has write permission ('S' ou 'N').
        :param edit: If user group has edit permission ('S' ou 'N').
        :param remove: If user group has remove permission ('S' ou 'N').

        :return: None

        :raise NomeGrupoUsuarioDuplicadoError: User group name already exists.
        :raise ValorIndicacaoPermissaoInvalidoError: Read, write, edit or remove value is invalid.
        :raise GrupoUsuarioNaoExisteError: User Group not found.
        :raise InvalidParameterError: At least one of the parameters is invalid or none.
        :raise DataBaseError: Networkapi failed to access database.
        :raise XMLError: Networkapi fails generating response XML.
        """
        if not is_valid_int_param(id_user_group):
            raise InvalidParameterError(
                u'Invalid or inexistent user group id.')

        url = 'ugroup/' + str(id_user_group) + '/'

        ugroup_map = dict()
        ugroup_map['nome'] = name
        ugroup_map['leitura'] = read
        ugroup_map['escrita'] = write
        ugroup_map['edicao'] = edit
        ugroup_map['exclusao'] = remove

        code, xml = self.submit({'user_group': ugroup_map}, 'PUT', url)

        return self.response(code, xml)

    def remover(self, id_user_group):
        """Removes a user group by its id.

        :param id_user_group: User Group's identifier. Valid integer greater than zero.

        :return: None

        :raise GrupoUsuarioNaoExisteError: User Group not found.
        :raise InvalidParameterError: User Group id is invalid or none.
        :raise DataBaseError: Networkapi failed to access database.
        :raise XMLError: Networkapi fails generating response XML.
        """
        if not is_valid_int_param(id_user_group):
            raise InvalidParameterError(
                u'Invalid or inexistent user group id.')

        url = 'ugroup/' + str(id_user_group) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)
