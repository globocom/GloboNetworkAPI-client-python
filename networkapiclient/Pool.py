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
            List All Pools To Populate Datatable

            :param pagination: Object Pagination

            :return: Following dictionary:{
                                            "total" : < total >,
                                            "pools" :[{
                                                "id": < id >
                                                "default_port": < default_port >,
                                                "identifier": < identifier >,
                                                "healthcheck": < healthcheck >,
                                            }, ... too ... ]}

            :raise NetworkAPIException: Falha ao acessar fonte de dados
        """

        uri = "api/pools/"

        data = dict()

        data["start_record"] = pagination.start_record
        data["end_record"] = pagination.end_record
        data["asorting_cols"] = pagination.asorting_cols
        data["searchable_columns"] = pagination.searchable_columns
        data["custom_search"] = pagination.custom_search or None

        return self.post(uri, data=data)

    def delete(self, ids):
        """
            Delete Pools

            :param ids: List of ids

            :return: None on success

            :raise ValidationException: Id(s) inválido(s)
            :raise NetworkAPIException: Falha ao acessar fonte de dados
        """

        data = dict()
        data["ids"] = ids

        uri = "api/pools/delete/"

        return self.post(uri, data)

    def remove(self, ids):
        """
            Remove Pools Running Script And Update to Not Created

            :param ids: List of ids

            :return: None on success

            :raise ValidationException: Id(s) inválido(s)
            :raise NetworkAPIException: Falha ao acessar fonte de dados
        """

        data = dict()
        data["ids"] = ids

        uri = "api/pools/remove/"

        return self.post(uri, data)
