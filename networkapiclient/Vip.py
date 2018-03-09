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
from networkapiclient.exception import InvalidParameterError
from networkapiclient.GenericClient import GenericClient
from networkapiclient.utils import is_valid_int_param


class Vip(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(Vip, self).__init__(networkapi_url, user, password, user_ldap)

    def edit_reals(
            self,
            id_vip,
            method_bal,
            reals,
            reals_prioritys,
            reals_weights,
            alter_priority=0):
        """Execute the script 'gerador_vips' several times with options -real, -add and -del to adjust vip request reals.
        :param id_vip: Identifier of the VIP. Integer value and greater than zero.
        :param method_bal: method_bal.
        :param reals: List of reals. Ex: [{'real_name':'Teste1', 'real_ip':'10.10.10.1'},{'real_name':'Teste2', 'real_ip':'10.10.10.2'}]
        :param reals_prioritys: List of reals_priority. Ex: ['1','5','3'].
        :param reals_weights: List of reals_weight. Ex: ['1','5','3'].
        :param alter_priority: 1 if priority has changed and 0 if hasn't changed.
        :return: None
        :raise VipNaoExisteError: Request VIP not registered.
        :raise InvalidParameterError: Identifier of the request is invalid or null VIP.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise EnvironmentVipError: The combination of finality, client and environment is invalid.
        :raise InvalidTimeoutValueError: The value of timeout is invalid.
        :raise InvalidBalMethodValueError: The value of method_bal is invalid.
        :raise InvalidCacheValueError: The value of cache is invalid.
        :raise InvalidPersistenceValueError: The value of persistence is invalid.
        :raise InvalidPriorityValueError: One of the priority values is invalid.
        :raise EquipamentoNaoExisteError: The equipment associated with this Vip Request doesn't exist.
        :raise IpEquipmentError: Association between equipment and ip of this Vip Request doesn't exist.
        :raise IpError: IP not registered.
        :raise RealServerPriorityError: Vip Request priority list has an error.
        :raise RealServerWeightError: Vip Request weight list has an error.
        :raise RealServerPortError: Vip Request port list has an error.
        :raise RealParameterValueError: Vip Request real server parameter list has an error.
        :raise RealServerScriptError: Vip Request real server script execution error.
        """

        if not is_valid_int_param(id_vip):
            raise InvalidParameterError(
                u'The identifier of vip is invalid or was not informed.')

        vip_map = dict()
        vip_map['vip_id'] = id_vip
        # vip_map['metodo_bal'] = method_bal
        vip_map['reals'] = {'real': reals}
        vip_map['reals_prioritys'] = {'reals_priority': reals_prioritys}
        vip_map['reals_weights'] = {'reals_weight': reals_weights}
        vip_map['alter_priority'] = alter_priority

        url = 'vip/real/edit/'

        code, xml = self.submit({'vip': vip_map}, 'PUT', url)

        return self.response(code, xml)
