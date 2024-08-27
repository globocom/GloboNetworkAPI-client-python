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
from networkapiclient.utils import is_valid_int_param
from networkapiclient.exception import InvalidParameterError


class UsuarioGrupo(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            UsuarioGrupo,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def inserir(self, id_user, id_group):
        """Create a relationship between User and Group.

        :param id_user: Identifier of the User. Integer value and greater than zero.
        :param id_group: Identifier of the Group. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::
            {'user_group': {'id': < id_user_group >}}

        :raise InvalidParameterError: The identifier of User or Group is null and invalid.
        :raise GrupoUsuarioNaoExisteError: UserGroup not registered.
        :raise UsuarioNaoExisteError: User not registered.
        :raise UsuarioGrupoError: User already registered in the group.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_user):
            raise InvalidParameterError(
                'The identifier of User is invalid or was not informed.')

        if not is_valid_int_param(id_group):
            raise InvalidParameterError(
                'The identifier of Group is invalid or was not informed.')

        url = 'usergroup/user/' + \
            str(id_user) + '/ugroup/' + str(id_group) + '/associate/'

        code, xml = self.submit(None, 'PUT', url)

    def remover(self, id_user, id_group):
        """Removes relationship between User and Group.

        :param id_user: Identifier of the User. Integer value and greater than zero.
        :param id_group: Identifier of the Group. Integer value and greater than zero.

        :return: None

        :raise UsuarioGrupoNaoExisteError: Association between user and group not registered.
        :raise GrupoUsuarioNaoExisteError: UserGroup not registered.
        :raise UsuarioNaoExisteError: User not registered.
        :raise UsuarioGrupoError: User already registered in the group.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_user):
            raise InvalidParameterError(
                'The identifier of User is invalid or was not informed.')

        if not is_valid_int_param(id_group):
            raise InvalidParameterError(
                'The identifier of Group is invalid or was not informed.')

        url = 'usergroup/user/' + \
            str(id_user) + '/ugroup/' + str(id_group) + '/dissociate/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)
