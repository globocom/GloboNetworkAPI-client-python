# -*- coding: utf-8 -*-
import os
from unittest import TestCase

from nose.tools import assert_equal
from nose.tools import assert_greater
from nose.tools import assert_in
from nose.tools import assert_is_instance
from nose.tools import assert_raises
from nose.tools import assert_true

from networkapiclient.ClientFactory import ClientFactory
from networkapiclient.exception import NetworkAPIClientError

NETWORKAPI_URL = os.getenv('NETWORKAPI_URL', 'http://10.0.0.2:8000/')
NETWORKAPI_USER = os.getenv('NETWORKAPI_USER', 'networkapi')
NETWORKAPI_PWD = os.getenv('NETWORKAPI_PWD', 'networkapi')


class TestNetworkIPv4(TestCase):

    """ Class to test the network creation """

    def setUp(self):
        self.client = ClientFactory(NETWORKAPI_URL, NETWORKAPI_USER,
                                    NETWORKAPI_PWD)
        self.api_net_ipv4 = self.client.create_api_network_ipv4()

    def test_list_networks(self):
        """ List all IPv4 networks """

        networks = self.api_net_ipv4.list()

        assert_is_instance(networks, list)
        assert_greater(len(networks), 1)

    def test_create_new_ipv4_network_dinamically_by_prefix(self):
        """ Create a new IPv4 network """
        data = {
            'vlan': 3,
            'network_type': 2,
            'environmentvip': None,
            'prefix': 28,
        }

        network_id = self.api_net_ipv4.create([data])[0]['id']
        network = self.api_net_ipv4.get([network_id])['networks'][0]
        assert_equal(network['prefix'], 28)
        assert_equal(network['broadcast'], '10.0.1.15')

        self.api_net_ipv4.delete([network_id])

    def test_create_new_ipv4_network_by_octets(self):
        """ Creates new IPv4 network by the octets """

        data = {
            'vlan': 3,
            'network_type': 2,
            'environmentvip': None,
            'prefix': 30,
            'oct1': 10,
            'oct2': 0,
            'oct3': 1,
            'oct4': 0,
        }

        network_id = self.api_net_ipv4.create([data])[0]['id']
        network = self.api_net_ipv4.get([network_id])['networks'][0]

        assert_equal(network['prefix'], 30)
        assert_equal(network['broadcast'], '10.0.1.3')
        assert_equal(network['mask_oct4'], 252)

        self.api_net_ipv4.delete([network_id])

    def test_create_a_network_with_only_network_type(self):
        """ Create new IPv4 network using only the network_type """

        data = {
            'vlan': 3,
            'network_type': 2,
        }

        network_id = self.api_net_ipv4.create([data])[0]['id']
        network = self.api_net_ipv4.get([network_id])['networks'][0]

        assert_equal(network['vlan'], data['vlan'])
        assert_equal(network['network_type'], data['network_type'])
        assert_equal(network['id'], network_id)

        self.api_net_ipv4.delete([network_id])

    def test_delete_network(self):
        """ Deletes a ipv4 newtork """

        data = {
            'vlan': 3,
            'network_type': 2,
        }

        network_id = self.api_net_ipv4.create([data])[0]['id']
        response = self.api_net_ipv4.delete([network_id])

        assert_is_instance(response, list)
        assert_equal(len(response), 0)

    def test_delete_a_non_existent_ipv4_network(self):
        """ Tries to delete a non existent ipv4 network """

        with assert_raises(NetworkAPIClientError):
            response = self.api_net_ipv4.delete([5555])

    def test_delete_an_active_network(self):
        """ Tries to delete an active ipv4 network """

        active_network_id = 7

        with assert_raises(NetworkAPIClientError):
            self.api_net_ipv4.delete([active_network_id])

    def test_update_network(self):
        """ Updating ipv4 network data """

        data = {
            'vlan': 3,
            'network_type': 2,
        }

        network_id = self.api_net_ipv4.create([data])[0]['id']

        data['network_type'] = 6
        data.update({'id': network_id})
        self.api_net_ipv4.update([data])

        network = self.api_net_ipv4.get([network_id])['networks'][0]
        assert_equal(network['network_type'], data['network_type'])

        self.api_net_ipv4.delete([network_id])

    def test_update_a_field_not_editable_on_a_network(self):
        """ Tries to update a field not editable on a network """

        data = {
            'id': 7,
            'vlan': 3,
            'network_type': 2,
            'active': False,
        }
        self.api_net_ipv4.update([data])

        network = self.api_net_ipv4.get([data['id']])['networks'][0]
        assert_true(network['active'])

    def test_create_network_on_an_environment_that_have_a_router(self):
        """ Creates a network on an environment that have a router """

        data = {
            'vlan': 10,
            'network_type': 2,
        }
        expected_equipament_id = 12  # This equipament is a router

        network_id = self.api_net_ipv4.create([data])[0]['id']

        api_ip = self.client.create_api_ipv4()
        network = api_ip.search(
            search={'networkipv4': network_id},
            include=['equipments']
        )
        equipments_ids = []
        for ip in network['ips']:
            for equipment in ip['equipments']:
                equipments_ids.append(equipment['id'])

        assert_in(expected_equipament_id, equipments_ids)
        self.api_net_ipv4.delete([network_id])

    def test_create_network_on_an_environment_that_have_two_routers(self):
        """ Creates a network on an environment that have two routers """
        data = {
            'vlan': 3,
            'network_type': 2,
        }
        expected_equipaments_id = (26, 27)  # These equipaments are routers

        network_id = self.api_net_ipv4.create([data])[0]['id']

        api_ip = self.client.create_api_ipv4()
        network = api_ip.search(
            search={'networkipv4': network_id},
            include=['equipments']
        )

        equipments_ids = []
        for ip in network['ips']:
            for equipment in ip['equipments']:
                equipments_ids.append(equipment['id'])

        assert_in(expected_equipaments_id[0], equipments_ids)
        assert_in(expected_equipaments_id[1], equipments_ids)

        self.api_net_ipv4.delete([network_id])
