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


class ApiPoolDeploy(ApiGenericClient):
    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiPoolDeploy, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def delete(self, ids):
        """
        Method to undeploy pool's by their ids

        :param ids: Identifiers of deployed pool's
        :return: Empty Dict
        """
        url = build_uri_with_ids('api/v3/pool/deploy/%s/', ids)

        return super(ApiPoolDeploy, self).delete(url)

    def update(self, pools):
        """
        Method to update deployed pool's

        :param pools: List containing deployed pool's desired to updated
        :return: Empty Dict
        """

        data = {'server_pools': pools}
        pools_ids = [str(pool.get('id'))
                     for pool in pools]

        return super(ApiPoolDeploy, self).put('api/v3/pool/deploy/%s/' %
                                        ';'.join(pools_ids), data)

    def create(self, ids):
        """
        Method to deploy pool's

        :param pools: Identifiers of pool's desired to be deployed
        :return: Empty Dict
        """

        url = build_uri_with_ids('api/v3/pool/deploy/%s/', ids)
        return super(ApiPoolDeploy, self).post(url)

