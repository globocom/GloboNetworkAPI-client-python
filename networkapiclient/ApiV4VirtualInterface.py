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


class ApiV4VirtualInterface(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None, log_level='INFO'):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiV4VirtualInterface, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def search(self, **kwargs):
        """
        Method to search Virtual Interfaces based on extends search.

        :param search: Dict containing QuerySets to find Virtual Interfaces.
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields:  Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing Virtual Interfaces
        """

        return super(ApiV4VirtualInterface, self).get(self.prepare_url(
            'api/v4/virtual-interface/', kwargs))

    def get(self, ids, **kwargs):
        """
        Method to get Virtual Interfaces by their ids

        :param ids: List containing identifiers of Virtual Interfaces
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields: Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing Virtual Interfaces
        """
        url = build_uri_with_ids('api/v4/virtual-interface/%s/', ids)
        return super(ApiV4VirtualInterface, self).get(self.prepare_url(url, kwargs))

    def delete(self, ids):
        """
        Method to delete Virtual Interfaces by their id's

        :param ids: Identifiers of Virtual Interfaces
        :return: None
        """
        url = build_uri_with_ids('api/v4/virtual-interface/%s/', ids)
        return super(ApiV4VirtualInterface, self).delete(url)

    def update(self, virtual_interfaces):
        """
        Method to update Virtual Interfaces

        :param Virtual Interfaces: List containing Virtual Interfaces desired to updated
        :return: None
        """

        data = {'virtual_interfaces': virtual_interfaces}
        virtual_interfaces_ids = [str(env.get('id')) for env in virtual_interfaces]

        return super(ApiV4VirtualInterface, self).put\
            ('api/v4/virtual-interface/%s/' % ';'.join(virtual_interfaces_ids), data)

    def create(self, virtual_interfaces):
        """
        Method to create Virtual Interfaces

        :param Virtual Interfaces: List containing Virtual Interfaces desired to be created on database
        :return: None
        """

        data = {'virtual_interfaces': virtual_interfaces}
        return super(ApiV4VirtualInterface, self).post\
            ('api/v4/virtual-interface/', data)
