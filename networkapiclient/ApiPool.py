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
from utils import build_uri_with_ids


class ApiPool(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiPool, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def pool_by_environmentvip(self, environment_vip_id):
        """
        Method to return list object pool by environment vip id
        Param environment_vip_id: environment vip id
        Return list object pool
        """

        uri = "api/v3/pool/environment-vip/%s/" % environment_vip_id

        return super(ApiPool, self).get(uri)

    def pool_by_id(self, pool_id):
        """
        Method to return object pool by id
        Param pool_id: pool id
        Returns object pool
        """

        uri = "api/v3/pool/%s/" % pool_id

        return super(ApiPool, self).get(uri)

    def get_pool_details(self, pool_id):
        """
        Method to return object pool by id
        Param pool_id: pool id
        Returns object pool
        """

        uri = "api/v3/pool/details/%s/" % pool_id

        return super(ApiPool, self).get(uri)
    
    def search(self, **kwargs):
        """
        Method to search pool's based on extends search.

        :param search: Dict containing QuerySets to find pool's.
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields:  Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing pool's
        """

        return super(ApiPool, self).get(self.prepare_url('api/v3/pool/',
                                                                kwargs))

    def get(self, ids, **kwargs):
        """
        Method to get pool's by their ids

        :param ids: List containing identifiers of pool's
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields: Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing pool's
        """
        url = build_uri_with_ids('api/v3/pool/%s/', ids)

        return super(ApiPool, self).get(self.prepare_url(url, kwargs))

    def delete(self, ids):
        """
        Method to delete pool's by their ids

        :param ids: Identifiers of pool's
        :return: None
        """
        url = build_uri_with_ids('api/v3/pool/%s/', ids)

        return super(ApiPool, self).delete(url)

    def update(self, pools):
        """
        Method to update pool's

        :param pools: List containing pool's desired to updated
        :return: None
        """

        data = {'server_pools': pools}
        pools_ids = [str(pool.get('id'))
                            for pool in pools]

        return super(ApiPool, self).put('api/v3/pool/%s/' %
                                               ';'.join(pools_ids), data)

    def create(self, pools):
        """
        Method to create pool's

        :param pools: List containing pool's desired to be created on database
        :return: None
        """

        data = {'server_pools': pools}
        return super(ApiPool, self).post('api/v3/pool/', data)

