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
from networkapiclient.utils import is_valid_int_param, is_valid_ip, get_list_map


class Ip(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(Ip, self).__init__(networkapi_url, user, password, user_ldap)

    def get_ipv4(self, id_ip):
        """Get IPv4 by id.

        :param id_ip: ID of IPv4.

        :return: Dictionary with the following structure:

        ::

            {'ip': {'id': < id >,
            'networkipv4': < networkipv4 >,
            'oct4': < oct4 >,
            'oct3': < oct3 >,
            'oct2': < oct2 >,
            'oct1': < oct1 >,
            'descricao': < descricao >,
            'equipamentos': [ { all name of equipments related } ] , }}

        :raise IpNaoExisteError: IP is not registered.
        :raise InvalidParameterError: IP identifier is null or invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_ip):
            raise InvalidParameterError(
                u'The IPv4 identifier is invalid or was not informed.')

        url = 'ip/get-ipv4/' + str(id_ip) + '/'

        code, xml = self.submit(None, 'GET', url)

        key = 'ipv4'
        return get_list_map(self.response(code, xml, ["equipamentos"]), key)

    def get_ipv6(self, id_ip):
        """Get IPv6 by id.

        :param id_ip: ID of IPv6.

        :return: Dictionary with the following structure:

        ::

            {'ip': {'id': < id >,
            'networkipv6': < networkipv6 >,
            'block1': < block1 >,
            'block2': < block2 >,
            'block3': < block3 >,
            'block4': < block4 >,
            'block5': < block5 >,
            'block6': < block6 >,
            'block7': < block7 >,
            'block8': < block8 >,
            'description': < description >,
            'equipamentos': [ { all name of equipments related } ] , }}

        :raise IpNaoExisteError: IP is not registered.
        :raise InvalidParameterError: IP identifier is null or invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_ip):
            raise InvalidParameterError(
                u'The IPv6 identifier is invalid or was not informed.')

        url = 'ip/get-ipv6/' + str(id_ip) + '/'

        code, xml = self.submit(None, 'GET', url)

        key = 'ipv6'
        return get_list_map(self.response(code, xml, ["equipamentos"]), key)

    def buscar_por_ip_ambiente(self, ip, id_environment):
        """Get IP with an associated environment.

        :param ip: IP address in the format x1.x2.x3.x4.
        :param id_environment: Identifier of the environment. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            {'ip': {'id': < id >,
            'id_vlan': < id_vlan >,
            'oct4': < oct4 >,
            'oct3': < oct3 >,
            'oct2': < oct2 >,
            'oct1': < oct1 >,
            'descricao': < descricao > }}

        :raise IpNaoExisteError: IP is not registered or not associated with environment.
        :raise InvalidParameterError: The environment identifier and/or IP is/are null or invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        """

        if not is_valid_int_param(id_environment):
            raise InvalidParameterError(
                u'Environment identifier is invalid or was not informed.')

        if not is_valid_ip(ip):
            raise InvalidParameterError(u'IP is invalid or was not informed.')

        url = 'ip/' + str(ip) + '/ambiente/' + str(id_environment) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def get_available_ip4(self, id_network):
        """
        Get a available IP in the network ipv4

        :param id_network: Network identifier. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            {'ip': {'ip': < available_ip >}}

        :raise IpNotAvailableError: Network dont have available IP for insert a new IP
        :raise NetworkIPv4NotFoundError: Network is not found
        :raise UserNotAuthorizedError: User dont have permission to get a available IP
        :raise InvalidParameterError: Network identifier is null or invalid.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise DataBaseError: Networkapi failed to access the database.
        """

        if not is_valid_int_param(id_network):
            raise InvalidParameterError(
                u'Network identifier is invalid or was not informed.')

        url = 'ip/availableip4/' + str(id_network) + "/"

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def get_ip_by_equip_and_vip(self, equip_name, id_evip):
        """
        Get a available IP in the Equipment related Environment VIP

        :param equip_name: Equipment Name.
        :param id_evip: Vip environment identifier. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            { 'ipv4': [ {'id': < id >, 'ip': < ip >, 'network': { 'id': < id >, 'network': < network >, 'mask': < mask >, }} ... ],
            'ipv6': [ {'id': < id >, 'ip': < ip >, 'network': { 'id': < id >, 'network': < network >, 'mask': < mask >, }} ... ] }

        :raise InvalidParameterError: Vip environment identifier or equipment name is none or invalid.
        :raise EquipamentoNotFoundError: Equipment not registered.
        :raise EnvironmentVipNotFoundError: Vip environment not registered.
        :raise UserNotAuthorizedError: User dont have permission to perform operation.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise DataBaseError: Networkapi failed to access the database.
        """

        if not is_valid_int_param(id_evip):
            raise InvalidParameterError(
                u'Vip environment is invalid or was not informed.')

        ip_map = dict()
        ip_map['equip_name'] = equip_name
        ip_map['id_evip'] = id_evip

        url = "ip/getbyequipandevip/"

        code, xml = self.submit({'ip_map': ip_map}, 'POST', url)

        return self.response(code, xml)

    def get_ipv4_or_ipv6(self, ip):
        """
        Get a Ipv4 or Ipv6 by IP

        :param ip: IPv4 or Ipv6. 'xxx.xxx.xxx.xxx or xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx'

        :return: Dictionary with the following structure:

        ::

            {'ips': [{'oct4': < oct4 >, 'oct2': < oct2 >, 'oct3': < oct3 >,
            'oct1': < oct1 >, 'version': < version >,
            'networkipv4': < networkipv4 >, 'id': < id >, 'descricao': < descricao >}, ... ] }.
            or
            {'ips': [ {'block1': < block1 >, 'block2': < block2 >, 'block3': < block3 >, 'block4': < block4 >, 'block5': < block5 >, 'block6': < block6 >, 'block7': < block7 >, 'block8': < block8 >,
            'version': < version >, 'networkipv6': < networkipv6 >, 'id': < id >, 'descricao': < descricao >}, ... ] }.

        :raise IpNaoExisteError: Ipv4 or Ipv6 not found.
        :raise UserNotAuthorizedError: User dont have permission to perform operation.
        :raise InvalidParameterError: Ip string is none or invalid.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise DataBaseError: Networkapi failed to access the database.
        """

        ip_map = dict()
        ip_map['ip'] = ip

        url = "ip/getbyoctblock/"

        code, xml = self.submit({'ip_map': ip_map}, 'POST', url)

        return self.response(code, xml)

    def check_vip_ip(self, ip, id_evip):
        """
        Get a Ipv4 or Ipv6 for Vip request

        :param ip: IPv4 or Ipv6. 'xxx.xxx.xxx.xxx or xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx'

        :return: Dictionary with the following structure:

        ::

            {'ip': {'ip': < ip - octs for ipv4, blocks for ipv6 - >,
            'id': <id>,
            'network4 or network6'}}.

        :raise IpNaoExisteError: Ipv4 or Ipv6 not found.
        :raise EnvironemntVipNotFoundError: Vip environment not found.
        :raise IPNaoDisponivelError: Ip not available for Vip Environment.
        :raise UserNotAuthorizedError: User dont have permission to perform operation.
        :raise InvalidParameterError: Ip string or vip environment is none or invalid.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise DataBaseError: Networkapi failed to access the database.

        """

        ip_map = dict()
        ip_map['ip'] = ip
        ip_map['id_evip'] = id_evip

        url = "ip/checkvipip/"

        code, xml = self.submit({'ip_map': ip_map}, 'POST', url)

        return self.response(code, xml)

    def get_available_ip6(self, id_network6):
        """
        Get a available IP in Network ipv6

        :param id_network6: Network ipv6 identifier. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            {'ip6': {'ip6': < available_ip6 >}}

        :raise IpNotAvailableError: Network dont have available IP.
        :raise NetworkIPv4NotFoundError: Network was not found.
        :raise UserNotAuthorizedError: User dont have permission to get a available IP.
        :raise InvalidParameterError: Network ipv6 identifier is none or invalid.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise DataBaseError: Networkapi failed to access the database.

        """

        if not is_valid_int_param(id_network6):
            raise InvalidParameterError(
                u'Network ipv6 identifier is invalid or was not informed.')

        url = 'ip/availableip6/' + str(id_network6) + "/"

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def get_available_ip6_for_vip(self, id_evip, name):
        """
        Get and save a available IP in the network ipv6 for vip request

        :param id_evip: Vip environment identifier. Integer value and greater than zero.
        :param name: Ip description

        :return: Dictionary with the following structure:

        ::

            {'ip': {'bloco1':<bloco1>,
            'bloco2':<bloco2>,
            'bloco3':<bloco3>,
            'bloco4':<bloco4>,
            'bloco5':<bloco5>,
            'bloco6':<bloco6>,
            'bloco7':<bloco7>,
            'bloco8':<bloco8>,
            'id':<id>,
            'networkipv6':<networkipv6>,
            'description':<description>}}

        :raise IpNotAvailableError: Network dont have available IP for vip environment.
        :raise EnvironmentVipNotFoundError: Vip environment not registered.
        :raise UserNotAuthorizedError: User dont have permission to perform operation.
        :raise InvalidParameterError: Vip environment identifier is none or invalid.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise DataBaseError: Networkapi failed to access the database.

        """

        if not is_valid_int_param(id_evip):
            raise InvalidParameterError(
                u'Vip environment identifier is invalid or was not informed.')

        url = 'ip/availableip6/vip/' + str(id_evip) + "/"

        ip_map = dict()
        ip_map['id_evip'] = id_evip
        ip_map['name'] = name

        code, xml = self.submit({'ip_map': ip_map}, 'POST', url)

        return self.response(code, xml)

    def get_available_ip4_for_vip(self, id_evip, name):
        """
        Get and save a available IP in the network ipv6 for vip request

        :param id_evip: Vip environment identifier. Integer value and greater than zero.
        :param name: Ip description

        :return: Dictionary with the following structure:

        ::

            {'ip': {'oct1': < oct1 >,
            'oct2': < oct2 >,
            'oct3': < oct3 >,
            'oct4': < oct4 >,
            'networkipv4': <networkipv4>,
            'id': <id>,
            'descricao': <descricao>}}

        :raise IpNotAvailableError: Network dont have available IP for vip environment.
        :raise EnvironmentVipNotFoundError: Vip environment not registered.
        :raise UserNotAuthorizedError: User dont have permission to perform operation.
        :raise InvalidParameterError: Vip environment identifier is none or invalid.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise DataBaseError: Networkapi failed to access the database.

        """

        if not is_valid_int_param(id_evip):
            raise InvalidParameterError(
                u'Vip environment identifier is invalid or was not informed.')

        url = 'ip/availableip4/vip/' + str(id_evip) + "/"

        ip_map = dict()
        ip_map['id_evip'] = id_evip
        ip_map['name'] = name

        code, xml = self.submit({'ip_map': ip_map}, 'POST', url)

        return self.response(code, xml)

    def edit_ipv4(self, ip4, descricao, id_ip):
        """
        Edit a IP4

        :param ip4: An IP4 available to save in format x.x.x.x.
        :param id_ip: IP identifier. Integer value and greater than zero.
        :param descricao: IP description.

        :return: None
        """

        if not is_valid_int_param(id_ip):
            raise InvalidParameterError(
                u'Ip identifier is invalid or was not informed.')

        if ip4 is None or ip4 == "":
            raise InvalidParameterError(
                u'The IP4 is invalid or was not informed.')

        ip_map = dict()
        ip_map['descricao'] = descricao
        ip_map['ip4'] = ip4
        ip_map['id_ip'] = id_ip

        url = "ip4/edit/"

        code, xml = self.submit({'ip_map': ip_map}, 'POST', url)

        return self.response(code, xml)

    def save_ipv4(self, ip4, id_equip, descricao, id_net):
        """
        Save a IP4 and associate with equipment

        :param ip4: An IP4 available to save in format x.x.x.x.
        :param id_equip: Equipment identifier. Integer value and greater than zero.
        :param descricao: IP description.
        :param id_net: Network identifier. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            { ip: { id: <id_ip4>,
            oct1: <oct1>,
            oct2: <oct2>,
            oct3: <oct3>,
            oct4: <oct4>,
            equipamento: [ { all equipamentos related } ] ,
            descricao: <descricao> } }
        """
        if not is_valid_int_param(id_net):
            raise InvalidParameterError(
                u'Network identifier is invalid or was not informed.')

        if not is_valid_int_param(id_equip):
            raise InvalidParameterError(
                u'Equipment identifier is invalid or was not informed.')

        if ip4 is None or ip4 == "":
            raise InvalidParameterError(u'IP4 is invalid or was not informed.')

        ip_map = dict()
        ip_map['id_net'] = id_net
        ip_map['descricao'] = descricao
        ip_map['ip4'] = ip4
        ip_map['id_equip'] = id_equip

        url = "ipv4/save/"

        code, xml = self.submit({'ip_map': ip_map}, 'POST', url)

        return self.response(code, xml)

    def edit_ipv6(self, ip6, descricao, id_ip):
        """
        Edit a IP6

        :param ip6: An IP6 available to save in format xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx.
        :param descricao: IP description.
        :param id_ip: Ipv6 identifier. Integer value and greater than zero.

        :return: None
        """

        if not is_valid_int_param(id_ip):
            raise InvalidParameterError(
                u'Ipv6 identifier is invalid or was not informed.')

        if ip6 is None or ip6 == "":
            raise InvalidParameterError(u'IP6 is invalid or was not informed.')

        ip_map = dict()
        ip_map['descricao'] = descricao
        ip_map['ip6'] = ip6
        ip_map['id_ip'] = id_ip

        url = "ipv6/edit/"

        code, xml = self.submit({'ip_map': ip_map}, 'POST', url)

        return self.response(code, xml)

    def find_ip4_by_id(self, id_ip):
        """
        Get an IP by ID

        :param id_ip: IP identifier. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            { ips { id: <id_ip4>,
            oct1: <oct1>,
            oct2: <oct2>,
            oct3: <oct3>,
            oct4: <oct4>,
            equipamento: [ {all equipamentos related} ] ,
            descricao: <descricao>} }

        :raise IpNotAvailableError: Network dont have available IP.
        :raise NetworkIPv4NotFoundError: Network was not found.
        :raise UserNotAuthorizedError: User dont have permission to perform operation.
        :raise InvalidParameterError: Ip identifier is none or invalid.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise DataBaseError: Networkapi failed to access the database.

        """

        if not is_valid_int_param(id_ip):
            raise InvalidParameterError(
                u'Ip identifier is invalid or was not informed.')

        url = 'ip/get/' + str(id_ip) + "/"

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def find_ips_by_equip(self, id_equip):
        """
        Get Ips related to equipment by its identifier

        :param id_equip: Equipment identifier. Integer value and greater than zero.

        :return: Dictionary with the following structure:

            { ips: { ipv4:[
            id: <id_ip4>,
            oct1: <oct1>,
            oct2: <oct2>,
            oct3: <oct3>,
            oct4: <oct4>,
            descricao: <descricao> ]
            ipv6:[
            id: <id_ip6>,
            block1: <block1>,
            block2: <block2>,
            block3: <block3>,
            block4: <block4>,
            block5: <block5>,
            block6: <block6>,
            block7: <block7>,
            block8: <block8>,
            descricao: <descricao> ] } }

        :raise UserNotAuthorizedError: User dont have permission to list ips.
        :raise InvalidParameterError: Equipment identifier is none or invalid.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise DataBaseError: Networkapi failed to access the database.

        """
        url = 'ip/getbyequip/' + str(id_equip) + "/"

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml, ['ipv4', 'ipv6'])

    def find_ip6_by_id(self, id_ip):
        """
        Get an IP6 by ID

        :param id_ip: IP6 identifier. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            {'ip': {'id': < id >,
            'block1': <block1>,
            'block2': <block2>,
            'block3': <block3>,
            'block4': <block4>,
            'block5': <block5>,
            'block6': <block6>,
            'block7': <block7>,
            'block8': <block8>,
            'descricao': < description >,
            'equipamento': [ { all name equipamentos related} ], }}


        :raise IpNotAvailableError: Network dont have available IPv6.
        :raise NetworkIPv4NotFoundError: Network was not found.
        :raise UserNotAuthorizedError: User dont have permission to perform operation.
        :raise InvalidParameterError: IPv6 identifier is none or invalid.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise DataBaseError: Networkapi failed to access the database.

        """

        if not is_valid_int_param(id_ip):
            raise InvalidParameterError(
                u'Ipv6 identifier is invalid or was not informed.')

        url = 'ipv6/get/' + str(id_ip) + "/"

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def save_ipv6(self, ip6, id_equip, descricao, id_net):
        """
        Save an IP6 and associate with equipment

        :param ip6: An IP6 available to save in format xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx.
        :param id_equip: Equipment identifier. Integer value and greater than zero.
        :param descricao: IPv6 description.
        :param id_net: Network identifier. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            {'ipv6': {'id': < id >,
            'block1': <block1>,
            'block2': <block2>,
            'block3': <block3>,
            'block4': <block4>,
            'block5': <block5>,
            'block6': <block6>,
            'block7': <block7>,
            'block8': <block8>,
            'descricao': < description >,
            'equipamento': [ { all name equipamentos related } ], }}
        """
        if not is_valid_int_param(id_net):
            raise InvalidParameterError(
                u'Network identifier is invalid or was not informed.')

        if not is_valid_int_param(id_equip):
            raise InvalidParameterError(
                u'Equipment identifier is invalid or was not informed.')

        if ip6 is None or ip6 == "":
            raise InvalidParameterError(
                u'IPv6 is invalid or was not informed.')

        ip_map = dict()
        ip_map['id_net'] = id_net
        ip_map['descricao'] = descricao
        ip_map['ip6'] = ip6
        ip_map['id_equip'] = id_equip

        url = "ipv6/save/"

        code, xml = self.submit({'ip_map': ip_map}, 'POST', url)

        return self.response(code, xml)

    def delete_ip4(self, id_ip):
        """
        Delete an IP4

        :param id_ip: Ipv4 identifier. Integer value and greater than zero.

        :return: None

        :raise IpNotFoundError: IP is not registered.
        :raise DataBaseError: Networkapi failed to access the database.

        """

        if not is_valid_int_param(id_ip):
            raise InvalidParameterError(
                u'Ipv4 identifier is invalid or was not informed.')

        url = 'ip4/delete/' + str(id_ip) + "/"

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def delete_ip6(self, id_ip):
        """
        Delete an IP6

        :param id_ip: Ipv6 identifier. Integer value and greater than zero.

        :return: None

        :raise IpNotFoundError: IP is not registered.
        :raise DataBaseError: Networkapi failed to access the database.

        """

        if not is_valid_int_param(id_ip):
            raise InvalidParameterError(
                u'Ipv6 identifier is invalid or was not informed.')

        url = 'ipv6/delete/' + str(id_ip) + "/"

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def find_ip4_by_network(self, id_network):
        """List IPv4 from network.

        :param id_network: Networkv ipv4 identifier. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            {'ip': {'id': < id >,
            'id_vlan': < id_vlan >,
            'oct4': < oct4 >,
            'oct3': < oct3 >,
            'oct2': < oct2 >,
            'oct1': < oct1 >,
            'descricao': < descricao >
            'equipamento': [ { all name equipamentos related } ], }}

        :raise IpNaoExisteError: Network does not have any ips.
        :raise InvalidParameterError: Network identifier is none or invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        """

        if not is_valid_int_param(id_network):
            raise InvalidParameterError(
                u'Network identifier is invalid or was not informed.')

        url = 'ip/id_network_ipv4/' + str(id_network) + "/"

        code, xml = self.submit(None, 'GET', url)

        key = "ips"
        return get_list_map(self.response(code, xml, [key]), key)

    def find_ip6_by_network(self, id_network):
        """List IPv6 from network.

        :param id_network: Network ipv6 identifier. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            {'ip': {'id': < id >,
            'id_vlan': < id_vlan >,
            'block1': <block1>,
            'block2': <block2>,
            'block3': <block3>,
            'block4': <block4>,
            'block5': <block5>,
            'block6': <block6>,
            'block7': <block7>,
            'block8': <block8>,
            'descricao': < description >
            'equipamento': [ { all name equipamentos related } ], }}

        :raise IpNaoExisteError: Network does not have any ips.
        :raise InvalidParameterError: Network identifier is none or invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        """

        if not is_valid_int_param(id_network):
            raise InvalidParameterError(
                u'Network identifier is invalid or was not informed.')

        url = 'ip/id_network_ipv6/' + str(id_network) + "/"

        code, xml = self.submit(None, 'GET', url)

        key = "ips"
        return get_list_map(self.response(code, xml, [key]), key)

    def search_ipv6_environment(self, ipv6, id_environment):
        """Get IPv6 with an associated environment.

        :param ipv6: IPv6 address in the format x1:x2:x3:x4:x5:x6:x7:x8.
        :param id_environment: Environment identifier. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::


            {'ipv6': {'id': < id >,
            'id_vlan': < id_vlan >,
            'bloco1': < bloco1 >,
            'bloco2': < bloco2 >,
            'bloco3': < bloco3 >,
            'bloco4': < bloco4 >,
            'bloco5': < bloco5 >,
            'bloco6': < bloco6 >,
            'bloco7': < bloco7 >,
            'bloco8': < bloco8 >,
            'descricao': < descricao > }}

        :raise IpNaoExisteError: IPv6 is not registered or is not associated to the environment.
        :raise AmbienteNaoExisteError: Environment not found.
        :raise InvalidParameterError: Environment identifier and/or IPv6 string is/are none or invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_environment):
            raise InvalidParameterError(
                u'Environment identifier is invalid or was not informed.')

        ipv6_map = dict()
        ipv6_map['ipv6'] = ipv6
        ipv6_map['id_environment'] = id_environment

        code, xml = self.submit(
            {'ipv6_map': ipv6_map}, 'POST', 'ipv6/environment/')

        return self.response(code, xml)

    def assoc_ipv4(self, id_ip, id_equip, id_net):
        """
        Associate an IP4 with equipment.

        :param id_ip: IPv4 identifier.
        :param id_equip: Equipment identifier. Integer value and greater than zero.
        :param id_net: Network identifier. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: IPv4, Equipment or Network identifier is none or invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_ip):
            raise InvalidParameterError(
                u'Ip identifier is invalid or was not informed.')

        if not is_valid_int_param(id_net):
            raise InvalidParameterError(
                u'Network identifier is invalid or was not informed.')

        if not is_valid_int_param(id_equip):
            raise InvalidParameterError(
                u'Equipment identifier is invalid or was not informed.')

        ip_map = dict()
        ip_map['id_ip'] = id_ip
        ip_map['id_net'] = id_net
        ip_map['id_equip'] = id_equip

        url = "ipv4/assoc/"

        code, xml = self.submit({'ip_map': ip_map}, 'POST', url)

        return self.response(code, xml)

    def assoc_ipv6(self, id_ip, id_equip, id_net):
        """
        Associate an IP6 with equipment.

        :param id_ip: IPv6 identifier.
        :param id_equip: Equipment identifier. Integer value and greater than zero.
        :param id_net: Network identifier. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: IPv6, Equipment or Network identifier is none or invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_ip):
            raise InvalidParameterError(
                u'Ipv6 identifier is invalid or was not informed.')

        if not is_valid_int_param(id_net):
            raise InvalidParameterError(
                u'Network identifier is invalid or was not informed.')

        if not is_valid_int_param(id_equip):
            raise InvalidParameterError(
                u'Equipment identifier is invalid or was not informed.')

        ip_map = dict()
        ip_map['id_ip'] = id_ip
        ip_map['id_net'] = id_net
        ip_map['id_equip'] = id_equip

        url = "ipv6/assoc/"

        code, xml = self.submit({'ip_map': ip_map}, 'POST', url)

        return self.response(code, xml)
