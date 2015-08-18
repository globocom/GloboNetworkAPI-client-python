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

from networkapiclient.exception import InvalidParameterError
from networkapiclient.utils import is_valid_int_param
from networkapiclient.ApiGenericClient import ApiGenericClient


class OptionPool(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            OptionPool,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)



    def add(self, tipo_opcao, nome_opcao):
        """Inserts a new Option Pool and returns its identifier.

        :param tipo_opcao: Type. String with a maximum of 50 characters and respect [a-zA-Z\_-]
        :param nome_opcao_txt: Name Option. String with a maximum of 50 characters and respect [a-zA-Z\_-]

        :return: Following dictionary:

        ::

            {'id': < id > , 'type':<type>, 'name':<name>}

        :raise InvalidParameterError: The value of tipo_opcao or nome_opcao_txt is invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        #optionpool_map = dict()
        #optionpool_map['type'] = tipo_opcao
        #optionpool_map['name'] = nome_opcao

        url='api/pools/options/save/'

        return self.post(url, {'type': tipo_opcao, "name":nome_opcao })


    def modify(self, id_option_pool, tipo_opcao, nome_opcao):
        """Change Option Pool from by id.

        :param id_option_pool: Identifier of the Option Pool. Integer value and greater than zero.
        :param tipo_opcao: Type. String with a maximum of 50 characters and respect [a-zA-Z\_-]
        :param nome_opcao_txt: Name Option. String with a maximum of 50 characters and respect [a-zA-Z\_-]

        :return: None

        :raise InvalidParameterError: Option Pool identifier is null or invalid.
        :raise InvalidParameterError: The value of tipo_opcao or nome_opcao_txt is invalid.
        :raise optionpoolNotFoundError: Option pool not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_option_pool):
            raise InvalidParameterError(
                u'The identifier of Option Pool is invalid or was not informed.')

        #optionpool_map = dict()
        #optionpool_map['type'] = tipo_opcao
        #optionpool_map['name'] = nome_opcao_txt

        url = 'api/pools/options/' + str(id_option_pool) + '/'

        return self.put(url,{'type': tipo_opcao, "name":nome_opcao } )

    def remove(self, id_option_pool):
        """Remove Option pool  by  identifier and all Environment related .

        :param id_option_pool: Identifier of the Option Pool. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: Option Pool identifier is null and invalid.
        :raise optionpoolNotFoundError: Option Pool not registered.
        :raise optionpoolError: Option Pool associated with Pool.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_option_pool):
            raise InvalidParameterError(
                u'The identifier of Option Pool is invalid or was not informed.')

        url = 'api/pools/options/' + str(id_option_pool) + '/'

        return self.delete(url)

    def get_option_pool(self, id_option_pool):
        """Search Option Pool by id.

        :param id_option_pool: Identifier of the Option Pool. Integer value and greater than zero.

        :return: Following dictionary:

        ::

            {‘id’: < id_option_pool >,
            ‘type’: < tipo_opcao >,
            ‘name’: < nome_opcao_txt >}

        :raise InvalidParameterError: Option Pool identifier is null and invalid.
        :raise optionpoolNotFoundError: Option Pool not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_option_pool):
            raise InvalidParameterError(
                u'The identifier of Option Pool is invalid or was not informed.')

        url = 'api/pools/options/' + str(id_option_pool) + '/'

        return self.get(url)

    def get_all_option_pool(self, option_type=None):
        """Get all Option Pool.

        :return: Dictionary with the following structure:

        ::

            {[{‘id’: < id >,
            ‘type’: < tipo_opcao >,
            ‘name’: < nome_opcao_txt >}, ... other option pool ...] }

        :raise optionpoolNotFoundError: Option Pool not registered.
        :raise DataBaseError: Can't connect to networkapi database.
        :raise XMLError: Failed to generate the XML response.
        """
        if option_type:
            url = 'api/pools/options/?type='+option_type
        else:
            url = 'api/pools/options/'


        return self.get(url)

    def get_all_environment_option_pool(self, id_environment=None, option_id=None, option_type=None):
        """Get all Option VIP by Environment .

        :return: Dictionary with the following structure:

        ::

            {[{‘id’: < id >,
                option: {
                    'id': <id>
                    'type':<type>
                    'name':<name> }
                environment: {
                    'id':<id>
                    .... all environment info }
                    etc to option pools ...] }

        :raise EnvironmentVipNotFoundError: Environment Pool not registered.
        :raise DataBaseError: Can't connect to networkapi database.
        :raise XMLError: Failed to generate the XML response.
        """
        url='api/pools/environment_options/'

        if id_environment:
            if  option_id:
                if option_type:
                    url = url + "?environment_id=" + str(id_environment)+ "&option_id=" + str(option_id)  + "&option_type=" + option_type
                else:
                    url = url + "?environment_id=" + str(id_environment)+ "&option_id=" + str(option_id)
            else:
                if option_type:
                    url = url + "?environment_id=" + str(id_environment) + "&option_type=" + option_type
                else:
                    url = url + "?environment_id=" + str(id_environment)
        elif option_id:
            if option_type:
                url = url + "?option_id=" + str(option_id)  + "&option_type=" + option_type
            else:
                url = url + "?option_id=" + str(option_id)
        elif option_type:
            url = url + "?option_type=" + option_type


        return self.get(url)


    def associate_environment_option_pool(self, id_option_pool, id_environment):
        """Create a relationship of optionpool with Environment.

        :param id_option_pool: Identifier of the Option Pool. Integer value and greater than zero.
        :param id_environment: Identifier of the Environment . Integer value and greater than zero.
        :return: Dictionary with the following structure:


            {‘id’: < id >,
                option: {
                    'id': <id>
                    'type':<type>
                    'name':<name> }
                environment: {
                    'id':<id>
                    .... all environment info }
                }

        :raise InvalidParameterError: Option Pool/Environment Pool identifier is null and/or invalid.
        :raise optionpoolNotFoundError: Option Pool not registered.
        :raise EnvironmentVipNotFoundError: Environment Pool not registered.
        :raise optionpoolError: Option Pool is already associated with the environment pool.
        :raise UserNotAuthorizedError: User does not have authorization to make this association.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_option_pool):
            raise InvalidParameterError(
                u'The identifier of Option Pool is invalid or was not informed.')

        if not is_valid_int_param(id_environment):
            raise InvalidParameterError(
                u'The identifier of Environment Pool is invalid or was not informed.')



        url= 'api/pools/environment_options/save/'

        return self.post(url,  {'option_id': id_option_pool,"environment_id":id_environment })


    def get_environment_option_pool(self, environment_option_id ):
        """Get Environment Option Pool by id .

        :return: Dictionary with the following structure:

        ::

            {‘id’: < id >,
                option: {
                    'id': <id>
                    'type':<type>
                    'name':<name> }
                environment: {
                    'id':<id>
                    .... all environment info }
                }

        :raise EnvironmentVipNotFoundError: Environment Pool not registered.
        :raise DataBaseError: Can't connect to networkapi database.
        :raise XMLError: Failed to generate the XML response.
        """

        url = 'api/pools/environment_options/' + str(environment_option_id) + '/'

        return self.get(url)

    def disassociate_environment_option_pool(self, environment_option_id):
        """Remove a relationship of optionpool with Environment.

        :param id_option_pool: Identifier of the Option Pool. Integer value and greater than zero.
        :param id_environment: Identifier of the Environment Pool. Integer value and greater than zero.

        :return: { 'id': < environment_option_id> }

        :raise InvalidParameterError: Option Pool/Environment Pool identifier is null and/or invalid.
        :raise optionpoolNotFoundError: Option Pool not registered.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise optionpoolError: Option pool is not associated with the environment pool
        :raise UserNotAuthorizedError: User does not have authorization to make this association.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(environment_option_id):
            raise InvalidParameterError(
                u'The identifier of Option Pool is invalid or was not informed.')

        if not is_valid_int_param(environment_option_id):
            raise InvalidParameterError(
                u'The identifier of Environment Pool is invalid or was not informed.')

        url = 'api/pools/environment_options/' + str(environment_option_id) +  '/'

        return self.delete(url)


    def modify_environment_option_pool(self, environment_option_id, id_option_pool,id_environment ):
        """Remove a relationship of optionpool with Environment.

        :param id_option_pool: Identifier of the Option Pool. Integer value and greater than zero.
        :param id_environment: Identifier of the Environment Pool. Integer value and greater than zero.

                :return: Dictionary with the following structure:

        ::

            {‘id’: < id >,
                option: {
                    'id': <id>
                    'type':<type>
                    'name':<name> }
                environment: {
                    'id':<id>
                    .... all environment info }
                }

        :raise InvalidParameterError: Option Pool/Environment Pool identifier is null and/or invalid.
        :raise optionpoolNotFoundError: Option Pool not registered.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise optionpoolError: Option pool is not associated with the environment pool
        :raise UserNotAuthorizedError: User does not have authorization to make this association.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(environment_option_id):
            raise InvalidParameterError(
                u'The identifier of Environment Option Pool is invalid or was not informed.')

        #optionpool_map = dict()
        #optionpool_map['option'] = option_id
        #optionpool_map['environment'] = environment_id


        url = 'api/pools/environment_options/' + str(environment_option_id) +  '/'

        return self.put(url, {'option_id': id_option_pool,"environment_id":id_environment })