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


class GrupoEquipamento(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            GrupoEquipamento,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def search(self, id_egroup):
        """Search Group Equipament from by the identifier.

        :param id_egroup: Identifier of the Group Equipament. Integer value and greater than zero.

        :return: Following dictionary:

        ::

            {‘group_equipament’:  {‘id’: < id_egrupo >,
            ‘nome’: < nome >} }

        :raise InvalidParameterError: Group Equipament identifier is null and invalid.
        :raise GrupoEquipamentoNaoExisteError: Group Equipament not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_egroup):
            raise InvalidParameterError(
                u'The identifier of Group Equipament is invalid or was not informed.')

        url = 'egroup/' + str(id_egroup) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def listar(self):
        """Lista todos os grupos de equipamentos.

        :return: Dicionário com a seguinte estrutura:

        ::

            {'grupo':
            [{'id': < id >,
            'nome': < nome >},
            ... demais grupos ...]}

        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """
        code, map = self.submit(None, 'GET', 'egrupo/')

        key = 'grupo'
        return get_list_map(self.response(code, map, [key]), key)

    def listar_por_equip(self, equip_id):
        """Lista todos os grupos de equipamentos por equipamento especifico.

        :return: Dicionário com a seguinte estrutura:

        ::

            {'grupo':  [{'id': < id >,
            'nome': < nome >},
            ... demais grupos ...]}

        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """

        if equip_id is None:
            raise InvalidParameterError(
                u'O id do equipamento não foi informado.')

        url = 'egrupo/equip/' + str(equip_id) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def inserir(self, nome):
        """Insere um novo grupo de equipamento e retorna o seu identificador.

        :param nome: Nome do grupo de equipamento.

        :return: Dicionário com a seguinte estrutura: {'grupo': {'id': < id >}}

        :raise InvalidParameterError: Nome do grupo é nulo ou vazio.
        :raise NomeGrupoEquipamentoDuplicadoError: Nome do grupo de equipmaneto duplicado.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """
        egrupo_map = dict()
        egrupo_map['nome'] = nome

        code, xml = self.submit({'grupo': egrupo_map}, 'POST', 'egrupo/')

        return self.response(code, xml)

    def alterar(self, id_egrupo, nome):
        """Altera os dados de um grupo de equipamento a partir do seu identificador.

        :param id_egrupo: Identificador do grupo de equipamento.
        :param nome: Nome do grupo de equipamento.

        :return: None

        :raise InvalidParameterError: O identificador e/ou o nome do grupo são nulos ou inválidos.
        :raise GrupoEquipamentoNaoExisteError: Grupo de equipamento não cadastrado.
        :raise NomeGrupoEquipamentoDuplicadoError: Nome do grupo de equipamento duplicado.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """
        if not is_valid_int_param(id_egrupo):
            raise InvalidParameterError(
                u'O identificador do grupo de equipamento é inválido ou não foi informado.')

        url = 'egrupo/' + str(id_egrupo) + '/'

        egrupo_map = dict()
        egrupo_map['nome'] = nome

        code, xml = self.submit({'grupo': egrupo_map}, 'PUT', url)

        return self.response(code, xml)

    def remover(self, id_egrupo):
        """Remove um grupo de equipamento a partir do seu identificador.

        :param id_egrupo: Identificador do grupo de equipamento.

        :return: None

        :raise GrupoEquipamentoNaoExisteError: Grupo de equipamento não cadastrado.
        :raise InvalidParameterError: O identificador do grupo é nulo ou inválido.
        :raise GroupDontRemoveError:
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """
        if not is_valid_int_param(id_egrupo):
            raise InvalidParameterError(
                u'O identificador do grupo de equipamento é inválido ou não foi informado.')

        url = 'egrupo/' + str(id_egrupo) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def associa_equipamento(self, id_equip, id_grupo_equipamento):
        """Associa um equipamento a um grupo.

        :param id_equip: Identificador do equipamento.
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
        equip_map['id_equipamento'] = id_equip

        code, xml = self.submit(
            {'equipamento_grupo': equip_map}, 'POST', 'equipamentogrupo/associa/')

        return self.response(code, xml)

    def remove(self, id_equipamento, id_egrupo):
        """Remove a associacao de um grupo de equipamento com um equipamento a partir do seu identificador.

        :param id_egrupo: Identificador do grupo de equipamento.
        :param id_equipamento: Identificador do equipamento.

        :return: None

        :raise EquipamentoNaoExisteError: Equipamento não cadastrado.
        :raise GrupoEquipamentoNaoExisteError: Grupo de equipamento não cadastrado.
        :raise InvalidParameterError: O identificador do grupo é nulo ou inválido.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """

        if not is_valid_int_param(id_egrupo):
            raise InvalidParameterError(
                u'O identificador do grupo de equipamento é inválido ou não foi informado.')

        if not is_valid_int_param(id_equipamento):
            raise InvalidParameterError(
                u'O identificador do equipamento é inválido ou não foi informado.')

        url = 'egrupo/equipamento/' + \
            str(id_equipamento) + '/egrupo/' + str(id_egrupo) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)
