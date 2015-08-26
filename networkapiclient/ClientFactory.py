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
from ApiVlan import ApiVlan

from networkapiclient.Ambiente import Ambiente
from networkapiclient.Equipamento import Equipamento
from networkapiclient.TipoRede import TipoRede
from networkapiclient.Vip import Vip
from networkapiclient.Vlan import Vlan
from networkapiclient.GrupoVirtual import GrupoVirtual
from networkapiclient.AmbienteLogico import AmbienteLogico
from networkapiclient.DivisaoDc import DivisaoDc
from networkapiclient.EquipamentoAcesso import EquipamentoAcesso
from networkapiclient.EquipamentoAmbiente import EquipamentoAmbiente
from networkapiclient.EquipamentoRoteiro import EquipamentoRoteiro
from networkapiclient.GrupoEquipamento import GrupoEquipamento
from networkapiclient.GrupoL3 import GrupoL3
from networkapiclient.GrupoUsuario import GrupoUsuario
from networkapiclient.Interface import Interface
from networkapiclient.Ip import Ip
from networkapiclient.Marca import Marca
from networkapiclient.Modelo import Modelo
from networkapiclient.PermissaoAdministrativa import PermissaoAdministrativa
from networkapiclient.Roteiro import Roteiro
from networkapiclient.TipoAcesso import TipoAcesso
from networkapiclient.TipoEquipamento import TipoEquipamento
from networkapiclient.TipoRoteiro import TipoRoteiro
from networkapiclient.Usuario import Usuario
from networkapiclient.UsuarioGrupo import UsuarioGrupo
from networkapiclient.DireitoGrupoEquipamento import DireitoGrupoEquipamento
from networkapiclient.Network import Network
from networkapiclient.EnvironmentVIP import EnvironmentVIP
from networkapiclient.OptionVIP import OptionVIP
from networkapiclient.Filter import Filter
from networkapiclient.Permission import Permission
from networkapiclient.EventLog import EventLog
from networkapiclient.BlockRule import BlockRule
from networkapiclient.Pool import Pool
from networkapiclient.OptionPool import OptionPool
from networkapiclient.Healthcheck import Healthcheck
from networkapiclient.ApiVipRequest import ApiVipRequest
from networkapiclient.ApiInterface import ApiInterfaceRequest
from networkapiclient.Rack import Rack
from networkapiclient.RackServers import RackServers



class ClientFactory(object):

    """Factory to create entities for NetworkAPI-Client."""

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        self.networkapi_url = networkapi_url
        self.user = user
        self.password = password
        self.user_ldap = user_ldap

    def create_ambiente(self):
        """Get an instance of ambiente services facade."""
        return Ambiente(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_ambiente_logico(self):
        """Get an instance of ambiente_logico services facade."""
        return AmbienteLogico(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_divisao_dc(self):
        """Get an instance of divisao_dc services facade."""
        return DivisaoDc(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_equipamento(self):
        """Get an instance of equipamento services facade."""
        return Equipamento(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_equipamento_acesso(self):
        """Get an instance of equipamento_acesso services facade."""
        return EquipamentoAcesso(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_equipamento_ambiente(self):
        """Get an instance of equipamento_ambiente services facade."""
        return EquipamentoAmbiente(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_equipamento_roteiro(self):
        """Get an instance of equipamento_roteiro services facade."""
        return EquipamentoRoteiro(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_grupo_equipamento(self):
        """Get an instance of grupo_equipamento services facade."""
        return GrupoEquipamento(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_grupo_l3(self):
        """Get an instance of grupo_l3 services facade."""
        return GrupoL3(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_grupo_usuario(self):
        """Get an instance of grupo_usuario services facade."""
        return GrupoUsuario(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_grupo_virtual(self):
        """Get an instance of grupo_virtual services facade."""
        return GrupoVirtual(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_interface(self):
        """Get an instance of interface services facade."""
        return Interface(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_ip(self):
        """Get an instance of ip services facade."""
        return Ip(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_marca(self):
        """Get an instance of marca services facade."""
        return Marca(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_modelo(self):
        """Get an instance of modelo services facade."""
        return Modelo(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_permissao_administrativa(self):
        """Get an instance of permissao_administrativa services facade."""
        return PermissaoAdministrativa(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_roteiro(self):
        """Get an instance of roteiro services facade."""
        return Roteiro(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_tipo_acesso(self):
        """Get an instance of tipo_acesso services facade."""
        return TipoAcesso(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_tipo_equipamento(self):
        """Get an instance of tipo_equipamento services facade."""
        return TipoEquipamento(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_tipo_rede(self):
        """Get an instance of tipo_rede services facade."""
        return TipoRede(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_tipo_roteiro(self):
        """Get an instance of tipo_roteiro services facade."""
        return TipoRoteiro(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_usuario(self):
        """Get an instance of usuario services facade."""
        return Usuario(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_usuario_grupo(self):
        """Get an instance of usuario_grupo services facade."""
        return UsuarioGrupo(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_vip(self):
        """Get an instance of vip services facade."""
        return Vip(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_vlan(self):
        """Get an instance of vlan services facade."""
        return Vlan(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_direito_grupo_equipamento(self):
        """Get an instance of direito_grupo_equipamento services facade."""
        return DireitoGrupoEquipamento(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_network(self):
        """Get an instance of vlan services facade."""
        return Network(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_environment_vip(self):
        """Get an instance of environment_vip services facade."""
        return EnvironmentVIP(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_option_vip(self):
        """Get an instance of option_vip services facade."""
        return OptionVIP(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_option_pool(self):
        """Get an instance of option_pool services facade."""
        return OptionPool(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_filter(self):
        """Get an instance of filter services facade."""
        return Filter(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_permission(self):
        """Get an instance of permission services facade."""
        return Permission(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_log(self):
        """Get an instance of log services facade."""
        return EventLog(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_rule(self):
        """Get an instance of block rule services facade."""
        return BlockRule(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_pool(self):

        """Get an instance of Poll services facade."""

        return Pool(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap
        )

    def create_healthcheck(self):

        """Get an instance of Poll services facade."""

        return Healthcheck(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap
        )

    def create_api_vip_request(self):

        """Get an instance of Api Vip Requests services facade."""

        return ApiVipRequest(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap
        )

    def create_api_interface_request(self):

        """Get an instance of Api Vip Requests services facade."""

        return ApiInterfaceRequest(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap
        )


    def create_rack(self):
        """Get an instance of rack services facade."""
        return Rack(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)

    def create_rackservers(self):
        """Get an instance of rackservers services facade."""
        return RackServers(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap)
    def create_api_vlan(self):

        """Get an instance of Api Vlan services facade."""

        return ApiVlan(
            self.networkapi_url,
            self.user,
            self.password,
            self.user_ldap
        )
