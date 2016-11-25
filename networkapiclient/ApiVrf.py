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


class ApiVrf(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiVrf, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def search(self, **kwargs):
        """
        Method to search vrf's based on extends search.

        :param search: Dict containing QuerySets to find vrf's.
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields:  Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing vrf's
        """

        return super(ApiVrf, self).get(self.prepare_url('api/v3/vrf/',
                                                        kwargs))

    def get(self, ids, **kwargs):
        """
        Method to get vrfs by their id's

        :param ids: List containing identifiers of vrf's
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields: Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing vrf's
        """
        url = build_uri_with_ids('api/v3/vrf/%s/', ids)

        return super(ApiVrf, self).get(self.prepare_url(url, kwargs))

    def delete(self, ids):
        """
        Method to delete vrf's by their id's

        :param ids: Identifiers of vrf's
        :return: None
        """
        url = build_uri_with_ids('api/v3/vrf/%s/', ids)

        return super(ApiVrf, self).delete(url)

    def update(self, vrfs):
        """
        Method to update vrf's

        :param vrfs: List containing vrf's desired to updated
        :return: None
        """

        data = {'vrfs': vrfs}
        vrfs_ids = [str(vrf.get('id')) for vrf in vrfs]

        return super(ApiVrf, self).put('api/v3/vrf/%s/' %
                                       ';'.join(vrfs_ids), data)

    def create(self, vrfs):
        """
        Method to create vrf's

        :param vrfs: List containing vrf's desired to be created on database
        :return: None
        """

        data = {'vrfs': vrfs}
        return super(ApiVrf, self).post('api/v3/vrf/', data)
