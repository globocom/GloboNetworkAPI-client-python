# -*- coding: utf-8 -*-
import os
from unittest import TestCase

from nose.tools import assert_equal
from nose.tools import assert_in
from nose.tools import assert_raises

from networkapiclient.ClientFactory import ClientFactory
from networkapiclient.exception import NetworkAPIClientError


NETWORKAPI_URL = os.getenv('NETWORKAPI_URL', 'http://10.0.0.2:8000/')
NETWORKAPI_USER = os.getenv('NETWORKAPI_USER', 'networkapi')
NETWORKAPI_PWD = os.getenv('NETWORKAPI_PWD', 'networkapi')


class TestApiVlan(TestCase):

    def setUp(self):
        self.client = ClientFactory(NETWORKAPI_URL, NETWORKAPI_USER,
                                    NETWORKAPI_PWD)
        self.api_vlan = self.client.create_api_vlan()

    def test_search_a_vlan(self):
        """ Tests the vlan search """

        vlan_name = 'Vlan 31'
        search_data = {
            'extends_search': [{
                'nome': vlan_name
            }]
        }

        vlans = self.api_vlan.search(search=search_data)

        assert_equal(vlans['total'], 1)
        assert_equal(vlans['vlans'][0]['name'], vlan_name)

    def test_get_vlans_by_id(self):
        """ Gets vlans by ids """
        vlans_ids = [1, 3, 5]

        vlans = self.api_vlan.get(vlans_ids)

        assert_equal(len(vlans['vlans']), 3)
        for vlan in vlans['vlans']:
            assert_in(vlan['id'], vlans_ids)

    def test_get_only_one_vlan_by_id(self):
        """ Gets only one vlan by its id """

        vlan_id = 7
        vlan = self.api_vlan.get([vlan_id])

        assert_equal(len(vlan['vlans']), 1)
        assert_equal(vlan['vlans'][0]['id'], vlan_id)

    def test_get_a_non_existing_vlan(self):
        """ Attenpts to get a non existing vlan """

        vlan_id = 15
        with assert_raises(NetworkAPIClientError):
            vlan = self.api_vlan.get([vlan_id])

    def test_insert_new_vlan(self):
        """ Tries to insert a new vlan """
        vlan_data = {
            'name': 'Vlan 15',
            'environment': 1,
        }

        vlan_id = self.api_vlan.create([vlan_data])[0]['id']
        vlan = self.api_vlan.get([vlan_id])

        assert_equal(len(vlan['vlans']), 1)
        assert_equal(vlan['vlans'][0]['id'], vlan_id)

        self.api_vlan.delete([vlan_id])

    def test_insert_a_duplicated_vlan(self):
        """ Tries to insert a duplicated vlan """

        vlan_data = {
            'name': 'Vlan 25',
            'environment': 1,
            'num_vlan': 15,
        }

        vlan_id = self.api_vlan.create([vlan_data])[0]['id']

        with assert_raises(NetworkAPIClientError):
            self.api_vlan.create([vlan_data])

        self.api_vlan.delete([vlan_id])

    def test_insert_a_list_of_vlans(self):
        """ Tries to insert a list of vlans """

        vlans_data = [{
            'name': 'Vlan 40',
            'environment': 1,
        }, {
            'name': 'Vlan 41',
            'environment': 2,
        }, {
            'name': 'Vlan 42',
            'environment': 2,
        }]

        vlans_ids = [vlan['id'] for vlan in self.api_vlan.create(vlans_data)]
        vlans = self.api_vlan.get(vlans_ids)

        assert_equal(len(vlans['vlans']), 3)
        for vlan in vlans['vlans']:
            assert_in(vlan['id'], vlans_ids)

        self.api_vlan.delete(vlans_ids)

    def test_insert_a_vlan_with_wrong_data(self):
        """ Tries to insert a vlan with wrong data """

        vlan_data = {
            'name': 'Vlan 33',
            'environment': 3,
            'fake_data': True,
        }

        with assert_raises(NetworkAPIClientError):
            self.api_vlan.create([vlan_data])

    def test_delete_a_single_vlan(self):
        """ Tries to delete a single vlan """

        vlan_data = {
            'name': 'Vlan 15',
            'environment': 1,
        }

        vlan_id = self.api_vlan.create([vlan_data])[0]['id']
        self.api_vlan.delete([vlan_id])

        with assert_raises(NetworkAPIClientError):
            vlan = self.api_vlan.get([vlan_id])

    def test_delete_a_list_of_vlans(self):
        """ Tries to delete a list of vlans """

        vlans_data = [{
            'name': 'Vlan 40',
            'environment': 1,
        }, {
            'name': 'Vlan 41',
            'environment': 2,
        }, {
            'name': 'Vlan 42',
            'environment': 2,
        }]

        vlans_ids = [vlan['id'] for vlan in self.api_vlan.create(vlans_data)]
        self.api_vlan.delete(vlans_ids)

        with assert_raises(NetworkAPIClientError):
            self.api_vlan.get(vlans_ids)

    def test_delete_a_non_existent_vlan(self):
        """ Tries to delete a non existent vlan """

        with assert_raises(NetworkAPIClientError):
            self.api_vlan.delete([44])

    def test_update_a_vlan(self):
        """ Updates a single vlan """

        vlan_data = {
            'name': 'Vlan 38',
            'environment': 1,
        }

        vlan_id = self.api_vlan.create([vlan_data])[0]['id']
        vlan = self.api_vlan.get([vlan_id])['vlans'][0]

        new_name = vlan['name'] = 'Vlan 40'
        self.api_vlan.update([vlan])
        vlan = self.api_vlan.get([vlan_id])['vlans'][0]

        assert_equal(vlan['name'], new_name)

        self.api_vlan.delete([vlan_id])

    def test_update_a_non_existent_vlan(self):
        """ Tries to update a non existent vlan """

        vlan = self.api_vlan.get([1])['vlans'][0]
        vlan['id'] = 55

        with assert_raises(NetworkAPIClientError):
            self.api_vlan.update([vlan])

    def test_create_vlan_with_unauthorized_number_for_environment(self):
        """ Do not allow create a vlan with unauthorized number """
        vlan_data = {
            'name': 'Vlan 38',
            'environment': 3,
        }

        with assert_raises(NetworkAPIClientError):
            self.api_vlan.create([vlan_data])
