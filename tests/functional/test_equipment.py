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


class TestApiequipment(TestCase):

    def setUp(self):
        self.client = ClientFactory(NETWORKAPI_URL, NETWORKAPI_USER,
                                    NETWORKAPI_PWD)
        self.api_environment = self.client.create_api_environment()

        self.api_equipment = self.client.create_api_equipment()

        self.non_existent_eqpt = 1000

    def tearDown(self):
        pass

    # get tests

    def test_get_an_equipment_by_id(self):
        """ Get an equipment by id """

        eqpt = self.api_equipment.get([1])
        assert_equal(eqpt['equipments'][0]['id'], 1)

    def test_try_to_get_a_non_existent_equipment_by_id(self):
        """ Tries to get a non existent equipment by id """

        with assert_raises(NetworkAPIClientError):
            self.api_equipment.get([self.non_existent_eqpt])

    # search tests

    def test_search_an_equipment(self):
        """ Searches an equipment """

        equipment_type = 2

        search_data = {
            'extends_search': [{
                'tipo_equipamento': equipment_type,
            }]
        }

        eqpts = self.api_equipment.search(search=search_data)

        assert_equal(eqpts['total'], 6)

        for eqpt in eqpts['equipments']:
            assert_equal(eqpt['equipment_type'], equipment_type)

    def test_search_a_list_of_equipments(self):
        """ Searches a list of equipment """

        equipment_types = [2, 3]

        search_data = {
            'extends_search': [{
                'tipo_equipamento__in': equipment_types,
            }]
        }
        eqpts = self.api_equipment.search(search=search_data)

        assert_equal(eqpts['total'], 9)
        for eqpt in eqpts['equipments']:
            assert_in(eqpt['equipment_type'], equipment_types)

    def test_search_a_non_existent_equipment(self):
        """ Searches a non existent equipment """

        search_data = {
            'extends_search': [{
                'tipo_equipamento': 10,
            }]
        }
        eqpts = self.api_equipment.search(search=search_data)

        assert_equal(eqpts['total'], 0)

    # post tests

    def test_create_equipment(self):
        """ Tries to create a new equipment """
        eqpt_data = [{
            'name': 'Eqpt Teste',
            'maintenance': False,
            'equipment_type': 1,
            'model': 1
        }]

        eqpt_id = self.api_equipment.create(eqpt_data)[0]['id']
        eqpt = self.api_equipment.get([eqpt_id])

        assert_equal(eqpt['equipments'][0]['id'], eqpt_id)
        self.api_equipment.delete([eqpt_id])

    def test_create_many_equipments(self):
        """ Tries to create many equipments """

        eqpts_data = [{
            'name': 'Eqpt Teste-1',
            'maintenance': False,
            'equipment_type': 1,
            'model': 1
        }, {
            'name': 'Eqpt Teste-2',
            'maintenance': False,
            'equipment_type': 1,
            'model': 1
        }]

        eqpts_ids = [e['id'] for e in self.api_equipment.create(eqpts_data)]
        eqpts = self.api_equipment.get(eqpts_ids)

        assert_equal(len(eqpts['equipments']), 2)
        for eqpt in eqpts['equipments']:
            assert_in(eqpt['id'], eqpts_ids)
        self.api_equipment.delete(eqpts_ids)

    # put tests

    def test_update_an_equipment(self):
        """ Updates an equipment """

        eqpt_data = [{
            'name': 'Eqpt Test To Update',
            'maintenance': False,
            'equipment_type': 1,
            'model': 1
        }]

        eqpt_id = self.api_equipment.create(eqpt_data)[0]['id']
        eqpt = self.api_equipment.get([eqpt_id])['equipments'][0]

        assert_equal(eqpt['id'], eqpt_id)

        new_name = eqpt['name'] = 'Eqpt New Test To Update'
        self.api_equipment.update([eqpt])
        eqpt = self.api_equipment.get([eqpt_id])['equipments'][0]

        assert_equal(eqpt['name'].lower(), new_name.lower())
        self.api_equipment.delete([eqpt_id])

    def test_update_a_non_existent_equipment(self):
        """ Tries to update a non existent equipment """

        eqpt_data = {
            'id': self.non_existent_eqpt,
            'name': 'Eqpt Teste',
            'maintenance': False,
            'equipment_type': 1,
            'model': 1
        }

        with assert_raises(NetworkAPIClientError):
            self.api_equipment.update([eqpt_data])

    # delete tests

    def test_delete_equipment(self):
        """ Tests if we can delete an equipment """

        eqpt_data = [{
            'name': 'Eqpt Teste',
            'maintenance': False,
            'equipment_type': 1,
            'model': 1
        }]

        eqpt_id = self.api_equipment.create(eqpt_data)[0]['id']
        assert_is_instance(self.api_equipment.get([eqpt_id]), dict)

        self.api_equipment.delete([eqpt_id])
        with assert_raises(NetworkAPIClientError):
            self.api_equipment.get([eqpt_id])

    def test_delete_a_non_existent_equipment(self):
        """ Tries to delete a non existent equipment """

        with assert_raises(NetworkAPIClientError):
            self.api_equipment.delete([self.non_existent_eqpt])
