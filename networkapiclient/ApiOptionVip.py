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


class ApiOptionVip(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiOptionVip, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def option_vip_by_environment_vip_type(self, environment_vip_id, type_option):
        """
        List option vip.
        param environment_vip_id: Id of Environment Vip
        Param type_option: type option vip
        """

        uri = "api/v3/option-vip/environment-vip/%s/type-option/%s/" % (environment_vip_id, type_option)

        return self.get(uri)

    def option_vip_by_environment(self, environment_vip_id):
        """
        List option vip.
        param environment_vip_id: Id of Environment Vip
        """

        uri = "api/v3/option-vip/environment-vip/%s/" % (environment_vip_id)

        return self.get(uri)
