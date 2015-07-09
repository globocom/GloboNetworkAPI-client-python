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

from networkapiclient.GenericClient import GenericClient
from networkapiclient.utils import get_list_map

class RackServers(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            RackServers,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)


    def listar_tipo_servidores(self):

        url = 'rackservers/lista-tipo-servidores/'
        code, map = self.submit(None, 'GET', url)

        key = 'tipo_servidor'
        return get_list_map(self.response(code, map, [key]), key)

    def insert_rack(
            self,
            rack,
            servidor,
            tipo_servidor,
            ambiente):

        server_map = dict()
        server_map['id_rack'] = rack
        server_map['id_equip'] = servidor
        server_map['id_tiposervidor'] = tipo_servidor
        server_map['id_ambiente'] = ambiente

        code, xml = self.submit({'server': server_map}, 'POST', 'rackservers/insert/')

        return self.response(code, xml)


