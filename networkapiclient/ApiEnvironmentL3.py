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


class ApiL3Environment(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiL3Environment, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def get(self, ids=None, **kwargs):
        """
        Method to get dc environments by their ids or list all.

        :param ids: List containing identifiers of environments
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields: Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing environments
        """
        url = build_uri_with_ids('api/v3/environment/l3/', ids)
        return super(ApiL3Environment, self).get(self.prepare_url(url, kwargs))

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

        return super(ApiL3Environment, self).get(self.prepare_url('api/v3/environment/l3/', kwargs))

    def create(self, environments):
        """
        Method to create environments

        :param environments: Dict containing environments desired to be created on database
        :return: None
        """

        data = dict(l3=environments)
        return super(ApiL3Environment, self).post('api/v3/environment/l3/', data)
