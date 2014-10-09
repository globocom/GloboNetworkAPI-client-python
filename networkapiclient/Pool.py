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

from networkapiclient.ApiGenericClient import ApiGenericClient


class Pool(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(Pool, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def list_all(self, pagination):
        """
        List all pools

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

        uri = "api/pools/"

        data = dict()

        data["start_record"] = pagination.start_record
        data["end_record"] = pagination.end_record
        data["asorting_cols"] = pagination.asorting_cols
        data["searchable_columns"] = pagination.searchable_columns
        data["custom_search"] = pagination.custom_search or None

        return self.post(uri, data=data)

    def inserir(self, identifier, default_port, environment, balancing,
                healthcheck, maxcom, ip_list_full, id_equips, priorities, ports_reals):

        uri = "api/pools/insert/"
        import json
        data = dict()
        data['identifier'] = identifier
        data['default_port'] = default_port
        data['environment'] = environment
        data['balancing'] = balancing
        data['healthcheck'] = healthcheck
        data['maxcom'] = maxcom
        data['ip_list_full'] = json.dumps(ip_list_full)
        data['id_equips'] = id_equips
        data['priorities'] = priorities
        data['ports_reals'] = ports_reals

        return self.post(uri, data=data)


    def list_healthchecks(self):
        """
        List all pools

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

        uri = "api/pools/list_healthchecks/"

        return self.get(uri)

    def delete(self, ids):

        data = dict()
        data["ids"] = ids

        uri = "api/pools/delete/"

        return self.post(uri, data)

