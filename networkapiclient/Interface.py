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
import urllib
from utils import is_valid_0_1


class Interface(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            Interface,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def listar_por_equipamento(self, id_equipamento):
        """List all interfaces of an equipment.

        :param id_equipamento: Equipment identifier.

        :return: Dictionary with the following:

        ::

            {'interface':
            [{'protegida': < protegida >,
            'nome': < nome >,
            'id_ligacao_front': < id_ligacao_front >,
            'id_equipamento': < id_equipamento >,
            'id': < id >,
            'descricao': < descricao >,
            'id_ligacao_back': < id_ligacao_back >}, ... other interfaces ...]}

        :raise InvalidParameterError: Equipment identifier is invalid or none.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_equipamento):
            raise InvalidParameterError(
                u'Equipment id is invalid or was not informed.')

        url = 'interface/equipamento/' + str(id_equipamento) + '/'

        code, map = self.submit(None, 'GET', url)

        key = 'interface'
        return get_list_map(self.response(code, map, [key]), key)

    def list_all_by_equip(self, id_equipamento):
        """List all interfaces of an equipment.

        :param id_equipamento: Equipment identifier.

        :return: Following dictionary:

        ::

            {'interfaces': [ {'id': < id >,
            'interface': < interface >,
            'descricao': < descricao >,
            'protegida': < protegida >,
            'tipo_equip': < id_tipo_equipamento >,
            'equipamento': < id_equipamento >,
            'equipamento_nome': < nome_equipamento >
            'ligacao_front': < id_ligacao_front >,
            'nome_ligacao_front': < interface_name >,
            'nome_equip_l_front': < equipment_name >,
            'ligacao_back': < id_ligacao_back >,
            'nome_ligacao_back': < interface_name >,
            'nome_equip_l_back': < equipment_name > }, ... other interfaces ...]}

        :raise InvalidParameterError: Equipment identifier is invalid or none.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_equipamento):
            raise InvalidParameterError(
                u'Equipment id is invalid or was not informed.')

        url = 'interface/equipment/' + str(id_equipamento) + '/'

        code, map = self.submit(None, 'GET', url)

        key = 'interfaces'
        return get_list_map(self.response(code, map, [key]), key)

    def get_by_id(self, id_interface):
        """Get an interface by id.

        :param id_interface: Interface identifier.

        :return: Following dictionary:

        ::

            {'interface': {'id': < id >,
            'interface': < interface >,
            'descricao': < descricao >,
            'protegida': < protegida >,
            'tipo_equip': < id_tipo_equipamento >,
            'equipamento': < id_equipamento >,
            'equipamento_nome': < nome_equipamento >
            'ligacao_front': < id_ligacao_front >,
            'nome_ligacao_front': < interface_name >,
            'nome_equip_l_front': < equipment_name >,
            'ligacao_back': < id_ligacao_back >,
            'nome_ligacao_back': < interface_name >,
            'nome_equip_l_back': < equipment_name > }}

        :raise InvalidParameterError: Interface identifier is invalid or none.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_interface):
            raise InvalidParameterError(
                u'Interface id is invalid or was not informed.')

        url = 'interface/' + str(id_interface) + '/get/'

        code, map = self.submit(None, 'GET', url)

        return self.response(code, map)

    def inserir(
            self,
            nome,
            protegida,
            descricao,
            id_ligacao_front,
            id_ligacao_back,
            id_equipamento,
            tipo=None,
            vlan=None):
        """Insert new interface for an equipment.

        :param nome: Interface name.
        :param protegida: Indication of protected ('0' or '1').
        :param descricao: Interface description.
        :param id_ligacao_front: Front end link interface identifier.
        :param id_ligacao_back: Back end link interface identifier.
        :param id_equipamento: Equipment identifier.

        :return: Dictionary with the following: {'interface': {'id': < id >}}

        :raise EquipamentoNaoExisteError: Equipment does not exist.
        :raise InvalidParameterError: The parameters nome, protegida and/or equipment id are none or invalid.
        :raise NomeInterfaceDuplicadoParaEquipamentoError: There is already an interface with this name for this equipment.
        :raise InterfaceNaoExisteError: Front link interface and/or back link interface doesn't exist.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        interface_map = dict()
        interface_map['nome'] = nome
        interface_map['protegida'] = protegida
        interface_map['descricao'] = descricao
        interface_map['id_ligacao_front'] = id_ligacao_front
        interface_map['id_ligacao_back'] = id_ligacao_back
        interface_map['id_equipamento'] = id_equipamento
        interface_map['tipo'] = tipo
        interface_map['vlan'] = vlan

        code, xml = self.submit({'interface': interface_map}, 'POST', 'interface/')
        return self.response(code, xml)

    def alterar(
            self,
            id_interface,
            nome,
            protegida,
            descricao,
            id_ligacao_front,
            id_ligacao_back,
            tipo=None,
            vlan=None):
        """Edit an interface by its identifier.

        Equipment identifier is not changed.

        :param nome: Interface name.
        :param protegida: Indication of protected ('0' or '1').
        :param descricao: Interface description.
        :param id_ligacao_front: Front end link interface identifier.
        :param id_ligacao_back: Back end link interface identifier.
        :param id_interface: Interface identifier.

        :return: None

        :raise InvalidParameterError: The parameters interface id, nome and protegida are none or invalid.
        :raise NomeInterfaceDuplicadoParaEquipamentoError: There is already an interface with this name for this equipment.
        :raise InterfaceNaoExisteError: Front link interface and/or back link interface doesn't exist.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_interface):
            raise InvalidParameterError(
                u'Interface id is invalid or was not informed.')

        url = 'interface/' + str(id_interface) + '/'

        interface_map = dict()
        interface_map['nome'] = nome
        interface_map['protegida'] = protegida
        interface_map['descricao'] = descricao
        interface_map['id_ligacao_front'] = id_ligacao_front
        interface_map['id_ligacao_back'] = id_ligacao_back
        interface_map['tipo'] = tipo
        interface_map['vlan'] = vlan

        code, xml = self.submit({'interface': interface_map}, 'PUT', url)

        return self.response(code, xml)

    def remover(self, id_interface):
        """Remove an interface by its identifier.

        :param id_interface: Interface identifier.

        :return: None

        :raise InterfaceNaoExisteError: Interface doesn't exist.
        :raise InterfaceError: Interface is linked to another interface.
        :raise InvalidParameterError: The interface identifier is invalid or none.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_interface):
            raise InvalidParameterError(
                u'Interface id is invalid or was not informed.')

        url = 'interface/' + str(id_interface) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def remove_connection(self, id_interface, back_or_front):
        """
        Remove a connection between two interfaces

        :param id_interface: One side of relation
        :param back_or_front: This side of relation is back(0) or front(1)

        :return: None

        :raise InterfaceInvalidBackFrontError: Front or Back of interfaces not match to remove connection
        :raise InvalidParameterError: Interface id or back or front indicator is none or invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        msg_err = u'Parameter %s is invalid. Value: %s.'

        if not is_valid_0_1(back_or_front):
            raise InvalidParameterError(
                msg_err %
                ("back_or_front", back_or_front))

        if not is_valid_int_param(id_interface):
            raise InvalidParameterError(
                msg_err %
                ("id_interface", id_interface))

        url = "interface/%s/%s/" % (str(id_interface), str(back_or_front))

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def listar_ligacoes(self, nome_interface, id_equipamento):
        """List interfaces linked to back and front of specified interface.

        :param nome_interface: Interface name.
        :param id_equipamento: Equipment identifier.

        :return: Dictionary with the following:

        ::

            {'interface': [{'protegida': < protegida >,
            'nome': < nome >,
            'id_ligacao_front': < id_ligacao_front >,
            'id_equipamento': < id_equipamento >,
            'id': < id >,
            'descricao': < descricao >,
            'id_ligacao_back': < id_ligacao_back >}, ... other interfaces ...]}

        :raise InterfaceNaoExisteError: Interface doesn't exist or is not associated with this equipment.
        :raise EquipamentoNaoExisteError: Equipment doesn't exist.
        :raise InvalidParameterError: Interface name and/or equipment identifier are none or invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_equipamento):
            raise InvalidParameterError(
                u'Equipment identifier is none or was not informed.')

        if (nome_interface is None) or (nome_interface == ''):
            raise InvalidParameterError(u'Interface name was not informed.')

        url = 'interface/' + \
            urllib.quote(nome_interface) + '/equipamento/' + str(id_equipamento) + '/'

        code, map = self.submit(None, 'GET', url)

        key = 'interface'
        return get_list_map(self.response(code, map, [key]), key)

    def list_connections(self, nome_interface, id_equipamento):
        """List interfaces linked to back and front of specified interface.

        :param nome_interface: Interface name.
        :param id_equipamento: Equipment identifier.

        :return: Dictionary with the following:

        ::

            {'interfaces':[ {'id': < id >,
            'interface': < nome >,
            'descricao': < descricao >,
            'protegida': < protegida >,
            'equipamento': < id_equipamento >,
            'tipo_equip': < id_tipo_equipamento >,
            'ligacao_front': < id_ligacao_front >,
            'nome_ligacao_front': < interface_name >,
            'nome_equip_l_front': < equipment_name >,
            'ligacao_back': < id_ligacao_back >,
            'nome_ligacao_back': < interface_name >,
            'nome_equip_l_back': < equipment_name > }, ... other interfaces ...]}

        :raise InterfaceNaoExisteError: Interface doesn't exist or is not associated with this equipment.
        :raise EquipamentoNaoExisteError: Equipment doesn't exist.
        :raise InvalidParameterError: Interface name and/or equipment identifier are none or invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(id_equipamento):
            raise InvalidParameterError(
                u'Equipment identifier is none or was not informed.')

        if (nome_interface is None) or (nome_interface == ''):
            raise InvalidParameterError(u'Interface name was not informed.')

        # Temporário, remover. Fazer de outra forma.
        nome_interface = nome_interface.replace('/', 's2it_replace')

        url = 'interface/' + \
            urllib.quote(nome_interface) + '/equipment/' + str(id_equipamento) + '/'

        code, map = self.submit(None, 'GET', url)

        key = 'interfaces'
        return get_list_map(self.response(code, map, [key]), key)


    def listar_switch_router(self, id_equipamento):

        url = 'int/getbyidequip/' + str(id_equipamento) + '/'
        code, xml = self.submit(None, 'GET', url)

        key = 'interfaces'
        return get_list_map(self.response(code, xml, [key]), key)


    def list_all_interface_types(self):

        url = 'interfacetype/get-type/'
        code, xml = self.submit(None, 'GET', url)

        key = 'tipo_interface'
        return get_list_map(self.response(code, xml, [key]), key)

    def associar_ambiente(self, ambiente, interface):

        interface_map = dict()
        interface_map['ambiente'] = ambiente
        interface_map['interface'] = interface

        code, xml = self.submit(
            {'interface': interface_map}, 'POST', 'int/associar-ambiente/')

        return self.response(code, xml)

    def dissociar(self, interface):

        interface_map = dict()
        interface_map['interface'] = interface

        code, xml = self.submit({'interface': interface_map}, 'DELETE', 'int/associar-ambiente/')

        return self.response(code, xml)

    def inserir_channel (self, interfaces, nome, lacp, int_type, vlan, envs):

        channel_map = dict ()
        channel_map['interfaces'] = interfaces
        channel_map['nome'] = nome
        channel_map['lacp'] = lacp
        channel_map['int_type'] = int_type
        channel_map['vlan'] = vlan
        channel_map['envs'] = envs

        code, xml = self.submit({'channel': channel_map}, 'POST', 'channel/inserir/')

        return self.response(code, xml)

    def get_env_by_id(self, id_interface):

        if not is_valid_int_param(id_interface):
            raise InvalidParameterError(u'Interface id is invalid or was not informed.')

        url = 'int/get-env-by-interface/' + str(id_interface)

        code, map = self.submit(None, 'GET', url)

        return self.response(code, map)

    def delete_channel(self, channel_name):

        url = 'channel/delete/' + str(channel_name) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def get_interface_by_channel(self, channel_name):

        url = 'interface/get-by-channel/' + str(channel_name) + '/'

        code, map = self.submit(None, 'GET', url)

        return self.response(code, map)

    def editar_channel (self, id_channel, nome, lacp, int_type, vlan, envs, ids_interface):

        channel_map = dict ()
        channel_map['id_channel'] = id_channel
        channel_map['nome'] = nome
        channel_map['lacp'] = lacp
        channel_map['int_type'] = int_type
        channel_map['vlan'] = vlan
        channel_map['envs'] = envs
        channel_map['ids_interface'] = ids_interface

        code, xml = self.submit({'channel': channel_map}, 'PUT', 'channel/editar/')

        return self.response(code, xml)

    def list_available_interfaces(self, channel_name, id_equip):

        url = 'interface/get/' + str(channel_name) + '/' + str(id_equip) + '/'

        code, map = self.submit(None, 'GET', url)

        return self.response(code, map)