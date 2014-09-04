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


class EquipamentoRoteiro(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            EquipamentoRoteiro,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def listar(self):
        """List all Related Equipment with Script.

        Somente retorna os relacionamentos dos equipamentos que o usuário autenticado tem
        permissão de leitura em pelo menos um grupo do equipamento.

        :return: Dictionary with the following structure:

        ::

          {'equipamento_roteiro': [{'roteiro': {'nome_tipo_roteiro': < nome_tipo_roteiro >,
          'descricao': < descricao >,
          'nome': < nome >,
          'id': < id >,
          'id_tipo_roteiro': < id_tipo_roteiro >,
          'descricao_tipo_roteiro': < descrição_tipo_roteiro >},
          'equipamento': {'id_modelo': < id_modelo >,
          'nome': < nome >,
          'nome_marca': < nome_marca >,
          'nome_modelo': < nome_modelo >,
          'id_marca': < id_marca >,
          'nome_tipo_equipamento': < nome_tipo_equipamento >,
          'id_tipo_equipamento': < id_tipo_equipamento >,
          'id': < id >}},
          ... demais equipamento_roteiro´s ...]}

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response
        """
        code, map = self.submit(None, 'GET', 'equipmentscript/all/')

        key = 'equipamento_roteiro'
        return get_list_map(self.response(code, map, [key]), key)

    def list_by_equip(self, name):
        """
        List all equipment script by equipment name

        :return: Dictionary with the following structure:

        ::

          {‘equipamento_roteiro’:[ {'id': <id_equipment_script>,
          'roteiro_id': <id_script>,
          'roteiro_name': <name_script>,
          'roteiro_desc': <desc_script>,
          'tipo_roteiro_id': <id_script_type>,
          'tipo_roteiro_name': <name_script_type>,
          'tipo_roteiro_desc': <desc_script_type>, }],
          'equipamento':
          {'id': <id_equipment>,
          'name': <name_equipment>,}}

        :raise InvalidParameterError: Name is null and invalid.
        :raise EquipamentoNotFoundError: Equipment name not found in database.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response
        """
        equip_script_map = dict()
        equip_script_map['name'] = name

        code, xml = self.submit(
            {"equipamento_roteiro": equip_script_map}, 'POST', 'equipamentoroteiro/name/')

        key = 'equipamento_roteiro'
        return get_list_map(self.response(code, xml, [key]), key)

    def inserir(self, id_equipment, id_script):
        """Inserts a new Related Equipment with Script and returns its identifier

        :param id_equipment: Identifier of the Equipment. Integer value and greater than zero.
        :param id_script: Identifier of the Script. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

          {'equipamento_roteiro': {'id': < id_equipment_script >}}

        :raise InvalidParameterError: The identifier of Equipment or Script is null and invalid.
        :raise RoteiroNaoExisteError: Script not registered.
        :raise EquipamentoNaoExisteError: Equipment not registered.
        :raise EquipamentoRoteiroError: Equipment is already associated with the script.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response
        """
        equipment_script_map = dict()
        equipment_script_map['id_equipment'] = id_equipment
        equipment_script_map['id_script'] = id_script

        code, xml = self.submit(
            {'equipment_script': equipment_script_map}, 'POST', 'equipmentscript/')

        return self.response(code, xml)

    def remover(self, id_equipment, id_script):
        """Remove Related Equipment with Script from by the identifier.

        :param id_equipment: Identifier of the Equipment. Integer value and greater than zero.
        :param id_script: Identifier of the Script. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: The identifier of Equipment or Script is null and invalid.
        :raise RoteiroNaoExisteError: Script not registered.
        :raise EquipamentoNaoExisteError: Equipment not registered.
        :raise EquipamentoRoteiroNaoExisteError: Equipment is not associated with the script.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response
        """
        if not is_valid_int_param(id_equipment):
            raise InvalidParameterError(
                u'The identifier of Equipment is invalid or was not informed.')

        if not is_valid_int_param(id_script):
            raise InvalidParameterError(
                u'The identifier of Script is invalid or was not informed.')

        url = 'equipmentscript/' + \
            str(id_equipment) + '/' + str(id_script) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)
