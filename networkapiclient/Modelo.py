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


class Modelo(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(Modelo, self).__init__(networkapi_url, user, password, user_ldap)

    def listar_por_marca(self, id_brand):
        """List all Model by Brand.

        :param id_brand: Identifier of the Brand. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            {‘model’: [{‘id’: < id >,
            ‘nome’: < nome >,
            ‘id_marca’: < id_marca >}, ... too Model ...]}

        :raise InvalidParameterError: The identifier of Brand is null and invalid.
        :raise MarcaNaoExisteError: Brand not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response
        """

        if not is_valid_int_param(id_brand):
            raise InvalidParameterError(
                'The identifier of Brand is invalid or was not informed.')

        url = 'model/brand/' + str(id_brand) + '/'

        code, map = self.submit(None, 'GET', url)

        key = 'model'
        return get_list_map(self.response(code, map, [key]), key)

    def get_by_script_id(self, script_id):

        if not is_valid_int_param(script_id):
            raise InvalidParameterError(
                'The identifier of Script is invalid or was not informed.')

        url = 'model/script/' + str(script_id) + '/'

        code, map = self.submit(None, 'GET', url)

        key = 'model'
        return get_list_map(self.response(code, map, [key]), key)

    def listar(self):
        """List all Model.

        :return: Dictionary with the following structure:

        ::

            {‘model’: [{‘id’: < id >,
            ‘nome’:< nome >,
            ‘id_marca’:< id_marca >,
            ‘nome_marca’:< nome_marca >}, ... too Model ... ]}

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response
        """
        code, map = self.submit(None, 'GET', 'model/all/')

        key = 'model'
        return get_list_map(self.response(code, map, [key]), key)

    def inserir(self, id_brand, name):
        """Inserts a new Model and returns its identifier

        :param id_brand: Identifier of the Brand. Integer value and greater than zero.
        :param name: Model name. String with a minimum 3 and maximum of 100 characters

        :return: Dictionary with the following structure:

        ::

            {'model': {'id': < id_model >}}

        :raise InvalidParameterError: The identifier of Brand or name is null and invalid.
        :raise NomeMarcaModeloDuplicadoError: There is already a registered Model with the value of name and brand.
        :raise MarcaNaoExisteError: Brand not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response
        """
        model_map = dict()
        model_map['name'] = name
        model_map['id_brand'] = id_brand

        code, xml = self.submit({'model': model_map}, 'POST', 'model/')

        return self.response(code, xml)

    def alterar(self, id_model, id_brand, name):
        """Change Model from by the identifier.

        :param id_model: Identifier of the Model. Integer value and greater than zero.
        :param id_brand: Identifier of the Brand. Integer value and greater than zero.
        :param name: Model name. String with a minimum 3 and maximum of 100 characters

        :return: None

        :raise InvalidParameterError: The identifier of Model, Brand or name is null and invalid.
        :raise MarcaNaoExisteError: Brand not registered.
        :raise ModeloEquipamentoNaoExisteError: Model not registered.
        :raise NomeMarcaModeloDuplicadoError: There is already a registered Model with the value of name and brand.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response
        """

        if not is_valid_int_param(id_model):
            raise InvalidParameterError(
                'The identifier of Model is invalid or was not informed.')

        model_map = dict()
        model_map['name'] = name
        model_map['id_brand'] = id_brand

        url = 'model/' + str(id_model) + '/'

        code, xml = self.submit({'model': model_map}, 'PUT', url)

        return self.response(code, xml)

    def remover(self, id_model):
        """Remove Model from by the identifier.

        :param id_model: Identifier of the Model. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: The identifier of Model is null and invalid.
        :raise ModeloEquipamentoNaoExisteError: Model not registered.
        :raise ModeloEquipamentoError: The Model is associated with a equipment.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response
        """

        if not is_valid_int_param(id_model):
            raise InvalidParameterError(
                'The identifier of Model is invalid or was not informed.')

        url = 'model/' + str(id_model) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)
