# -*- coding:utf-8 -*-
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


class ApiInterfaceRequest(ApiGenericClient):
    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiInterfaceRequest, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def deploy_interface_config_sync(self, interface_id):
        """
        """

        uri = "api/interface/%s/deploy_config_sync/" % interface_id

        data = dict()

        return self.put(uri, data)

    def deploy_channel_config_sync(self, channel_id):
        """
        """

        uri = "api/interface/channel/%s/deploy_config_sync/" % channel_id

        data = dict()

        return self.put(uri, data)

    def remove_connection(self, interface1, interface2):
        """Remove a connection between two interfaces"""

        uri = "api/interface/disconnect/%s/%s/" % (interface1, interface2)

        return self.delete(uri)

    def search(self, **kwargs):
        """
        Method to search interfaces based on extends search.
        :return: Dict containing interfaces.
        """

        return super(ApiInterfaceRequest, self).get(self.prepare_url('api/v3/interface/', kwargs))

    def get(self, ids, **kwargs):
        """
        Method to get interfaces by their ids.
        :param ids: List containing identifiers of interfaces.
        :return: Dict containing interfaces.
        """

        url = build_uri_with_ids('api/v3/interface/%s/', ids)

        return super(ApiInterfaceRequest, self).get(self.prepare_url(url, kwargs))

    def remove(self, ids, **kwargs):
        """
        Method to delete interface by id.
        :param ids: List containing identifiers of interfaces.
        """
        url = build_uri_with_ids('api/v3/interface/%s/', ids)

        return super(ApiInterfaceRequest, self).delete(self.prepare_url(url, kwargs))

    def create(self, interface):
        """
        Method to add an interface.
        :param interface: List containing interface's desired to be created on database.
        :return: Id.
        """

        data = {'interfaces': interface}
        return super(ApiInterfaceRequest, self).post('api/v3/interface/', data)

    def get_interface_type(self, ids=None, **kwargs):
        """
        Method to get interfaces by their ids.
        :param ids: List containing identifiers of interfaces.
        :return: Dict containing interfaces.git 
        """

        url = 'api/v3/interfacetype/'

        if ids:
            url = build_uri_with_ids(url, ids)

        return super(ApiInterfaceRequest, self).get(self.prepare_url(url, kwargs))
