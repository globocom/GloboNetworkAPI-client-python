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


class ApiVlan(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiVlan, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def acl_remove_draft(self, id_vlan, type_acl):
        """
            Remove Acl draft by type

            :param id_vlan: Identity of Vlan
            :param type_acl: Acl type v4 or v6

            :return: None

            :raise VlanDoesNotExistException: Vlan Does Not Exist.
            :raise InvalidIdVlanException: Invalid id for Vlan.
            :raise NetworkAPIException: Failed to access the data source.
        """

        parameters = dict(id_vlan=id_vlan, type_acl=type_acl)

        uri = 'api/vlan/acl/remove/draft/%(id_vlan)s/%(type_acl)s/' % parameters

        return super(ApiVlan, self).get(uri)

    def acl_save_draft(self, id_vlan, type_acl, content_draft):
        """
            Save Acl draft by type

            :param id_vlan: Identity of Vlan
            :param type_acl: Acl type v4 or v6

            :return: None

            :raise VlanDoesNotExistException: Vlan Does Not Exist.
            :raise InvalidIdVlanException: Invalid id for Vlan.
            :raise NetworkAPIException: Failed to access the data source.
        """

        parameters = dict(id_vlan=id_vlan, type_acl=type_acl)

        data = dict(content_draft=content_draft)

        uri = 'api/vlan/acl/save/draft/%(id_vlan)s/%(type_acl)s/' % parameters

        return super(ApiVlan, self).post(uri, data=data)

    def search(self, **kwargs):
        """
        Method to search vlan's based on extends search.

        :param search: Dict containing QuerySets to find vlan's.
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields:  Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing vlan's
        """

        return super(ApiVlan, self).get(self.prepare_url('api/v3/vlan/',
                                                         kwargs))

    def get(self, ids, **kwargs):
        """
        Method to get vlan's by their id's

        :param ids: List containing identifiers of vlan's
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields: Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing vlan's
        """
        url = build_uri_with_ids('api/v3/vlan/%s/', ids)

        return super(ApiVlan, self).get(self.prepare_url(url, kwargs))

    def delete(self, ids):
        """
        Method to delete vlan's by their ids

        :param ids: Identifiers of vlan's
        :return: None
        """
        url = build_uri_with_ids('api/v3/vlan/%s/', ids)

        return super(ApiVlan, self).delete(url)

    def update(self, vlans):
        """
        Method to update vlan's

        :param vlans: List containing vlan's desired to updated
        :return: None
        """

        data = {'vlans': vlans}
        vlans_ids = [str(vlan.get('id')) for vlan in vlans]

        return super(ApiVlan, self).put('api/v3/vlan/%s/' %
                                        ';'.join(vlans_ids), data)

    def create(self, vlans):
        """
        Method to create vlan's

        :param vlans: List containing vlan's desired to be created on database
        :return: None
        """

        data = {'vlans': vlans}
        return super(ApiVlan, self).post('api/v3/vlan/', data)
