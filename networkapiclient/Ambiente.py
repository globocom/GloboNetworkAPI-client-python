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
from networkapiclient.utils import is_valid_int_param, get_list_map, is_valid_ip
import urllib


class Ambiente(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            Ambiente,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def list_all(self):
        """
        List all environments in DB

        :return: Following dictionary:

        ::

            {'ambiente': [{ 'id': <id_environment>,
            'grupo_l3': <id_group_l3>,
            'grupo_l3_name': <name_group_l3>,
            'ambiente_logico': <id_logical_environment>,
            'ambiente_logico_name': <name_ambiente_logico>,
            'divisao_dc': <id_dc_division>,
            'divisao_dc_name': <name_divisao_dc>,
            'filter': <id_filter>,
            'filter_name': <filter_name>,
            'link': <link> }, ... ]}


        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        """

        url = "ambiente/list/"

        code, xml = self.submit(None, 'GET', url)

        key = 'ambiente'
        return get_list_map(self.response(code, xml, [key]), key)

    def listar(self, id_divisao=None, id_ambiente_logico=None):
        """Lista os ambientes filtrados conforme parâmetros informados.

        Se os dois parâmetros têm o valor None então retorna todos os ambientes.
        Se o id_divisao é diferente de None então retorna os ambientes filtrados
        pelo valor de id_divisao.
        Se o id_divisao e id_ambiente_logico são diferentes de None então retorna
        os ambientes filtrados por id_divisao e id_ambiente_logico.

        :param id_divisao: Identificador da divisão de data center.
        :param id_ambiente_logico: Identificador do ambiente lógico.

        :return: Dicionário com a seguinte estrutura:

        ::

            {'ambiente': [{'id': < id_ambiente >,
            'link': < link >,
            'id_divisao': < id_divisao >,
            'nome_divisao': < nome_divisao >,
            'id_ambiente_logico': < id_ambiente_logico >,
            'nome_ambiente_logico': < nome_ambiente_logico >,
            'id_grupo_l3': < id_grupo_l3 >,
            'nome_grupo_l3': < nome_grupo_l3 >,
            'id_filter': < id_filter >,
            'filter_name': < filter_name >,
            'ambiente_rede': < ambiente_rede >},
            ... demais ambientes ... ]}

        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """

        url = 'ambiente/'

        if is_valid_int_param(id_divisao) and not is_valid_int_param(
                id_ambiente_logico):
            url = 'ambiente/divisao_dc/' + str(id_divisao) + '/'
        elif is_valid_int_param(id_divisao) and is_valid_int_param(id_ambiente_logico):
            url = 'ambiente/divisao_dc/' + \
                str(id_divisao) + '/ambiente_logico/' + str(id_ambiente_logico) + '/'

        code, xml = self.submit(None, 'GET', url)

        key = 'ambiente'
        return get_list_map(self.response(code, xml, [key]), key)

    def buscar_por_equipamento(self, nome_equipamento, ip_equipamento):
        """Obtém um ambiente a partir do ip e nome de um equipamento.

        :param nome_equipamento: Nome do equipamento.
        :param ip_equipamento: IP do equipamento no formato XXX.XXX.XXX.XXX.

        :return: Dicionário com a seguinte estrutura:

        ::

            {'ambiente': {'id': < id_ambiente >,
            'link': < link >,
            'id_divisao': < id_divisao >,
            'nome_divisao': < nome_divisao >,
            'id_ambiente_logico': < id_ambiente_logico >,
            'nome_ambiente_logico': < nome_ambiente_logico >,
            'id_grupo_l3': < id_grupo_l3 >,
            'nome_grupo_l3': < nome_grupo_l3 >,
            'id_filter': < id_filter >,
            'filter_name': < filter_name >,
            'ambiente_rede': < ambiente_rede >}}

        :raise IpError: IP não cadastrado para o equipamento.
        :raise InvalidParameterError: O nome e/ou o IP do equipamento são vazios ou nulos, ou o IP é inválido.
        :raise EquipamentoNaoExisteError: Equipamento não cadastrado.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """

        if nome_equipamento == '' or nome_equipamento is None:
            raise InvalidParameterError(
                u'O nome do equipamento não foi informado.')

        if not is_valid_ip(ip_equipamento):
            raise InvalidParameterError(
                u'O IP do equipamento é inválido ou não foi informado.')

        url = 'ambiente/equipamento/' + \
            urllib.quote(nome_equipamento) + '/ip/' + str(ip_equipamento) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def buscar_por_id(self, id_ambiente):
        """Obtém um ambiente a partir da chave primária (identificador).

        :param id_ambiente: Identificador do ambiente.

        :return: Dicionário com a seguinte estrutura:

        ::

            {'ambiente': {'id': < id_ambiente >,
            'link': < link >,
            'id_divisao': < id_divisao >,
            'nome_divisao': < nome_divisao >,
            'id_ambiente_logico': < id_ambiente_logico >,
            'nome_ambiente_logico': < nome_ambiente_logico >,
            'id_grupo_l3': < id_grupo_l3 >,
            'nome_grupo_l3': < nome_grupo_l3 >,
            'id_filter': < id_filter >,
            'filter_name': < filter_name >,
            'acl_path': < acl_path >,
            'ipv4_template': < ipv4_template >,
            'ipv6_template': < ipv6_template >,
            'ambiente_rede': < ambiente_rede >}}

        :raise AmbienteNaoExisteError: Ambiente não cadastrado.
        :raise InvalidParameterError: Identificador do ambiente é nulo ou inválido.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """
        if not is_valid_int_param(id_ambiente):
            raise InvalidParameterError(
                u'O identificador do ambiente é inválido ou não foi informado.')

        url = 'environment/id/' + str(id_ambiente) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def buscar_healthcheck_por_id(self, id_healthcheck):
        """Get HealthCheck by id.

        :param id_healthcheck: HealthCheck ID.

        :return: Following dictionary:

        ::

            {'healthcheck_expect': {'match_list': < match_list >,
             'expect_string': < expect_string >,
             'id': < id >,
             'ambiente': < ambiente >}}

        :raise HealthCheckNaoExisteError:  HealthCheck not registered.
        :raise InvalidParameterError: HealthCheck identifier is null and invalid.
        :raise DataBaseError: Can't connect to networkapi database.
        :raise XMLError: Failed to generate the XML response.
        """
        if not is_valid_int_param(id_healthcheck):
            raise InvalidParameterError(
                u'O identificador do healthcheck é inválido ou não foi informado.')

        url = 'healthcheckexpect/get/' + str(id_healthcheck) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def listar_por_equip(self, equip_id):
        """Lista todos os ambientes por equipamento especifico.

        :return: Dicionário com a seguinte estrutura:

        ::

            {'ambiente': {'id': < id_ambiente >,
            'link': < link >,
            'id_divisao': < id_divisao >,
            'nome_divisao': < nome_divisao >,
            'id_ambiente_logico': < id_ambiente_logico >,
            'nome_ambiente_logico': < nome_ambiente_logico >,
            'id_grupo_l3': < id_grupo_l3 >,
            'nome_grupo_l3': < nome_grupo_l3 >,
            'id_filter': < id_filter >,
            'filter_name': < filter_name >,
            'ambiente_rede': < ambiente_rede >}}

        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """

        if equip_id is None:
            raise InvalidParameterError(
                u'O id do equipamento não foi informado.')

        url = 'ambiente/equip/' + str(equip_id) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def listar_healthcheck_expect(self, id_ambiente):
        """Lista os healthcheck_expect´s de um ambiente.

        :param id_ambiente: Identificador do ambiente.

        :return: Dicionário com a seguinte estrutura:

        ::

            {'healthcheck_expect': [{'id': < id_healthcheck_expect >,
             'expect_string': < expect_string >,
             'match_list': < match_list >,
             'id_ambiente': < id_ambiente >},
             ... demais healthcheck_expects ...]}

        :raise InvalidParameterError: O identificador do ambiente é nulo ou inválido.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """

        if not is_valid_int_param(id_ambiente):
            raise InvalidParameterError(
                u'O identificador do ambiente é inválido ou não foi informado.')

        url = 'healthcheckexpect/ambiente/' + str(id_ambiente) + '/'

        code, xml = self.submit(None, 'GET', url)

        key = 'healthcheck_expect'
        return get_list_map(self.response(code, xml, [key]), key)

    def add_healthcheck_expect(self, id_ambiente, expect_string, match_list):
        """Insere um novo healthckeck_expect e retorna o seu identificador.

        :param expect_string: expect_string.
        :param id_ambiente: Identificador do ambiente lógico.
        :param match_list: match list.

        :return: Dicionário com a seguinte estrutura: {'healthcheck_expect': {'id': < id >}}

        :raise InvalidParameterError: O identificador do ambiente, match_lis,expect_string, são inválidos ou nulo.
        :raise HealthCheckExpectJaCadastradoError: Já existe um healthcheck_expect com os mesmos dados cadastrados.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """

        healthcheck_map = dict()
        healthcheck_map['id_ambiente'] = id_ambiente
        healthcheck_map['expect_string'] = expect_string
        healthcheck_map['match_list'] = match_list

        url = 'healthcheckexpect/add/'

        code, xml = self.submit({'healthcheck': healthcheck_map}, 'POST', url)

        return self.response(code, xml)

    def inserir(
            self,
            id_grupo_l3,
            id_ambiente_logico,
            id_divisao,
            link,
            id_filter=None,
            acl_path=None,
            ipv4_template=None,
            ipv6_template=None,
            min_num_vlan_1=None,
            max_num_vlan_1=None,
            min_num_vlan_2=None,
            max_num_vlan_2=None,
            vrf=None):
        """Insere um novo ambiente e retorna o seu identificador.

        :param id_grupo_l3: Identificador do grupo layer 3.
        :param id_ambiente_logico: Identificador do ambiente lógico.
        :param id_divisao: Identificador da divisão data center.
        :param id_filter: Filter identifier.
        :param link: Link
        :param acl_path: Path where the ACL will be stored
        :param ipv4_template: Template that will be used in Ipv6
        :param ipv6_template: Template that will be used in Ipv4
        :param min_num_vlan_1: Min 1 num vlan valid for this environment
        :param max_num_vlan_1: Max 1 num vlan valid for this environment
        :param min_num_vlan_2: Min 2 num vlan valid for this environment
        :param max_num_vlan_2: Max 2 num vlan valid for this environment

        :return: Dicionário com a seguinte estrutura: {'ambiente': {'id': < id >}}

        :raise InvalidParameterError: O identificador do grupo l3, o identificador do ambiente lógico, e/ou
            o identificador da divisão de data center são nulos ou inválidos.
        :raise GrupoL3NaoExisteError: Grupo layer 3 não cadastrado.
        :raise AmbienteLogicoNaoExisteError: Ambiente lógico não cadastrado.
        :raise DivisaoDcNaoExisteError: Divisão datacenter não cadastrada.
        :raise AmbienteDuplicadoError: Ambiente com o mesmo id_grupo_l3, id_ambiente_logico e id_divisao
            já cadastrado.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """

        ambiente_map = dict()
        ambiente_map['id_grupo_l3'] = id_grupo_l3
        ambiente_map['id_ambiente_logico'] = id_ambiente_logico
        ambiente_map['id_divisao'] = id_divisao
        ambiente_map['id_filter'] = id_filter
        ambiente_map['link'] = link
        ambiente_map['acl_path'] = acl_path
        ambiente_map['ipv4_template'] = ipv4_template
        ambiente_map['ipv6_template'] = ipv6_template
        ambiente_map['min_num_vlan_1'] = min_num_vlan_1
        ambiente_map['max_num_vlan_1'] = max_num_vlan_1
        ambiente_map['min_num_vlan_2'] = min_num_vlan_2
        ambiente_map['max_num_vlan_2'] = max_num_vlan_2
        ambiente_map['vrf'] = vrf

        code, xml = self.submit(
            {'ambiente': ambiente_map}, 'POST', 'ambiente/')

        return self.response(code, xml)

    def insert_with_ip_range(
            self,
            id_l3_group,
            id_logical_environment,
            id_division,
            id_ip_config,
            link,
            id_filter=None):
        """Insert new environment with ip config and returns your id.

        :param id_l3_group: Layer 3 Group ID.
        :param id_logical_environment: Logical Environment ID.
        :param id_division: Data Center Division ID.
        :param id_filter: Filter identifier.
        :param id_ip_config: IP Configuration ID.
        :param link: Link.

        :return: Following dictionary: {'ambiente': {'id': < id >}}

        :raise ConfigEnvironmentDuplicateError: Error saving duplicate Environment Configuration.
        :raise InvalidParameterError: Some parameter was invalid.
        :raise GrupoL3NaoExisteError: Layer 3 Group not found.
        :raise AmbienteLogicoNaoExisteError: Logical Environment not found.
        :raise DivisaoDcNaoExisteError: Data Center Division not found.
        :raise AmbienteDuplicadoError: Environment with this parameters already exists.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        environment_map = dict()
        environment_map['id_grupo_l3'] = id_l3_group
        environment_map['id_ambiente_logico'] = id_logical_environment
        environment_map['id_divisao'] = id_division
        environment_map['id_filter'] = id_filter
        environment_map['id_ip_config'] = id_ip_config
        environment_map['link'] = link

        code, xml = self.submit(
            {'ambiente': environment_map}, 'POST', 'ambiente/ipconfig/')

        return self.response(code, xml)

    def add_ip_range(self, id_environment, id_ip_config):
        """Makes relationship of environment with ip config and returns your id.

        :param id_environment: Environment ID.
        :param id_ip_config: IP Configuration ID.

        :return: Following dictionary:

        {'config_do_ambiente': {'id_config_do_ambiente': < id_config_do_ambiente >}}

        :raise InvalidParameterError: Some parameter was invalid.
        :raise ConfigEnvironmentDuplicateError: Error saving duplicate Environment Configuration.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        environment_map = dict()
        environment_map['id_environment'] = id_environment
        environment_map['id_ip_config'] = id_ip_config

        code, xml = self.submit(
            {'ambiente': environment_map}, 'POST', 'ipconfig/')

        return self.response(code, xml)

    def alterar(
            self,
            id_ambiente,
            id_grupo_l3,
            id_ambiente_logico,
            id_divisao,
            link,
            id_filter=None,
            acl_path=None,
            ipv4_template=None,
            ipv6_template=None,
            min_num_vlan_1=None,
            max_num_vlan_1=None,
            min_num_vlan_2=None,
            max_num_vlan_2=None,
            vrf=None):
        """Altera os dados de um ambiente a partir do seu identificador.

        :param id_ambiente: Identificador do ambiente.
        :param id_grupo_l3: Identificador do grupo layer 3.
        :param id_ambiente_logico: Identificador do ambiente lógico.
        :param id_divisao: Identificador da divisão data center.
        :param id_filter: Filter identifier.
        :param link: Link
        :param acl_path: Path where the ACL will be stored
        :param ipv4_template: Template that will be used in Ipv6
        :param ipv6_template: Template that will be used in Ipv4
        :param min_num_vlan_1: Min 1 num vlan valid for this environment
        :param max_num_vlan_1: Max 1 num vlan valid for this environment
        :param min_num_vlan_2: Min 2 num vlan valid for this environment
        :param max_num_vlan_2: Max 2 num vlan valid for this environment

        :return: None

        :raise InvalidParameterError: O identificador do ambiente, o identificador do grupo l3, o identificador do ambiente lógico, e/ou o identificador da divisão de data center são nulos ou inválidos.
        :raise GrupoL3NaoExisteError: Grupo layer 3 não cadastrado.
        :raise AmbienteLogicoNaoExisteError: Ambiente lógico não cadastrado.
        :raise DivisaoDcNaoExisteError: Divisão data center não cadastrada.
        :raise AmbienteDuplicadoError: Ambiente com o mesmo id_grupo_l3, id_ambiente_logico e id_divisao já cadastrado.
        :raise AmbienteNaoExisteError: Ambiente não cadastrado.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """

        if not is_valid_int_param(id_ambiente):
            raise InvalidParameterError(
                u'O identificador do ambiente é inválido ou não foi informado.')

        url = 'ambiente/' + str(id_ambiente) + '/'

        ambiente_map = dict()
        ambiente_map['id_grupo_l3'] = id_grupo_l3
        ambiente_map['id_ambiente_logico'] = id_ambiente_logico
        ambiente_map['id_divisao'] = id_divisao
        ambiente_map['id_filter'] = id_filter
        ambiente_map['link'] = link
        ambiente_map['vrf'] = vrf
        ambiente_map['acl_path'] = acl_path
        ambiente_map['ipv4_template'] = ipv4_template
        ambiente_map['ipv6_template'] = ipv6_template
        ambiente_map['min_num_vlan_1'] = min_num_vlan_1
        ambiente_map['max_num_vlan_1'] = max_num_vlan_1
        ambiente_map['min_num_vlan_2'] = min_num_vlan_2
        ambiente_map['max_num_vlan_2'] = max_num_vlan_2

        code, xml = self.submit({'ambiente': ambiente_map}, 'PUT', url)

        return self.response(code, xml)

    def remover(self, id_ambiente):
        """Remove um ambiente a partir de seu identificador.

        :param id_ambiente: Identificador do ambiente.

        :return: None

        :raise AmbienteNaoExisteError: Ambiente não cadastrado.
        :raise AmbienteError: Ambiente está associado a um equipamento e/ou a uma VLAN.
        :raise InvalidParameterError: O identificador do ambiente é nulo ou inválido.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """

        if not is_valid_int_param(id_ambiente):
            raise InvalidParameterError(
                u'O identificador do ambiente é inválido ou não foi informado.')

        url = 'ambiente/' + str(id_ambiente) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def add_expect_string_healthcheck(self, expect_string):
        """Inserts a new healthckeck_expect  with only expect_string.

        :param expect_string: expect_string.

        :return: Dictionary with the following structure:

        ::

            {'healthcheck_expect': {'id': < id >}}

        :raise InvalidParameterError: The value of expect_string is invalid.
        :raise HealthCheckExpectJaCadastradoError: There is already a healthcheck_expect registered with the same data.
        :raise HealthCheckExpectNaoExisteError: Healthcheck_expect not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.

        """

        healthcheck_map = dict()
        healthcheck_map['expect_string'] = expect_string

        url = 'healthcheckexpect/add/expect_string/'

        code, xml = self.submit({'healthcheck': healthcheck_map}, 'POST', url)

        return self.response(code, xml)

    def listar_healtchcheck_expect_distinct(self):
        """Get all expect_string.

        :return: Dictionary with the following structure:

        ::

            {'healthcheck_expect': [
             'expect_string': < expect_string >,
             ... demais healthcheck_expects ...]}


        :raise InvalidParameterError: Identifier is null and invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        url = 'healthcheckexpect/distinct/busca/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def list_acl_path(self):
        """Get all distinct acl paths.

        :return: Dictionary with the following structure:

        ::

            {'acl_paths': [
             < acl_path >,
             ... ]}



        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        url = 'environment/acl_path/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def set_template(self, id_environment, name, network):
        """Set template value. If id_environment = 0, set '' to all environments related with the template name.

        :param id_environment: Environment Identifier.
        :param name: Template Name.
        :param network: IPv4 or IPv6.

        :return: None

        :raise InvalidParameterError: Invalid param.
        :raise AmbienteNaoExisteError: Ambiente não cadastrado.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """

        url = 'environment/set_template/' + str(id_environment) + '/'

        environment_map = dict()
        environment_map['name'] = name
        environment_map['network'] = network

        code, xml = self.submit({'environment': environment_map}, 'POST', url)

        return self.response(code, xml)

    def get_environment_template(self, name, network):
        """Get environments by template name

        :param name: Template name.
        :param network: IPv4 or IPv6.

        :return: Following dictionary:

        ::

            {'ambiente': [divisao_dc - ambiente_logico - grupo_l3, other envs...] }

        :raise InvalidParameterError: Invalid param.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """
        url = 'environment/get_env_template/'

        map_dict = dict()
        map_dict['name'] = name
        map_dict['network'] = network

        code, xml = self.submit({'map': map_dict}, 'PUT', url)

        return self.response(code, xml)

    def save_blocks(self, id_env, blocks):
        """
        Save blocks from environment

        :param id_env: Environment id
        :param blocks: Lists of blocks in order. Ex: ['content one', 'content two', ...]

        :return: None

        :raise AmbienteNaoExisteError: Ambiente não cadastrado.
        :raise InvalidValueError: Invalid parameter.
        :raise UserNotAuthorizedError: Permissão negada.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """

        url = 'environment/save_blocks/'

        map_dict = dict()

        map_dict['id_env'] = id_env
        map_dict['blocks'] = blocks

        code, xml = self.submit({'map': map_dict}, 'POST', url)

        return self.response(code, xml)

    def update_blocks(self, id_env, blocks):
        """
        Update blocks from environment

        :param id_env: Environment id
        :param blocks: Lists of blocks in order. Ex: ['content one', 'content two', ...]

        :return: None

        :raise AmbienteNaoExisteError: Ambiente não cadastrado.
        :raise InvalidValueError: Invalid parameter.
        :raise UserNotAuthorizedError: Permissão negada.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """

        url = 'environment/update_blocks/'

        map_dict = dict()

        map_dict['id_env'] = id_env
        map_dict['blocks'] = blocks

        code, xml = self.submit({'map': map_dict}, 'PUT', url)

        return self.response(code, xml)

    def get_blocks(self, id_env):
        """
        Get blocks by environment

        :param id_env: Environment id

        :return: Following dictionary:

        ::

            {'blocks': [{'id' : <id>, 'content' : <content>},...] }

        :raise UserNotAuthorizedError: Permissão negada.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.

        """

        url = 'environment/get_blocks/' + str(id_env)

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml, ['blocks'])

    def list_no_blocks(self):
        """
        List all environments in DB without blocks

        :return: Following dictionary:

        ::

            {'ambiente': [{'id': <id_environment>,
              'grupo_l3': <id_group_l3>,
              'grupo_l3_name': <name_group_l3>
              'ambiente_logico': <id_logical_environment>,
              'ambiente_logico_name': <name_ambiente_logico>
              'divisao_dc': <id_dc_division>,
              'divisao_dc_name': <name_divisao_dc>,
              'filter': <id_filter>,
              'filter_name': <filter_name>,
              'link': <link> }, ... ]}


        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        """

        url = "environment/list_no_blocks/"

        code, xml = self.submit(None, 'PUT', url)

        key = 'ambiente'
        return get_list_map(self.response(code, xml, [key]), key)

    def get_rule_by_pk(self, id_rule):
        """
        Get a rule by its identifier

        :param id_rule: Rule identifier.

        :return: Seguinte estrutura

        ::

            { 'rule': {'id': < id >,
              'environment': < Environment Object >,
              'content': < content >,
              'name': < name >,
              'custom': < custom > }}

        :raise AmbienteNaoExisteError: Ambiente não cadastrado.
        :raise InvalidValueError: Invalid parameter.
        :raise UserNotAuthorizedError: Permissão negada.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """
        url = 'rule/get_by_id/' + str(id_rule)
        code, xml = self.submit(None, 'GET', url)
        return self.response(code, xml)

    def save_rule(self, name, id_env, contents, blocks_id):
        """
        Save an environment rule

        :param name: Name of the rule
        :param id_env: Environment id
        :param contents: Lists of contents in order. Ex: ['content one', 'content two', ...]
        :param blocks_id: Lists of blocks id or 0 if is as custom content. Ex: ['0', '5', '0' ...]

        :return: None

        :raise AmbienteNaoExisteError: Ambiente não cadastrado.
        :raise InvalidValueError: Invalid parameter.
        :raise UserNotAuthorizedError: Permissão negada.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """

        url = 'rule/save/'

        map_dict = dict()

        map_dict['name'] = name
        map_dict['id_env'] = id_env
        map_dict['contents'] = contents
        map_dict['blocks_id'] = blocks_id

        code, xml = self.submit({'map': map_dict}, 'POST', url)

        return self.response(code, xml)

    def update_rule(self, name, id_env, contents, blocks_id, id_rule):
        """
        Save an environment rule

        :param name: Name of the rule
        :param id_env: Environment id
        :param contents: Lists of contents in order. Ex: ['content one', 'content two', ...]
        :param blocks_id: Lists of blocks id or 0 if is as custom content. Ex: ['0', '5', '0' ...]
        :param id_rule: Rule id

        :return: None

        :raise AmbienteNaoExisteError: Ambiente não cadastrado.
        :raise InvalidValueError: Invalid parameter.
        :raise UserNotAuthorizedError: Permissão negada.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """

        url = 'rule/update/'

        map_dict = dict()

        map_dict['name'] = name
        map_dict['id_env'] = id_env
        map_dict['contents'] = contents
        map_dict['blocks_id'] = blocks_id
        map_dict['id_rule'] = id_rule

        try:
            code, xml = self.submit({'map': map_dict}, 'PUT', url)
        except Exception as e:
            raise e

        return self.response(code, xml)

    def delete_rule(self, id_rule):
        """
        Removes an environment rule

        :param id_rule: Rule id

        :return: None

        :raise AmbienteNaoExisteError: Ambiente não cadastrado.
        :raise InvalidValueError: Invalid parameter.
        :raise UserNotAuthorizedError: Permissão negada.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """

        url = 'rule/delete/%s/' % str(id_rule)

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def get_all_rules(self, id_env):
        """Save an environment rule

        :param id_env: Environment id

        :return: Estrutura:

        ::

            { 'rules': [{'id': < id >,
            'environment': < Environment Object >,
            'content': < content >,
            'name': < name >,
            'custom': < custom > },... ]}

        :raise AmbienteNaoExisteError: Ambiente não cadastrado.
        :raise UserNotAuthorizedError: Permissão negada.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """

        url = 'rule/all/' + str(id_env)
        code, xml = self.submit(None, 'GET', url)
        return self.response(code, xml, ['rules'])

    def configuration_save(
            self,
            id_environment,
            network,
            prefix,
            ip_version,
            network_type):
        """
        Add new prefix configuration

        :param id_environment: Identifier of the Environment. Integer value and greater than zero.
        :param network: Network Ipv4 or Ipv6.
        :param prefix: Prefix 0-32 to Ipv4 or 0-128 to Ipv6.
        :param ip_version: v4 to IPv4 or v6 to IPv6
        :param network_type: type network

        :return: Following dictionary:

        ::

            {'network':{'id_environment': <id_environment>,
            'id_vlan': <id_vlan>,
            'network_type': <network_type>,
            'network': <network>,
            'prefix': <prefix>} }

        :raise ConfigEnvironmentInvalidError: Invalid Environment Configuration or not registered.
        :raise InvalidValueError: Invalid Id for environment or network or network_type or prefix.
        :raise AmbienteNotFoundError: Environment not registered.
        :raise DataBaseError: Failed into networkapi access data base.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        network_map = dict()
        network_map['id_environment'] = id_environment
        network_map['network'] = network
        network_map['prefix'] = prefix
        network_map['ip_version'] = ip_version
        network_map['network_type'] = network_type

        code, xml = self.submit(
            {'ambiente': network_map}, 'POST', 'environment/configuration/save/')

        return self.response(code, xml)

    def configuration_list_all(self, environment_id):
        """
        List all prefix configurations by environment in DB

        :return: Following dictionary:

        ::

            {'lists_configuration': [{
            'id': <id_ipconfig>,
            'subnet': <subnet>,
            'type': <type>,
            'new_prefix': <new_prefix>,
            }, ... ]}


        :raise InvalidValueError: Invalid ID for Environment.
        :raise AmbienteNotFoundError: Environment not registered.
        :raise DataBaseError: Failed into networkapi access data base.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        data = dict()
        data["environment_id"] = environment_id

        url = ("environment/configuration/list/%(environment_id)s/" % data)

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml, force_list=['lists_configuration'])

    def configuration_remove(self, environment_id, configuration_id):
        """
        Remove Prefix Configuration

        :return: None

        :raise InvalidValueError: Invalid Id for Environment or IpConfig.
        :raise IPConfigNotFoundError: Ipconfig not resgistred.
        :raise AmbienteNotFoundError: Environment not registered.
        :raise DataBaseError: Failed into networkapi access data base.
        :raise XMLError: Networkapi failed to generate the XML response.

        """

        data = dict()

        data["configuration_id"] = configuration_id
        data["environment_id"] = environment_id

        url = (
            "environment/configuration/remove/%(environment_id)s/%(configuration_id)s/" %
            data)

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def associate(self, environment_id, environment_vip_id):

        """Associate a news Environment on Environment VIP and returns its identifier.

        :param environment_id: Identifier of the Environment. Integer value and greater than zero.
        :param environment_vip_id: Identifier of the Environment VIP. Integer value and greater than zero.

        :return: Following dictionary:

        ::

            {'environment_environment_vip': {'id': < id >}}

        :raise InvalidParameterError: The value of environment_id or environment_vip_id is invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        if not is_valid_int_param(environment_id):
            raise InvalidParameterError(
                u'The identifier of Environment VIP is invalid or was not informed.')

        if not is_valid_int_param(environment_vip_id):
            raise InvalidParameterError(
                u'The identifier of Environment is invalid or was not informed.')

        environment_environment_vip_map = dict()
        environment_environment_vip_map['environment_id'] = environment_id
        environment_environment_vip_map['environment_vip_id'] = environment_vip_id

        url = 'environment/{}/environmentvip/{}/'.format(environment_id, environment_vip_id)

        code, xml = self.submit(None, 'PUT', url)

        return self.response(code, xml)

    def disassociate(self, environment_id, environment_vip_id):
        """Remove a relationship of Environment with EnvironmentVip.

        :param environment_id: Identifier of the Environment. Integer value and greater than zero.
        :param environment_vip_id: Identifier of the Environment VIP. Integer value and greater than zero.

        :return: Nothing

        :raise InvalidParameterError: Environment/Environment VIP identifier is null and/or invalid.
        :raise EnvironmentNotFoundError: Environment not registered.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise EnvironmentError: Option vip is not associated with the environment vip
        :raise UserNotAuthorizedError: User does not have authorization to make this association.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(environment_id):
            raise InvalidParameterError(
                u'The identifier of Environment VIP is invalid or was not informed.')

        if not is_valid_int_param(environment_vip_id):
            raise InvalidParameterError(
                u'The identifier of Environment is invalid or was not informed.')

        environment_environment_vip_map = dict()
        environment_environment_vip_map['environment_id'] = environment_id
        environment_environment_vip_map['environment_vip_id'] = environment_vip_id

        url = 'environment/{}/environmentvip/{}/'.format(environment_id, environment_vip_id)

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def get_related_environment_list(self, environment_vip_id):
        """Get all Environment by Environment Vip.

        :return: Following dictionary:

        ::

            {'ambiente': [{ 'id': <id_environment>,
            'grupo_l3': <id_group_l3>,
            'grupo_l3_name': <name_group_l3>,
            'ambiente_logico': <id_logical_environment>,
            'ambiente_logico_name': <name_ambiente_logico>,
            'divisao_dc': <id_dc_division>,
            'divisao_dc_name': <name_divisao_dc>,
            'filter': <id_filter>,
            'filter_name': <filter_name>,
            'link': <link> }, ... ]}


        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise DataBaseError: Can't connect to networkapi database.
        :raise XMLError: Failed to generate the XML response.
        """

        url = 'environment/environmentvip/{}/'.format(environment_vip_id)

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml, ['environment_related_list'])