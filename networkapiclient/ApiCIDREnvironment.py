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


class ApiCIDREnvironment(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiCIDREnvironment, self).__init__(
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
        url = build_uri_with_ids('api/v3/cidr/', ids)
        return super(ApiCIDREnvironment, self).get(self.prepare_url(url, kwargs))

    def get_by_env(self, env_id=None, **kwargs):

        url = build_uri_with_ids('api/v3/cidr/environment/%s', env_id)
        return super(ApiCIDREnvironment, self).get(self.prepare_url(url, kwargs))

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

        return super(ApiCIDREnvironment, self).get(self.prepare_url('api/v3/cidr/', kwargs))

    def post(self, cidrs):
        """
        Method to allocate a new network block.
        :param cidrs: List containing cidr objects.
        :return: The cidr id.
        """

        data = dict(cidr=cidrs)
        return super(ApiCIDREnvironment, self).post('api/v3/cidr/', data)

    def delete(self, cidr_id=None, environment_id=None):
        """
        Method to delete cidrs by their id's

        :param ids: Identifiers of cidrs
        :return: None
        """

        if cidr_id:
            url = build_uri_with_ids('api/v3/cidr/%s/', cidr_id)
        else:
            url = build_uri_with_ids('api/v3/cidr/environment/%s/', environment_id)

        return super(ApiCIDREnvironment, self).delete(url)
