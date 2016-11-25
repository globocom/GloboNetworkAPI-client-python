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


class ApiEquipment(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None, log_level='INFO'):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiEquipment, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def get_equipment(self, **kwargs):
        """
        Return list environments related with environment vip
        """

        uri = 'api/v3/equipment/'
        uri = self.prepare_url(uri, kwargs)

        return super(ApiEquipment, self).get(uri)

    def search(self, **kwargs):
        """
        Method to search equipments based on extends search.

        :param search: Dict containing QuerySets to find equipments.
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields:  Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing equipments
        """

        return super(ApiEquipment, self).get(self.prepare_url('api/v3/equipment/',
                                                              kwargs))

    def get(self, ids, **kwargs):
        """
        Method to get equipments by their ids

        :param ids: List containing identifiers of equipments
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields: Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing equipments
        """
        url = build_uri_with_ids('api/v3/equipment/%s/', ids)
        return super(ApiEquipment, self).get(self.prepare_url(url, kwargs))

    def delete(self, ids):
        """
        Method to delete equipments by their id's

        :param ids: Identifiers of equipments
        :return: None
        """
        url = build_uri_with_ids('api/v3/equipment/%s/', ids)
        return super(ApiEquipment, self).delete(url)

    def update(self, equipments):
        """
        Method to update equipments

        :param equipments: List containing equipments desired to updated
        :return: None
        """

        data = {'equipments': equipments}
        equipments_ids = [str(env.get('id')) for env in equipments]

        return super(ApiEquipment, self).put('api/v3/equipment/%s/' %
                                             ';'.join(equipments_ids), data)

    def create(self, equipments):
        """
        Method to create equipments

        :param equipments: List containing equipments desired to be created on database
        :return: None
        """

        data = {'equipments': equipments}
        return super(ApiEquipment, self).post('api/v3/equipment/', data)
