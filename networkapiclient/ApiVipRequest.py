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


class ApiVipRequest(ApiGenericClient):
    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiVipRequest, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def add_pools(self, vip_request_id, pool_ids):
        """
        """

        uri = "api/vip/request/add/pools/"

        data = dict()

        data["vip_request_id"] = vip_request_id
        data["pool_ids"] = pool_ids

        return self.post(uri, data=data)

    def delete(self, ids, delete_pools=True):
        """
        """

        uri = "api/vip/request/delete/%s/" % (delete_pools)

        data = dict()

        data["ids"] = ids

        return self.post(uri, data=data)

    def list_environment_by_environmet_vip(self, environment_vip_id):
        """
        """

        uri = "api/vip/list/environment/by/environment/vip/%s/" % (environment_vip_id)

        return self.get(uri)

    def save(
            self,
            id_ipv4,
            id_ipv6,
            finality,
            client,
            environment,
            cache,
            persistence,
            timeout,
            host,
            areanegocio,
            nome_servico,
            l7_filter,
            vip_ports_to_pools=None,
            rule_id=None,
            pk=None
    ):
        """
        """

        data = dict()

        data['ip'] = id_ipv4
        data['ipv6'] = id_ipv6
        data['finalidade'] = finality
        data['cliente'] = client
        data['ambiente'] = environment
        data['cache'] = cache
        data['timeout'] = timeout
        data['persistencia'] = persistence
        data['timeout'] = timeout
        data['host'] = host
        data['areanegocio'] = areanegocio
        data['nome_servico'] = nome_servico
        data['l7_filter'] = l7_filter
        data['rule'] = rule_id
        data['vip_ports_to_pools'] = vip_ports_to_pools

        uri = "api/vip/request/save/"

        if pk:
            uri += "%s/" % pk
            return self.put(uri, data=data)

        return self.post(uri, data=data)

    def get_by_pk(self, pk):
        """
        Get Request Vip by Identifier.

        :param pk: Identifier Vip Request.

        :return: Following dictionary:

        {'vip': {
            'persistencia': <persistencia>,
            'id': <id>,
            'portas_servicos': [{ 'vip_port_id': <vip_port_id>, 'porta': <porta>}, ...],
            'cache': <cache>,
            'ambiente':<ambiente>,
            'cliente': <cliente>,
            'areanegocio': '<areanegocio>'
            'vip_criado': <vip_criado>,
            'id_ip': <id_ip>,
            'reals': {
                'real': [{
                    'id_ip': <id_ip>,
                    'port_real': <port_real>,
                    'real_ip': <real_ip>,
                    'port_vip': <port_vip>,
                    'real_name': <real_name>
                },...]
            },
            'id_healthcheck_expect': <id_healthcheck_expect>,
            'reals_weights':{'reals_weight': [<reals_weight>,...]},
            'host': <host>,
            'l7_filter': <l7_filter>,
            'validado': <validado>,
            'reals_prioritys':{'reals_priority':[<reals_priority>,...]},
            'finalidade': <finalidade>,
            'rule_id': <rule_id>,
            'id_ipv6': <id_ipv6>,
            'nome_servico': '<nome_servico>',
            'timeout': <timeout>,
            'pools':[{
                'lb_method': <lb_method>,
                'server_pool_members':[{
                    'status': <status>,
                    'port_real': <port_real>,
                    'weight': <weight>,
                    'ip':{'ip_formated': <ip_formated>},
                    'ipv6': {'ip_formated': <ip_formated>},
                    'equipment_name': <equipment_name>,
                    'id': <id>,
                    'priority': <priority>,
                    'limit': <limit>,
                    'healthcheck': {
                        'healthcheck_type': <healthcheck_type>
                    },
                    'identifier': '<identifier>',
                    'server_pool': <server_pool>
                },...],
                'healthcheck': <healthcheck>,
                'pool_created': <pool_created>,
                'id': <id>,
                'environment': <environment>,
                'port_vip_id': <port_vip_id>,
                'default_port': <default_port>,
                'default_limit': <default_limit>,
                'identifier': <identifier>,
                'port_vip': <port_vip>
            },...],
        }}

        :raise InvalidIdVipRequestException: Invalid Id For Vip Request.
        :raise VipRequestDoesNotExistException: Vip Request Does Not Exists.
        :raise NetworkAPIException: Fail to Access Data Base.
        """
        uri = "api/vip/request/get/%s/" % pk

        return self.get(uri)