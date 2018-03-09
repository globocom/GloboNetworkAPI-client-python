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
import urllib

from networkapiclient.ApiGenericClient import ApiGenericClient
from networkapiclient.utils import build_uri_with_ids


class ApiVipRequest(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None, log_level='INFO'):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiVipRequest, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap,
            log_level
        )

    def list_environment_by_environmet_vip(self, environment_vip_id):
        """
        """

        uri = 'api/vip/list/environment/by/environment/vip/%s/' % (
            environment_vip_id)

        return super(ApiVipRequest, self).get(uri)

    #######################
    # API V3
    #######################
    def option_vip_by_environmentvip(self, environment_vip_id):
        """
        List Option Vip by Environment Vip

        param environment_vip_id: Id of Environment Vip
        """

        uri = 'api/v3/option-vip/environment-vip/%s/' % environment_vip_id

        return super(ApiVipRequest, self).get(uri)

    def get_vip_request_details(self, vip_request_id):
        """
        Method to get details of vip request

        param vip_request_id: vip_request id
        """
        uri = 'api/v3/vip-request/details/%s/' % vip_request_id

        return super(ApiVipRequest, self).get(uri)

    def search_vip_request_details(self, search):
        """
        Method to list vip request

        param search: search
        """
        uri = 'api/v3/vip-request/details/?%s' % urllib.urlencode(
            {'search': search})

        return super(ApiVipRequest, self).get(uri)

    def get_vip_request(self, vip_request_id):
        """
        Method to get vip request

        param vip_request_id: vip_request id
        """
        uri = 'api/v3/vip-request/%s/' % vip_request_id

        return super(ApiVipRequest, self).get(uri)

    def search_vip_request(self, search):
        """
        Method to list vip request

        param search: search
        """
        uri = 'api/v3/vip-request/?%s' % urllib.urlencode({'search': search})

        return super(ApiVipRequest, self).get(uri)

    def save_vip_request(self, vip_request):
        """
        Method to save vip request

        param vip_request: vip_request object
        """
        uri = 'api/v3/vip-request/'

        data = dict()
        data['vips'] = list()
        data['vips'].append(vip_request)

        return super(ApiVipRequest, self).post(uri, data)

    def update_vip_request(self, vip_request, vip_request_id):
        """
        Method to update vip request

        param vip_request: vip_request object
        param vip_request_id: vip_request id
        """
        uri = 'api/v3/vip-request/%s/' % vip_request_id

        data = dict()
        data['vips'] = list()
        data['vips'].append(vip_request)

        return super(ApiVipRequest, self).put(uri, data)

    def delete_vip_request(self, vip_request_ids):
        """
        Method to delete vip request

        param vip_request_ids: vip_request ids
        """
        uri = 'api/v3/vip-request/%s/' % vip_request_ids

        return super(ApiVipRequest, self).delete(uri)

    def create_vip(self, vip_request_ids):
        """
        Method to create vip request

        param vip_request_ids: vip_request ids
        """
        uri = 'api/v3/vip-request/deploy/%s/' % vip_request_ids

        return super(ApiVipRequest, self).post(uri)

    def update_vip(self, vip_request, vip_request_id):
        """
        Method to update vip request

        param vip_request: vip_request object
        param vip_request_id: vip_request id
        """
        uri = 'api/v3/vip-request/deploy/%s/' % vip_request_id

        data = dict()
        data['vips'] = list()
        data['vips'].append(vip_request)

        return super(ApiVipRequest, self).put(uri, data)

    def remove_vip(self, vip_request_ids):
        """
        Method to delete vip request

        param vip_request_ids: vip_request ids
        """
        uri = 'api/v3/vip-request/deploy/%s/' % vip_request_ids

        return super(ApiVipRequest, self).delete(uri)

    def search(self, **kwargs):
        """
        Method to search vip's based on extends search.

        :param search: Dict containing QuerySets to find vip's.
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields:  Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing vip's
        """

        return super(ApiVipRequest, self).get(self.prepare_url('api/v3/vip-request/',
                                                               kwargs))

    def get(self, ids, **kwargs):
        """
        Method to get vips by their id's

        :param ids: List containing identifiers of vip's
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields: Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing vip's
        """
        url = build_uri_with_ids('api/v3/vip-request/%s/', ids)

        return super(ApiVipRequest, self).get(self.prepare_url(url, kwargs))

    def delete(self, ids):
        """
        Method to delete vip's by their id's

        :param ids: Identifiers of vip's
        :return: None
        """
        url = build_uri_with_ids('api/v3/vip-request/%s/', ids)

        return super(ApiVipRequest, self).delete(url)

    def update(self, vips):
        """
        Method to update vip's

        :param vips: List containing vip's desired to updated
        :return: None
        """

        data = {'vips': vips}
        vips_ids = [str(vip.get('id')) for vip in vips]

        return super(ApiVipRequest, self).put('api/v3/vip-request/%s/' %
                                              ';'.join(vips_ids), data)

    def create(self, vips):
        """
        Method to create vip's

        :param vips: List containing vip's desired to be created on database
        :return: None
        """

        data = {'vips': vips}
        return super(ApiVipRequest, self).post('api/v3/vip-request/', data)

    def deploy(self, ids):
        """
        Method to deploy vip's

        :param vips: List containing vip's desired to be deployed on equipment
        :return: None
        """
        url = build_uri_with_ids('api/v3/vip-request/deploy/%s/', ids)

        return super(ApiVipRequest, self).post(url)

    def undeploy(self, ids, clean_up=0):
        """
        Method to undeploy vip's

        :param vips: List containing vip's desired to be undeployed on equipment
        :return: None
        """
        url = build_uri_with_ids('api/v3/vip-request/deploy/%s/?cleanup=%s', ids, clean_up)

        return super(ApiVipRequest, self).delete(url)

    def redeploy(self, vips):
        """
        Method to redeploy vip's

        :param vips: List containing vip's desired to updated on equipment
        :return: None
        """

        data = {'vips': vips}
        vips_ids = [str(vip.get('id')) for vip in vips]

        return super(ApiVipRequest, self).put('api/v3/vip-request/deploy/%s/' %
                                              ';'.join(vips_ids), data)