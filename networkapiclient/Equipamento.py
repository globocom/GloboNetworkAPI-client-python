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

import urllib.request, urllib.parse, urllib.error
from networkapiclient.GenericClient import GenericClient
from networkapiclient.exception import InvalidParameterError
from networkapiclient.utils import is_valid_int_param, get_list_map
from networkapiclient.Pagination import Pagination


class Equipamento(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            Equipamento,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def get_real_related(self, id_equip):
        """
        Find reals related with equipment

        :param id_equip: Identifier of equipment

        :return: Following dictionary:

        ::

            {'vips': [{'port_real': < port_real >,
            'server_pool_member_id': < server_pool_member_id >,
            'ip': < ip >,
            'port_vip': < port_vip >,
            'host_name': < host_name >,
            'id_vip': < id_vip >, ...],
            'equip_name': < equip_name > }}

        :raise EquipamentoNaoExisteError: Equipment not registered.
        :raise InvalidParameterError: Some parameter was invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        url = 'equipamento/get_real_related/' + str(id_equip) + '/'

        code, xml = self.submit(None, 'GET', url)

        data = self.response(code, xml)
        return data

    def find_equips(
            self,
            name,
            iexact,
            environment,
            equip_type,
            group,
            ip,
            pagination):
        """
        Find vlans by all search parameters

        :param name: Filter by vlan name column
        :param iexact: Filter by name will be exact?
        :param environment: Filter by environment ID related
        :param equip_type: Filter by equipment_type ID related
        :param group: Filter by equipment group ID related
        :param ip: Filter by each octs in ips related
        :param pagination: Class with all data needed to paginate

        :return: Following dictionary:

        ::

            {'equipamento': {'id': < id_vlan >,
            'nome': < nome_vlan >,
            'num_vlan': < num_vlan >,
            'id_ambiente': < id_ambiente >,
            'descricao': < descricao >,
            'acl_file_name': < acl_file_name >,
            'acl_valida': < acl_valida >,
            'ativada': < ativada >,
            'ambiente_name': < divisao_dc-ambiente_logico-grupo_l3 >
            'redeipv4': [ { all networkipv4 related  } ],
            'redeipv6': [ { all networkipv6 related } ] },
            'total': {< total_registros >} }

        :raise InvalidParameterError: Some parameter was invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not isinstance(pagination, Pagination):
            raise InvalidParameterError(
                "Invalid parameter: pagination must be a class of type 'Pagination'.")

        equip_map = dict()

        equip_map["start_record"] = pagination.start_record
        equip_map["end_record"] = pagination.end_record
        equip_map["asorting_cols"] = pagination.asorting_cols
        equip_map["searchable_columns"] = pagination.searchable_columns
        equip_map["custom_search"] = pagination.custom_search

        equip_map["nome"] = name
        equip_map["exato"] = iexact
        equip_map["ambiente"] = environment
        equip_map["tipo_equipamento"] = equip_type
        equip_map["grupo"] = group
        equip_map["ip"] = ip

        url = "equipamento/find/"

        code, xml = self.submit({"equipamento": equip_map}, "POST", url)

        key = "equipamento"
        return get_list_map(
            self.response(
                code, xml, [
                    key, "ips", "grupos"]), key)

    def inserir(self, name, id_equipment_type, id_model, id_group, maintenance=False):
        """Inserts a new Equipment and returns its identifier

        Além de inserir o equipamento, a networkAPI também associa o equipamento
        ao grupo informado.

        :param name: Equipment name. String with a minimum 3 and maximum of 30 characters
        :param id_equipment_type: Identifier of the Equipment Type. Integer value and greater than zero.
        :param id_model: Identifier of the Model. Integer value and greater than zero.
        :param id_group: Identifier of the Group. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            {'equipamento': {'id': < id_equipamento >},
            'equipamento_grupo': {'id': < id_grupo_equipamento >}}

        :raise InvalidParameterError: The identifier of Equipment type, model, group or name  is null and invalid.
        :raise TipoEquipamentoNaoExisteError: Equipment Type not registered.
        :raise ModeloEquipamentoNaoExisteError: Model not registered.
        :raise GrupoEquipamentoNaoExisteError: Group not registered.

        :raise EquipamentoError: Equipamento com o nome duplicado ou
            Equipamento do grupo “Equipamentos Orquestração” somente poderá ser
            criado com tipo igual a “Servidor Virtual".

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response
        """
        equip_map = dict()
        equip_map['id_tipo_equipamento'] = id_equipment_type
        equip_map['id_modelo'] = id_model
        equip_map['nome'] = name
        equip_map['id_grupo'] = id_group
        equip_map['maintenance'] = maintenance
        
        code, xml = self.submit(
            {'equipamento': equip_map}, 'POST', 'equipamento/')

        return self.response(code, xml)

    def edit(self, id_equip, nome, id_tipo_equipamento, id_modelo, maintenance=None):
        """Change Equipment from by the identifier.

        :param id_equip: Identifier of the Equipment. Integer value and greater than zero.
        :param nome: Equipment name. String with a minimum 3 and maximum of 30 characters
        :param id_tipo_equipamento: Identifier of the Equipment Type. Integer value and greater than zero.
        :param id_modelo: Identifier of the Model. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: The identifier of Equipment, model, equipment type or name  is null and invalid.
        :raise EquipamentoNaoExisteError: Equipment not registered.
        :raise TipoEquipamentoNaoExisteError: Equipment Type not registered.
        :raise ModeloEquipamentoNaoExisteError: Model not registered.
        :raise GrupoEquipamentoNaoExisteError: Group not registered.

        :raise EquipamentoError: Equipamento com o nome duplicado ou
            Equipamento do grupo “Equipamentos Orquestração” somente poderá ser
            criado com tipo igual a “Servidor Virtual".

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response

        """

        equip_map = dict()
        equip_map['id_equip'] = id_equip
        equip_map['id_tipo_equipamento'] = id_tipo_equipamento
        equip_map['id_modelo'] = id_modelo
        equip_map['nome'] = nome
        if maintenance is not None:
            equip_map['maintenance'] = maintenance

        url = 'equipamento/edit/' + str(id_equip) + '/'

        code, xml = self.submit({'equipamento': equip_map}, 'POST', url)

        return self.response(code, xml)

    def criar_ip(self, id_vlan, id_equipamento, descricao):
        """Aloca um IP em uma VLAN para um equipamento.

        Insere um novo IP para a VLAN e o associa ao equipamento.

        :param id_vlan: Identificador da vlan.
        :param id_equipamento: Identificador do equipamento.
        :param descricao: Descriçao do IP.

        :return: Dicionário com a seguinte estrutura:

        ::

            {'ip': {'id': < id_ip >,
            'id_network_ipv4': < id_network_ipv4 >,
            'oct1’: < oct1 >,
            'oct2': < oct2 >,
            'oct3': < oct3 >,
            'oct4': < oct4 >,
            'descricao': < descricao >}}

        :raise InvalidParameterError: O identificador da VLAN e/ou do equipamento são nulos ou inválidos.
        :raise EquipamentoNaoExisteError: Equipamento não cadastrado.
        :raise VlanNaoExisteError: VLAN não cadastrada.
        :raise IPNaoDisponivelError: Não existe IP disponível para a VLAN informada.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """
        ip_map = dict()
        ip_map['id_vlan'] = id_vlan
        ip_map['descricao'] = descricao
        ip_map['id_equipamento'] = id_equipamento

        code, xml = self.submit({'ip': ip_map}, 'POST', 'ip/')

        return self.response(code, xml)

    def add_ipv4(self, id_network_ipv4, id_equipamento, descricao):
        """Allocate an IP on a network to an equipment.
        Insert new IP for network and associate to the equipment

        :param id_network_ipv4: ID for NetworkIPv4.
        :param id_equipamento: ID for Equipment.
        :param descricao: Description for IP.

        :return: Following dictionary:

        ::

            {'ip': {'id': < id_ip >,
            'id_network_ipv4': < id_network_ipv4 >,
            'oct1’: < oct1 >,
            'oct2': < oct2 >,
            'oct3': < oct3 >,
            'oct4': < oct4 >,
            'descricao': < descricao >}}

        :raise InvalidParameterError: Invalid ID for NetworkIPv4 or Equipment.
        :raise InvalidParameterError: The value of description is invalid.
        :raise EquipamentoNaoExisteError: Equipment not found.
        :raise RedeIPv4NaoExisteError: NetworkIPv4 not found.
        :raise IPNaoDisponivelError: There is no network address is available to create the VLAN.
        :raise ConfigEnvironmentInvalidError: Invalid Environment Configuration or not registered
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        ip_map = dict()
        ip_map['id_network_ipv4'] = id_network_ipv4
        ip_map['description'] = descricao
        ip_map['id_equipment'] = id_equipamento

        code, xml = self.submit({'ip': ip_map}, 'POST', 'ipv4/')

        return self.response(code, xml)

    def add_ipv6(self, id_network_ipv6, id_equip, description):
        """Allocate an IP on a network to an equipment.
        Insert new IP for network and associate to the equipment

        :param id_network_ipv6: ID for NetworkIPv6.
        :param id_equip: ID for Equipment.
        :param description: Description for IP.

        :return: Following dictionary:

        ::

            {'ip': {'id': < id_ip >,
            'id_network_ipv6': < id_network_ipv6 >,
            'bloco1': < bloco1 >,
            'bloco2': < bloco2 >,
            'bloco3': < bloco3 >,
            'bloco4': < bloco4 >,
            'bloco5': < bloco5 >,
            'bloco6': < bloco6 >,
            'bloco7': < bloco7 >,
            'bloco8': < bloco8 >,
            'descricao': < descricao >}}

        :raise InvalidParameterError: NetworkIPv6 identifier or Equipament identifier  is null and invalid,
        :raise InvalidParameterError: The value of description is invalid.
        :raise EquipamentoNaoExisteError: Equipment not found.
        :raise RedeIPv6NaoExisteError: NetworkIPv6 not found.
        :raise IPNaoDisponivelError: There is no network address is available to create the VLAN.
        :raise ConfigEnvironmentInvalidError: Invalid Environment Configuration or not registered
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        ip_map = dict()
        ip_map['id_network_ipv6'] = id_network_ipv6
        ip_map['description'] = description
        ip_map['id_equip'] = id_equip

        code, xml = self.submit({'ip': ip_map}, 'POST', 'ipv6/')

        return self.response(code, xml)

    def remover_ip(self, id_equipamento, id_ip):
        """Removes association of IP and Equipment.
        If IP has no other association with equipments, IP is also removed.

        :param id_equipamento: Equipment identifier
        :param id_ip: IP identifier.

        :return: None

        :raise VipIpError: Ip can't be removed because there is a created Vip Request.
        :raise IpEquipCantDissociateFromVip: Equipment is the last balancer for created Vip Request.
        :raise IpError: IP not associated with equipment.
        :raise InvalidParameterError: Equipment or IP identifier is none or invalid.
        :raise EquipamentoNaoExisteError: Equipment doesn't exist.
        :raise DataBaseError: Networkapi failed to access database.
        :raise XMLError: Networkapi failed to build response XML.
        """

        if not is_valid_int_param(id_equipamento):
            raise InvalidParameterError(
                'O identificador do equipamento é inválido ou não foi informado.')

        if not is_valid_int_param(id_ip):
            raise InvalidParameterError(
                'O identificador do ip é inválido ou não foi informado.')

        url = 'ip/' + str(id_ip) + '/equipamento/' + str(id_equipamento) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def associar_ip(self, id_equipamento, id_ip):
        """Associa um IP a um equipamento.

        :param id_equipamento: Identificador do equipamento.
        :param id_ip: Identificador do IP.

        :return: Dicionário com a seguinte estrutura:
            {'ip_equipamento': {'id': < id_ip_do_equipamento >}}

        :raise EquipamentoNaoExisteError: Equipamento não cadastrado.
        :raise IpNaoExisteError: IP não cadastrado.
        :raise IpError: IP já está associado ao equipamento.
        :raise InvalidParameterError: O identificador do equipamento e/ou do IP são nulos ou inválidos.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """

        if not is_valid_int_param(id_equipamento):
            raise InvalidParameterError(
                'O identificador do equipamento é inválido ou não foi informado.')

        if not is_valid_int_param(id_ip):
            raise InvalidParameterError(
                'O identificador do ip é inválido ou não foi informado.')

        url = 'ip/' + str(id_ip) + '/equipamento/' + str(id_equipamento) + '/'

        code, xml = self.submit(None, 'PUT', url)

        return self.response(code, xml)

    def associate_ipv6(self, id_equip, id_ipv6):
        """Associates an IPv6 to a equipament.

        :param id_equip: Identifier of the equipment. Integer value and greater than zero.
        :param id_ipv6: Identifier of the ip. Integer value and greater than zero.

        :return: Dictionary with the following structure:
            {'ip_equipamento': {'id': < id_ip_do_equipamento >}}

        :raise EquipamentoNaoExisteError: Equipment is not registered.
        :raise IpNaoExisteError: IP not registered.
        :raise IpError: IP is already associated with the equipment.
        :raise InvalidParameterError:  Identifier of the equipment and/or IP is null or invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_equip):
            raise InvalidParameterError(
                'The identifier of equipment is invalid or was not informed.')

        if not is_valid_int_param(id_ipv6):
            raise InvalidParameterError(
                'The identifier of ip is invalid or was not informed.')

        url = 'ipv6/' + str(id_ipv6) + '/equipment/' + str(id_equip) + '/'

        code, xml = self.submit(None, 'PUT', url)

        return self.response(code, xml)

    def remove_ipv6(self, id_equip, id_ipv6):
        """Remove an IPv6 to a equipament.

        :param id_equip: Identifier of the equipment. Integer value and greater than zero.
        :param id_ipv6: Identifier of the ip. Integer value and greater than zero.

        :return: None

        :raise EquipamentoNaoExisteError: Equipment is not registered.
        :raise IpNaoExisteError: IP not registered.
        :raise IpError: Dont  IP is already associated with the equipment.
        :raise InvalidParameterError:  Identifier of the equipment and/or IP is null or invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_equip):
            raise InvalidParameterError(
                'The identifier of equipment is invalid or was not informed.')

        if not is_valid_int_param(id_ipv6):
            raise InvalidParameterError(
                'The identifier of ip is invalid or was not informed.')

        url = 'ipv6/' + str(id_ipv6) + '/equipment/' + \
            str(id_equip) + '/remove/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def listar_por_tipo_ambiente(self, id_tipo_equipamento, id_ambiente):
        """Lista os equipamentos de um tipo e que estão associados a um ambiente.

        :param id_tipo_equipamento: Identificador do tipo do equipamento.
        :param id_ambiente: Identificador do ambiente.

        :return: Dicionário com a seguinte estrutura:

        ::

            {'equipamento': [{'id': < id_equipamento >,
            'nome': < nome_equipamento >,
            'id_tipo_equipamento': < id_tipo_equipamento >,
            'nome_tipo_equipamento': < nome_tipo_equipamento >,
            'id_modelo': < id_modelo >,
            'nome_modelo': < nome_modelo >,
            'id_marca': < id_marca >,
            'nome_marca': < nome_marca >
            }, ... demais equipamentos ...]}

        :raise InvalidParameterError: O identificador do tipo de equipamento e/ou do ambiente são nulos ou inválidos.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """

        if not is_valid_int_param(id_tipo_equipamento):
            raise InvalidParameterError(
                'O identificador do tipo do equipamento é inválido ou não foi informado.')

        if not is_valid_int_param(id_ambiente):
            raise InvalidParameterError(
                'O identificador do ambiente é inválido ou não foi informado.')

        url = 'equipamento/tipoequipamento/' + \
            str(id_tipo_equipamento) + '/ambiente/' + str(id_ambiente) + '/'

        code, xml = self.submit(None, 'GET', url)

        key = 'equipamento'
        return get_list_map(self.response(code, xml, [key]), key)

    def listar_por_nome(self, nome):
        """Obtém um equipamento a partir do seu nome.

        :param nome: Nome do equipamento.

        :return: Dicionário com a seguinte estrutura:

        ::

            {'equipamento': {'id': < id_equipamento >,
            'nome': < nome_equipamento >,
            'id_tipo_equipamento': < id_tipo_equipamento >,
            'nome_tipo_equipamento': < nome_tipo_equipamento >,
            'id_modelo': < id_modelo >,
            'nome_modelo': < nome_modelo >,
            'id_marca': < id_marca >,
            'nome_marca': < nome_marca >}}

        :raise EquipamentoNaoExisteError: Equipamento com o
            nome informado não cadastrado.
        :raise InvalidParameterError: O nome do equipamento é nulo ou vazio.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """

        if nome == '' or nome is None:
            raise InvalidParameterError(
                'O nome do equipamento não foi informado.')

        url = 'equipamento/nome/' + urllib.parse.quote(nome) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def listar_por_id(self, id):
        """Obtém um equipamento a partir do seu identificador.

        :param id: ID do equipamento.

        :return: Dicionário com a seguinte estrutura:

        ::

            {'equipamento': {'id': < id_equipamento >,
            'nome': < nome_equipamento >,
            'id_tipo_equipamento': < id_tipo_equipamento >,
            'nome_tipo_equipamento': < nome_tipo_equipamento >,
            'id_modelo': < id_modelo >,
            'nome_modelo': < nome_modelo >,
            'id_marca': < id_marca >,
            'nome_marca': < nome_marca >}}

        :raise EquipamentoNaoExisteError: Equipamento com o
            id informado não cadastrado.
        :raise InvalidParameterError: O nome do equipamento é nulo ou vazio.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """

        if id is None:
            raise InvalidParameterError(
                'O id do equipamento não foi informado.')

        url = 'equipamento/id/' + urllib.parse.quote(id) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def list_all(self):
        """Return all equipments in database

        :return: Dictionary with the following structure:

        ::

            {'equipaments': {'name' :< name_equipament >}, {... demais equipamentos ...} }

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        url = 'equipamento/list/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def get_all(self):
        """Return all equipments in database

        :return: Dictionary with the following structure:

        ::
            {'equipaments': {'name' :< name_equipament >}, {... demais equipamentos ...} }

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        url = 'equipment/all'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def remover(self, id_equipamento):
        """Remove um equipamento a partir do seu identificador.

        Além de remover o equipamento, a API também remove:

            - O relacionamento do equipamento com os tipos de acessos.
            - O relacionamento do equipamento com os roteiros.
            - O relacionamento do equipamento com os IPs.
            - As interfaces do equipamento.
            - O relacionamento do equipamento com os ambientes.
            - O relacionamento do equipamento com os grupos.

        :param id_equipamento: Identificador do equipamento.

        :return: None

        :raise EquipamentoNaoExisteError: Equipamento não cadastrado.
        :raise InvalidParameterError: O identificador do equipamento é nulo ou inválido.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """
        if not is_valid_int_param(id_equipamento):
            raise InvalidParameterError(
                'O identificador do equipamento é inválido ou não foi informado.')

        url = 'equipamento/' + str(id_equipamento) + '/'

        code, map = self.submit(None, 'DELETE', url)

        return self.response(code, map)

    def associar_grupo(self, id_equipamento, id_grupo_equipamento):
        """Associa um equipamento a um grupo.

        :param id_equipamento: Identificador do equipamento.
        :param id_grupo_equipamento: Identificador do grupo de equipamento.

        :return: Dicionário com a seguinte estrutura:
            {'equipamento_grupo':{'id': < id_equip_do_grupo >}}

        :raise GrupoEquipamentoNaoExisteError: Grupo de equipamento não cadastrado.
        :raise InvalidParameterError: O identificador do equipamento e/ou do grupo são nulos ou inválidos.
        :raise EquipamentoNaoExisteError: Equipamento não cadastrado.
        :raise EquipamentoError: Equipamento já está associado ao grupo.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """

        equip_map = dict()
        equip_map['id_grupo'] = id_grupo_equipamento
        equip_map['id_equipamento'] = id_equipamento

        code, xml = self.submit(
            {'equipamento_grupo': equip_map}, 'POST', 'equipamentogrupo/')

        return self.response(code, xml)

    def remover_grupo(self, id_equipamento, id_grupo):
        """Remove a associação de um equipamento com um grupo de equipamento.

        :param id_equipamento: Identificador do equipamento.
        :param id_grupo: Identificador do grupo de equipamento.

        :return: None

        :raise EquipamentoGrupoNaoExisteError: Associação entre grupo e equipamento não cadastrada.
        :raise EquipamentoNaoExisteError: Equipamento não cadastrado.
        :raise EquipmentDontRemoveError: Failure to remove an association between an equipment and a group because the group is related only to a group.
        :raise InvalidParameterError: O identificador do equipamento e/ou do grupo são nulos ou inválidos.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """

        if not is_valid_int_param(id_equipamento):
            raise InvalidParameterError(
                'O identificador do equipamento é inválido ou não foi informado.')

        if not is_valid_int_param(id_grupo):
            raise InvalidParameterError(
                'O identificador do grupo é inválido ou não foi informado.')

        url = 'equipamentogrupo/equipamento/' + \
            str(id_equipamento) + '/egrupo/' + str(id_grupo) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def list_by_group(self, id_egroup):
        """Search Group Equipment from by the identifier.

        :param id_egroup: Identifier of the Group Equipment. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            {'equipaments':
            [{'nome': < name_equipament >, 'grupos': < id_group >,
            'mark': {'id': < id_mark >, 'nome': < name_mark >},'modelo': < id_model >,
            'tipo_equipamento': < id_type >,
            'model': {'nome': , 'id': < id_model >, 'marca': < id_mark >},
            'type': {id': < id_type >, 'tipo_equipamento': < name_type >},
            'id': < id_equipment >}, ... ]}

        :raise InvalidParameterError: Group Equipment is null and invalid.
        :raise GrupoEquipamentoNaoExisteError: Group Equipment not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if id_egroup is None:
            raise InvalidParameterError(
                'The identifier of Group Equipament is invalid or was not informed.')

        url = 'equipment/group/' + str(id_egroup) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def get_ips_by_equipment_and_environment(self, equip_nome, id_ambiente):
        """Search Group Equipment from by the identifier.

        :param id_egroup: Identifier of the Group Equipment. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            {'equipaments':
            [{'nome': < name_equipament >, 'grupos': < id_group >,
            'mark': {'id': < id_mark >, 'nome': < name_mark >},'modelo': < id_model >,
            'tipo_equipamento': < id_type >,
            'model': {'nome': , 'id': < id_model >, 'marca': < id_mark >},
            'type': {id': < id_type >, 'tipo_equipamento': < name_type >},
            'id': < id_equipment >}, ... ]}

        :raise InvalidParameterError: Group Equipment is null and invalid.
        :raise GrupoEquipamentoNaoExisteError: Group Equipment not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if id_ambiente is None:
            raise InvalidParameterError(
                'The environment id is invalid or was not informed.')

        url = 'equipment/getipsbyambiente/' + str(equip_nome) + '/' + str(id_ambiente)

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)
