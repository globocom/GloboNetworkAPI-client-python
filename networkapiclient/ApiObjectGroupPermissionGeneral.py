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


class ApiObjectGroupPermissionGeneral(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiObjectGroupPermissionGeneral, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def search(self, **kwargs):
        """
        Method to search object group permissions general based on extends search.

        :param search: Dict containing QuerySets to find object group permissions general.
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields:  Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing object group permissions general
        """

        return super(ApiObjectGroupPermissionGeneral, self).get(self.prepare_url('api/v3/object-group-perm-general/',
                                                                                 kwargs))

    def get(self, ids, **kwargs):
        """
        Method to get object group permissions general by their ids

        :param ids: List containing identifiers of object group permissions general
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields: Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing object group permissions general
        """
        url = build_uri_with_ids('api/v3/object-group-perm-general/%s/', ids)
        return super(ApiObjectGroupPermissionGeneral, self).get(self.prepare_url(url, kwargs))

    def delete(self, ids):
        """
        Method to delete object group permissions general by their ids

        :param ids: Identifiers of object group permissions general
        :return: None
        """
        url = build_uri_with_ids('api/v3/object-group-perm-general/%s/', ids)
        return super(ApiObjectGroupPermissionGeneral, self).delete(url)

    def update(self, ogpgs):
        """
        Method to update object group permissions general

        :param ogpgs: List containing object group permissions general desired to updated
        :return: None
        """

        data = {'ogpgs': ogpgs}
        ogpgs_ids = [str(ogpg.get('id')) for ogpg in ogpgs]

        return super(ApiObjectGroupPermissionGeneral, self).put('api/v3/object-group-perm-general/%s/' %
                                                                ';'.join(ogpgs_ids), data)

    def create(self, ogpgs):
        """
        Method to create object group permissions general

        :param ogpgs: List containing vrf desired to be created on database
        :return: None
        """

        data = {'ogpgs': ogpgs}
        return super(ApiObjectGroupPermissionGeneral, self).post('api/v3/object-group-perm-general/', data)
