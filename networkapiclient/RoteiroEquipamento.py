# -*- coding:utf-8 -*-
'''
Created on 02/09/2009

@author: eduardo.ferreira
'''
from networkapiclient.GenericClient import GenericClient


class RoteiroEquipamento(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            RoteiroEquipamento,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def listar_todos(self):
        pass

    def listar(self, id_equipamento):
        pass

    def criar(self, id_equipamento, id_roteiro):
        pass

    def remover(self, id_equipamento, id_roteiro):
        pass
