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


class ApiV4Neighbor(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None, log_level='INFO'):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiV4Neighbor, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def search(self, **kwargs):
        """
        Method to search neighbors based on extends search.

        :param search: Dict containing QuerySets to find neighbors.
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields:  Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing neighbors
        """

        return super(ApiV4Neighbor, self).get(self.prepare_url(
            'api/v4/neighbor/', kwargs))

    def get(self, ids, **kwargs):
        """
        Method to get neighbors by their ids

        :param ids: List containing identifiers of neighbors
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields: Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing neighbors
        """
        url = build_uri_with_ids('api/v4/neighbor/%s/', ids)
        return super(ApiV4Neighbor, self).get(self.prepare_url(url, kwargs))

    def delete(self, ids):
        """
        Method to delete neighbors by their id's

        :param ids: Identifiers of neighbors
        :return: None
        """
        url = build_uri_with_ids('api/v4/neighbor/%s/', ids)
        return super(ApiV4Neighbor, self).delete(url)

    def update(self, neighbors):
        """
        Method to update neighbors

        :param neighbors: List containing neighbors desired to updated
        :return: None
        """

        data = {'neighbors': neighbors}
        neighbors_ids = [str(env.get('id')) for env in neighbors]

        return super(ApiV4Neighbor, self).put('api/v4/neighbor/%s/' %
                                               ';'.join(neighbors_ids), data)

    def create(self, neighbors):
        """
        Method to create neighbors

        :param neighbors: List containing neighbors desired to be created on database
        :return: None
        """

        data = {'neighbors': neighbors}
        return super(ApiV4Neighbor, self).post('api/v4/neighbor/', data)
