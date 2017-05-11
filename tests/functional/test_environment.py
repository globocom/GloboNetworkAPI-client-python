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


class TestApiEnvironment(TestCase):

    def setUp(self):
        self.client = ClientFactory(NETWORKAPI_URL, NETWORKAPI_USER,
                                    NETWORKAPI_PWD)
        self.api_environment = self.client.create_api_environment()

    def tearDown(self):
        pass

    def test_create_environment(self):
        """ Tries to create a new network environment """
        env_data = {
            'grupo_l3': 32,
            'ambiente_logico': 12,
            'divisao_dc': 23,
            'default_vrf': 1,
        }

        env_id = self.api_environment.create([env_data])[0]['id']
        env = self.api_environment.get([env_id])

        assert_equal(env['environments'][0]['id'], env_id)
        self.api_environment.delete([env_id])

    def test_create_many_environments(self):
        """ Tries to create many environments """

        envs_data = [{
            'grupo_l3': 32,
            'ambiente_logico': 12,
            'divisao_dc': 23,
            'default_vrf': 1,
        }, {
            'grupo_l3': 32,
            'ambiente_logico': 11,
            'divisao_dc': 25,
            'default_vrf': 1,
        }]

        envs_ids = [e['id'] for e in self.api_environment.create(envs_data)]
        envs = self.api_environment.get(envs_ids)

        assert_equal(len(envs['environments']), 2)
        for env in envs['environments']:
            assert_in(env['id'], envs_ids)
        self.api_environment.delete(envs_ids)

    def test_insert_a_duplicated_environment(self):
        """ Tries to insert a duplicated environment """

        env_data = {
            'grupo_l3': 32,
            'ambiente_logico': 12,
            'divisao_dc': 22,
            'default_vrf': 1,
        }

        with assert_raises(NetworkAPIClientError):
            self.api_environment.create([env_data])

    def test_delete_environment(self):
        """ Tests if we can delete an environment """

        env_data = {
            'grupo_l3': 32,
            'ambiente_logico': 12,
            'divisao_dc': 23,
            'default_vrf': 1,
        }

        env_id = self.api_environment.create([env_data])[0]['id']
        assert_is_instance(self.api_environment.get([env_id]), dict)

        self.api_environment.delete([env_id])
        with assert_raises(NetworkAPIClientError):
            self.api_environment.get([env_id])

    def test_delete_a_non_existent_environment(self):
        """ Tries to delete a non existent environment """

        with assert_raises(NetworkAPIClientError):
            self.api_environment.delete([1111])

    def test_search_an_environment(self):
        """ Searches an environment """

        dc_division = 25
        logic_env = 15
        search_data = {
            'extends_search': [{
                'divisao_dc': dc_division,
                'ambiente_logico': logic_env,
            }]
        }

        envs = self.api_environment.search(search=search_data)

        assert_equal(envs['total'], 1)
        assert_equal(envs['environments'][0]['divisao_dc'], dc_division)
        assert_equal(envs['environments'][0]['ambiente_logico'], logic_env)

    def test_search_a_list_of_environments(self):
        """ Searches a list of environment """

        search_data = {
            'extends_search': [{
                'divisao_dc': 25,
                'ambiente_logico': 15,
            }, {
                'divisao_dc': 24,
                'ambiente_logico': 14,
            }]
        }
        envs = self.api_environment.search(search=search_data)

        assert_equal(envs['total'], 2)
        for env in envs['environments']:
            assert_in(env['divisao_dc'], (25, 24))
            assert_in(env['ambiente_logico'], (15, 14))

    def test_search_a_non_existent_environment(self):
        """ Searches a non existent environment """

        search_data = {
            'extends_search': [{
                'divisao_dc': 100,
                'ambiente_logico': 100,
            }]
        }
        envs = self.api_environment.search(search=search_data)

        assert_equal(envs['total'], 0)

    def test_get_an_environment_by_id(self):
        """ Get an enviroment by id """

        env = self.api_environment.get([1])
        assert_equal(env['environments'][0]['id'], 1)

    def test_try_to_get_a_non_existent_environment_by_id(self):
        """ Tries to get a non existent environment by id """

        with assert_raises(NetworkAPIClientError):
            self.api_environment.get([1000])

    def test_update_an_environment(self):
        """ Updates an environment """

        env_data = {
            'grupo_l3': 32,
            'ambiente_logico': 12,
            'divisao_dc': 21,
            'default_vrf': 1,
        }

        env_id = self.api_environment.create([env_data])[0]['id']
        env = self.api_environment.get([env_id])['environments'][0]

        assert_equal(env['id'], env_id)

        new_dc_division = env['divisao_dc'] = 23
        self.api_environment.update([env])
        env = self.api_environment.get([env_id])['environments'][0]

        assert_equal(env['divisao_dc'], new_dc_division)
        self.api_environment.delete([env_id])

    def test_update_a_non_existent_environment(self):
        """ Tries to update a non existent environment """

        env_data = {
            'id': 1000,
            'grupo_l3': 32,
            'ambiente_logico': 12,
            'divisao_dc': 21,
            'default_vrf': 1,
        }

        with assert_raises(NetworkAPIClientError):
            self.api_environment.update([env_data])
