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
from networkapiclient.Config import IP_VERSION
from networkapiclient.Pagination import Pagination


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
#        vip_map['metodo_bal'] = method_bal
        vip_map['reals'] = {'real': reals}
        vip_map['reals_prioritys'] = {'reals_priority': reals_prioritys}
        vip_map['reals_weights'] = {'reals_weight': reals_weights}
        vip_map['alter_priority'] = alter_priority

        url = 'vip/real/edit/'

        code, xml = self.submit({'vip': vip_map}, 'PUT', url)

        return self.response(code, xml)

    def alterar(
            self,
            id_vip,
            id_ip,
            id_healthcheck_expect,
            validado,
            vip_criado,
            finalidade,
            cliente,
            ambiente,
            cache,
            metodo_bal,
            persistencia,
            healthcheck_type,
            healthcheck,
            timeout,
            host,
            maxcon,
            dsr,
            bal_ativo,
            transbordos,
            reals,
            portas_servicos):
        """Altera uma requisição de VIP a partir do seu identificador.

        :param id_vip: Identificador da requisição de VIP.
        :param id_ip: Identificador do IP.
        :param id_healthcheck_expect: Identificador healthcheck expect.
        :param validado: Indicação de VIP Validado ('0' ou '1').
        :param vip_criado: Indicação de Vip criado ('0' ou '1').
        :param finalidade: Finalidade.
        :param cliente: Cliente.
        :param ambiente: Ambiente.
        :param cache: Cache.
        :param metodo_bal: Método de balanceamento.
        :param persistencia: Persistência.
        :param healthcheck_type: Tipo de healthcheck.
        :param healthcheck: Healthcheck.
        :param timeout: Timeout.
        :param host: Host.
        :param maxcon: Número máximo de conexões.
        :param dsr: DSR.
        :param bal_ativo: Balanceador ativo.
        :param transbordos: Lista com os IPs dos servidores de transbordo. Ex: ['10.10.100.1','192.168.1.1'].
        :param reals: Lista de reals. Ex: [{'real_name':'Teste1', 'real_ip':'10.10.10.1'},{'real_name':'Teste2', 'real_ip':'10.10.10.2'}]
        :param portas_servicos: Lista das portas.
               Para Update de Portas Adicionar Id do ServerPool,
               Para Novos Omitir a Chave que Representa o Id do Server Poll.
               Ex: s[{'port':'80', 'server_pool_id': 3358}, {'port':'8080'},{'port':'445'}].

        :return: None

        :raise VipError: Não é permitido alterar o IP de uma requisição de VIP já criada.
        :raise InvalidParameterError: Identificador do IP e/ou da requisição de VIP é nulo ou inválido.
        :raise InvalidParameterError: O valor de finalidade, cliente, ambiente, cache, metodo_bal, persistencia,
            healthcheck_type, healthcheck, timeout, host, maxcon, dsr, bal_ativo, transbordos, reals ou portas é inválido.
        :raise IpNaoExisteError: IP não cadastrado.
        :raise HealthCheckExpectNaoExisteError: Healthcheck_expect não cadastrado.
        :raise VipNaoExisteError: Requisição de VIP não cadastrada.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """
        if not is_valid_int_param(id_vip):
            raise InvalidParameterError(
                u'O identificador do vip é inválido ou não foi informado.')

        vip_map = dict()
        vip_map['id_ip'] = id_ip
        vip_map['id_healthcheck_expect'] = id_healthcheck_expect
        vip_map['validado'] = validado
        vip_map['vip_criado'] = vip_criado
        vip_map['finalidade'] = finalidade
        vip_map['cliente'] = cliente
        vip_map['ambiente'] = ambiente
        vip_map['cache'] = cache
        vip_map['maxcon'] = maxcon
        vip_map['metodo_bal'] = metodo_bal
        vip_map['persistencia'] = persistencia
        vip_map['healthcheck_type'] = healthcheck_type
        vip_map['healthcheck'] = healthcheck
        vip_map['timeout'] = timeout
        vip_map['host'] = host
        vip_map['dsr'] = dsr
        vip_map['bal_ativo'] = bal_ativo
        vip_map['transbordos'] = {'transbordo': transbordos}
        vip_map['reals'] = {'real': reals}
        vip_map['portas_servicos'] = {'porta': portas_servicos}

        url = 'vip/' + str(id_vip) + '/'

        code, xml = self.submit({'vip': vip_map}, 'PUT', url)

        return self.response(code, xml)

    def buscar(self, id_vip):
        """Obtém uma requisição de VIP a partir do seu identificador.

        :param id_vip: Identificador da requisição de VIP.

        :return: Dicionário com a seguinte estrutura:

        ::

            {‘vip’: {‘id’: < id >,
            ‘validado’: < validado >,
            ‘finalidade’: < finalidade >,
            ‘cliente’: < cliente >,
            ‘ambiente’: < ambiente >,
            ‘cache’: < cache >,
            ‘metodo_bal’: < método_bal >,
            ‘persistencia’: < persistencia >,
            ‘healthcheck_type’: <  healthcheck_type >,
            ‘healthcheck’: < healthcheck >,
            ‘timeout’: < timeout >,
            ‘host’: < host >,
            ‘maxcon’: < maxcon >,
            ‘dsr’: < dsr >,
            ‘bal_ativo’: < bal_ativo >,
            ‘transbordos’:{‘transbordo’:[< transbordo >, ... demais transbordos...]},
            ‘reals’:{‘real’:[{‘real_name’:< real_name >, ‘real_ip’:< real_ip >}, …demais reals …]},
            ‘portas_servicos’:{‘porta’:[< porta >, … demais portas …]},
            ‘vip_criado’: < vip_criado >,
            ‘id_ip’: < id_ip >,
            ‘id_ipv6’: < id_ipv6 >,
            ‘id_healthcheck_expect’: < id_healthcheck_expect >}}

        :raise VipNaoExisteError: Requisição de VIP não cadastrada.
        :raise InvalidParameterError: O identificador da requisição de VIP é nulo ou inválido.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """
        if not is_valid_int_param(id_vip):
            raise InvalidParameterError(
                u'O identificador do vip é inválido ou não foi informado.')

        url = 'vip/' + str(id_vip) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml, ['pools', 'server_pool_members'])

    def find_vip_requests(self, id_vip, ip, pagination, create=None):
        """Get VIPs by id or ipv4 or ipv6.

        :return: Dictionary with the following structure:

        ::

            {‘vip’: {‘id’: < id >,
            ‘validado’: < validado >,
            ‘ambiente’: < ambiente >,
            'ip':<ip>,
            'descricao':<descricao>,
            'equipamento':<equipamentos>,
            'criado':<criado>,
            'is_more':<is_more>, ... too vips ... } }

        :raise VipNaoExisteError: No request for registered VIP.
        :raise DataBaseError: Can't connect to networkapi database.
        :raise XMLError: Failed to generate the XML response.
        """

        url = 'requestvip/get_by_ip_id/'

        vip_map = dict()

        vip_map["start_record"] = pagination.start_record
        vip_map["end_record"] = pagination.end_record
        vip_map["asorting_cols"] = pagination.asorting_cols
        vip_map["searchable_columns"] = pagination.searchable_columns
        vip_map["custom_search"] = pagination.custom_search

        vip_map['id_vip'] = id_vip
        vip_map['ip'] = ip
        vip_map['create'] = create

        code, xml = self.submit({'vip': vip_map}, 'POST', url)

        key = "vip"
        return get_list_map(
            self.response(
                code, xml, [
                    "equipments", "environments", "ips"]), key)

    def get_by_id(self, id_vip):
        """Get VIPs by id.

        :return: Dictionary with the following structure:

        ::

            {‘vip’: {‘id’: < id >,
            ‘validado’: < validado >,
            'ips':<list of vip's ip (v4 and/or v6>),
            'descricao':<descricao>,
            'equipamento':<equipamentos>,
            'criado':<criado>,
            'environent':<ambientes>,
            'ipv4_description':<descricao ipv4>,
            'ipv6_description':<descricao ipv6>,
            'variaveis':<variaveis>,
            ‘id_healthcheck_expect’: < id_healthcheck_expect >,
            ‘cache’: < cache >, } }

        :raise VipNaoExisteError: No request for registered VIP.
        :raise DataBaseError: Can't connect to networkapi database.
        :raise XMLError: Failed to generate the XML response.
        """

        url = 'requestvip/getbyid/' + str(id_vip) + '/'

        code, xml = self.submit(None, 'GET', url)

        key = "vip"
        return get_list_map(
            self.response(
                code, xml, [
                    "equipamento", "ips"]), key)

    def get_all(self):
        """Get all VIPs.

        :return: Dictionary with the following structure:

        ::

            {‘vip_< id >’: {‘id’: < id >,
            ‘validado’: < validado >,
            ‘finalidade’: < finalidade >,
            ‘cliente’: < cliente >,
            ‘ambiente’: < ambiente >,
            ‘cache’: < cache >,
            ‘metodo_bal’: < método_bal >,
            ‘persistencia’: < persistencia >,
            ‘healthcheck_type’: <  healthcheck_type >,
            ‘healthcheck’: < healthcheck >,
            ‘timeout’: < timeout >,
            ‘host’: < host >,
            ‘maxcon’: < maxcon >,
            ‘dsr’: < dsr >,
            ‘bal_ativo’: < bal_ativo >,
            ‘transbordos’:{‘transbordo’:[< transbordo >, ... too transbordos ...]},
            ‘reals’:{‘real’:[{‘real_name’:< real_name >, ‘real_ip’:< real_ip >}, ... too reals ...]},
            ‘portas_servicos’:{‘porta’:[< porta >, ... too portas ...]},
            ‘vip_criado’: < vip_criado >,
            ‘id_ip’: < id_ip >,
            ‘id_ipv6’: < id_ipv6 >,
            ‘id_healthcheck_expect’: < id_healthcheck_expect >} ... too vips ... }

        :raise VipNaoExisteError: No request for registered VIP.
        :raise DataBaseError: Can't connect to networkapi database.
        :raise XMLError: Failed to generate the XML response.
        """

        url = 'vip/all/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def get_by_ipv4(self, ipv4, all_prop=0):
        """Get VIPs related to ipv4

        :param ipv4: The IPv4 to find all VIPs ralated
        :param all_prop: (Optional) Gets all properties, not only ids. (0 or 1)

        :return: Dictionary with the following structure:

        ::

            {'ips': [ {'vips': '[< id >, < id >]', 'oct4': < oct4 >, 'oct2': < oct2 >,
            'oct3': < oct3 >, 'oct1': < oct1 >, 'networkipv4': < networkipv4 >,
            'id': <id >, 'descricao': < descricao >}, ... ] }

        :raise VipNaoExisteError: No request for registered VIP.
        :raise DataBaseError: Can't connect to networkapi database.
        :raise XMLError: Failed to generate the XML response.
        """

        url = 'vip/ipv4/all/'

        vip_map = dict()
        vip_map['ipv4'] = ipv4
        vip_map['all_prop'] = all_prop

        code, xml = self.submit({'vip': vip_map}, 'POST', url)

        return self.response(code, xml, ['vips'])

    def get_by_ipv6(self, ipv6, all_prop=0):
        """Get VIPs related to ipv6

        :param ipv6: The IPv6 to find all VIPs related
        :param all_prop: (Optional) Gets all properties, not only ids. (0 or 1)

        :return: Dictionary with the following structure:

        ::

            {'ips': [ {'vips': '[< id >, < id >]', 'block4': < block4 >, 'block2': < block2 >,
            'block3': < block3 >, 'block1': < block1 >, 'block5': < block5 >,
            'block6': < block6 >, 'block7': < block7 >, 'block8': < block8 >,
            'networkipv6': < networkipv6 >, 'id': <id >, 'descricao': < descricao >}, ... ] }

        :raise VipNaoExisteError: No request for registered VIP.
        :raise DataBaseError: Can't connect to networkapi database.
        :raise XMLError: Failed to generate the XML response.
        """

        url = 'vip/ipv6/all/'

        vip_map = dict()
        vip_map['ipv6'] = ipv6
        vip_map['all_prop'] = all_prop

        code, xml = self.submit({'vip': vip_map}, 'POST', url)

        return self.response(code, xml)

    def add_block(self, id_vip, id_block, override):
        """ Add block in vip rule

        :param id_vip: Vip request id
        :param id_block: Block id
        :param override: 0 or 1 (1 if override filter to apply, 0 if only create new rule with the new block)

        :return: Dictionary with the following structure:

        ::

            {'sucesso': {'codigo': < code >, 'descricao': < descricao >}}

        :raise VipRequestBlockAlreadyInRule: Block is already in rule.
        :raise VipRequestNoBlockInRule: Rule don't have any block associated.
        :raise InvalidParameterError: Invalid param
        :raise UserNotAuthorizedError: User dont have permition.
        :raise VipNaoExisteError: No request for registered VIP.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        url = 'vip/add_block/' + \
            str(id_vip) + '/' + str(id_block) + '/' + str(override)

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)


if __name__ == '__main__':
    vip_cli = Vip('http://127.0.0.1:8080/', 'henrique', '12345678')
    print vip_cli.buscar(6628)