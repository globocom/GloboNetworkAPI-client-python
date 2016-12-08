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


class ApiEnvironmentVip(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiEnvironmentVip, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def get_environment_vip(self, environment_vip_id, fields=None):

        uri = 'api/v3/environment-vip/%s/' % environment_vip_id

        if fields:
            uri += '?fields={}'.format(','.join(fields))

        return super(ApiEnvironmentVip, self).get(
            uri)

    def environmentvip_step(self, finality='', client='', environmentp44=''):
        """
        List finality, client or environment vip list.
        Param finality: finality of environment(optional)
        Param client: client of environment(optional)
        Param environmentp44: environmentp44(optional)
        Return finality list: when request has no finality and client.
        Return client list: when request has only finality.
        Return list environment vip: when request has finality and client.
        Return environment vip: when request has finality, client and environmentvip
        """

        uri = 'api/v3/environment-vip/step/?finality=%s&client=%s&environmentp44=%s' % (
            finality, client, environmentp44)

        return super(ApiEnvironmentVip, self).get(
            uri)

    def search(self, **kwargs):
        """
        Method to search environments vip based on extends search.

        :param search: Dict containing QuerySets to find environments vip.
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields: Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail')
                     or basic ('basic').
        :return: Dict containing environments vip
        """

        return super(ApiEnvironmentVip, self).get(
            self.prepare_url('api/v3/environment-vip/', kwargs))

    def get(self, ids, **kwargs):
        """
        Method to get environments vip by their ids

        :param ids: List containing identifiers of environments vip
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields: Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail')
                     or basic ('basic').
        :return: Dict containing environments vip
        """
        uri = build_uri_with_ids('api/v3/environment-vip/%s/', ids)
        return super(ApiEnvironmentVip, self).get(
            self.prepare_url(uri, kwargs))

    def delete(self, ids):
        """
        Method to delete environments vip by their id's.

        :param ids: Identifiers of environments vip
        :return: None
        """
        url = build_uri_with_ids('api/v3/environment-vip/%s/', ids)
        return super(ApiEnvironmentVip, self).delete(url)

    def update(self, environments):
        """
        Method to update environments vip

        :param environments vip: List containing environments vip desired
                                 to updated
        :return: None
        """

        data = {'environments_vip': environments}
        environments_ids = [str(env.get('id')) for env in environments]

        uri = 'api/v3/environment-vip/%s/' % ';'.join(environments_ids)
        return super(ApiEnvironmentVip, self).put(uri, data)

    def create(self, environments):
        """
        Method to create environments vip

        :param environments vip: Dict containing environments vip desired
                                 to be created on database
        :return: None
        """

        data = {'environments_vip': environments}
        uri = 'api/v3/environment-vip/'
        return super(ApiEnvironmentVip, self).post(uri, data)
