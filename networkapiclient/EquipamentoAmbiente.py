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


class EquipamentoAmbiente(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            EquipamentoAmbiente,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def inserir(self, id_equipment, id_environment, is_router=0):
        """Inserts a new Related Equipment with Environment and returns its identifier

        :param id_equipment: Identifier of the Equipment. Integer value and greater than zero.
        :param id_environment: Identifier of the Environment. Integer value and greater than zero.
        :param is_router: Identifier of the Environment. Boolean value.

        :return: Dictionary with the following structure:

        ::

            {'equipamento_ambiente': {'id': < id_equipment_environment >}}

        :raise InvalidParameterError: The identifier of Equipment or Environment is null and invalid.
        :raise AmbienteNaoExisteError: Environment not registered.
        :raise EquipamentoNaoExisteError: Equipment not registered.
        :raise EquipamentoAmbienteError: Equipment is already associated with the Environment.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        equipment_environment_map = dict()
        equipment_environment_map['id_equipamento'] = id_equipment
        equipment_environment_map['id_ambiente'] = id_environment
        equipment_environment_map['is_router'] = is_router

        code, xml = self.submit(
            {'equipamento_ambiente': equipment_environment_map}, 'POST', 'equipamentoambiente/')

        return self.response(code, xml)

    def remover(self, id_equipment, id_environment):
        """Remove Related Equipment with Environment from by the identifier.

        :param id_equipment: Identifier of the Equipment. Integer value and greater than zero.
        :param id_environment: Identifier of the Environment. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError:  The identifier of Environment, Equipament is null and invalid.
        :raise EquipamentoNotFoundError: Equipment not registered.
        :raise EquipamentoAmbienteNaoExisteError: Environment not registered.
        :raise VipIpError: IP-related equipment is being used for a request VIP.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise DataBaseError: Networkapi failed to access the database.
        """

        if not is_valid_int_param(id_equipment):
            raise InvalidParameterError(
                u'The identifier of Equipment is invalid or was not informed.')

        if not is_valid_int_param(id_environment):
            raise InvalidParameterError(
                u'The identifier of Environment is invalid or was not informed.')

        url = 'equipment/' + \
            str(id_equipment) + '/environment/' + str(id_environment) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def update(self, id_equipment, id_environment, is_router):
        """Remove Related Equipment with Environment from by the identifier.

        :param id_equipment: Identifier of the Equipment. Integer value and greater than zero.
        :param id_environment: Identifier of the Environment. Integer value and greater than zero.
        :param is_router: Identifier of the Environment. Boolean value.

        :return: None

        :raise InvalidParameterError:  The identifier of Environment, Equipament is null and invalid.
        :raise EquipamentoNotFoundError: Equipment not registered.
        :raise EquipamentoAmbienteNaoExisteError: Environment not registered.
        :raise VipIpError: IP-related equipment is being used for a request VIP.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise DataBaseError: Networkapi failed to access the database.
        """

        if not is_valid_int_param(id_equipment):
            raise InvalidParameterError(
                u'The identifier of Equipment is invalid or was not informed.')

        if not is_valid_int_param(id_environment):
            raise InvalidParameterError(
                u'The identifier of Environment is invalid or was not informed.')

        equipment_environment_map = dict()
        equipment_environment_map['id_equipamento'] = id_equipment
        equipment_environment_map['id_ambiente'] = id_environment
        equipment_environment_map['is_router'] = is_router

        code, xml = self.submit(
            {'equipamento_ambiente': equipment_environment_map}, 'PUT', 'equipamentoambiente/update/')

        return self.response(code, xml)
