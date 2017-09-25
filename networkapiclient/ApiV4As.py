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


class ApiV4As(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None, log_level='INFO'):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiV4As, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def search(self, **kwargs):
        """
        Method to search asns based on extends search.

        :param search: Dict containing QuerySets to find asns.
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields:  Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing asns
        """

        return super(ApiV4As, self).get(self.prepare_url(
            'api/v4/as/', kwargs))

    def get(self, ids, **kwargs):
        """
        Method to get asns by their ids

        :param ids: List containing identifiers of asns
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields: Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing asns
        """
        url = build_uri_with_ids('api/v4/as/%s/', ids)
        return super(ApiV4As, self).get(self.prepare_url(url, kwargs))

    def delete(self, ids):
        """
        Method to delete asns by their id's

        :param ids: Identifiers of asns
        :return: None
        """
        url = build_uri_with_ids('api/v4/as/%s/', ids)
        return super(ApiV4As, self).delete(url)

    def update(self, asns):
        """
        Method to update asns

        :param asns: List containing asns desired to updated
        :return: None
        """

        data = {'asns': asns}
        asns_ids = [str(env.get('id')) for env in asns]

        return super(ApiV4As, self).put('api/v4/as/%s/' %
                                               ';'.join(asns_ids), data)

    def create(self, asns):
        """
        Method to create asns

        :param asns: List containing asns desired to be created on database
        :return: None
        """

        data = {'asns': asns}
        return super(ApiV4As, self).post('api/v4/as/', data)
