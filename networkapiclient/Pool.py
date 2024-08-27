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
import urllib.request, urllib.parse, urllib.error

from networkapiclient.ApiGenericClient import ApiGenericClient


class Pool(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(Pool, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def set_poolmember_state(self, id_pools, pools):
        """
        Enable/Disable pool member by list
        """

        data = dict()

        uri = "api/v3/pool/real/%s/member/status/" % ';'.join(id_pools)

        data["server_pools"] = pools

        return self.put(uri, data=data)

    def get_poolmember_state(self, id_pools, checkstatus=0):
        """
        Enable/Disable pool member by list
        """

        uri = "api/v3/pool/real/%s/member/status/?checkstatus=%s" % (';'.join(id_pools), checkstatus)

        return self.get(uri)

    def list_all(self, environment_id, pagination):
        """
            List All Pools To Populate Datatable

            :param pagination: Object Pagination

            :return: Following dictionary:{
                                            "total" : < total >,
                                            "pools" :[{
                                                "id": < id >
                                                "default_port": < default_port >,
                                                "identifier": < identifier >,
                                                "healthcheck": < healthcheck >,
                                            }, ... too ... ]}

            :raise NetworkAPIException: Falha ao acessar fonte de dados
        """

        uri = "api/pools/"

        data = dict()

        data["start_record"] = pagination.start_record
        data["end_record"] = pagination.end_record
        data["asorting_cols"] = pagination.asorting_cols
        data["searchable_columns"] = pagination.searchable_columns
        data["custom_search"] = pagination.custom_search or None
        data["environment_id"] = environment_id or None

        return self.post(uri, data=data)

    def list_all_by_reqvip(self, id_vip, pagination):
        """
            List All Pools To Populate Datatable

            :param pagination: Object Pagination

            :return: Following dictionary:{
                                            "total" : < total >,
                                            "pools" :[{
                                                "id": < id >
                                                "default_port": < default_port >,
                                                "identifier": < identifier >,
                                                "healthcheck": < healthcheck >,
                                            }, ... too ... ]}

            :raise NetworkAPIException: Falha ao acessar fonte de dados
        """

        uri = "api/pools/pool_list_by_reqvip/"

        data = dict()

        data["start_record"] = pagination.start_record
        data["end_record"] = pagination.end_record
        data["asorting_cols"] = pagination.asorting_cols
        data["searchable_columns"] = pagination.searchable_columns
        data["custom_search"] = pagination.custom_search or None
        data["id_vip"] = id_vip or None

        return self.post(uri, data=data)

    def inserir(self, identifier, default_port, environment, balancing, healthcheck_type, healthcheck_expect,
                healthcheck_request, old_healthcheck_id, maxcon, ip_list_full, nome_equips, id_equips, priorities,
                weight, ports_reals, servicedownaction=None):

        uri = "api/pools/insert/"

        data = dict()
        data['identifier'] = identifier
        data['default_port'] = default_port
        data['environment'] = environment
        data['balancing'] = balancing
        data['servicedownaction'] = servicedownaction
        data['healthcheck_type'] = healthcheck_type
        data['healthcheck_expect'] = healthcheck_expect
        data['healthcheck_request'] = healthcheck_request

        if old_healthcheck_id == '':
            old_healthcheck_id = None

        data['old_healthcheck_id'] = old_healthcheck_id
        data['maxcon'] = maxcon
        data['ip_list_full'] = ip_list_full
        data['id_equips'] = id_equips
        data['priorities'] = priorities
        data['ports_reals'] = ports_reals
        data['nome_equips'] = nome_equips
        data['weight'] = weight

        return self.post(uri, data=data)

    def save(self, id, identifier, default_port, environment, balancing, healthcheck_type, healthcheck_expect,
             healthcheck_request, maxcon, ip_list_full, nome_equips, id_equips, priorities,
             weight, ports_reals, id_pool_member, servicedownaction=None):

        uri = "api/pools/save/"

        data = dict()
        data['id'] = id
        data['identifier'] = identifier
        data['default_port'] = default_port
        data['environment'] = environment
        data['balancing'] = balancing
        data['servicedownaction'] = servicedownaction
        data['healthcheck_type'] = healthcheck_type
        data['healthcheck_expect'] = healthcheck_expect
        data['healthcheck_request'] = healthcheck_request
        data['maxcon'] = maxcon

        data['id_pool_member'] = id_pool_member
        data['ip_list_full'] = ip_list_full
        data['id_equips'] = id_equips
        data['priorities'] = priorities
        data['ports_reals'] = ports_reals
        data['nome_equips'] = nome_equips
        data['weight'] = weight

        return self.post(uri, data=data)

    def save_reals(self, id_server_pool, ip_list_full, nome_equips, id_equips, priorities, weight, ports_reals, id_pool_member):

        uri = "api/pools/save_reals/"

        data = dict()
        data['id_server_pool'] = id_server_pool

        data['id_pool_member'] = id_pool_member
        data['ip_list_full'] = ip_list_full
        data['id_equips'] = id_equips
        data['priorities'] = priorities
        data['ports_reals'] = ports_reals
        data['nome_equips'] = nome_equips
        data['weight'] = weight

        return self.post(uri, data=data)

    def update(self, id_server_pool, default_port, balancing, healthcheck_type, healthcheck_expect, healthcheck_request,
               old_healthcheck_id, maxcon, ip_list_full, nome_equips, id_equips, priorities, weight, ports_reals, servicedownaction=None):

        uri = "api/pools/edit/"

        data = dict()
        # data['identifier'] = identifier
        data['default_port'] = default_port
        # data['environment'] = environment
        data['balancing'] = balancing
        data['servicedownaction'] = servicedownaction
        data['healthcheck_type'] = healthcheck_type
        data['healthcheck_expect'] = healthcheck_expect
        data['healthcheck_request'] = healthcheck_request

        if old_healthcheck_id == '':
            old_healthcheck_id = None

        data['old_healthcheck_id'] = old_healthcheck_id
        data['maxcon'] = maxcon
        data['ip_list_full'] = ip_list_full
        data['id_equips'] = id_equips
        data['priorities'] = priorities
        data['ports_reals'] = ports_reals
        data['id_server_pool'] = id_server_pool
        data['nome_equips'] = nome_equips
        data['weight'] = weight

        return self.post(uri, data=data)

    def list_all_members_by_poolll_members(self, id_pools):

        uri = "api/pools/get_all_members/%s/" % id_pools

        return self.get(uri)

    def list_all_members_by_pool(self, id_server_pool, checkstatus=False, pagination=None):

        data = dict()

        uri = "api/pools/get_all_members/%s/?checkstatus=%s" % (id_server_pool, checkstatus)

        if pagination:
            data["start_record"] = pagination.start_record
            data["end_record"] = pagination.end_record
            data["asorting_cols"] = pagination.asorting_cols
            data["searchable_columns"] = pagination.searchable_columns
            data["custom_search"] = pagination.custom_search or None
            return self.post(uri, data=data)
        else:
            return self.get(uri)

    def get_equip_by_ip(self, id_ip):
        """
            Get equipment by IP id

            :param id_ip: IP id

            :return: Following dictionary:{
                                            "equipamento" :[{
                                                "id": < id >
                                                "tipo_equipamento": < tipo_equipamento >,
                                                "modelo": < modelo >,
                                                "nome": < nome >,
                                                "grupos": < grupos >
                                            }]

            :raise NetworkAPIException: Falha ao acessar fonte de dados
        """

        uri = "api/pools/get_equip_by_ip/%s/" % id_ip
        return self.get(uri)

    def list_healthchecks(self):
        """
        List all healthchecks

        :return: Following dictionary:

        ::

            {'ambiente': [{ 'id': <id_environment>,
            'grupo_l3': <id_group_l3>,
            'grupo_l3_name': <name_group_l3>,
            'ambiente_logico': <id_logical_environment>,
            'ambiente_logico_name': <name_ambiente_logico>,
            'divisao_dc': <id_dc_division>,
            'divisao_dc_name': <name_divisao_dc>,
            'filter': <id_filter>,
            'filter_name': <filter_name>,
            'link': <link> }, ... ]}


        :raise DataBaseError: Falha na networkapi ao acessar o banco de dados.
        """

        uri = "api/pools/list_healthchecks/"

        return self.get(uri)

    # def delete_pool(self, ids):
    #     """
    #         Delete Pools

    #         :param ids: List of ids

    #         :return: None on success

    #         :raise PoolConstraintVipException
    #         :raise ScriptDeletePoolException
    #         :raise InvalidIdPoolException
    #         :raise NetworkAPIException
    #     """

    #     data = dict()
    #     data["ids"] = ids

    #     uri = "api/pools/delete/"

    #     return self.post(uri, data)

    def get_by_pk(self, pk):
        uri = "api/pools/getbypk/%s/" % pk

        return self.get(uri)

    def remove(self, pools):
        """
            Remove Pools Running Script And Update to Not Created

            :param ids: List of ids

            :return: None on success

            :raise ScriptRemovePoolException
            :raise InvalidIdPoolException
            :raise NetworkAPIException
        """

        data = dict()
        data["pools"] = pools

        uri = "api/pools/v2/"

        return self.delete(uri, data)

    def create(self, pools):
        """
            Create Pools Running Script And Update to Created

            :param pools: List of pools

            :return: None on success

            :raise PoolDoesNotExistException
            :raise ScriptCreatePoolException
            :raise InvalidIdPoolException
            :raise NetworkAPIException
        """

        data = dict()
        data["pools"] = pools

        uri = "api/pools/v2/"

        return self.put(uri, data)

    def enable(self, ids):
        """
            Enable Pool Members Running Script

            :param ids: List of ids

            :return: None on success

            :raise PoolMemberDoesNotExistException
            :raise InvalidIdPoolMemberException
            :raise ScriptEnablePoolException
            :raise NetworkAPIException
        """

        data = dict()
        data["ids"] = ids

        uri = "api/pools/enable/"

        return self.post(uri, data)

    def disable(self, ids):
        """
            Disable Pool Members Running Script

            :param ids: List of ids

            :return: None on success

            :raise PoolMemberDoesNotExistException
            :raise InvalidIdPoolMemberException
            :raise ScriptDisablePoolException
            :raise NetworkAPIException
        """

        data = dict()
        data["ids"] = ids

        uri = "api/pools/disable/"

        return self.post(uri, data)

    def get_opcoes_pool_by_ambiente(self, id_ambiente):

        data = dict()
        data["id_environment"] = id_ambiente

        uri = "api/pools/get_opcoes_pool_by_ambiente/"

        return self.post(uri, data=data)

    def get_requisicoes_vip_by_pool(self, id_server_pool, pagination):

        data = dict()

        data["start_record"] = pagination.start_record
        data["end_record"] = pagination.end_record
        data["asorting_cols"] = pagination.asorting_cols
        data["searchable_columns"] = pagination.searchable_columns
        data["custom_search"] = pagination.custom_search or None

        uri = "api/pools/get_requisicoes_vip_by_pool/%s/" % id_server_pool

        return self.post(uri, data=data)

    def list_by_environment(self, environment_id):
        """
            Disable Pool Members Running Script

            :param ids: List of ids

            :return: Following dictionary:{
                                            "pools" :[{
                                                "id": < id >
                                                "default_port": < default_port >,
                                                "identifier": < identifier >,
                                                "healthcheck": < healthcheck >,
                                            }, ... too ... ]}

            :raise ObjectDoesNotExistException
            :raise ValidationException
            :raise NetworkAPIException
        """

        uri = "api/pools/list/by/environment/%s/" % (environment_id)

        return self.get(uri)

    def list_pool_members(self, pool_id):
        """
            Disable Pool Members Running Script

            :param ids: List of ids

            :return:

            :raise ObjectDoesNotExistException
            :raise ValidationException
            :raise NetworkAPIException
        """

        uri = "api/pools/list/members/%s/" % (pool_id)

        return self.get(uri)

    def list_by_environmet_vip(self, environment_vip_id):
        """
        """

        uri = "api/pools/list/by/environment/vip/%s/" % (environment_vip_id)

        return self.get(uri)

    def list_environments_with_pools(self):
        """
        """

        uri = "api/pools/list/environment/with/pools/"

        return self.get(uri)

    def list_all_environment_related_environment_vip(self):
        """
        """
        uri = "api/pools/list/environments/environmentvip/"

        return self.get(uri)

    def get_available_ips_to_add_server_pool(self, equip_name, id_ambiente):
        """
        """
        uri = "api/pools/getipsbyambiente/{}/{}/".format(equip_name, id_ambiente)

        return self.get(uri)

    #######################
    # API V3
    #######################
    def get_pool(self, pool_id):
        uri = "api/v3/pool/%s/" % pool_id

        return self.get(uri)

    def list_pool(self, search):

        uri = "api/v3/pool/?%s" % urllib.parse.urlencode({"search": search})
        return self.get(uri)

    def save_pool(self, pool):
        uri = "api/v3/pool/"

        data = dict()
        data['server_pools'] = list()
        data['server_pools'].append(pool)
        return self.post(uri, data)

    def update_pool(self, pool, pool_id):
        uri = "api/v3/pool/%s/" % pool_id

        data = dict()
        data['server_pools'] = list()
        data['server_pools'].append(pool)
        return self.put(uri, data)

    def delete_pool(self, pool_ids):
        uri = "api/v3/pool/%s/" % pool_ids

        return self.delete(uri)

    def get_pool_members(self, pool_id, checkstatus='0'):

        uri = "api/v3/pool/deploy/%s/member/status/?checkstatus=%s" % (pool_id, checkstatus)

        return self.get(uri)

    def deploy_update_pool(self, pool, pool_ids):

        uri = "api/v3/pool/deploy/%s/" % str(pool_ids)

        data = dict()
        data['server_pools'] = list()
        data['server_pools'].append(pool)
        return self.put(uri, data)

    def deploy_update_pool_members(self, pool_id, pool):

        uri = "api/v3/pool/deploy/%s/member/status/" % (pool_id)

        data = dict()
        data['server_pools'] = list()
        data['server_pools'].append(pool)
        return self.put(uri, data)

    def deploy_remove_pool(self, pool_ids):
        uri = "api/v3/pool/deploy/%s/" % pool_ids

        return self.delete(uri)

    def deploy_create_pool(self, pool_ids):
        uri = "api/v3/pool/deploy/%s/" % pool_ids

        return self.post(uri)

    def get_vip_by_pool(self, pool_id):

        uri = "api/v3/vip-request/pool/%s/" % pool_id

        return self.get(uri)

    def get_opcoes_pool_by_environment(self, env_id):

        uri = "api/v3/option-pool/environment/%s/" % env_id

        return self.get(uri)