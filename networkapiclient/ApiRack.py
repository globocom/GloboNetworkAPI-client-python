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

import logging
from networkapiclient.ApiGenericClient import ApiGenericClient


log = logging.getLogger(__name__)


class ApiRack(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(ApiRack,self).__init__( networkapi_url, user, password, user_ldap)


    def insert_rack(self, rack):

        data = dict()
        data['rack'] = list()
        data['rack'] = rack

        uri = "api/rack/"

        return self.post(uri, data)


    def rack_vlans( self, rack_id):

        data = dict()
        uri = "rack/alocar-config/" + str(rack_id) + "/"

        return self.post(uri, data=data)


    def rack_files( self, rack_id):

        data = dict()
        uri = "rack/gerar-configuracao/" + str(rack_id) + "/"

        return self.post(uri, data=data)


    def rack_deploy( self, rack_id):

        data = dict()
        uri = "api/rack/" + str(rack_id) + "/equipments/"
        return self.post(uri, data=data)


    def rack_delete( self, rack_id):

        data = dict()
        uri = "rack/" + str(rack_id)

        return self.delete(uri, data=data)


    def next_rack_number(self):
        """
        Method to return the next available rack number
        Param: None
        Return interger
        """

        uri = "/api/rack/next/"
        return self.get(uri)


    def list(self):
        """
        :return: Dictionary with the following structure:

        ::

            {Rack: {rack_number: < rack_number >,
            'sw1':< sw1 >,
            'mac1':< mac1 >,
            'sw2':< sw2 >,
            'mac2':< mac2 >,
            'ilo':< ilo >,
            'mac_ilo':< mac_ilo > } }

        :raise DataBaseError: Can't connect to networkapi database.
        :raise XMLError: Failed to generate the XML response.
        """

        uri = '/api/rack/list/all/'
        return self.get(uri)

##########

    def save_dc(self, dc):

        data = dict()
        data['dc'] = list()
        data['dc'] = dc

        uri = "api/dc/"

        return self.post(uri, data)


    def get_dc(self, dc_id=None, dcname=None, address=None):

        data = dict()

        if dc_id:
            uri = "api/dc/id/%s/" % dc_id
        elif dcname:
            uri = "api/dc/name/%s/" % dcname
        elif address:
            uri = "api/dc/address/%s/" % address
        else:
            uri = "api/dc/"

        return self.get(uri)


    def list(self):
        uri = "api/dc/"
        return self.get(uri)


    def save_fabric(self, dcroom):

        log.info("Post Fabric")

        data = dict()
        data['dcrooms'] = list()
        data['dcrooms'] = dcroom

        uri = "api/dcrooms/"

        return self.post(uri, data)


    def put_fabric(self, fabric_id, fabric):

        data = dict()
        data['fabric'] = fabric

        uri = "api/dcrooms/id/%s/" % fabric_id

        return self.put(uri, data)


    def newrack(self, rack):

        data = dict()
        data['rack'] = rack

        uri = "api/rack/"

        return self.post(uri, data)


    def get_fabric(self, dc_id=None, name=None, fabric_id=None):

        data = dict()

        if fabric_id:
            uri = "api/dcrooms/id/%s/" % fabric_id
        elif name:
            uri = "api/dcrooms/name/%s/" % name
        elif dc_id:
            uri = "api/dcrooms/dc/%s/" % dc_id
        else:
            uri = "api/dcrooms/"

        return self.get(uri)


    def get_rack(self, fabric_id=None, rack_id=None):

        data = dict()

        if fabric_id:
            uri = "api/rack/fabric/%s/" % fabric_id
        elif rack_id:
            uri = "api/rack/%s/" % rack_id
        else:
            uri = "api/rack/list/all/"

        return self.get(uri)


    def put_rack(self, rack_id, rack):

        data = dict()
        data['rack'] = rack

        uri = "api/rack/%s/" % rack_id

        return self.put(uri, data)


    def rackenvironments( self, rack_id):

        data = dict()
        uri = "api/rack/environmentvlan/" + str(rack_id) + "/"

        return self.post(uri, data=data)


    def rackfiles( self, rack_id):

        data = dict()
        uri = "api/rack/config/" + str(rack_id) + "/"

        return self.post(uri, data=data)


    def delete_rack( self, rack_id):

        data = dict()
        uri = "api/rack/" + str(rack_id)

        return self.delete(uri, data=data)