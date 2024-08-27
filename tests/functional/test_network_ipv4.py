# -*- coding: utf-8 -*-
import os
from unittest import TestCase

from networkapiclient.ClientFactory import ClientFactory
from networkapiclient.exception import NetworkAPIClientError

NETWORKAPI_URL = os.getenv('NETWORKAPI_URL', 'http://localhost:8000/')
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

        self.assertIsInstance(networks, list)
        self.assertGreater(len(networks), 1)

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
        self.assertEqual(network['prefix'], 28)
        self.assertEqual(network['broadcast'], '10.0.1.15')

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

        self.assertEqual(network['prefix'], 30)
        self.assertEqual(network['broadcast'], '10.0.1.3')
        self.assertEqual(network['mask_oct4'], 252)

        self.api_net_ipv4.delete([network_id])

    def test_create_a_network_with_only_network_type(self):
        """ Create new IPv4 network using only the network_type """

        data = {
            'vlan': 3,
            'network_type': 2,
        }

        network_id = self.api_net_ipv4.create([data])[0]['id']
        network = self.api_net_ipv4.get([network_id])['networks'][0]

        self.assertEqual(network['vlan'], data['vlan'])
        self.assertEqual(network['network_type'], data['network_type'])
        self.assertEqual(network['id'], network_id)

        self.api_net_ipv4.delete([network_id])

    def test_delete_network(self):
        """ Deletes a ipv4 newtork """

        data = {
            'vlan': 3,
            'network_type': 2,
        }

        network_id = self.api_net_ipv4.create([data])[0]['id']
        response = self.api_net_ipv4.delete([network_id])

        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 0)

    def test_delete_a_non_existent_ipv4_network(self):
        """ Tries to delete a non existent ipv4 network """

        with self.assertRaises(NetworkAPIClientError):
            response = self.api_net_ipv4.delete([5555])

    def test_delete_an_active_network(self):
        """ Tries to delete an active ipv4 network """

        active_network_id = 7

        with self.assertRaises(NetworkAPIClientError):
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
        self.assertEqual(network['network_type'], data['network_type'])

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
        self.assertTrue(network['active'])

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

        self.assertIn(expected_equipament_id, equipments_ids)
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

        self.assertIn(expected_equipaments_id[0], equipments_ids)
        self.assertIn(expected_equipaments_id[1], equipments_ids)

        self.api_net_ipv4.delete([network_id])
