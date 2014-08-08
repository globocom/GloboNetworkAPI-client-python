# -*- coding:utf-8 -*-

'''
Title: Infrastructure NetworkAPI
Author: globo.com / TQI
Copyright: ( c )  2009 globo.com todos os direitos reservados.
'''

from networkapiclient.GenericClient import GenericClient
from networkapiclient.EspecificacaoGrupoVirtual import EspecificacaoGrupoVirtual


class GrupoVirtual(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            GrupoVirtual,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def provisionar(self, equipamentos, vips):
        """Realiza a inserção ou alteração de um grupo virtual para o sistema de Orquestração de VM.

        :param equipamentos: Lista de equipamentos gerada pelo método "add_equipamento" da
          classe "EspecificacaoGrupoVirtual".
        :param vips: Lista de VIPs gerada pelo método "add_vip" da classe "EspecificacaoGrupoVirtual".

        :return: Retorno da operação de inserir ou alterar um grupo virtual:

        ::

          {'equipamentos': {'equipamento': [{'id': < id>,
          'nome': < nome>,
          'ip':  {'id': < id>,
          'id_vlan': < id_vlan>,
          'oct4': < oct4>,
          'oct3': < oct3>,
          'oct2': < oct2>,
          'oct1': < oct1>,
          'descricao': < descricao>},
          'vips': {'vip': [{'id': < id>,
          'ip': {'id': < id>,
          'id_vlan': < id_vlan>,
          'oct4': < oct4>,
          'oct3': < oct3>,
          'oct2': < oct2>,
          'oct1': < oct1>,
          'descricao': < descricao>}}, ... demais vips ...]}}, ... demais equipamentos...]},
          'vips': {'vip': [{'id': < id>,
          'ip': {'id': < id>,
          'id_vlan': < id_vlan>,
          'oct4': < oct4>,
          'oct3': < oct3>,
          'oct2': < oct2>,
          'oct1': < oct1>,
          'descricao': < descricao>},
          'requisicao_vip': {'id': < id>}}, ... demais vips...]}}

          {'equipamentos': {'equipamento': [{'id': < id>,
          'nome': < nome>,
          'ip': {'id': < id>,
          'id_vlan': < id_vlan>,
          'oct4': < oct4>,
          'oct3': < oct3>,
          'oct2': < oct2>,
          'oct1': < oct1>,
          'descricao': < descricao>},
          'vips': {'vip': [{'id': < id>,
          'ip': {'id': < id>,
          'id_vlan': < id_vlan>,
          'oct4': < oct4>,
          'oct3': < oct3>,
          'oct2': < oct2>,
          'oct1': < oct1>,
          'descricao': < descricao>}}, ... demais vips ...]}}, ... demais equipamentos...]},
          'vips': {'vip': [{'id': < id>,
          'requisicao_vip': {'id': < id>}}, ... demais vips...]}}

        :raise InvalidParameterError: Algum dado obrigatório não foi informado nas listas ou possui um valor inválido.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise VlanNaoExisteError: VLAN não cadastrada.
        :raise EquipamentoNaoExisteError: Equipamento não cadastrado.
        :raise IPNaoDisponivelError: Não existe IP disponível para a VLAN informada.
        :raise TipoEquipamentoNaoExisteError: Tipo de equipamento não cadastrado.
        :raise ModeloEquipamentoNaoExisteError: Modelo do equipamento não cadastrado.
        :raise GrupoEquipamentoNaoExisteError: Grupo de equipamentos não cadastrado.
        :raise EquipamentoError: Equipamento com o nome duplicado ou
          Equipamento do grupo “Equipamentos Orquestração” somente poderá ser
          criado com tipo igual a “Servidor Virtual".
        :raise IpNaoExisteError: IP não cadastrado.
        :raise IpError: IP já está associado ao equipamento.
        :raise VipNaoExisteError: Requisição de VIP não cadastrada.
        :raise HealthCheckExpectNaoExisteError: Healthcheck_expect não cadastrado.
        """
        code, map = self.submit(
            {
                'equipamentos': {
                    'equipamento': equipamentos}, 'vips': {
                    'vip': vips}}, 'POST', 'grupovirtual/')
        return self.response(code, map, force_list=['equipamento', 'vip'])

    def remover_provisionamento(self, equipamentos, vips):
        """Remove o provisionamento de um grupo virtual para o sistema de Orquestração VM.

        :param equipamentos: Lista de equipamentos gerada pelo método "add_equipamento_remove" da
          classe "EspecificacaoGrupoVirtual".
        :param vips: Lista de VIPs gerada pelo método "add_vip_remove" da classe "EspecificacaoGrupoVirtual".

        :return: None

        :raise InvalidParameterError: Algum dado obrigatório não foi informado nas listas ou possui um valor inválido.
        :raise IpNaoExisteError: IP não cadastrado.
        :raise EquipamentoNaoExisteError: Equipamento não cadastrado.
        :raise IpError: IP não está associado ao equipamento.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """

        code, map = self.submit({'equipamentos': {'equipamento': equipamentos}, 'vips': {
                                'vip': vips}}, 'DELETE', 'grupovirtual/')

        return self.response(code, map)
