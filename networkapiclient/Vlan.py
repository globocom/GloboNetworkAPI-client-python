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


class Vlan(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(Vlan, self).__init__(networkapi_url, user, password, user_ldap)

    def invalidate(self, id_vlan):
        """Invalidates ACL - IPv4 of VLAN from its identifier.

        Assigns 0 to 'acl_valida' and null to 'acl_file_name'.

        :param id_vlan: Identifier of the Vlan. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: Vlan identifier is null and invalid.
        :raise VlanNaoExisteError: Vlan not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_vlan):
            raise InvalidParameterError(
                u'The identifier of Vlan is invalid or was not informed.')

        url = 'vlan/%s/invalidate/%s/' % (str(id_vlan), IP_VERSION.IPv4[0])

        code, xml = self.submit(None, 'PUT', url)

        return self.response(code, xml)

    def invalidate_ipv6(self, id_vlan):
        """Invalidates ACL - IPv6 of VLAN from its identifier.

        Assigns 0 to 'acl_valida_v6' and null to 'acl_file_name_v6'.

        :param id_vlan: Identifier of the Vlan. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: Vlan identifier is null and invalid.
        :raise VlanNaoExisteError: Vlan not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_vlan):
            raise InvalidParameterError(
                u'The identifier of Vlan is invalid or was not informed.')

        url = 'vlan/%s/invalidate/%s/' % (str(id_vlan), IP_VERSION.IPv6[0])

        code, xml = self.submit(None, 'PUT', url)

        return self.response(code, xml)

    def find_vlans(
            self,
            number,
            name,
            iexact,
            environment,
            net_type,
            network,
            ip_version,
            subnet,
            acl,
            pagination):
        """
        Find vlans by all search parameters

        :param number: Filter by vlan number column
        :param name: Filter by vlan name column
        :param iexact: Filter by name will be exact?
        :param environment: Filter by environment ID related
        :param net_type: Filter by network_type ID related
        :param network: Filter by each octs in network
        :param ip_version: Get only version (0:ipv4, 1:ipv6, 2:all)
        :param subnet: Filter by octs will search by subnets?
        :param acl: Filter by vlan acl column
        :param pagination: Class with all data needed to paginate

        :return: Following dictionary:

        ::

          {'vlan': {'id': < id_vlan >,
          'nome': < nome_vlan >,
          'num_vlan': < num_vlan >,
          'id_ambiente': < id_ambiente >,
          'descricao': < descricao >,
          'acl_file_name': < acl_file_name >,
          'acl_valida': < acl_valida >,
          'acl_file_name_v6': < acl_file_name_v6 >,
          'acl_valida_v6': < acl_valida_v6 >,
          'ativada': < ativada >,
          'ambiente_name': < divisao_dc-ambiente_logico-grupo_l3 >
          'redeipv4': [ { all networkipv4 related } ],
          'redeipv6': [ { all networkipv6 related } ] },
          'total': {< total_registros >} }

        :raise InvalidParameterError: Some parameter was invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not isinstance(pagination, Pagination):
            raise InvalidParameterError(
                u"Invalid parameter: pagination must be a class of type 'Pagination'.")

        vlan_map = dict()

        vlan_map["start_record"] = pagination.start_record
        vlan_map["end_record"] = pagination.end_record
        vlan_map["asorting_cols"] = pagination.asorting_cols
        vlan_map["searchable_columns"] = pagination.searchable_columns
        vlan_map["custom_search"] = pagination.custom_search

        vlan_map["numero"] = number
        vlan_map["nome"] = name
        vlan_map["exato"] = iexact
        vlan_map["ambiente"] = environment
        vlan_map["tipo_rede"] = net_type
        vlan_map["rede"] = network
        vlan_map["versao"] = ip_version
        vlan_map["subrede"] = subnet
        vlan_map["acl"] = acl

        url = "vlan/find/"

        code, xml = self.submit({"vlan": vlan_map}, "POST", url)

        key = "vlan"
        return get_list_map(
            self.response(
                code, xml, [
                    key, "redeipv4", "redeipv6", "equipamentos"]), key)

    def list_all(self):
        """
        List all vlans

        :return: Following dictionary:

        ::

          {'vlan': [{'id': < id_vlan >,
          'name': < nome_vlan >} {... demais vlans ...} ] }

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        url = 'vlan/all/'

        code, xml = self.submit(None, 'GET', url)

        key = 'vlan'

        return get_list_map(self.response(code, xml, [key]), key)

    def listar_por_ambiente(self, id_ambiente):
        """List all VLANs from an environment.
        ** The itens returning from network is there to be compatible with other system **
        :param id_ambiente: Environment identifier.

        :return: Following dictionary:

        ::

          {'vlan': [{'id': < id_vlan >,
          'nome': < nome_vlan >,
          'num_vlan': < num_vlan >,
          'ambiente': < id_ambiente >,
          'descricao': < descricao >,
          'acl_file_name': < acl_file_name >,
          'acl_valida': < acl_valida >,
          'acl_file_name_v6': < acl_file_name_v6 >,
          'acl_valida_v6': < acl_valida_v6 >,
          'ativada': < ativada >,
          'id_tipo_rede': < id_tipo_rede >,
          'rede_oct1': < rede_oct1 >,
          'rede_oct2': < rede_oct2 >,
          'rede_oct3': < rede_oct3 >,
          'rede_oct4': < rede_oct4 >,
          'bloco': < bloco >,
          'mascara_oct1': < mascara_oct1 >,
          'mascara_oct2': < mascara_oct2 >,
          'mascara_oct3': < mascara_oct3 >,
          'mascara_oct4': < mascara_oct4 >,
          'broadcast': < broadcast >,} , ... other vlans ... ]}

        :raise InvalidParameterError: Environment id is none or invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_ambiente):
            raise InvalidParameterError(u'Environment id is none or invalid.')

        url = 'vlan/ambiente/' + str(id_ambiente) + '/'

        code, xml = self.submit(None, 'GET', url)

        key = 'vlan'
        return get_list_map(self.response(code, xml, [key]), key)

    def alocar(
            self,
            nome,
            id_tipo_rede,
            id_ambiente,
            descricao,
            id_ambiente_vip=None,
            vrf=None):
        """Inserts a new VLAN.

        :param nome: Name of Vlan. String with a maximum of 50 characters.
        :param id_tipo_rede: Identifier of the Network Type. Integer value and greater than zero.
        :param id_ambiente: Identifier of the Environment. Integer value and greater than zero.
        :param descricao: Description of Vlan. String with a maximum of 200 characters.
        :param id_ambiente_vip: Identifier of the Environment Vip. Integer value and greater than zero.

        :return: Following dictionary:

        ::

          {'vlan': {'id': < id_vlan >,
          'nome': < nome_vlan >,
          'num_vlan': < num_vlan >,
          'id_tipo_rede': < id_tipo_rede >,
          'id_ambiente': < id_ambiente >,
          'rede_oct1': < rede_oct1 >,
          'rede_oct2': < rede_oct2 >,
          'rede_oct3': < rede_oct3 >,
          'rede_oct4': < rede_oct4 >,
          'bloco': < bloco >,
          'mascara_oct1': < mascara_oct1 >,
          'mascara_oct2': < mascara_oct2 >,
          'mascara_oct3': < mascara_oct3 >,
          'mascara_oct4': < mascara_oct4 >,
          'broadcast': < broadcast >,
          'descricao': < descricao >,
          'acl_file_name': < acl_file_name >,
          'acl_valida': < acl_valida >,
          'ativada': < ativada >}}

        :raise VlanError: VLAN name already exists, VLAN name already exists, DC division of the environment invalid or does not exist VLAN number available.
        :raise VlanNaoExisteError: VLAN not found.
        :raise TipoRedeNaoExisteError: Network Type not registered.
        :raise AmbienteNaoExisteError: Environment not registered.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise InvalidParameterError: Name of Vlan and/or the identifier of the Environment is null or invalid.
        :raise IPNaoDisponivelError: There is no network address is available to create the VLAN.
        :raise ConfigEnvironmentInvalidError: Invalid Environment Configuration or not registered
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        vlan_map = dict()
        vlan_map['nome'] = nome
        vlan_map['id_tipo_rede'] = id_tipo_rede
        vlan_map['id_ambiente'] = id_ambiente
        vlan_map['descricao'] = descricao
        vlan_map['id_ambiente_vip'] = id_ambiente_vip
        vlan_map['vrf'] = vrf

        code, xml = self.submit({'vlan': vlan_map}, 'POST', 'vlan/')

        return self.response(code, xml)

    def insert_vlan(
            self,
            environment_id,
            name,
            number,
            description,
            acl_file,
            acl_file_v6,
            network_ipv4,
            network_ipv6,
            vrf=None):
        """Create new VLAN

        :param environment_id: ID for Environment.
        :param name: The name of VLAN.
        :param description: Some description to VLAN.
        :param number: Number of Vlan
        :param acl_file: Acl IPv4 File name to VLAN.
        :param acl_file_v6: Acl IPv6 File name to VLAN.
        :param network_ipv4: responsible for generating a network attribute ipv4 automatically.
        :param network_ipv6: responsible for generating a network attribute ipv6 automatically.

        :return: Following dictionary:

        ::

          {'vlan': {'id': < id_vlan >,
          'nome': < nome_vlan >,
          'num_vlan': < num_vlan >,
          'id_ambiente': < id_ambiente >,
          'descricao': < descricao >,
          'acl_file_name': < acl_file_name >,
          'acl_valida': < acl_valida >,
          'ativada': < ativada >
          'acl_file_name_v6': < acl_file_name_v6 >,
          'acl_valida_v6': < acl_valida_v6 >, } }

        :raise VlanError: VLAN name already exists, VLAN name already exists, DC division of the environment invalid or does not exist VLAN number available.
        :raise VlanNaoExisteError: VLAN not found.
        :raise AmbienteNaoExisteError: Environment not registered.
        :raise InvalidParameterError: Name of Vlan and/or the identifier of the Environment is null or invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(environment_id):
            raise InvalidParameterError(u'Environment id is none or invalid.')

        if not is_valid_int_param(number):
            raise InvalidParameterError(u'Vlan number is none or invalid')

        vlan_map = dict()
        vlan_map['environment_id'] = environment_id
        vlan_map['name'] = name
        vlan_map['description'] = description
        vlan_map['acl_file'] = acl_file
        vlan_map['acl_file_v6'] = acl_file_v6
        vlan_map['number'] = number
        vlan_map['network_ipv4'] = network_ipv4
        vlan_map['network_ipv6'] = network_ipv6
        vlan_map['vrf'] = vrf

        code, xml = self.submit({'vlan': vlan_map}, 'POST', 'vlan/insert/')

        return self.response(code, xml)

    def edit_vlan(
            self,
            environment_id,
            name,
            number,
            description,
            acl_file,
            acl_file_v6,
            id_vlan):
        """Edit a VLAN

        :param id_vlan: ID for Vlan
        :param environment_id: ID for Environment.
        :param name: The name of VLAN.
        :param description: Some description to VLAN.
        :param number: Number of Vlan
        :param acl_file: Acl IPv4 File name to VLAN.
        :param acl_file_v6: Acl IPv6 File name to VLAN.

        :return: None

        :raise VlanError: VLAN name already exists, DC division of the environment invalid or there is no VLAN number available.
        :raise VlanNaoExisteError: VLAN not found.
        :raise AmbienteNaoExisteError: Environment not registered.
        :raise InvalidParameterError: Name of Vlan and/or the identifier of the Environment is null or invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_vlan):
            raise InvalidParameterError(
                u'Vlan id is invalid or was not informed.')

        if not is_valid_int_param(environment_id):
            raise InvalidParameterError(u'Environment id is none or invalid.')

        if not is_valid_int_param(number):
            raise InvalidParameterError(u'Vlan number is none or invalid')

        vlan_map = dict()
        vlan_map['vlan_id'] = id_vlan
        vlan_map['environment_id'] = environment_id
        vlan_map['name'] = name
        vlan_map['description'] = description
        vlan_map['acl_file'] = acl_file
        vlan_map['acl_file_v6'] = acl_file_v6
        vlan_map['number'] = number

        code, xml = self.submit({'vlan': vlan_map}, 'POST', 'vlan/edit/')

        return self.response(code, xml)

    def create_vlan(self, id_vlan):
        """ Set column 'ativada = 1'.

        :param id_vlan: VLAN identifier.

        :return: None
        """

        vlan_map = dict()

        vlan_map['vlan_id'] = id_vlan

        code, xml = self.submit({'vlan': vlan_map}, 'PUT', 'vlan/create/')

        return self.response(code, xml)

    def allocate_without_network(self, environment_id, name, description, vrf=None):
        """Create new VLAN without add NetworkIPv4.

        :param environment_id: ID for Environment.
        :param name: The name of VLAN.
        :param description: Some description to VLAN.

        :return: Following dictionary:

        ::

          {'vlan': {'id': < id_vlan >,
          'nome': < nome_vlan >,
          'num_vlan': < num_vlan >,
          'id_ambiente': < id_ambiente >,
          'descricao': < descricao >,
          'acl_file_name': < acl_file_name >,
          'acl_valida': < acl_valida >,
          'acl_file_name_v6': < acl_file_name_v6 >,
          'acl_valida_v6': < acl_valida_v6 >,
          'ativada': < ativada > } }

        :raise VlanError: Duplicate name of VLAN, division DC of Environment not found/invalid or VLAN number not available.
        :raise AmbienteNaoExisteError: Environment not found.
        :raise InvalidParameterError: Some parameter was invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        vlan_map = dict()
        vlan_map['environment_id'] = environment_id
        vlan_map['name'] = name
        vlan_map['description'] = description
        vlan_map['vrf'] = vrf

        code, xml = self.submit({'vlan': vlan_map}, 'POST', 'vlan/no-network/')

        return self.response(code, xml)

    def adicionar_permissao(self, id_vlan, nome_equipamento, nome_interface):
        """Add communication permission for VLAN to trunk.

        Run script 'configurador'.

        :param id_vlan: VLAN identifier.
        :param nome_equipamento: Equipment name.
        :param nome_interface: Interface name.

        :return: Following dictionary:

        ::

          {‘sucesso’: {‘codigo’: < codigo >,
          ‘descricao’: {'stdout':< stdout >, 'stderr':< stderr >}}}

        :raise VlanNaoExisteError: VLAN does not exist.
        :raise InvalidParameterError: Vlan id is invalid or none.
        :raise InvalidParameterError: Equipment name and/or interface name is invalid or none.
        :raise EquipamentoNaoExisteError: Equipment does not exist.
        :raise LigacaoFrontInterfaceNaoExisteError: There is no interface on front link of informed interface.
        :raise InterfaceNaoExisteError: Interface does not exist or is not associated to equipment.
        :raise LigacaoFrontNaoTerminaSwitchError: Interface does not have switch connected.
        :raise InterfaceSwitchProtegidaError: Switch interface is protected.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise ScriptError: Failed to run the script.
        """
        if not is_valid_int_param(id_vlan):
            raise InvalidParameterError(
                u'Vlan id is invalid or was not informed.')

        url = 'vlan/' + str(id_vlan) + '/add/'

        vlan_map = dict()
        vlan_map['nome'] = nome_equipamento
        vlan_map['nome_interface'] = nome_interface

        code, xml = self.submit({'equipamento': vlan_map}, 'PUT', url)

        return self.response(code, xml)

    def remover_permissao(self, id_vlan, nome_equipamento, nome_interface):
        """Remove communication permission for VLAN to trunk.

        Run script 'configurador'.

        :param id_vlan: VLAN identifier.
        :param nome_equipamento: Equipment name.
        :param nome_interface: Interface name.

        :return: Following dictionary:

        ::

          {‘sucesso’: {‘codigo’: < codigo >,
          ‘descricao’: {'stdout':< stdout >, 'stderr':< stderr >}}}

        :raise VlanNaoExisteError: VLAN does not exist.
        :raise InvalidParameterError: VLAN id is none or invalid.
        :raise InvalidParameterError: Equipment name and/or interface name is invalid or none.
        :raise EquipamentoNaoExisteError: Equipment does not exist.
        :raise LigacaoFrontInterfaceNaoExisteError: There is no interface on front link of informed interface.
        :raise InterfaceNaoExisteError: Interface does not exist or is not associated to equipment.
        :raise LigacaoFrontNaoTerminaSwitchError: Interface does not have switch connected.
        :raise InterfaceSwitchProtegidaError: Switch interface is protected.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise ScriptError: Failed to run the script.
        """
        if not is_valid_int_param(id_vlan):
            raise InvalidParameterError(
                u'Vlan id is invalid or was not informed.')

        url = 'vlan/' + str(id_vlan) + '/del/'

        vlan_map = dict()
        vlan_map['nome'] = nome_equipamento
        vlan_map['nome_interface'] = nome_interface

        code, xml = self.submit({'equipamento': vlan_map}, 'PUT', url)

        return self.response(code, xml)

    def verificar_permissao(self, id_vlan, nome_equipamento, nome_interface):
        """Check if there is communication permission for VLAN to trunk.

        Run script 'configurador'.

        The "stdout" key value of response dictionary is 1(one) if VLAN has permission,
        or 0(zero), otherwise.

        :param id_vlan: VLAN identifier.
        :param nome_equipamento: Equipment name.
        :param nome_interface: Interface name.

        :return: Following dictionary:

        ::

          {‘sucesso’: {‘codigo’: < codigo >,
          ‘descricao’: {'stdout':< stdout >, 'stderr':< stderr >}}}

        :raise VlanNaoExisteError: VLAN does not exist.
        :raise InvalidParameterError: VLAN id is none or invalid.
        :raise InvalidParameterError: Equipment name and/or interface name is invalid or none.
        :raise EquipamentoNaoExisteError: Equipment does not exist.
        :raise LigacaoFrontInterfaceNaoExisteError: There is no interface on front link of informed interface.
        :raise InterfaceNaoExisteError: Interface does not exist or is not associated to equipment.
        :raise LigacaoFrontNaoTerminaSwitchError: Interface does not have switch connected.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise ScriptError: Failed to run the script.
        """
        if not is_valid_int_param(id_vlan):
            raise InvalidParameterError(
                u'Vlan id is invalid or was not informed.')

        url = 'vlan/' + str(id_vlan) + '/check/'

        vlan_map = dict()
        vlan_map['nome'] = nome_equipamento
        vlan_map['nome_interface'] = nome_interface

        code, xml = self.submit({'equipamento': vlan_map}, 'PUT', url)

        return self.response(code, xml)

    def buscar(self, id_vlan):
        """Get VLAN by its identifier.

        :param id_vlan: VLAN identifier.

        :return: Following dictionary:

        ::

          {'vlan': {'id': < id_vlan >,
          'nome': < nome_vlan >,
          'num_vlan': < num_vlan >,
          'id_ambiente': < id_ambiente >,
          'id_tipo_rede': < id_tipo_rede >,
          'rede_oct1': < rede_oct1 >,
          'rede_oct2': < rede_oct2 >,
          'rede_oct3': < rede_oct3 >,
          'rede_oct4': < rede_oct4 >,
          'bloco': < bloco >,
          'mascara_oct1': < mascara_oct1 >,
          'mascara_oct2': < mascara_oct2 >,
          'mascara_oct3': < mascara_oct3 >,
          'mascara_oct4': < mascara_oct4 >,
          'broadcast': < broadcast >,
          'descricao': < descricao >,
          'acl_file_name': < acl_file_name >,
          'acl_valida': < acl_valida >,
          'ativada': < ativada >}
          OR {'id': < id_vlan >,
          'nome': < nome_vlan >,
          'num_vlan': < num_vlan >,
          'id_tipo_rede': < id_tipo_rede >,
          'id_ambiente': < id_ambiente >,
          'bloco1': < bloco1 >,
          'bloco2': < bloco2 >,
          'bloco3': < bloco3 >,
          'bloco4': < bloco4 >,
          'bloco5': < bloco5 >,
          'bloco6': < bloco6 >,
          'bloco7': < bloco7 >,
          'bloco8': < bloco8 >,
          'bloco': < bloco >,
          'mask_bloco1': < mask_bloco1 >,
          'mask_bloco2': < mask_bloco2 >,
          'mask_bloco3': < mask_bloco3 >,
          'mask_bloco4': < mask_bloco4 >,
          'mask_bloco5': < mask_bloco5 >,
          'mask_bloco6': < mask_bloco6 >,
          'mask_bloco7': < mask_bloco7 >,
          'mask_bloco8': < mask_bloco8 >,
          'broadcast': < broadcast >,
          'descricao': < descricao >,
          'acl_file_name': < acl_file_name >,
          'acl_valida': < acl_valida >,
          'acl_file_name_v6': < acl_file_name_v6 >,
          'acl_valida_v6': < acl_valida_v6 >,
          'ativada': < ativada >}}

        :raise VlanNaoExisteError: VLAN does not exist.
        :raise InvalidParameterError: VLAN id is none or invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_vlan):
            raise InvalidParameterError(
                u'Vlan id is invalid or was not informed.')

        url = 'vlan/' + str(id_vlan) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def get(self, id_vlan):
        """Get a VLAN by your primary key.
        Network IPv4/IPv6 related will also be fetched.

        :param id_vlan: ID for VLAN.

        :return: Following dictionary:

        ::

          {'vlan': {'id': < id_vlan >,
          'nome': < nome_vlan >,
          'num_vlan': < num_vlan >,
          'id_ambiente': < id_ambiente >,
          'descricao': < descricao >,
          'acl_file_name': < acl_file_name >,
          'acl_valida': < acl_valida >,
          'acl_file_name_v6': < acl_file_name_v6 >,
          'acl_valida_v6': < acl_valida_v6 >,
          'ativada': < ativada >,
          'redeipv4': [ { all networkipv4 related } ],
          'redeipv6': [ { all networkipv6 related } ] } }

        :raise InvalidParameterError: Invalid ID for VLAN.
        :raise VlanNaoExisteError: VLAN not found.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_vlan):
            raise InvalidParameterError(
                u'Parameter id_vlan is invalid. Value: ' +
                id_vlan)

        url = 'vlan/' + str(id_vlan) + '/network/'

        code, xml = self.submit(None, 'GET', url)

        return get_list_map(
            self.response(
                code, xml, [
                    'redeipv4', 'redeipv6']), 'vlan')

    def listar_permissao(self, nome_equipamento, nome_interface):
        """List all VLANS having communication permission to trunk from a port in switch.

        Run script 'configurador'.

        ::

          The value of 'stdout' key of return dictionary can have a list of numbers or
          number intervals of VLAN´s, comma separated. Examples of possible returns of 'stdout' below:
              - 100,103,111,...
              - 100-110,...
              - 100-110,112,115,...
              - 100,103,105-111,113,115-118,...

        :param nome_equipamento: Equipment name.
        :param nome_interface: Interface name.

        :return: Following dictionary:

        ::

          {‘sucesso’: {‘codigo’: < codigo >,
          ‘descricao’: {'stdout':< stdout >, 'stderr':< stderr >}}}

        :raise InvalidParameterError: Equipment name and/or interface name is invalid or none.
        :raise EquipamentoNaoExisteError: Equipment does not exist.
        :raise LigacaoFrontInterfaceNaoExisteError: There is no interface on front link of informed interface.
        :raise InterfaceNaoExisteError: Interface does not exist or is not associated to equipment.
        :raise LigacaoFrontNaoTerminaSwitchError: Interface does not have switch connected.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise ScriptError: Failed to run the script.
        """
        vlan_map = dict()
        vlan_map['nome'] = nome_equipamento
        vlan_map['nome_interface'] = nome_interface

        code, xml = self.submit({'equipamento': vlan_map}, 'PUT', 'vlan/list/')

        return self.response(code, xml)

    def criar(self, id_vlan):
        """Create a VLAN with script 'navlan'.

        :param id_vlan: VLAN identifier.

        :return: Following dictionary:

        ::

          {‘sucesso’: {‘codigo’: < codigo >,
          ‘descricao’: {'stdout':< stdout >, 'stderr':< stderr >}}}

        :raise VlanNaoExisteError: VLAN does not exist.
        :raise EquipamentoNaoExisteError: Equipment in list does not exist.
        :raise VlanError: VLAN is active.
        :raise InvalidParameterError: VLAN identifier is none or invalid.
        :raise InvalidParameterError: Equipment list is none or empty.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise ScriptError: Failed to run the script.
        """

        if not is_valid_int_param(id_vlan):
            raise InvalidParameterError(
                u'Vlan id is invalid or was not informed.')

        url = 'vlan/' + str(id_vlan) + '/criar/'

        code, xml = self.submit({'vlan': None}, 'PUT', url)

        return self.response(code, xml)

    def create_ipv4(self, id_network_ipv4):
        """Create VLAN in layer 2 using script 'navlan'.

        :param id_network_ipv4: NetworkIPv4 ID.

        :return: Following dictionary:

        ::

          {‘sucesso’: {‘codigo’: < codigo >,
          ‘descricao’: {'stdout':< stdout >, 'stderr':< stderr >}}}

        :raise NetworkIPv4NaoExisteError: NetworkIPv4 not found.
        :raise EquipamentoNaoExisteError: Equipament in list not found.
        :raise VlanError: VLAN is active.
        :raise InvalidParameterError: VLAN identifier is none or invalid.
        :raise InvalidParameterError: Equipment list is none or empty.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise ScriptError: Failed to run the script.
        """

        url = 'vlan/v4/create/'

        vlan_map = dict()
        vlan_map['id_network_ip'] = id_network_ipv4

        code, xml = self.submit({'vlan': vlan_map}, 'POST', url)

        return self.response(code, xml)

    def create_ipv6(self, id_network_ipv6):
        """Create VLAN in layer 2 using script 'navlan'.

        :param id_network_ipv6: NetworkIPv6 ID.

        :return: Following dictionary:

        ::

          {‘sucesso’: {‘codigo’: < codigo >,
          ‘descricao’: {'stdout':< stdout >, 'stderr':< stderr >}}}

        :raise NetworkIPv6NaoExisteError: NetworkIPv6 not found.
        :raise EquipamentoNaoExisteError: Equipament in list not found.
        :raise VlanError: VLAN is active.
        :raise InvalidParameterError: VLAN identifier is none or invalid.
        :raise InvalidParameterError: Equipment list is none or empty.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise ScriptError: Failed to run the script.
        """

        url = 'vlan/v6/create/'

        vlan_map = dict()
        vlan_map['id_network_ip'] = id_network_ipv6

        code, xml = self.submit({'vlan': vlan_map}, 'POST', url)

        return self.response(code, xml)

    def apply_acl(self, equipments, vlan, environment, network):
        '''Apply the file acl in equipments

        :param equipments: list of equipments
        :param vlan: Vvlan
        :param environment: Environment
        :param network: v4 or v6

        :raise Exception: Failed to apply acl

        :return: True case Apply and sysout of script
        '''

        vlan_map = dict()
        vlan_map['equipments'] = equipments
        vlan_map['vlan'] = vlan
        vlan_map['environment'] = environment
        vlan_map['network'] = network

        url = 'vlan/apply/acl/'

        code, xml = self.submit({'vlan': vlan_map}, 'POST', url)

        return self.response(code, xml)

    def confirm_vlan(self, number_net, id_environment_vlan, ip_version=None):
        """Checking if the vlan insert need to be confirmed

        :param number_net: Filter by vlan number column
        :param id_environment_vlan: Filter by environment ID related
        :param ip_version: Ip version for checking

        :return: True is need confirmation, False if no need

        :raise AmbienteNaoExisteError: Ambiente não cadastrado.
        :raise InvalidParameterError: Invalid ID for VLAN.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        url = 'vlan/confirm/' + \
            str(number_net) + '/' + id_environment_vlan + '/' + str(ip_version)

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def check_number_available(self, id_environment, num_vlan, id_vlan):
        """Checking if environment has a number vlan available

        :param id_environment: Identifier of environment
        :param num_vlan: Vlan number
        :param id_vlan: Vlan indentifier (False if inserting a vlan)

        :return: True is has number available, False if hasn't

        :raise AmbienteNaoExisteError: Ambiente não cadastrado.
        :raise InvalidParameterError: Invalid ID for VLAN.
        :raise VlanNaoExisteError: VLAN not found.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        url = 'vlan/check_number_available/' + \
            str(id_environment) + '/' + str(num_vlan) + '/' + str(id_vlan)

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def validar(self, id_vlan):
        """Validates ACL - IPv4 of VLAN from its identifier.

        Assigns 1 to 'acl_valida'.

        :param id_vlan: Identifier of the Vlan. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: Vlan identifier is null and invalid.
        :raise VlanNaoExisteError: Vlan not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_vlan):
            raise InvalidParameterError(
                u'The identifier of Vlan is invalid or was not informed.')

        url = 'vlan/' + str(id_vlan) + '/validate/' + IP_VERSION.IPv4[0] + "/"

        code, xml = self.submit(None, 'PUT', url)

        return self.response(code, xml)

    def validate_ipv6(self, id_vlan):
        """Validates ACL - IPv6 of VLAN from its identifier.

        Assigns 1 to 'acl_valida_v6'.

        :param id_vlan: Identifier of the Vlan. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: Vlan identifier is null and invalid.
        :raise VlanNaoExisteError: Vlan not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_vlan):
            raise InvalidParameterError(
                u'The identifier of Vlan is invalid or was not informed.')

        url = 'vlan/' + str(id_vlan) + '/validate/' + IP_VERSION.IPv6[0] + "/"

        code, xml = self.submit(None, 'PUT', url)

        return self.response(code, xml)

    def remove(self, id_vlan):
        """Remove a VLAN by your primary key.
        Execute script to remove VLAN

        :param id_vlan: ID for VLAN.

        :return: Following dictionary:

        ::

          {‘sucesso’: {‘codigo’: < codigo >,
          ‘descricao’: {'stdout':< stdout >, 'stderr':< stderr >}}}

        :raise InvalidParameterError: Identifier of the VLAN is invalid.
        :raise VlanNaoExisteError: VLAN not found.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_vlan):
            raise InvalidParameterError(
                u'Parameter id_vlan is invalid. Value: ' +
                id_vlan)

        url = 'vlan/' + str(id_vlan) + '/remove/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def deallocate(self, id_vlan):
        """Deallocate all relationships between Vlan.

        :param id_vlan: Identifier of the VLAN. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: VLAN identifier is null and invalid.
        :raise VlanError: VLAN is active.
        :raise VlanNaoExisteError: VLAN not found.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_vlan):
            raise InvalidParameterError(
                u'The identifier of Vlan is invalid or was not informed.')

        url = 'vlan/' + str(id_vlan) + '/deallocate/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def allocate_IPv6(
            self,
            name,
            id_network_type,
            id_environment,
            description,
            id_environment_vip=None):
        """Inserts a new VLAN.

        :param name: Name of Vlan. String with a maximum of 50 characters.
        :param id_network_type: Identifier of the Netwok Type. Integer value and greater than zero.
        :param id_environment: Identifier of the Environment. Integer value and greater than zero.
        :param description: Description of Vlan. String with a maximum of 200 characters.
        :param id_environment_vip: Identifier of the Environment Vip. Integer value and greater than zero.

        :return: Following dictionary:

        ::

          {'vlan': {'id': < id_vlan >,
          'nome': < nome_vlan >,
          'num_vlan': < num_vlan >,
          'id_tipo_rede': < id_tipo_rede >,
          'id_ambiente': < id_ambiente >,
          'bloco1': < bloco1 >,
          'bloco2': < bloco2 >,
          'bloco3': < bloco3 >,
          'bloco4': < bloco4 >,
          'bloco5': < bloco5 >,
          'bloco6': < bloco6 >,
          'bloco7': < bloco7 >,
          'bloco8': < bloco8 >,
          'bloco': < bloco >,
          'mask_bloco1': < mask_bloco1 >,
          'mask_bloco2': < mask_bloco2 >,
          'mask_bloco3': < mask_bloco3 >,
          'mask_bloco4': < mask_bloco4 >,
          'mask_bloco5': < mask_bloco5 >,
          'mask_bloco6': < mask_bloco6 >,
          'mask_bloco7': < mask_bloco7 >,
          'mask_bloco8': < mask_bloco8 >,
          'descricao': < descricao >,
          'acl_file_name': < acl_file_name >,
          'acl_valida': < acl_valida >,
          'acl_file_name_v6': < acl_file_name_v6 >,
          'acl_valida_v6': < acl_valida_v6 >,
          'ativada': < ativada >}}

        :raise VlanError: VLAN name already exists, VLAN name already exists, DC division of the environment invalid or does not exist VLAN number available.
        :raise VlanNaoExisteError: VLAN not found.
        :raise TipoRedeNaoExisteError: Network Type not registered.
        :raise AmbienteNaoExisteError: Environment not registered.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise InvalidParameterError: Name of Vlan and/or the identifier of the Environment is null or invalid.
        :raise IPNaoDisponivelError: There is no network address is available to create the VLAN.
        :raise ConfigEnvironmentInvalidError: Invalid Environment Configuration or not registered
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        vlan_map = dict()
        vlan_map['name'] = name
        vlan_map['id_network_type'] = id_network_type
        vlan_map['id_environment'] = id_environment
        vlan_map['description'] = description
        vlan_map['id_environment_vip'] = id_environment_vip

        code, xml = self.submit({'vlan': vlan_map}, 'POST', 'vlan/ipv6/')

        return self.response(code, xml)

    def create_acl(self, id_vlan, network_type):
        '''Create the file acl

        :param id_vlan: Vlan Id
        :param network_type: v4 or v6

        :raise InvalidValueError: Attrs invalids.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise AclNotFoundError: ACL not created.
        :raise VlanNotFoundError: Vlan not registered.

        :return: Following dictionary:

        ::

          {'vlan': {
          'acl_file_name': < acl_file_name >,
          'ativada': < ativada >,
          'acl_valida': < acl_valida >,
          'nome': '< nome >',
          'acl_file_name_v6': < acl_file_name_v6 >,
          'acl_valida_v6': < acl_valida_v6 >,
          'ambiente': < ambiente >,
          'num_vlan': < num_vlan >,
          'id': < id >,
          'descricao': < descricao >
          }}
        '''

        vlan_map = dict()
        vlan_map['id_vlan'] = id_vlan
        vlan_map['network_type'] = network_type

        url = 'vlan/create/acl/'

        code, xml = self.submit({'vlan': vlan_map}, 'POST', url)

        return self.response(code, xml)

    def create_script_acl(self, id_vlan, network_type):
        '''Generate the script acl

        :param id_vlan: Vlan Id
        :param network_type: v4 or v6

        :raise InvalidValueError: Attrs invalids.
        :raise XMLError: Networkapi failed to generate the XML response.
        :raise VlanACLDuplicatedError: ACL name duplicate.
        :raise VlanNotFoundError: Vlan not registered.

        :return: Following dictionary:

        ::

          {'vlan': {
          'id': < id >,
          'nome': '< nome >',
          'num_vlan': < num_vlan >,
          'descricao': < descricao >
          'acl_file_name': < acl_file_name >,
          'ativada': < ativada >,
          'acl_valida': < acl_valida >,
          'acl_file_name_v6': < acl_file_name_v6 >,
          'redeipv6': < redeipv6 >,
          'acl_valida_v6': < acl_valida_v6 >,
          'redeipv4': < redeipv4 >,
          'ambiente': < ambiente >,
          }}
        '''

        vlan_map = dict()
        vlan_map['id_vlan'] = id_vlan
        vlan_map['network_type'] = network_type

        url = 'vlan/create/script/acl/'

        code, xml = self.submit({'vlan': vlan_map}, 'POST', url)

        return self.response(code, xml)
