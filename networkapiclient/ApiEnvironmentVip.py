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

    def environmentvip_step(self, finality='', client='', environmentvip=''):
        """
        List finality, client or environment vip list.
        Param finality: finality of environment(optional)
        Param client: client of environment(optional)
        Param environmentvip: environment vip(optional)
        Return finality list: when request has no finality and client.
        Return client list: when request has only finality.
        Return list environment vip: when request has finality and client.
        Return environment vip: when request has finality, client and environmentvip
        """

        uri = "api/environment-vip/step/?finality=%s&client=%s&environmentvip=%s" % (finality, client, environmentvip)

        return self.get(uri)
