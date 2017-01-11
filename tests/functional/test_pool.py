import os
from unittest import TestCase

from nose.tools import assert_equal
from nose.tools import assert_in
from nose.tools import assert_is_instance
from nose.tools import assert_raises

from networkapiclient.ClientFactory import ClientFactory
from networkapiclient.exception import NetworkAPIClientError

NETWORKAPI_URL = os.getenv('NETWORKAPI_URL', 'http://10.0.0.2:8000/')
NETWORKAPI_USER = os.getenv('NETWORKAPI_USER', 'networkapi')
NETWORKAPI_PWD = os.getenv('NETWORKAPI_PWD', 'networkapi')


class TestApiPool(TestCase):
    def setUp(self):
        self.client = ClientFactory(NETWORKAPI_URL, NETWORKAPI_USER,
                                    NETWORKAPI_PWD)
        self.api_environment = self.client.create_api_environment()
        self.api_equipment = self.client.create_api_equipment()
        self.api_pool = self.client.create_api_pool()
        self.api_environment_vip = self.client.create_api_environment_vip()
        self.api_vlan = self.client.create_api_vlan()
        self.api_network_ipv4 = self.client.create_api_network_ipv4()
        self.api_network_ipv6 = self.client.create_api_network_ipv6()
        self.api_ipv4 = self.client.create_api_ipv4()
        self.api_ipv6 = self.client.create_api_ipv6()

    def tearDown(self):
        pass

    # post tests - no deploy

    def test_create_pool_without_reals(self):
        """ Tries to create a pool without reals """

        pool_data = [{
            'identifier': 'Pool-Test-Network-API-Without-Reals',
            'default_port': 555,
            'environment': 1,
            'servicedownaction': {
                'id': 6,
                'name': 'drop'
            },
            'lb_method': 'least-conn',
            'healthcheck': {
                'identifier': 'Test-Network-API-Ident',
                'healthcheck_type': 'TCP',
                'healthcheck_request': '',
                'healthcheck_expect': '',
                'destination': '*:*'
            },
            'default_limit': 0,
            'server_pool_members': [
            ],
            'pool_created': False
        }]

        pool_id = self.api_pool.create(pool_data)[0]['id']
        pool = self.api_pool.get([pool_id])

        assert_equal(pool['server_pools'][0]['id'], pool_id)
        self.api_pool.delete([pool_id])

    def test_create_pool_with_two_reals_and_https_protocol(self):
        """ Tries to create a pool with one real and https protocol in healthcheck """

        id_env_of_eqpt = self.create_environment_of_equipment()
        id_env_of_pool = self.create_environment_of_pool()

        id_env_vip = self.create_environment_vip(id_env_of_eqpt)

        id_vlan_of_env_eqpt = self.create_vlan(id_env_of_eqpt)
        id_vlan_of_env_pool = self.create_vlan(id_env_of_pool)

        id_netipv4_of_vlan_env_eqpt = self.create_netipv4(id_vlan_of_env_eqpt, None)
        id_netipv6_of_vlan_env_eqpt = self.create_netipv6(id_vlan_of_env_eqpt, None)

        id_netipv4_of_vlan_env_pool = self.create_netipv4(id_vlan_of_env_pool, id_env_vip)
        id_netipv6_of_vlan_env_pool = self.create_netipv6(id_vlan_of_env_pool, id_env_vip)

        # creating three reals (servers) equipments

        id_reals = [self.create_real_equipment(i, id_env_of_eqpt) for i in range(1)]

        id_load_balancer = self.create_load_balancer_equipment(id_env_of_pool)

        ipsv4_of_reals = [self.create_ipv4(id_netipv4_of_vlan_env_eqpt) for id_real in id_reals]

        ipsv6_of_reals = [self.create_ipv6(id_netipv6_of_vlan_env_eqpt) for id_real in id_reals]

        pool_data = [{
            'identifier': 'Pool-Test-Network-API-With-Real-And-HTTPS-Prot',
            'default_port': 443,
            'environment': id_env_of_pool,
            'servicedownaction': {
                'id': 5,
                'name': 'none'
            },
            'lb_method': 'least-conn',
            'healthcheck': {
                'identifier': 'Test-Network-API-Ident',
                'healthcheck_type': 'HTTPS',
                'healthcheck_request': '',
                'healthcheck_expect': '',
                'destination': '*:*'
            },
            'default_limit': 0,
            'server_pool_members': [
                {
                    'ip': {
                        'id': ipsv4_of_reals[0]['id'],
                        'ip_formated': ipsv4_of_reals[0]['ip_formated']
                    },
                    'ipv6': None,
                    'priority': 0,
                    'weight': 0,
                    'limit': 0,
                    'port_real': 442,
                    'member_status': 7,
                    'last_status_update_formated': None,
                    'equipment': {
                        'id': id_reals[0]
                    }
                }
            ],
            'pool_created': False
        }]

        pool_id = self.api_pool.create(pool_data)[0]['id']
        pool = self.api_pool.get([pool_id])

        assert_equal(pool['server_pools'][0]['id'], pool_id)
        self.api_pool.delete([pool_id])

        # deleting all created

        for ipv4 in ipsv4_of_reals:
            self.api_ipv4.delete([ipv4['id']])

        for ipv6 in ipsv6_of_reals:
            self.api_ipv6.delete([ipv6['id']])

        self.api_network_ipv4.delete([id_netipv4_of_vlan_env_eqpt, id_netipv4_of_vlan_env_pool])
        self.api_network_ipv6.delete([id_netipv6_of_vlan_env_eqpt, id_netipv6_of_vlan_env_pool])

        self.api_vlan.delete([id_vlan_of_env_eqpt, id_vlan_of_env_pool])

        self.api_equipment.delete(id_reals)
        self.api_equipment.delete([id_load_balancer])

        self.api_environment_vip.delete([id_env_vip])

        self.api_environment.delete([id_env_of_eqpt, id_env_of_pool])

    def test_create_pool_with_one_real_and_tcp_protocol(self):
        """ Tries to create a pool with one real and tcp protocol """

        # pool_data = [{
        #     'identifier': 'Pool-Test-Network-API-With-Real-And-TCP-Prot',
        #     'default_port': 20,
        #     'environment': 1,
        #     'servicedownaction': {
        #         'id': 5,
        #         'name': 'none'
        #     },
        #     'lb_method': 'least-conn',
        #     'healthcheck': {
        #         'identifier': 'Test-Network-API-Ident',
        #         'healthcheck_type': 'TCP',
        #         'healthcheck_request': '',
        #         'healthcheck_expect': '',
        #         'destination': '*:*'
        #     },
        #     'default_limit': 0,
        #     'server_pool_members': [
        #         {
        #             'ip': {
        #                 'id': 7,
        #                 'ip_formated': '10.237.128.1'
        #             },
        #             'ipv6': None,
        #             'priority': 0,
        #             'weight': 0,
        #             'limit': 0,
        #             'port_real': 20,
        #             'member_status': 7,
        #             'last_status_update_formated': None,
        #             'equipment': {
        #                 'id': 14
        #             }
        #         }
        #     ],
        #     'pool_created': False
        # }]
        #
        # pool_id = self.api_pool.create(pool_data)[0]['id']
        # pool = self.api_pool.get([pool_id])
        #
        # assert_equal(pool['server_pools'][0]['id'], pool_id)
        # self.api_pool.delete([pool_id])

    def test_create_pool_with_one_real_and_udp_protocol(self):
        """ Tries to create a pool with one real and udp protocol """

        pass

    def test_create_pool_with_one_real_and_http_protocol(self):
        """ Tries to create a pool with one real and http protocol """

        pass

    def test_create_pool_with_three_reals_and_weight_balancing(self):
        """ Tries to create a pool with three reals and weight balancing """

        pass

    def test_create_pool_with_three_reals_and_least_conn_balancing(self):
        """ Tries to create a pool with three reals and least-conn balancing """

        pass

    def create_environment_vip(self, id_env):
        env_vip_data = [
            {
                'finalidade_txt': 'Fin-Test',
                'cliente_txt': 'ClientTxt-Test',
                'ambiente_p44_txt': 'EnvP44Txt-Test',
                'description': 'Description-Test',
                'name': 'EnvVIP NetworkAPI Test',
                'environments': [
                    {
                        'environment': id_env
                    }
                ]
            }
        ]

        return self.api_environment_vip.create(env_vip_data)[0]['id']

    def create_vlan(self, id_env):
        vlan_data = [
            {
                'name': 'Vlan of Test',
                'environment': id_env,
            }
        ]

        return self.api_vlan.create(vlan_data)[0]['id']

    def create_environment_of_equipment(self):
        env_data = [
            {
                'grupo_l3': 33,
                'ambiente_logico': 11,
                'divisao_dc': 21,
                'filter': None,
                'acl_path': None,
                'ipv4_template': None,
                'ipv6_template': None,
                'link': None,
                'min_num_vlan_1': 1,
                'max_num_vlan_1': 500,
                'min_num_vlan_2': 501,
                'max_num_vlan_2': 1000,
                'vrf': None,
                'default_vrf': 1,
                'configs': [{
                    'subnet': '192.168.104.0/22',
                    'new_prefix': '27',
                    'type': 'v4',
                    'network_type': 2
                }, {
                    'subnet': 'fdbe:bebe:bebe:11c0:0000:0000:0000:0000/58',
                    'new_prefix': '64',
                    'type': 'v6',
                    'network_type': 2
                }]
            }

        ]

        return self.api_environment.create(env_data)[0]['id']

    def create_environment_of_pool(self):
        env_data = [

            {
                'grupo_l3': 33,
                'ambiente_logico': 12,
                'divisao_dc': 21,
                'filter': None,
                'acl_path': None,
                'ipv4_template': None,
                'ipv6_template': None,
                'link': None,
                'min_num_vlan_1': 1,
                'max_num_vlan_1': 500,
                'min_num_vlan_2': 501,
                'max_num_vlan_2': 1000,
                'vrf': None,
                'default_vrf': 1,
                'configs': [{
                    'subnet': '10.237.128.0/18',
                    'new_prefix': '28',
                    'type': 'v4',
                    'network_type': 2
                }, {
                    'subnet': 'fdbe:bebe:bebe:1200:0:0:0:0/57',
                    'new_prefix': '64',
                    'type': 'v6',
                    'network_type': 2
                }]
            }
        ]

        return self.api_environment.create(env_data)[0]['id']

    def create_real_equipment(self, name_eqpt, id_env):
        eqpt_data = [
            {
                'name': 'Server %s' % name_eqpt,
                'maintenance': False,
                'equipment_type': 2,
                'model': 1,
                'environments': [
                    {
                        'environment': id_env,
                        'is_router': False
                    }
                ]
            }
        ]

        return self.api_equipment.create(eqpt_data)[0]['id']

    def create_load_balancer_equipment(self, id_env):
        eqpt_data = [
            {
                'name': 'Load Balancer',
                'maintenance': False,
                'equipment_type': 5,
                'model': 1,
                'environments': [
                    {
                        'environment': id_env,
                        'is_router': False
                    }
                ]

            }
        ]

        return self.api_equipment.create(eqpt_data)[0]['id']

    def create_netipv4(self, id_vlan, id_env_vip):
        net_data = [
            {
                'vlan': id_vlan,
                'network_type': 2,
                'environmentvip': id_env_vip
            }
        ]

        return self.api_network_ipv4.create(net_data)[0]['id']

    def create_netipv6(self, id_vlan, id_env_vip):
        net_data = [
            {
                'vlan': id_vlan,
                'network_type': 2,
                'environmentvip': id_env_vip
            }
        ]

        return self.api_network_ipv6.create(net_data)[0]['id']

    def create_ipv4(self, id_net):
        ip_data = [
            {
                'networkipv4': id_net,
                'description': 'IP of Real'
            }
        ]

        id_ip = self.api_ipv4.create(ip_data)[0]['id']
        return self.api_ipv4.get([id_ip], fields=['id', 'ip_formated'])['ips'][0]

    def create_ipv6(self, id_net):
        ip_data = [
            {
                'networkipv6': id_net,
                'description': 'IP of Real'
            }
        ]

        id_ip = self.api_ipv6.create(ip_data)[0]['id']
        return self.api_ipv6.get([id_ip], fields=['id', 'ip_formated'])['ips'][0]
