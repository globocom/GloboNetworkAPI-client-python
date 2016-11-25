# -*- coding: utf-8 -*-
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
from networkapiclient.utils import build_uri_with_ids


class ApiEnvironment(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiEnvironment, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def list_all_environment_related_environment_vip(self):
        """
        Return list environments related with environment vip
        """

        uri = 'api/v3/environment/environment-vip/'

        return super(ApiEnvironment, self).get(uri)

    def get_environment(self, environment_ids):
        """
        Method to get environment
        """

        uri = 'api/v3/environment/%s/' % environment_ids

        return super(ApiEnvironment, self).get(uri)

    def create_environment(self, environment):
        """
        Method to create environment
        """

        uri = 'api/v3/environment/'

        data = dict()
        data['environments'] = list()
        data['environments'].append(environment)

        return super(ApiEnvironment, self).post(uri, data)

    def update_environment(self, environment, environment_ids):
        """
        Method to update environment

        :param environment_ids: Ids of Environment
        """

        uri = 'api/v3/environment/%s/' % environment_ids

        data = dict()
        data['environments'] = list()
        data['environments'].append(environment)

        return super(ApiEnvironment, self).put(uri, data)

    def delete_environment(self, environment_ids):
        """
        Method to delete environment

        :param environment_ids: Ids of Environment
        """
        uri = 'api/v3/environment/%s/' % environment_ids

        return super(ApiEnvironment, self).delete(uri)

    def search(self, **kwargs):
        """
        Method to search environments based on extends search.

        :param search: Dict containing QuerySets to find environments.
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields:  Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing environments
        """

        return super(ApiEnvironment, self).get(self.prepare_url('api/v3/environment/',
                                                                kwargs))

    def get(self, ids, **kwargs):
        """
        Method to get environments by their ids

        :param ids: List containing identifiers of environments
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields: Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing environments
        """
        url = build_uri_with_ids('api/v3/environment/%s/', ids)
        return super(ApiEnvironment, self).get(self.prepare_url(url, kwargs))

    def delete(self, ids):
        """
        Method to delete environments by their id's

        :param ids: Identifiers of environments
        :return: None
        """
        url = build_uri_with_ids('api/v3/environment/%s/', ids)
        return super(ApiEnvironment, self).delete(url)

    def update(self, environments):
        """
        Method to update environments

        :param environments: List containing environments desired to updated
        :return: None
        """

        data = {'environments': environments}
        environments_ids = [str(env.get('id')) for env in environments]

        return super(ApiEnvironment, self).put('api/v3/environment/%s/' %
                                               ';'.join(environments_ids), data)

    def create(self, environments):
        """
        Method to create environments

        :param environments: Dict containing environments desired to be created on database
        :return: None
        """

        data = {'environments': environments}
        return super(ApiEnvironment, self).post('api/v3/environment/', data)
