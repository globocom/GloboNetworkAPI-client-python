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


class PermissaoAdministrativa(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            PermissaoAdministrativa,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def list_by_group(self, id_ugroup):
        """Search Administrative Permission by Group User by identifier.

        :param id_ugroup: Identifier of the Group User. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            {'perms': [{'ugrupo': < ugrupo_id >, 'permission':  { 'function' < function >, 'id': < id > },
            'id': < id >, 'escrita': < escrita >,
            'leitura': < leitura >}, ... ] }

        :raise InvalidParameterError: Group User is null and invalid.
        :raise UGrupoNotFoundError: Group User not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if id_ugroup is None:
            raise InvalidParameterError(
                'The identifier of Group User is invalid or was not informed.')

        url = 'aperms/group/' + str(id_ugroup) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def search(self, id_perm):
        """Search Administrative Permission from by the identifier.

        :param id_perm: Identifier of the Administrative Permission. Integer value and greater than zero.

        :return: Following dictionary:

        ::

            {'perm': {'ugrupo': < ugrupo_id >,
            'permission': < permission_id >, 'id': < id >,
            'escrita': < escrita >, 'leitura': < leitura >}}

        :raise InvalidParameterError: Group User identifier is null and invalid.
        :raise PermissaoAdministrativaNaoExisteError: Administrative Permission not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_perm):
            raise InvalidParameterError(
                'The identifier of Administrative Permission is invalid or was not informed.')

        url = 'aperms/get/' + str(id_perm) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def listar(self):
        """List all Administrative Permission.

        :return: Dictionary with the following structure:

        ::

            {'perms': [{'ugrupo': < ugrupo_id >,
            'permission': < permission_id >,
            'id': < id >,
            'escrita': < escrita >,
            'leitura': < leitura >}, ... demais permissões ...]}

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        code, map = self.submit(None, 'GET', 'aperms/all/')

        key = 'perms'
        return get_list_map(self.response(code, map, [key]), key)

    def inserir(self, id_permission, read, write, id_group):
        """Inserts a new Administrative Permission and returns its identifier.

        :param id_permission: Identifier of the Permission. Integer value and greater than zero.
        :param read: Read. 0 or 1
        :param write: Write. 0 or 1
        :param id_group: Identifier of the Group of User. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            {'perm': {'id': < id_perm >}}

        :raise InvalidParameterError: The identifier of Administrative Permission, identifier of Group of User, read or  write is null and invalid.
        :raise ValorIndicacaoPermissaoInvalidoError: The value of read or write is null and invalid.
        :raise PermissaoAdministrativaDuplicadaError: Function already registered for the user group.
        :raise GrupoUsuarioNaoExisteError: Group of User not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        perms_map = dict()
        perms_map['id_permission'] = id_permission
        perms_map['read'] = read
        perms_map['write'] = write
        perms_map['id_group'] = id_group

        code, xml = self.submit(
            {'administrative_permission': perms_map}, 'POST', 'aperms/')

        return self.response(code, xml)

    def alterar(self, id_perm, id_permission, read, write, id_group):
        """Change Administrative Permission from by the identifier.

        :param id_perm: Identifier of the Administrative Permission. Integer value and greater than zero.
        :param id_permission: Identifier of the Permission. Integer value and greater than zero.
        :param read: Read. 0 or 1
        :param write: Write. 0 or 1
        :param id_group: Identifier of the Group of User. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: The identifier of Administrative Permission, identifier of Permission, identifier of Group of User, read or  write is null and invalid.
        :raise ValorIndicacaoPermissaoInvalidoError: The value of read or write is null and invalid.
        :raise PermissaoAdministrativaNaoExisteError: Administrative Permission not registered.
        :raise GrupoUsuarioNaoExisteError: Group of User not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_perm):
            raise InvalidParameterError(
                'The identifier of Administrative Permission is invalid or was not informed.')

        url = 'aperms/' + str(id_perm) + '/'

        perms_map = dict()
        perms_map['id_perm'] = id_perm
        perms_map['id_permission'] = id_permission
        perms_map['read'] = read
        perms_map['write'] = write
        perms_map['id_group'] = id_group

        code, xml = self.submit(
            {'administrative_permission': perms_map}, 'PUT', url)

        return self.response(code, xml)

    def remover(self, id_perms):
        """Remove Administrative Permission from by the identifier.

        :param id_perms: Identifier of the Administrative Permission. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: The identifier of Administrative Permission is null and invalid.
        :raise PermissaoAdministrativaNaoExisteError: Administrative Permission not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_perms):
            raise InvalidParameterError(
                'The identifier of Administrative Permission is invalid or was not informed.')

        url = 'aperms/' + str(id_perms) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)
