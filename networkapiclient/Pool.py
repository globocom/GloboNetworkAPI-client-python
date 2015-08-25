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
                healthcheck_request, old_healthcheck_id, maxcom, ip_list_full, nome_equips, id_equips, priorities,
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
        data['maxcom'] = maxcom
        data['ip_list_full'] = ip_list_full
        data['id_equips'] = id_equips
        data['priorities'] = priorities
        data['ports_reals'] = ports_reals
        data['nome_equips'] = nome_equips
        data['weight'] = weight

        return self.post(uri, data=data)

    def save(self, id, identifier, default_port, environment, balancing, healthcheck_type, healthcheck_expect,
                healthcheck_request, maxcom, ip_list_full, nome_equips, id_equips, priorities,
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
        data['maxcom'] = maxcom

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
               old_healthcheck_id, maxcom, ip_list_full, nome_equips, id_equips, priorities, weight, ports_reals, servicedownaction=None):

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
        data['maxcom'] = maxcom
        data['ip_list_full'] = ip_list_full
        data['id_equips'] = id_equips
        data['priorities'] = priorities
        data['ports_reals'] = ports_reals
        data['id_server_pool'] = id_server_pool
        data['nome_equips'] = nome_equips
        data['weight'] = weight

        return self.post(uri, data=data)

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

    def delete(self, ids):
        """
            Delete Pools

            :param ids: List of ids

            :return: None on success

            :raise PoolConstraintVipException
            :raise ScriptDeletePoolException
            :raise InvalidIdPoolException
            :raise NetworkAPIException
        """

        data = dict()
        data["ids"] = ids

        uri = "api/pools/delete/"

        return self.post(uri, data)

    def get_by_pk(self, pk):
        uri = "api/pools/getbypk/%s/" % pk

        return self.get(uri)

    def remove(self, ids):
        """
            Remove Pools Running Script And Update to Not Created

            :param ids: List of ids

            :return: None on success

            :raise ScriptRemovePoolException
            :raise InvalidIdPoolException
            :raise NetworkAPIException
        """

        data = dict()
        data["ids"] = ids

        uri = "api/pools/remove/"

        return self.post(uri, data)

    def create(self, ids):
        """
            Create Pools Running Script And Update to Created

            :param ids: List of ids

            :return: None on success

            :raise PoolDoesNotExistException
            :raise ScriptCreatePoolException
            :raise InvalidIdPoolException
            :raise NetworkAPIException
        """

        data = dict()
        data["ids"] = ids

        uri = "api/pools/create/"

        return self.post(uri, data)

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