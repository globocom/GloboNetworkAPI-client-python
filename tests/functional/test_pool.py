# -*- coding: utf-8 -*-
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
        self.api_pool_deploy = self.client.create_api_pool_deploy()

        self.ipsv4 = [{'id': 7, 'ip_formated': '192.168.104.2'},
                      {'id': 8, 'ip_formated': '192.168.104.3'},
                      {'id': 9, 'ip_formated': '192.168.104.4'},
                      {'id': 10, 'ip_formated': '192.168.104.5'},
                      {'id': 11, 'ip_formated': '192.168.104.6'}]

        self.id_env_of_pool = 10

    def tearDown(self):
        pass

    # post tests - no deploy

    def test_create_pool_without_reals(self):
        """ Tries to create a pool without reals """

        pool_data = self.build_pool(id_env_of_pool=self.id_env_of_pool)

        pool_id = self.api_pool.create([pool_data])[0]['id']

        pool = self.api_pool.get([pool_id])

        assert_equal(pool['server_pools'][0]['id'], pool_id)
        self.api_pool.delete([pool_id])

    def test_create_pool_with_one_real_and_https_protocol(self):
        """ Tries to create a pool with one real and HTTPS protocol
            in healthcheck
        """

        qt_reals = range(1)

        server_pool_members = [
            self.build_server_pool_member(
                ip__id=self.ipsv4[i]['id'],
                ip__ip_formated=self.ipsv4[i]['ip_formated'],
                port_real=1000 +
                i) for i in qt_reals]

        healthcheck_healthcheck_type = 'HTTPS'

        pool_data = self.build_pool(
            server_pool_members=server_pool_members,
            healthcheck__healthcheck_type=healthcheck_healthcheck_type,
            id_env_of_pool=self.id_env_of_pool)

        pool_id = self.api_pool.create([pool_data])[0]['id']

        pool = self.api_pool.get([pool_id])

        assert_equal(pool['server_pools'][0]['id'], pool_id)
        assert_equal(
            pool['server_pools'][0]['healthcheck']['healthcheck_type'],
            healthcheck_healthcheck_type)

        self.api_pool.delete([pool_id])

    def test_create_pool_with_one_real_and_tcp_protocol(self):
        """ Tries to create a pool with one real and TCP protocol
            in healthcheck
        """

        qt_reals = range(1)

        server_pool_members = [
            self.build_server_pool_member(
                ip__id=self.ipsv4[i]['id'],
                ip__ip_formated=self.ipsv4[i]['ip_formated'],
                port_real=1000 +
                i) for i in qt_reals]

        healthcheck_healthcheck_type = 'TCP'

        pool_data = self.build_pool(
            server_pool_members=server_pool_members,
            healthcheck__healthcheck_type=healthcheck_healthcheck_type,
            id_env_of_pool=self.id_env_of_pool)

        pool_id = self.api_pool.create([pool_data])[0]['id']

        pool = self.api_pool.get([pool_id])

        assert_equal(pool['server_pools'][0]['id'], pool_id)
        assert_equal(
            pool['server_pools'][0]['healthcheck']['healthcheck_type'],
            healthcheck_healthcheck_type)

        self.api_pool.delete([pool_id])

    def test_create_pool_with_one_real_and_udp_protocol(self):
        """ Tries to create a pool with one real and UDP protocol
            in healthcheck
        """

        qt_reals = range(1)

        server_pool_members = [
            self.build_server_pool_member(
                ip__id=self.ipsv4[i]['id'],
                ip__ip_formated=self.ipsv4[i]['ip_formated'],
                port_real=1000 +
                i) for i in qt_reals]

        healthcheck_healthcheck_type = 'UDP'

        pool_data = self.build_pool(
            server_pool_members=server_pool_members,
            healthcheck__healthcheck_type=healthcheck_healthcheck_type,
            id_env_of_pool=self.id_env_of_pool)

        pool_id = self.api_pool.create([pool_data])[0]['id']

        pool = self.api_pool.get([pool_id])

        assert_equal(pool['server_pools'][0]['id'], pool_id)
        assert_equal(
            pool['server_pools'][0]['healthcheck']['healthcheck_type'],
            healthcheck_healthcheck_type)

        self.api_pool.delete([pool_id])

    def test_create_pool_with_one_real_and_http_protocol(self):
        """ Tries to create a pool with one real and HTTP protocol
            in healthcheck
        """

        qt_reals = range(1)

        server_pool_members = [
            self.build_server_pool_member(
                ip__id=self.ipsv4[i]['id'],
                ip__ip_formated=self.ipsv4[i]['ip_formated'],
                port_real=1000 +
                i) for i in qt_reals]

        healthcheck_healthcheck_type = 'HTTP'

        pool_data = self.build_pool(
            server_pool_members=server_pool_members,
            healthcheck__healthcheck_type=healthcheck_healthcheck_type,
            id_env_of_pool=self.id_env_of_pool)

        pool_id = self.api_pool.create([pool_data])[0]['id']

        pool = self.api_pool.get([pool_id])

        assert_equal(pool['server_pools'][0]['id'], pool_id)
        assert_equal(
            pool['server_pools'][0]['healthcheck']['healthcheck_type'],
            healthcheck_healthcheck_type)

        self.api_pool.delete([pool_id])

    def test_create_pool_with_three_reals_and_weight_balancing(self):
        """ Tries to create a pool with three reals and weight balancing """

        qt_reals = range(3)

        weights = [1, 2, 1]

        server_pool_members = [
            self.build_server_pool_member(
                ip__id=self.ipsv4[i]['id'],
                ip__ip_formated=self.ipsv4[i]['ip_formated'],
                port_real=1000 + i,
                weight=weights[i]) for i in qt_reals]

        pool_data = self.build_pool(
            server_pool_members=server_pool_members,
            id_env_of_pool=self.id_env_of_pool)

        pool_id = self.api_pool.create([pool_data])[0]['id']

        pool = self.api_pool.get([pool_id])

        assert_equal(pool['server_pools'][0]['id'], pool_id)

        self.api_pool.delete([pool_id])

    def test_create_pool_with_three_reals_and_least_conn_balancing(self):
        """ Tries to create a pool with three reals and
            least-conn balancing
        """

        qt_reals = range(3)

        priorities = [1, 2, 1]

        server_pool_members = [
            self.build_server_pool_member(
                ip__id=self.ipsv4[i]['id'],
                ip__ip_formated=self.ipsv4[i]['ip_formated'],
                port_real=1000 + i,
                priority=priorities[i]) for i in qt_reals]

        pool_data = self.build_pool(
            server_pool_members=server_pool_members,
            id_env_of_pool=self.id_env_of_pool)

        pool_id = self.api_pool.create([pool_data])[0]['id']

        pool = self.api_pool.get([pool_id])

        assert_equal(pool['server_pools'][0]['id'], pool_id)

        self.api_pool.delete([pool_id])

    # put tests - no deploy

    def test_update_pool_without_reals(self):
        """ Tries to update pool without reals adding two reals to it """

        qt_reals = range(2)

        pool_data = self.build_pool(
            id_env_of_pool=self.id_env_of_pool)
        pool_id = self.api_pool.create([pool_data])[0]['id']

        server_pool_members = [
            self.build_server_pool_member(
                ip__id=self.ipsv4[i]['id'],
                ip__ip_formated=self.ipsv4[i]['ip_formated'],
                port_real=1000 +
                i) for i in qt_reals]

        new_pool_data = self.build_pool(
            id=pool_id,
            id_env_of_pool=self.id_env_of_pool,
            identifier='Pool-New-Test',
            servicedownaction__name='drop',
            healthcheck__healthcheck_type='HTTPS',
            server_pool_members=server_pool_members)

        self.api_pool.update([new_pool_data])

        pool = self.api_pool.get([pool_id])['server_pools'][0]

        assert_equal(pool['identifier'], new_pool_data['identifier'])
        assert_equal(
            pool['servicedownaction']['name'],
            new_pool_data['servicedownaction']['name'])
        assert_equal(
            pool['healthcheck']['healthcheck_type'],
            new_pool_data['healthcheck']['healthcheck_type'])

        assert_equal(len(pool['server_pool_members']), 2)

        self.api_pool.delete([pool_id])

    def test_update_pool_with_reals_removing_them(self):
        """ Tries to update pool with reals removing them """

        qt_reals = range(2)

        server_pool_members = [
            self.build_server_pool_member(
                ip__id=self.ipsv4[i]['id'],
                ip__ip_formated=self.ipsv4[i]['ip_formated'],
                port_real=1000 +
                i) for i in qt_reals]

        pool_data = self.build_pool(
            id_env_of_pool=self.id_env_of_pool,
            server_pool_members=server_pool_members)

        pool_id = self.api_pool.create([pool_data])[0]['id']

        new_pool_data = self.build_pool(
            id=pool_id,
            id_env_of_pool=self.id_env_of_pool)

        self.api_pool.update([new_pool_data])

        pool = self.api_pool.get([pool_id])['server_pools'][0]

        assert_equal(len(pool['server_pool_members']), 0)

        self.api_pool.delete([pool_id])

    def test_update_pool_removing_half_of_reals(self):
        """ Tries to remove half of the reals in a server pool """

        qt_reals = range(4)

        server_pool_members = [
            self.build_server_pool_member(
                ip__id=self.ipsv4[i]['id'],
                ip__ip_formated=self.ipsv4[i]['ip_formated'],
                port_real=1000 +
                i) for i in qt_reals]

        pool_data = self.build_pool(
            id_env_of_pool=self.id_env_of_pool,
            server_pool_members=server_pool_members)

        pool_id = self.api_pool.create([pool_data])[0]['id']

        half = range(2)
        for i in half:
            server_pool_members.pop()

        new_pool_data = self.build_pool(
            id=pool_id,
            id_env_of_pool=self.id_env_of_pool,
            server_pool_members=server_pool_members)

        self.api_pool.update([new_pool_data])

        pool = self.api_pool.get([pool_id])['server_pools'][0]

        assert_equal(len(pool['server_pool_members']), 2)

        self.api_pool.delete([pool_id])

    def test_update_pool_removing_half_of_reals_and_adding_another(self):
        """ Tries to remove half of the reals in a server pool and
            at same time add a new real
        """

        qt_reals = range(5)

        server_pool_members = [
            self.build_server_pool_member(
                ip__id=self.ipsv4[i]['id'],
                ip__ip_formated=self.ipsv4[i]['ip_formated'],
                port_real=1000 +
                i) for i in range(4)]

        pool_data = self.build_pool(
            id_env_of_pool=self.id_env_of_pool,
            server_pool_members=server_pool_members)

        pool_id = self.api_pool.create([pool_data])[0]['id']

        half = range(2)
        for i in half:
            server_pool_members.pop()

        server_pool_members += [self.build_server_pool_member(
            ip__id=self.ipsv4[i]['id'],
            ip__ip_formated=self.ipsv4[i]['ip_formated'],
            port_real=1000 +
            i) for i in range(4, 5)]

        new_pool_data = self.build_pool(
            id=pool_id,
            id_env_of_pool=self.id_env_of_pool,
            server_pool_members=server_pool_members)

        self.api_pool.update([new_pool_data])

        pool = self.api_pool.get([pool_id])['server_pools'][0]

        assert_equal(len(pool['server_pool_members']), 3)

        self.api_pool.delete([pool_id])

    # delete tests

    def test_delete_pool_without_reals(self):
        """ Tries to delete pool without reals """

        pool_data = self.build_pool(
            id_env_of_pool=1)

        pool_id = self.api_pool.create([pool_data])[0]['id']

        self.api_pool.delete([pool_id])
        with assert_raises(NetworkAPIClientError):
            self.api_pool.get([pool_id])

    def test_delete_pool_with_reals(self):
        """ Tries to delete pool with five reals """

        qt_reals = range(5)

        server_pool_members = [
            self.build_server_pool_member(
                ip__id=self.ipsv4[i]['id'],
                ip__ip_formated=self.ipsv4[i]['ip_formated'],
                port_real=1000 +
                i) for i in qt_reals]

        pool_data = self.build_pool(
            id_env_of_pool=self.id_env_of_pool,
            server_pool_members=server_pool_members)

        pool_id = self.api_pool.create([pool_data])[0]['id']

        self.api_pool.delete([pool_id])
        with assert_raises(NetworkAPIClientError):
            self.api_pool.get([pool_id])

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

    def create_ipv4(self, id_net, id_equip):
        ip_data = [
            {
                'networkipv4': id_net,
                'description': 'IP of Real',
                'equipments': [
                    {'id': id_equip}
                ]
            }
        ]

        id_ip = self.api_ipv4.create(ip_data)[0]['id']
        return self.api_ipv4.get(
            [id_ip],
            fields=[
                'id',
                'ip_formated'])['ips'][0]

    def create_ipv6(self, id_net, id_equip):
        ip_data = [
            {
                'networkipv6': id_net,
                'description': 'IP of Real',
                'equipments': [
                    {'id': id_equip}
                ]
            }
        ]

        id_ip = self.api_ipv6.create(ip_data)[0]['id']
        return self.api_ipv6.get(
            [id_ip],
            fields=[
                'id',
                'ip_formated'])['ips'][0]

    def create_initial_data(self, **kwargs):

        weights = None
        priorities = None
        qt_reals = 0

        for key in kwargs:
            if key == 'qt_reals':
                qt_reals = kwargs[key]
            elif key == 'weights':
                weights = kwargs[key]
            elif key == 'priorities':
                priorities = kwargs[key]

        id_env_of_eqpt = self.create_environment_of_equipment()
        id_env_of_pool = self.create_environment_of_pool()

        id_env_vip = self.create_environment_vip(id_env_of_eqpt)

        id_vlan_of_env_eqpt = self.create_vlan(id_env_of_eqpt)
        id_vlan_of_env_pool = self.create_vlan(id_env_of_pool)

        id_netipv4_of_vlan_env_eqpt = self.create_netipv4(
            id_vlan_of_env_eqpt,
            None)
        id_netipv6_of_vlan_env_eqpt = self.create_netipv6(
            id_vlan_of_env_eqpt,
            None)

        id_netipv4_of_vlan_env_pool = self.create_netipv4(
            id_vlan_of_env_pool,
            id_env_vip)
        id_netipv6_of_vlan_env_pool = self.create_netipv6(
            id_vlan_of_env_pool,
            id_env_vip)

        # creating three reals (servers) equipments

        id_reals = [
            self.create_real_equipment(
                i,
                id_env_of_eqpt) for i in qt_reals]

        id_load_balancer = self.create_load_balancer_equipment(id_env_of_pool)

        ipsv4_of_reals = [
            self.create_ipv4(
                id_netipv4_of_vlan_env_eqpt,
                id_real) for id_real in id_reals]

        ipsv6_of_reals = [
            self.create_ipv6(
                id_netipv6_of_vlan_env_eqpt,
                id_real) for id_real in id_reals]

        return {
            'id_env_of_eqpt': id_env_of_eqpt,
            'id_env_of_pool': id_env_of_pool,
            'id_env_vip': id_env_vip,
            'id_vlan_of_env_eqpt': id_vlan_of_env_eqpt,
            'id_vlan_of_env_pool': id_vlan_of_env_pool,
            'id_netipv4_of_vlan_env_eqpt': id_netipv4_of_vlan_env_eqpt,
            'id_netipv6_of_vlan_env_eqpt': id_netipv6_of_vlan_env_eqpt,
            'id_netipv4_of_vlan_env_pool': id_netipv4_of_vlan_env_pool,
            'id_netipv6_of_vlan_env_pool': id_netipv6_of_vlan_env_pool,
            'id_reals': id_reals,
            'id_load_balancer': id_load_balancer,
            'ipsv4_of_reals': ipsv4_of_reals,
            'ipsv6_of_reals': ipsv6_of_reals,
            'weights': weights if weights is not None else None,
            'priorities': priorities if priorities is not None else None
        }

    def delete_initial_data(self, initial_data):

        for ipv4 in self.ipsv4:
            self.api_ipv4.delete([ipv4['id']])

        for ipv6 in initial_data['ipsv6_of_reals']:
            self.api_ipv6.delete([ipv6['id']])

        self.api_network_ipv4.delete(
            [initial_data['id_netipv4_of_vlan_env_eqpt']])
        self.api_network_ipv4.delete(
            [initial_data['id_netipv4_of_vlan_env_pool']])
        self.api_network_ipv6.delete(
            [initial_data['id_netipv6_of_vlan_env_eqpt']])
        self.api_network_ipv6.delete(
            [initial_data['id_netipv6_of_vlan_env_pool']])

        self.api_vlan.delete([initial_data['id_vlan_of_env_eqpt']])
        self.api_vlan.delete([initial_data['id_vlan_of_env_pool']])

        self.api_equipment.delete(initial_data['id_reals'])
        self.api_equipment.delete([initial_data['id_load_balancer']])

        self.api_environment_vip.delete([initial_data['id_env_vip']])

        self.api_environment.delete([initial_data['id_env_of_eqpt']])
        self.api_environment.delete([initial_data['id_env_of_pool']])

    def build_pool(self, **kwargs):

        id_env_of_pool = None
        healthcheck__healthcheck_type = None
        server_pool_members = None
        id = None
        identifier = None
        servicedownaction__name = None

        for key in kwargs:
            if key == 'id_env_of_pool':
                id_env_of_pool = kwargs[key]
            elif key == 'healthcheck__healthcheck_type':
                healthcheck__healthcheck_type = kwargs[key]
            elif key == 'server_pool_members':
                server_pool_members = kwargs[key]
            elif key == 'id':
                id = kwargs[key]
            elif key == 'identifier':
                identifier = kwargs[key]
            elif key == 'servicedownaction__name':
                servicedownaction__name = kwargs[key]

        return {
            'id': id,
            'identifier': identifier if identifier is not None else 'Pool-Test',
            'default_port': 443,
            'environment': id_env_of_pool,
            'servicedownaction': {
                'name': servicedownaction__name
                if servicedownaction__name is not None
                else 'none'
            },
            'lb_method': 'least-conn',
            'healthcheck': {
                'identifier': 'Test-Network-API-Ident',
                'healthcheck_type': healthcheck__healthcheck_type
                if healthcheck__healthcheck_type is not None
                else 'HTTP',
                'healthcheck_request': '',
                'healthcheck_expect': '',
                'destination': '*:*'},
            'default_limit': 0,
            'server_pool_members': server_pool_members
            if server_pool_members is not None
            else []
        }

    def build_server_pool_member(self, **kwargs):

        ip__id = None
        ip__ip_formated = None

        ipv6__id = None
        ipv6__ip_formated = None

        port_real = None
        weight = None
        priority = None

        id = None

        for key in kwargs:

            if key == 'ip__id':
                ip__id = kwargs[key]
            elif key == 'ip__ip_formated':
                ip__ip_formated = kwargs[key]
            elif key == 'ipv6__id':
                ipv6__id = kwargs[key]
            elif key == 'ipv6__ip_formated':
                ipv6__ip_formated = kwargs[key]
            elif key == 'port_real':
                port_real = kwargs[key]
            elif key == 'weight':
                weight = kwargs[key]
            elif key == 'priority':
                priority = kwargs[key]
            elif key == 'id':
                id = kwargs[key]

        return {
            'id': id,
            'ip': {
                'id': ip__id,
                'ip_formated': ip__ip_formated
            } if ip__id is not None and ip__ip_formated is not None else None,
            'ipv6': {
                'id': ip__id,
                'ip_formated': ip__ip_formated
            } if ipv6__id is not None and ipv6__ip_formated is not None else None,
            'priority': priority if priority is not None else 0,
            'weight': weight if weight is not None else 0,
            'limit': 0,
            'port_real': port_real,
            'member_status': 7,
            'last_status_update_formated': None
        }
