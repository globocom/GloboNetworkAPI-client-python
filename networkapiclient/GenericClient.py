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

from networkapiclient.rest import RestRequest, RestError
from networkapiclient.exception import ErrorHandler
from networkapiclient.xml_utils import loads


class GenericClient(object):

    """Class inherited by all NetworkAPI-Client classes who implements access methods to networkAPI."""

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

    def get_url(self, postfix):
        """Constroe e retorna a URL completa para acesso à networkAPI.

        :param postfix: Posfixo a ser colocado na URL básica. Ex: /ambiente

        :return: URL completa.
        """
        return self.networkapi_url + postfix

    def submit(self, map, method, postfix):
        '''Realiza um requisição HTTP para a networkAPI.

        :param map: Dicionário com os dados para gerar o XML enviado no corpo da requisição HTTP.
        :param method: Método da requisição HTTP ('GET', 'POST', 'PUT' ou 'DELETE').
        :param postfix: Posfixo a ser colocado na URL básica de acesso à networkAPI. Ex: /ambiente

        :return: Tupla com o código e o corpo da resposta HTTP:
            (< codigo>, < descricao>)

        :raise NetworkAPIClientError: Erro durante a chamada HTTP para acesso à networkAPI.
        '''
        try:
            rest_request = RestRequest(
                self.get_url(postfix),
                method,
                self.user,
                self.password,
                self.user_ldap)
            return rest_request.submit(map)
        except RestError as e:
            raise ErrorHandler.handle(None, str(e))

    def get_error(self, xml):
        '''Obtem do XML de resposta, o código e a descrição do erro.

        O XML corresponde ao corpo da resposta HTTP de código 500.

        :param xml: XML contido na resposta da requisição HTTP.

        :return: Tupla com o código e a descrição do erro contido no XML:
            (< codigo_erro>, < descricao_erro>)
        '''
        map = loads(xml)
        network_map = map['networkapi']
        error_map = network_map['erro']
        return int(error_map['codigo']), str(error_map['descricao'])

    def response(self, code, xml, force_list=None):
        """Cria um dicionário com os dados de retorno da requisição HTTP ou
            lança uma exceção correspondente ao erro ocorrido.

        Se a requisição HTTP retornar o código 200 então este método retorna o
            dicionário com os dados da resposta.
        Se a requisição HTTP retornar um código diferente de 200 então este método
            lança uma exceção correspondente ao erro.

        Todas as exceções lançadas por este método deverão herdar de NetworkAPIClientError.

        :param code: Código de retorno da requisição HTTP.
        :param xml: XML ou descrição (corpo) da resposta HTTP.
        :param force_list: Lista com as tags do XML de resposta que deverão ser transformadas
            obrigatoriamente em uma lista no dicionário de resposta.

        :return: Dicionário com os dados da resposta HTTP retornada pela networkAPI.
        """
        if int(code) == 200:
            # Retorna o map
            return loads(xml, force_list)['networkapi']
        elif int(code) == 500:
            code, description = self.get_error(xml)
            return ErrorHandler.handle(code, description)
        else:
            return ErrorHandler.handle(code, xml)
