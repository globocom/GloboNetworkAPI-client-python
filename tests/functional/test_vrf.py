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


class TestApiVrf(TestCase):

    def setUp(self):
        self.client = ClientFactory(NETWORKAPI_URL, NETWORKAPI_USER,
                                    NETWORKAPI_PWD)
        self.api_vrf = self.client.create_api_vrf()
        self.api_environment = self.client.create_api_environment()

    def tearDown(self):
        pass

    # post tests

    def test_create_vrf(self):
        """ Tries to create a new vrf """
        vrf_data = [{
            'internal_name': 'Vrf-1',
            'vrf': 'Vrf-1'
        }]

        vrf_id = self.api_vrf.create(vrf_data)[0]['id']
        vrf = self.api_vrf.get([vrf_id])

        assert_equal(vrf['vrfs'][0]['id'], vrf_id)
        self.api_vrf.delete([vrf_id])

    def test_create_many_vrfs(self):
        """ Tries to create many vrfs """

        vrfs_data = [{
            'internal_name': 'Vrf-1',
            'vrf': 'Vrf-1'
        }, {
            'internal_name': 'Vrf-2',
            'vrf': 'Vrf-2'
        }]

        vrfs_ids = [e['id'] for e in self.api_vrf.create(vrfs_data)]
        vrfs = self.api_vrf.get(vrfs_ids)

        assert_equal(len(vrfs['vrfs']), 2)
        for vrf in vrfs['vrfs']:
            assert_in(vrf['id'], vrfs_ids)
        self.api_vrf.delete(vrfs_ids)

    # delete tests

    def test_delete_vrf(self):
        """ Tests if we can delete an vrf """

        vrf_data = {
            'internal_name': 'Vrf-1',
            'vrf': 'Vrf-1'
        }

        vrf_id = self.api_vrf.create([vrf_data])[0]['id']
        assert_is_instance(self.api_vrf.get([vrf_id]), dict)

        self.api_vrf.delete([vrf_id])
        with assert_raises(NetworkAPIClientError):
            self.api_vrf.get([vrf_id])

    def test_delete_a_non_existent_vrf(self):
        """ Tries to delete a non existent vrf """

        with assert_raises(NetworkAPIClientError):
            self.api_vrf.delete([1111])

    def test_search_an_vrf(self):
        """ Searches an vrf """

        internal_name = 'Vrf-1'
        vrf = 'Vrf-1'

        search_data = {
            'extends_search': [{
                'internal_name': internal_name,
                'vrf': vrf,
            }]
        }

        vrfs = self.api_vrf.search(search=search_data)

        assert_equal(vrfs['total'], 1)
        assert_equal(vrfs['vrfs'][0]['internal_name'], internal_name)
        assert_equal(vrfs['vrfs'][0]['vrf'], vrf)

    def test_search_a_list_of_vrfs(self):
        """ Searches a list of vrf """

        internal_names = vrf_names = ['Vrf-1', 'Vrf-2']

        search_data = {
            'extends_search': [{
                'internal_name': internal_names[0],
                'vrf': vrf_names[0],
            }, {
                'internal_name': internal_names[1],
                'vrf': vrf_names[1],
            }]
        }
        vrfs = self.api_vrf.search(search=search_data)

        assert_equal(vrfs['total'], 2)
        for vrf in vrfs['vrfs']:
            assert_in(vrf['internal_name'], internal_names)
            assert_in(vrf['vrf'], vrf_names)

    def test_search_a_non_existent_vrf(self):
        """ Searches a non existent vrf """

        search_data = {
            'extends_search': [{
                'internal_name': 'Vrf-K-7',
            }]
        }
        vrfs = self.api_vrf.search(search=search_data)

        assert_equal(vrfs['total'], 0)

    def test_get_an_vrf_by_id(self):
        """ Get an vrf by id """

        vrf = self.api_vrf.get([1])
        assert_equal(vrf['vrfs'][0]['id'], 1)

    def test_try_to_get_a_non_existent_vrf_by_id(self):
        """ Tries to get a non existent vrf by id """

        with assert_raises(NetworkAPIClientError):
            self.api_vrf.get([1000])

    def test_update_an_vrf(self):
        """ Updates an vrf """

        internal_name = vrf = 'Vrf-3'

        vrf_data = {
            'internal_name': internal_name,
            'vrf': vrf
        }

        vrf_id = self.api_vrf.create([vrf_data])[0]['id']
        vrf = self.api_vrf.get([vrf_id])['vrfs'][0]

        assert_equal(vrf['id'], vrf_id)

        new_internal_name = vrf['internal_name'] = 'Vrf-3-1'
        self.api_vrf.update([vrf])
        vrf = self.api_vrf.get([vrf_id])['vrfs'][0]

        assert_equal(vrf['internal_name'], new_internal_name)
        self.api_vrf.delete([vrf_id])

    def test_update_a_non_existent_vrf(self):
        """ Tries to update a non existent vrf """

        vrf_data = {
            'id': 1000,
            'internal_name': 'Vrf-3-1',
            'vrf': 'Vrf-3-1'
        }

        with assert_raises(NetworkAPIClientError):
            self.api_vrf.update([vrf_data])

    def test_delete_vrf_used_by_environment(self):
        """ Try to violate delete restriction when Vrf is used by some environment """

        vrf_data = [{
            'internal_name': 'Vrf-1',
            'vrf': 'Vrf-1'
        }]

        vrf_id = self.api_vrf.create(vrf_data)[0]['id']

        env_data = [{
            'grupo_l3': 32,
            'ambiente_logico': 12,
            'divisao_dc': 21,
            'default_vrf': vrf_id,
        }]

        env_id = self.api_environment.create(env_data)[0]['id']

        with assert_raises(NetworkAPIClientError):
            self.api_vrf.delete([vrf_id])

        self.api_environment.delete([env_id])
        self.api_vrf.delete([vrf_id])

    def test_try_delete_vrf_assoc_to_equipment(self):
        """ Try to delete vrf associated to equipment """
        # TODO Need more things to continue
        pass

    def test_try_delete_vrf_assoc_to_vlan_eqpt(self):
        """ Try to violate delete restriction when Vrf is associated to vlan-eqpt """
        # TODO Need more things to continue
        pass
