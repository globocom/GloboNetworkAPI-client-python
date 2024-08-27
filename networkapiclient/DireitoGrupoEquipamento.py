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


class DireitoGrupoEquipamento(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            DireitoGrupoEquipamento,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def listar(self):
        """Lista todos os direitos de grupos de usuário em grupos de equipamento.

        :return: Dicionário com a seguinte estrutura:

        ::

            {'direito_grupo_equipamento':
            [{'id_grupo_equipamento': < id_grupo_equipamento >,
            'exclusao': < exclusao >,
            'alterar_config': < alterar_config >,
            'nome_grupo_equipamento': < nome_grupo_equipamento >,
            'id_grupo_usuario': < id_grupo_usuario >,
            'escrita': < escrita >,
            'nome_grupo_usuario': < nome_grupo_usuario >,
            'id': < id >,
            'leitura': < leitura >}, … demais direitos …]}

        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """
        code, map = self.submit(None, 'GET', 'direitosgrupoequipamento/')

        key = 'direito_grupo_equipamento'
        return get_list_map(self.response(code, map, [key]), key)

    def listar_por_grupo_usuario(self, id_grupo_usuario):
        """Lista todos os direitos de um grupo de usuário em grupos de equipamento.

        :param id_grupo_usuario: Identificador do grupo de usuário para filtrar a pesquisa.

        :return: Dicionário com a seguinte estrutura:

        ::

            {'direito_grupo_equipamento':
            [{'id_grupo_equipamento': < id_grupo_equipamento >,
            'exclusao': < exclusao >,
            'alterar_config': < alterar_config >,
            'nome_grupo_equipamento': < nome_grupo_equipamento >,
            'id_grupo_usuario': < id_grupo_usuario >,
            'escrita': < escrita >,
            'nome_grupo_usuario': < nome_grupo_usuario >,
            'id': < id >,
            'leitura': < leitura >}, … demais direitos …]}

        :raise InvalidParameterError: O identificador do grupo de usuário é nulo ou inválido.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """
        if not is_valid_int_param(id_grupo_usuario):
            raise InvalidParameterError(
                'O identificador do grupo de usuário é inválido ou não foi informado.')

        url = 'direitosgrupoequipamento/ugrupo/' + str(id_grupo_usuario) + '/'

        code, map = self.submit(None, 'GET', url)

        key = 'direito_grupo_equipamento'
        return get_list_map(self.response(code, map, [key]), key)

    def listar_por_grupo_equipamento(self, id_grupo_equipamento):
        """Lista todos os direitos de grupos de usuário em um grupo de equipamento.

        :param id_grupo_equipamento: Identificador do grupo de equipamento para filtrar a pesquisa.

        :return: Dicionário com a seguinte estrutura:

        ::

            {'direito_grupo_equipamento':
            [{'id_grupo_equipamento': < id_grupo_equipamento >,
            'exclusao': < exclusao >,
            'alterar_config': < alterar_config >,
            'nome_grupo_equipamento': < nome_grupo_equipamento >,
            'id_grupo_usuario': < id_grupo_usuario >,
            'escrita': < escrita >,
            'nome_grupo_usuario': < nome_grupo_usuario >,
            'id': < id >,
            'leitura': < leitura >}, … demais direitos …]}

        :raise InvalidParameterError: O identificador do grupo de equipamento é nulo ou inválido.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """
        if not is_valid_int_param(id_grupo_equipamento):
            raise InvalidParameterError(
                'O identificador do grupo de equipamento é inválido ou não foi informado.')

        url = 'direitosgrupoequipamento/egrupo/' + \
            str(id_grupo_equipamento) + '/'

        code, map = self.submit(None, 'GET', url)

        key = 'direito_grupo_equipamento'
        return get_list_map(self.response(code, map, [key]), key)

    def buscar_por_id(self, id_direito):
        """Obtém os direitos de um grupo de usuário e um grupo de equipamento.

        :param id_direito: Identificador do direito grupo equipamento.

        :return: Dicionário com a seguinte estrutura:

        ::

            {'direito_grupo_equipamento':
            {'id_grupo_equipamento': < id_grupo_equipamento >,
            'exclusao': < exclusao >,
            'alterar_config': < alterar_config >,
            'nome_grupo_equipamento': < nome_grupo_equipamento >,
            'id_grupo_usuario': < id_grupo_usuario >,
            'escrita': < escrita >,
            'nome_grupo_usuario': < nome_grupo_usuario >,
            'id': < id >,
            'leitura': < leitura >}}

        :raise InvalidParameterError: O identificador do direito grupo equipamento é nulo ou inválido.
        :raise DireitoGrupoEquipamentoNaoExisteError: Direito Grupo Equipamento não cadastrado.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """
        if not is_valid_int_param(id_direito):
            raise InvalidParameterError(
                'O identificador do direito grupo equipamento é inválido ou não foi informado.')

        url = 'direitosgrupoequipamento/' + str(id_direito) + '/'

        code, map = self.submit(None, 'GET', url)

        return self.response(code, map)

    def inserir(
            self,
            id_grupo_usuario,
            id_grupo_equipamento,
            leitura,
            escrita,
            alterar_config,
            exclusao):
        """Cria um novo direito de um grupo de usuário em um grupo de equipamento e retorna o seu identificador.

        :param id_grupo_usuario: Identificador do grupo de usuário.
        :param id_grupo_equipamento: Identificador do grupo de equipamento.
        :param leitura: Indicação de permissão de leitura ('0' ou '1').
        :param escrita: Indicação de permissão de escrita ('0' ou '1').
        :param alterar_config: Indicação de permissão de alterar_config ('0' ou '1').
        :param exclusao: Indicação de permissão de exclusão ('0' ou '1').

        :return: Dicionário com a seguinte estrutura: {'direito_grupo_equipamento': {'id': < id>}}

        :raise InvalidParameterError: Pelo menos um dos parâmetros é nulo ou inválido.
        :raise GrupoEquipamentoNaoExisteError: Grupo de Equipamento não cadastrado.
        :raise GrupoUsuarioNaoExisteError: Grupo de Usuário não cadastrado.
        :raise ValorIndicacaoDireitoInvalidoError: Valor de leitura, escrita, alterar_config e/ou exclusão inválido.
        :raise DireitoGrupoEquipamentoDuplicadoError: Já existe direitos cadastrados para o grupo de usuário e grupo
            de equipamento informados.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """
        direito_map = dict()
        direito_map['id_grupo_usuario'] = id_grupo_usuario
        direito_map['id_grupo_equipamento'] = id_grupo_equipamento
        direito_map['leitura'] = leitura
        direito_map['escrita'] = escrita
        direito_map['alterar_config'] = alterar_config
        direito_map['exclusao'] = exclusao

        code, xml = self.submit(
            {'direito_grupo_equipamento': direito_map}, 'POST', 'direitosgrupoequipamento/')

        return self.response(code, xml)

    def alterar(self, id_direito, leitura, escrita, alterar_config, exclusao):
        """Altera os direitos de um grupo de usuário em um grupo de equipamento a partir do seu identificador.

        :param id_direito: Identificador do direito grupo equipamento.
        :param leitura: Indicação de permissão de leitura ('0' ou '1').
        :param escrita: Indicação de permissão de escrita ('0' ou '1').
        :param alterar_config: Indicação de permissão de alterar_config ('0' ou '1').
        :param exclusao: Indicação de permissão de exclusão ('0' ou '1').

        :return: None

        :raise InvalidParameterError: Pelo menos um dos parâmetros é nulo ou inválido.
        :raise ValorIndicacaoDireitoInvalidoError: Valor de leitura, escrita, alterar_config e/ou exclusão inválido.
        :raise DireitoGrupoEquipamentoNaoExisteError: Direito Grupo Equipamento não cadastrado.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao ler o XML de requisição ou gerar o XML de resposta.
        """
        if not is_valid_int_param(id_direito):
            raise InvalidParameterError(
                'O identificador do direito grupo equipamento é inválido ou não foi informado.')

        url = 'direitosgrupoequipamento/' + str(id_direito) + '/'

        direito_map = dict()
        direito_map['leitura'] = leitura
        direito_map['escrita'] = escrita
        direito_map['alterar_config'] = alterar_config
        direito_map['exclusao'] = exclusao

        code, xml = self.submit(
            {'direito_grupo_equipamento': direito_map}, 'PUT', url)

        return self.response(code, xml)

    def remover(self, id_direito):
        """Remove os direitos de um grupo de usuário em um grupo de equipamento a partir do seu identificador.

        :param id_direito: Identificador do direito grupo equipamento

        :return: None

        :raise DireitoGrupoEquipamentoNaoExisteError: Direito Grupo Equipamento não cadastrado.
        :raise InvalidParameterError: O identificador do direito grupo equipamento é nulo ou inválido.
        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        :raise XMLError: Falha na networkapi ao gerar o XML de resposta.
        """
        if not is_valid_int_param(id_direito):
            raise InvalidParameterError(
                'O identificador do direito grupo equipamento é inválido ou não foi informado.')

        url = 'direitosgrupoequipamento/' + str(id_direito) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)
