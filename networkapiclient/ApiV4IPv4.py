# -*- coding: utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from networkapiclient.ApiGenericClient import ApiGenericClient
from networkapiclient.utils import build_uri_with_ids


class ApiV4IPv4(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiV4IPv4, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def search(self, **kwargs):
        """
        Method to search ipv4's based on extends search.

        :param search: Dict containing QuerySets to find ipv4's.
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields:  Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing ipv4's
        """

        return super(ApiV4IPv4, self).get(self.prepare_url('api/v4/ipv4/',
                                                           kwargs))

    def get(self, ids, **kwargs):
        """
        Method to get ipv4's by their ids

        :param ids: List containing identifiers of ipv4's
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields: Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing ipv4's
        """
        url = build_uri_with_ids('api/v4/ipv4/%s/', ids)

        return super(ApiV4IPv4, self).get(self.prepare_url(url, kwargs))

    def delete(self, ids):
        """
        Method to delete ipv4's by their ids

        :param ids: Identifiers of ipv4's
        :return: None
        """
        url = build_uri_with_ids('api/v4/ipv4/%s/', ids)

        return super(ApiV4IPv4, self).delete(url)

    def update(self, ipv4s):
        """
        Method to update ipv4's

        :param ipv4s: List containing ipv4's desired to updated
        :return: None
        """

        data = {'ips': ipv4s}
        ipv4s_ids = [str(ipv4.get('id')) for ipv4 in ipv4s]

        return super(ApiV4IPv4, self).put('api/v4/ipv4/%s/' %
                                          ';'.join(ipv4s_ids), data)

    def create(self, ipv4s):
        """
        Method to create ipv4's

        :param ipv4s: List containing ipv4's desired to be created on database
        :return: None
        """

        data = {'ips': ipv4s}
        return super(ApiV4IPv4, self).post('api/v4/ipv4/', data)
