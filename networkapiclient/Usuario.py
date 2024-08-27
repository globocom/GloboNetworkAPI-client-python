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


class Usuario(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            Usuario,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def list_by_group(self, id_ugroup):
        """Search Users by Group User by identifier.

        :param id_ugroup: Identifier of the Group User. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            {'users': [{'nome': < nome >, 'grupos': < grupos_id >,
            'email': < email >, 'pwd': < pwd >,
            'user': < user >, 'ativo': < ativo >,
            'id': < id >}, ... ] }

        :raise InvalidParameterError: Group User is null and invalid.
        :raise UGrupoNotFoundError: Group User not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if id_ugroup is None:
            raise InvalidParameterError(
                'The identifier of Group User is invalid or was not informed.')

        url = 'user/group/' + str(id_ugroup) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def list_by_group_out(self, id_ugroup):
        """Search Users out group by Group User by identifier.

        :param id_ugroup: Identifier of the Group User. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            {'users': [{'nome': < nome >, 'grupos': < grupos_id >,
            'email': < email >, 'pwd': < pwd >,
            'user': < user >, 'ativo': < ativo >,
            'id': < id >}, ... ] }

        :raise InvalidParameterError: Group User is null and invalid.
        :raise UGrupoNotFoundError: Group User not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if id_ugroup is None:
            raise InvalidParameterError(
                'The identifier of Group User is invalid or was not informed.')

        url = 'user/out/group/' + str(id_ugroup) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def listar(self):
        """List all user.

        :return: Dictionary with the following structure:

        ::

            {'usuario': [{'nome': < nome >,
            'id': < id >,
            'pwd': < pwd >,
            'user': < user >,
            'ativo': < ativo >,
            'email': < email >,
            'user_ldap': < ldap user >}, ...more user...]}

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        code, map = self.submit(None, 'GET', 'user/all/')

        key = 'usuario'
        return get_list_map(self.response(code, map, [key]), key)

    def list_with_usergroup(self):
        """List all users and their user groups.
        is_more -If  more than 3 of groups of users or no, to control expansion Screen.

        :return: Dictionary with the following structure:

        ::

            {'usuario': [{'nome': < nome >,
            'id': < id >,
            'pwd': < pwd >,
            'user': < user >,
            'ativo': < ativo >,
            'email': < email >,
            'is_more': <True ou False>,
            'grupos': [nome_grupo, ...more user groups...]}, ...more user...]}


        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        url = 'usuario/get/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def get_by_id(self, id_user):
        """Get user by the identifier and their user groups.
        is_more -If  more than 3 of groups of users or no, to control expansion Screen.

        :return: Dictionary with the following structure:

        ::

            {'usuario': [{'nome': < nome >,
            'id': < id >,
            'pwd': < pwd >,
            'user': < user >,
            'ativo': < ativo >,
            'email': < email >,
            'grupos': [nome_grupo, ...more user groups...],
            'user_ldap': < user_ldap >}}


        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_user):
            raise InvalidParameterError(
                'The identifier of User is invalid or was not informed.')

        url = 'user/get/' + str(id_user) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def get_by_user_ldap(self, user_name):
        """Get user by the ldap name.
        is_more -If  more than 3 of groups of users or no, to control expansion Screen.

        :return: Dictionary with the following structure:

        ::

            {'usuario': [{'nome': < nome >,
            'id': < id >,
            'pwd': < pwd >,
            'user': < user >,
            'ativo': < ativo >,
            'email': < email >,
            'grupos': [nome_grupo, ...more user groups...],
            'user_ldap': < user_ldap >}}


        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        url = 'user/get/ldap/' + str(user_name) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def inserir(self, user, pwd, name, email, user_ldap):
        """Inserts a new User and returns its identifier.

        The user will be created with active status.

        :param user: Username. String with a minimum 3 and maximum of 45 characters
        :param pwd: User password. String with a minimum 3 and maximum of 45 characters
        :param name: User name. String with a minimum 3 and maximum of 200 characters
        :param email: User Email. String with a minimum 3 and maximum of 300 characters
        :param user_ldap: LDAP Username. String with a minimum 3 and maximum of 45 characters

        :return: Dictionary with the following structure:

        ::

            {'usuario': {'id': < id_user >}}

        :raise InvalidParameterError: The identifier of User, user, pwd, name or email is null and invalid.
        :raise UserUsuarioDuplicadoError: There is already a registered user with the value of user.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        user_map = dict()
        user_map['user'] = user
        user_map['password'] = pwd
        user_map['name'] = name
        user_map['email'] = email
        user_map['user_ldap'] = user_ldap

        code, xml = self.submit({'user': user_map}, 'POST', 'user/')

        return self.response(code, xml)

    def alterar(self, id_user, user, password, nome, ativo, email, user_ldap):
        """Change User from by the identifier.

        :param id_user: Identifier of the User. Integer value and greater than zero.
        :param user: Username. String with a minimum 3 and maximum of 45 characters
        :param password: User password. String with a minimum 3 and maximum of 45 characters
        :param nome: User name. String with a minimum 3 and maximum of 200 characters
        :param email: User Email. String with a minimum 3 and maximum of 300 characters
        :param ativo: Status. 0 or 1
        :param user_ldap: LDAP Username. String with a minimum 3 and maximum of 45 characters

        :return: None

        :raise InvalidParameterError: The identifier of User, user, pwd, name, email or  active is null and invalid.
        :raise UserUsuarioDuplicadoError: There is already a registered user with the value of user.
        :raise UsuarioNaoExisteError: User not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.

        """
        if not is_valid_int_param(id_user):
            raise InvalidParameterError(
                'The identifier of User is invalid or was not informed.')

        url = 'user/' + str(id_user) + '/'

        user_map = dict()
        user_map['user'] = user
        user_map['password'] = password
        user_map['name'] = nome
        user_map['active'] = ativo
        user_map['email'] = email
        user_map['user_ldap'] = user_ldap

        code, xml = self.submit({'user': user_map}, 'PUT', url)

        return self.response(code, xml)

    def change_password(self, id_user, user_current_password, password):
        """Change password of User from by the identifier.

        :param id_user: Identifier of the User. Integer value and greater than zero.
        :param user_current_password: Senha atual do usuário.
        :param password: Nova Senha do usuário.

        :return: None

        :raise UsuarioNaoExisteError: User not registered.
        :raise InvalidParameterError: The identifier of User is null and invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.

        """
        if not is_valid_int_param(id_user):
            raise InvalidParameterError(
                'The identifier of User is invalid or was not informed.')

        if password is None or password == "":
            raise InvalidParameterError(
                'A nova senha do usuário é inválida ou não foi informada')

        user_map = dict()
        user_map['user_id'] = id_user
        user_map['password'] = password

        code, xml = self.submit(
            {'user': user_map}, 'POST', 'user-change-pass/')

        return self.response(code, xml)

    def remover(self, id_user):
        """Remove User from by the identifier.

        :param id_user: Identifier of the User. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: The identifier of User is null and invalid.
        :raise UsuarioNaoExisteError: User not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_user):
            raise InvalidParameterError(
                'The identifier of User is invalid or was not informed.')

        url = 'user/' + str(id_user) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def authenticate(self, username, password, is_ldap_user):
        """Get user by username and password and their permissions.

        :param username: Username. String with a minimum 3 and maximum of 45 characters
        :param password: User password. String with a minimum 3 and maximum of 45 characters

        :return: Following dictionary:

        ::

            {'user': {'id': < id >}
            {'user': < user >}
            {'nome': < nome >}
            {'pwd': < pwd >}
            {'email': < email >}
            {'active': < active >}
            {'permission':[ {'<function>': { 'write': <value>, 'read': <value>}, ... more function ... ] } } }

        :raise InvalidParameterError: The value of username or password is invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        user_map = dict()
        user_map['username'] = username
        user_map['password'] = password
        user_map['is_ldap_user'] = is_ldap_user

        code, xml = self.submit({'user': user_map}, 'POST', 'authenticate/')

        return self.response(code, xml)

    def authenticate_ldap(self, username, password):
        """Get user by username and password and their permissions.

        :param username: Username. String with a minimum 3 and maximum of 45 characters
        :param password: User password. String with a minimum 3 and maximum of 45 characters

        :return: Following dictionary:

        ::

            {'user': {'id': < id >}
            {'user': < user >}
            {'nome': < nome >}
            {'pwd': < pwd >}
            {'email': < email >}
            {'active': < active >}
            {'permission':[ {'<function>': { 'write': <value>, 'read': <value>}, ... more function ... ] } } }

        :raise InvalidParameterError: The value of username or password is invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        user_map = dict()
        user_map['username'] = username
        user_map['password'] = password

        code, xml = self.submit(
            {'user': user_map}, 'POST', 'authenticate/ldap/')

        return self.response(code, xml)
