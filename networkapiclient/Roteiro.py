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


class Roteiro(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            Roteiro,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def listar(self):
        """List all Script.

        :return: Dictionary with the following structure:

        ::

            {‘script’: [{‘id’: < id >,
            ‘tipo_roteiro’: < tipo_roteiro >,
            ‘nome’: < nome >,
            ‘descricao’: < descricao >}, ...more Script...]}

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        code, map = self.submit(None, 'GET', 'script/all/')

        key = 'script'
        return get_list_map(self.response(code, map, [key]), key)

    def inserir(self, id_script_type, script, model, description):
        """Inserts a new Script and returns its identifier.

        :param id_script_type: Identifier of the Script Type. Integer value and greater than zero.
        :param script: Script name. String with a minimum 3 and maximum of 40 characters
        :param description: Script description. String with a minimum 3 and maximum of 100 characters

        :return: Dictionary with the following structure:

        ::

            {'script': {'id': < id_script >}}

        :raise InvalidParameterError: The identifier of Script Type, script or description is null and invalid.
        :raise TipoRoteiroNaoExisteError: Script Type not registered.
        :raise NomeRoteiroDuplicadoError: Script already registered with informed.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        script_map = dict()
        script_map['id_script_type'] = id_script_type
        script_map['script'] = script
        script_map['model'] = model
        script_map['description'] = description

        code, xml = self.submit({'script': script_map}, 'POST', 'script/')

        return self.response(code, xml)

    def alterar(self, id_script, id_script_type, script, description, model=None):
        """Change Script from by the identifier.

        :param id_script: Identifier of the Script. Integer value and greater than zero.
        :param id_script_type: Identifier of the Script Type. Integer value and greater than zero.
        :param script: Script name. String with a minimum 3 and maximum of 40 characters
        :param description: Script description. String with a minimum 3 and maximum of 100 characters

        :return: None

        :raise InvalidParameterError: The identifier of Script, script Type, script or description is null and invalid.
        :raise RoteiroNaoExisteError: Script not registered.
        :raise TipoRoteiroNaoExisteError: Script Type not registered.
        :raise NomeRoteiroDuplicadoError: Script already registered with informed.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_script):
            raise InvalidParameterError('The identifier of Script is invalid or was not informed.')

        script_map = dict()
        script_map['id_script_type'] = id_script_type
        script_map['script'] = script
        script_map['model'] = model
        script_map['description'] = description

        url = 'script/edit/' + str(id_script) + '/'

        code, xml = self.submit({'script': script_map}, 'PUT', url)

        return self.response(code, xml)

    def remover(self, id_script):
        """Remove Script from by the identifier.

        :param id_script: Identifier of the Script. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: The identifier of Script is null and invalid.
        :raise RoteiroNaoExisteError: Script not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_script):
            raise InvalidParameterError(
                'The identifier of Script is invalid or was not informed.')

        url = 'script/' + str(id_script) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def listar_por_tipo(self, id_script_type):
        """List all Script by Script Type.

        :param id_script_type: Identifier of the Script Type. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            {‘script’: [{‘id’: < id >,
            ‘tipo_roteiro': < id_tipo_roteiro >,
            ‘nome': < nome >,
            ‘descricao’: < descricao >}, ...more Script...]}

        :raise InvalidParameterError: The identifier of Script Type is null and invalid.
        :raise TipoRoteiroNaoExisteError: Script Type not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_script_type):
            raise InvalidParameterError(
                'The identifier of Script Type is invalid or was not informed.')

        url = 'script/scripttype/' + str(id_script_type) + '/'

        code, map = self.submit(None, 'GET', url)

        key = 'script'
        return get_list_map(self.response(code, map, [key]), key)

    def listar_por_equipamento(self, id_equipment):
        """List all Script related Equipment.

        :param id_equipment: Identifier of the Equipment. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            {script': [{‘id’: < id >,
            ‘nome’: < nome >,
            ‘descricao’: < descricao >,
            ‘id_tipo_roteiro’: < id_tipo_roteiro >,
            ‘nome_tipo_roteiro’: < nome_tipo_roteiro >,
            ‘descricao_tipo_roteiro’: < descricao_tipo_roteiro >}, ...more Script...]}

        :raise InvalidParameterError: The identifier of Equipment is null and invalid.
        :raise EquipamentoNaoExisteError: Equipment not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_equipment):
            raise InvalidParameterError(
                'The identifier of Equipment is invalid or was not informed.')

        url = 'script/equipment/' + str(id_equipment) + '/'

        code, map = self.submit(None, 'GET', url)

        key = 'script'
        return get_list_map(self.response(code, map, [key]), key)

    def get_by_id(self, id_script):

        if not is_valid_int_param(id_script):
            raise InvalidParameterError(
                'Script id is invalid or was not informed.')

        url = 'script/get/' + str(id_script)

        code, map = self.submit(None, 'GET', url)

        return self.response(code, map)
