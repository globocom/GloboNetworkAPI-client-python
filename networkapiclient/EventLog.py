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
from networkapiclient.Pagination import Pagination
import urllib


class EventLog(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            EventLog,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def find_logs(
            self,
            user_name,
            first_date,
            start_time,
            last_date,
            end_time,
            action,
            functionality,
            parameter,
            pagination):
        """
        Search all logs, filtering by the given parameters.
        :param user_name: Filter by user_name
        :param first_date: Sets initial date for begin of the filter
        :param start_time: Sets initial time
        :param last_date: Sets final date
        :param end_time: Sets final time and ends the filter. That defines the searching gap
        :param action: Filter by action (Create, Update or Delete)
        :param functionality: Filter by class
        :param parameter: Filter by parameter
        :param pagination: Class with all data needed to paginate

        :return: Following dictionary:

        ::

            {'eventlog': {'id_usuario' : < id_user >,
            'hora_evento': < hora_evento >,
            'acao': < acao >,
            'funcionalidade': < funcionalidade >,
            'parametro_anterior': < parametro_anterior >,
            'parametro_atual': < parametro_atual > }
            'total' : {< total_registros >} }

        :raise InvalidParameterError: Some parameter was invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not isinstance(pagination, Pagination):
            raise InvalidParameterError(
                u"Invalid parameter: pagination must be a class of type 'Pagination'.")

        eventlog_map = dict()

        eventlog_map["start_record"] = pagination.start_record
        eventlog_map["end_record"] = pagination.end_record
        eventlog_map["asorting_cols"] = pagination.asorting_cols
        eventlog_map["searchable_columns"] = pagination.searchable_columns
        eventlog_map["custom_search"] = pagination.custom_search

        eventlog_map["usuario"] = user_name
        eventlog_map["data_inicial"] = first_date
        eventlog_map["hora_inicial"] = start_time
        eventlog_map["data_final"] = last_date
        eventlog_map["hora_final"] = end_time
        eventlog_map["acao"] = action
        eventlog_map["funcionalidade"] = functionality
        eventlog_map["parametro"] = parameter

        url = "eventlog/find/"

        code, xml = self.submit({'eventlog': eventlog_map}, 'POST', url)

        key = "eventlog"
        return get_list_map(self.response(code, xml, key), key)

    def get_choices(self):
        """
        Returns a dictionary with the values used to construct the select box of actions,
        functionalities and users.

        :return: the following dictionary:

        ::


            {'choices_map': {'usuario' : [{ 'usuario' : < user_id >
            'usuario__nome' : < nome >
            'usuario__user' : < user > }]
            'acao' : ['action1', 'action2', 'action3' .. 'actionN']
            'funcionalidade' : ['functionality1', 'functionality2', .. 'functionalityN'] }}
        """

        url = "eventlog/choices/"

        code, xml = self.submit(None, 'POST', url)

        key = "choices"
        return get_list_map(self.response(code, xml, key), key)

    def get_version(self):
        """
        Returns the API's version

        :return:

        ::

            {'version_api': <version_api> }

        """

        url = "eventlog/version/"

        code, xml = self.submit(None, 'GET', url)

        key = "version"
        return get_list_map(self.response(code, xml, key), key)
