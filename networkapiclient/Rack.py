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
from networkapiclient.exception import InvalidParameterError
from networkapiclient.utils import is_valid_int_param, get_list_map
from networkapiclient.Pagination import Pagination
from Config import IP_VERSION

class Rack(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            Rack,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def insert_rack(
            self,
            number,
            name,
            mac_address_sw1,
            mac_address_sw2,
            mac_address_ilo,
            id_sw1,
            id_sw2,
            id_ilo):
        """Create new Rack
        :param number: Number of Rack
        :return: Following dictionary:
        ::
          {'rack': {'id': < id_rack >,
          'num_rack': < num_rack >,
          'name_rack': < name_rack >,
          'mac_sw1': < mac_sw1 >, 
          'mac_sw2': < mac_sw2 >, 
          'mac_ilo': < mac_ilo >, 
          'id_sw1': < id_sw1 >,
          'id_sw2': < id_sw2 >, 
          'id_ilo': < id_ilo >, } }
        :raise RacksError: Rack already registered with informed.
        :raise NumeroRackDuplicadoError: There is already a registered Rack with the value of number.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(number):
            raise InvalidParameterError(u'Rack number is none or invalid')

        rack_map = dict()
        rack_map['number'] = number
        rack_map['name'] = name
        rack_map['mac_address_sw1'] = mac_address_sw1
        rack_map['mac_address_sw2'] = mac_address_sw2
        rack_map['mac_address_ilo'] = mac_address_ilo
        rack_map['id_sw1'] = id_sw1
        rack_map['id_sw2'] = id_sw2
        rack_map['id_ilo'] = id_ilo

        code, xml = self.submit({'rack': rack_map}, 'POST', 'rack/insert/')

        return self.response(code, xml)

    def find_racks(self):
        """
        :return: Dictionary with the following structure:

        ::

            {Rack: {rack_number: < rack_number >,
            'sw1':< sw1 >,
            'mac1':< mac1 >,
            'sw2':< sw2 >,
        'mac2':< mac2 >,
            'ilo':< ilo >,
            'mac_ilo':< mac_ilo > } }

        :raise VipNaoExisteError: No request for registered VIP.
        :raise DataBaseError: Can't connect to networkapi database.
        :raise XMLError: Failed to generate the XML response.
        """

        url = 'rack/find/'
        code, xml = self.submit(None, 'GET', url)

        key = "rack"
        return get_list_map(self.response(code, xml, [key]), key)

    def list(self):
        """
        :return: Dictionary with the following structure:

        ::

            {Rack: {rack_number: < rack_number >,
            'sw1':< sw1 >,
            'mac1':< mac1 >,
            'sw2':< sw2 >,
        'mac2':< mac2 >,
            'ilo':< ilo >,
            'mac_ilo':< mac_ilo > } }

        :raise VipNaoExisteError: No request for registered VIP.
        :raise DataBaseError: Can't connect to networkapi database.
        :raise XMLError: Failed to generate the XML response.
        """

        url = 'rack/list/'
        code, xml = self.submit(None, 'GET', url)

        key = "rack"
        return get_list_map(self.response(code, xml, [key]), key)

    def get_rack(self, name):


        url = 'rack/find/' + str(name) + '/'
        code, xml = self.submit(None, 'GET', url)

        key = "rack"
        return get_list_map(self.response(code, xml, [key]), key)

    def edit_rack(self,
            id_rack, 
            number, 
            name, 
            mac_sw1, 
            mac_sw2, 
            mac_ilo, 
            id_sw1, 
            id_sw2, 
            id_ilo):

        rack_map = dict()
        rack_map['id_rack'] = id_rack
        rack_map['number'] = number
        rack_map['name'] = name
        rack_map['mac_address_sw1'] = mac_sw1
        rack_map['mac_address_sw2'] = mac_sw2
        rack_map['mac_address_ilo'] = mac_ilo
        rack_map['id_sw1'] = id_sw1
        rack_map['id_sw2'] = id_sw2
        rack_map['id_ilo'] = id_ilo

        code, xml = self.submit({'rack': rack_map}, 'POST', 'rack/edit/')

        return self.response(code, xml)


    def remover(self, id_rack):
        """Remove Rack by the identifier.

        :param id_rack: Identifier of the Rack. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: The identifier of Rack is null and invalid.
        :raise RackNaoExisteError: Rack not registered.
        :raise RackError: Rack is associated with a script.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_rack):
            raise InvalidParameterError(
                u'The identifier of Rack is invalid or was not informed.')

        url = 'rack/' + str(id_rack) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

   
    def gerar_arq_config (self, id_rack):
        """Create the configuration file of each equipment on the Rack and create 
        all racks vlan and environments.
 
        :param id_rack: Identifier of the Rack. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: The identifier of Rack is null and invalid.
        :raise RackNaoExisteError: Rack not registered.
        :raise RackError: Rack is associated with a script.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """  

        if not is_valid_int_param(id_rack):
            raise InvalidParameterError(
                u'The identifier of Rack is invalid or was not informed.')

        url = 'rack/gerar-configuracao/' + str(id_rack) + '/'
        code, xml = self.submit(None, 'POST', url)

        return self.response(code, xml)


    def aplicar_configuracao(self, id_rack):
        

        if not is_valid_int_param(id_rack):
            raise InvalidParameterError(
                u'The identifier of Rack is invalid or was not informed.')

        url = 'rack/aplicar-config/' + str(id_rack) + '/'
        code, xml = self.submit(None, 'POST', url)

        return self.response(code, xml)

    def list_all_rack_environments(self, id_rack):

        url = 'rack/list-rack-environment/' + str(id_rack) + '/'
        code, xml = self.submit(None, 'GET', url)

        key = 'ambiente'
        return get_list_map(self.response(code, xml, [key]), key)


    def get_rack_by_equip_id(self, equip_id):

        url = 'rack/get-by-equip/' + str(equip_id) + '/'
        code, xml = self.submit(None, 'GET', url)

        key = 'rack'
        return get_list_map(self.response(code, xml, [key]), key)