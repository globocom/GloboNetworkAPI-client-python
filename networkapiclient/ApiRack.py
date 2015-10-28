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


class ApiRack(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(ApiRack,self).__init__( networkapi_url, user, password, user_ldap)

    def insert_rack(
            self,
            number,
            name,
            mac_address_sw1,
            mac_address_sw2,
            mac_address_ilo,
            id_sw1,
            id_sw2,
            id_ilo):

        data = dict()
        data['number'] = number
        data['name'] = name
        data['mac_address_sw1'] = mac_address_sw1
        data['mac_address_sw2'] = mac_address_sw2
        data['mac_address_ilo'] = mac_address_ilo
        data['id_sw1'] = id_sw1
        data['id_sw2'] = id_sw2
        data['id_ilo'] = id_ilo

        uri = "api/rack/"

        return self.post(uri, data=data)

    def rack_deploy( self, rack_id):

        data = dict()
        uri = "api/rack/" + str(rack_id) + "/equipments/"

        return self.post(uri, data=data)