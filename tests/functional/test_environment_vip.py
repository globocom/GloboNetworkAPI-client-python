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


class TestApiEnvironmentVip(TestCase):

    def setUp(self):
        self.client = ClientFactory(NETWORKAPI_URL, NETWORKAPI_USER,
                                    NETWORKAPI_PWD)
        self.api_environment_vip = self.client.create_api_environment_vip()
        self.api_network_ipv4 = self.client.create_api_network_ipv4()
        self.api_network_ipv6 = self.client.create_api_network_ipv6()
        self.api_environment = self.client.create_api_environment()
        self.api_vlan = self.client.create_api_vlan()
        self.non_existent_env_vip_id = 1111

    def tearDown(self):
        pass

    # get tests

    def test_get_an_environment_vip_by_id(self):
        """ Get an environment vip by id """

        env = self.api_environment_vip.get([1])
        assert_equal(env['environments_vip'][0]['id'], 1)

    def test_try_to_get_a_non_existent_environment_vip_by_id(self):
        """ Try to get a non existent environment vip by id """

        with assert_raises(NetworkAPIClientError):
            self.api_environment_vip.get([self.non_existent_env_vip_id])

    # search tests

    def test_search_environment_vip_by_extends_search(self):
        """ Search expecting list with one environment vips """

        finalidade_txt = 'Red'
        cliente_txt = 'Red'

        search_data = {
            'extends_search': [{
                'finalidade_txt': finalidade_txt,
                'cliente_txt': cliente_txt,
            }]
        }

        envs_vip = self.api_environment_vip.search(search=search_data)

        assert_equal(envs_vip['total'], 1)
        assert_equal(
            envs_vip['environments_vip'][0]['finalidade_txt'],
            finalidade_txt)
        assert_equal(
            envs_vip['environments_vip'][0]['cliente_txt'],
            cliente_txt)

    def test_search_a_list_of_environment_vips(self):
        """ Search expecting list with two environment vips """

        search_data = {
            'extends_search': [{
                'finalidade_txt': 'Blue',
                'cliente_txt': 'Red',
            }, {
                'finalidade_txt': 'Green',
                'cliente_txt': 'Green',
            }]
        }

        envs_vip = self.api_environment_vip.search(search=search_data)

        assert_equal(envs_vip['total'], 2)
        for env in envs_vip['environments_vip']:
            assert_in(env['finalidade_txt'], ('Blue', 'Green'))
            assert_in(env['cliente_txt'], ('Red', 'Green'))

    def test_search_a_non_existent_environment_vip(self):
        """ Search expecting list with zero environment vips """

        search_data = {
            'extends_search': [{
                'finalidade_txt': 'Green',
                'cliente_txt': 'Red',
            }]
        }
        envs = self.api_environment_vip.search(search=search_data)

        assert_equal(envs['total'], 0)

    # post tests

    def test_create_environment_vip(self):
        """ Try to create a new environment vip """
        env_vip_data = {
            'finalidade_txt': 'Fin-1',
            'cliente_txt': 'ClientTxt-1',
            'ambiente_p44_txt': 'EnvP44Txt-1',
            'description': 'Description-1',
        }

        env_vip_id = self.api_environment_vip.create([env_vip_data])[0]['id']
        env_vip = self.api_environment_vip.get([env_vip_id])

        assert_equal(env_vip['environments_vip'][0]['id'], env_vip_id)
        self.api_environment_vip.delete([env_vip_id])

    def test_create_many_environment_vips(self):
        """ Try to create many environment vips """

        envs_vip_data = [{
            'finalidade_txt': 'Fin-1',
            'cliente_txt': 'ClientTxt-1',
            'ambiente_p44_txt': 'EnvP44Txt-1',
            'description': 'Description-1',
        }, {
            'finalidade_txt': 'Fin-2',
            'cliente_txt': 'ClientTxt-2',
            'ambiente_p44_txt': 'EnvP44Txt-2',
            'description': 'Description-2',
        }]

        envs_vip_ids = self.api_environment_vip.create(envs_vip_data)
        envs_vip_ids = [e['id'] for e in envs_vip_ids]
        envs_vip = self.api_environment_vip.get(envs_vip_ids)

        assert_equal(len(envs_vip['environments_vip']), 2)
        for envs_vip in envs_vip['environments_vip']:
            assert_in(envs_vip['id'], envs_vip_ids)
        self.api_environment_vip.delete(envs_vip_ids)

    # put tests

    def test_update_environment_vip(self):
        """ Try to update an environment vip """

        env_vip_data = {
            'finalidade_txt': 'Fin-1',
            'cliente_txt': 'ClientTxt-1',
            'ambiente_p44_txt': 'EnvP44Txt-1',
            'description': 'Description-1',
        }

        env_vip_id = self.api_environment_vip.create([env_vip_data])[0]['id']
        env_vip = self.api_environment_vip.get(
            [env_vip_id])['environments_vip'][0]

        assert_equal(env_vip['id'], env_vip_id)

        new_finality_txt = env_vip['finalidade_txt'] = 'Fin-Updated'

        self.api_environment_vip.update([env_vip])
        env_vip = self.api_environment_vip.get(
            [env_vip_id])['environments_vip'][0]

        assert_equal(env_vip['finalidade_txt'], new_finality_txt)
        self.api_environment_vip.delete([env_vip_id])

    def test_update_a_non_existent_environment_vip(self):
        """ Try to update a non existent environment vip """

        env_vip_data = {
            'id': self.non_existent_env_vip_id,
            'finalidade_txt': 'Green',
            'cliente_txt': 'Red',
            'description': 'Red',
            'ambiente_p44_txt': 'Red',
        }

        with assert_raises(NetworkAPIClientError):
            self.api_environment_vip.update([env_vip_data])

    # delete tests

    def test_delete_environment_vip(self):
        """ Test if we can delete an environment vip """

        env_vip_data = {
            'finalidade_txt': 'Fin-1',
            'cliente_txt': 'ClientTxt-1',
            'ambiente_p44_txt': 'EnvP44Txt-1',
            'description': 'Description-1',
        }

        env_vip_id = self.api_environment_vip.create([env_vip_data])[0]['id']
        assert_is_instance(self.api_environment_vip.get([env_vip_id]), dict)

        self.api_environment_vip.delete([env_vip_id])
        with assert_raises(NetworkAPIClientError):
            self.api_environment_vip.get([env_vip_id])

    def test_delete_two_environments_vip(self):
        """ Test if we can delete two environment vips """

        envs_vip_data = [
            {
                'finalidade_txt': 'Fin-1',
                'cliente_txt': 'ClientTxt-1',
                'ambiente_p44_txt': 'EnvP44Txt-1',
                'description': 'Description-1',
            },
            {
                'finalidade_txt': 'Fin-2',
                'cliente_txt': 'ClientTxt-2',
                'ambiente_p44_txt': 'EnvP44Txt-2',
                'description': 'Description-2',
            }
        ]

        envs_vip_id = [e['id']
                       for e in self.api_environment_vip.create(envs_vip_data)]
        assert_is_instance(self.api_environment_vip.get(envs_vip_id), dict)

        self.api_environment_vip.delete(envs_vip_id)

        for env_vip_id in envs_vip_id:
            with assert_raises(NetworkAPIClientError):
                self.api_environment_vip.get([env_vip_id])

    def test_delete_a_non_existent_environment_vip(self):
        """ Try to delete a non existent environment vip """

        with assert_raises(Exception):
            self.api_environment_vip.delete([self.non_existent_env_vip_id])

    def test_try_delete_environment_vip_assoc_with_netipv4(self):
        """ Try to violate delete restriction on environment vip removal when
            env vip is associated with some network ipv4
        """

        with assert_raises(Exception):
            self.api_environment_vip.delete([13])

    def test_try_delete_environment_vip_assoc_with_netipv6(self):
        """ Try to violate delete restriction on environment vip removal when
            env vip is associated with some network ipv6
        """

        with assert_raises(Exception):
            self.api_environment_vip.delete([13])

    def test_try_delete_environment_vip_assoc_to_option_vip(self):
        """ Try to delete environment vip associated to some option vip """

        env_vip_data = {
            'finalidade_txt': 'Fin-Test',
            'cliente_txt': 'ClientTxt-Test',
            'ambiente_p44_txt': 'EnvP44Txt-Test',
            'description': 'Description-Test',
        }

        env_vip_id = self.api_environment_vip.create([env_vip_data])[0]['id']

        option_vip = self.client.create_option_vip()\
            .add('tipo_opcao', 'nome_opcao_txt')
        self.client.create_option_vip()\
            .associate(option_vip['option_vip']['id'], env_vip_id)

        self.api_environment_vip.delete([env_vip_id])

        with assert_raises(NetworkAPIClientError):
            self.api_environment_vip.get([env_vip_id])

    def test_try_delete_environment_vip_assoc_to_env(self):
        """ Try to delete environment vip associated to some environment """

        env_vip_data = {
            'finalidade_txt': 'Fin-Test',
            'cliente_txt': 'ClientTxt-Test',
            'ambiente_p44_txt': 'EnvP44Txt-Test',
            'description': 'Description-Test',
        }

        env_vip_id = self.api_environment_vip.create([env_vip_data])[0]['id']

        env = 7

        self.client.create_ambiente().associate(env, env_vip_id)

        self.api_environment_vip.delete([env_vip_id])

        with assert_raises(NetworkAPIClientError):
            self.api_environment_vip.get([env_vip_id])

    def test_try_delete_environment_vip_assoc_to_options_vip_and_envs(self):
        """ Try to delete environment vip associated to some options vip
            and environments
        """

        env_vip_data = {
            'finalidade_txt': 'Fin-Test',
            'cliente_txt': 'ClientTxt-Test',
            'ambiente_p44_txt': 'EnvP44Txt-Test',
            'description': 'Description-Test',
        }

        env_vip_id = self.api_environment_vip.create([env_vip_data])[0]['id']

        options_vip = [1, 2]
        environments = [7, 8]

        for opt in options_vip:
            self.client.create_option_vip().associate(opt, env_vip_id)

        for env in environments:
            self.client.create_ambiente().associate(env, env_vip_id)

        self.api_environment_vip.delete([env_vip_id])

        with assert_raises(NetworkAPIClientError):
            self.api_environment_vip.get([env_vip_id])
