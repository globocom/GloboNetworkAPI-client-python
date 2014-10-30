# -*- coding:utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from networkapiclient.GenericClient import GenericClient
from networkapiclient.exception import InvalidParameterError
from networkapiclient.utils import is_valid_int_param, get_list_map


class EnvironmentVIP(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            EnvironmentVIP,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def list_all(self):
        """
        List all environment vips

        :return: Following dictionary:

        ::

            {'environment_vip': [{'id': <id>,
            'finalidade_txt': <finalidade_txt>,
            'cliente_txt': <cliente_txt>,
            'ambiente_p44_txt': <ambiente_p44_txt> } {... other environments vip ...}]}

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        url = 'environmentvip/all/'

        code, xml = self.submit(None, 'GET', url)

        key = 'environment_vip'

        return get_list_map(self.response(code, xml, [key]), key)

    def list_all_available(self, id_vlan):
        """
        List all environment vips availables

        :return: Following dictionary:

        ::

            {'environment_vip': [{'id': <id>,
            'finalidade_txt': <finalidade_txt>,
            'cliente_txt': <cliente_txt>,
            'ambiente_p44_txt': <ambiente_p44_txt> }
            {... other environments vip ...}]}

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        url = 'environmentvip/search/' + str(id_vlan)

        code, xml = self.submit(None, 'GET', url)

        key = 'environment_vip'

        return get_list_map(self.response(code, xml, [key]), key)

    def add(self, finalidade_txt, cliente_txt, ambiente_p44_txt, description):
        """Inserts a new Environment VIP and returns its identifier.

        :param finalidade_txt: Finality. String with a maximum of 50 characters and respect [a-zA-Z\_-]
        :param cliente_txt: ID  Client. String with a maximum of 50 characters and respect [a-zA-Z\_-]
        :param ambiente_p44_txt: Environment P44. String with a maximum of 50 characters and respect [a-zA-Z\_-]

        :return: Following dictionary:

        ::

            {'environment_vip': {'id': < id >}}

        :raise InvalidParameterError: The value of finalidade_txt, cliente_txt or ambiente_p44_txt is invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        environmentvip_map = dict()
        environmentvip_map['finalidade_txt'] = finalidade_txt
        environmentvip_map['cliente_txt'] = cliente_txt
        environmentvip_map['ambiente_p44_txt'] = ambiente_p44_txt
        environmentvip_map['description'] = description

        code, xml = self.submit(
            {'environment_vip': environmentvip_map}, 'POST', 'environmentvip/')

        return self.response(code, xml)

    def alter(
            self,
            id_environment_vip,
            finalidade_txt,
            cliente_txt,
            ambiente_p44_txt,
            description):
        """Change Environment VIP from by the identifier.

        :param id_environment_vip: Identifier of the Environment VIP. Integer value and greater than zero.
        :param finalidade_txt: Finality. String with a maximum of 50 characters and respect [a-zA-Z\_-]
        :param cliente_txt: ID  Client. String with a maximum of 50 characters and respect [a-zA-Z\_-]
        :param ambiente_p44_txt: Environment P44. String with a maximum of 50 characters and respect [a-zA-Z\_-]

        :return: None

        :raise InvalidParameterError: Environment VIP identifier is null and invalid.
        :raise InvalidParameterError: The value of finalidade_txt, cliente_txt or ambiente_p44_txt is invalid.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_environment_vip):
            raise InvalidParameterError(
                u'The identifier of Environment VIP is invalid or was not informed.')

        environmentvip_map = dict()
        environmentvip_map['finalidade_txt'] = finalidade_txt
        environmentvip_map['cliente_txt'] = cliente_txt
        environmentvip_map['ambiente_p44_txt'] = ambiente_p44_txt
        environmentvip_map['description'] = description

        url = 'environmentvip/' + str(id_environment_vip) + '/'

        code, xml = self.submit(
            {'environment_vip': environmentvip_map}, 'PUT', url)

        return self.response(code, xml)

    def remove(self, id_environment_vip):
        """Remove Environment VIP from by the identifier.

        :param id_environment_vip: Identifier of the Environment VIP. Integer value and greater than zero.

        :return: None

        :raise InvalidParameterError: Environment VIP identifier is null and invalid.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise EnvironmentVipError: There networkIPv4 or networkIPv6 associated with environment vip.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_environment_vip):
            raise InvalidParameterError(
                u'The identifier of Environment VIP is invalid or was not informed.')

        url = 'environmentvip/' + str(id_environment_vip) + '/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def search(
            self,
            id_environment_vip=None,
            finalidade_txt=None,
            cliente_txt=None,
            ambiente_p44_txt=None):
        """Search Environment VIP from by parameters.

        Case the id parameter has been passed, the same it has priority over the other parameters.

        :param id_environment_vip: Identifier of the Environment VIP. Integer value and greater than zero.
        :param finalidade_txt: Finality. String with a maximum of 50 characters and respect [a-zA-Z\_-]
        :param cliente_txt: ID  Client. String with a maximum of 50 characters and respect [a-zA-Z\_-]
        :param ambiente_p44_txt: Environment P44. String with a maximum of 50 characters and respect [a-zA-Z\_-]

        :return: Following dictionary:

        ::

            {‘environment_vip’:
            {‘id’: < id >,
            ‘finalidade_txt’: < finalidade_txt >,
            ‘finalidade’: < finalidade >,
            ‘cliente_txt’: < cliente_txt >,
            ‘ambiente_p44_txt’: < ambiente_p44_txt >}}

        :raise InvalidParameterError: The value of id_environment_vip, finalidade_txt, cliente_txt or ambiente_p44_txt is invalid.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        environmentvip_map = dict()
        environmentvip_map['id_environment_vip'] = id_environment_vip
        environmentvip_map['finalidade_txt'] = finalidade_txt
        environmentvip_map['cliente_txt'] = cliente_txt
        environmentvip_map['ambiente_p44_txt'] = ambiente_p44_txt

        code, xml = self.submit(
            {'environment_vip': environmentvip_map}, 'POST', 'environmentvip/search/')

        return self.response(code, xml)

    def get_vips(self, id_environment_vip):
        """Get to list all the VIPs related to Environment VIP  from by the identifier.

        :param id_environment_vip: Identifier of the Environment VIP. Integer value and greater than zero.

        :return: Dictionary with the following structure:

        ::

            {‘vip_< id >’:
            {‘id’: < id >,
            ‘validado’: < validado >,
            ‘finalidade’: < finalidade >,
            ‘cliente’: < cliente >,
            ‘ambiente’: < ambiente >,
            ‘cache’: < cache >,
            ‘metodo_bal’: < método_bal >,
            ‘persistencia’: < persistencia >,
            ‘healthcheck_type’: <  healthcheck_type >,
            ‘healthcheck’: < healthcheck >,
            ‘timeout’: < timeout >,
            ‘host’: < host >,
            ‘maxcon’: < maxcon >,
            ‘dsr’: < dsr >,
            ‘bal_ativo’: < bal_ativo >,
            ‘transbordos’:{‘transbordo’:[< transbordo >]},
            ‘reals’:{‘real’:[{‘real_name’:< real_name >, ‘real_ip’:< real_ip >}]},
            ‘portas_servicos’:{‘porta’:[< porta >]},
            ‘vip_criado’: < vip_criado >,
            ‘id_ip’: < id_ip >,
            ‘id_ipv6’: < id_ipv6 >,
            ‘id_healthcheck_expect’: < id_healthcheck_expect >}}

        :raise InvalidParameterError: Environment VIP identifier is null and invalid.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_environment_vip):
            raise InvalidParameterError(
                u'The identifier of Environment VIP is invalid or was not informed.')

        url = 'environmentvip/' + str(id_environment_vip) + '/vip/all'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def buscar_finalidade(self):
        """Search finalidade_txt environment vip

        :return: Dictionary with the following structure:

        ::
            {‘finalidade’:  ‘finalidade’: <'finalidade_txt'>}

        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        url = 'environment-vip/get/finality'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def buscar_cliente_por_finalidade(self, finalidade_txt):
        """Search cliente_txt environment vip

        :return: Dictionary with the following structure:

        ::

            {‘cliente_txt’:
            ‘finalidade’: <'finalidade_txt'>,
            'cliente_txt: <'cliente_txt'>'}

        :raise InvalidParameterError: finalidade_txt is null and invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        vip_map = dict()
        vip_map['finalidade_txt'] = finalidade_txt

        url = 'environment-vip/get/cliente_txt/'

        code, xml = self.submit({'vip': vip_map}, 'POST', url)

        return self.response(code, xml)

    def buscar_ambientep44_por_finalidade_cliente(
            self,
            finalidade_txt,
            cliente_txt):
        """Search ambiente_p44_txt environment vip

        :return: Dictionary with the following structure:

        ::

            {‘ambiente_p44_txt’:
            'id':<'id_ambientevip'>,
            ‘finalidade’: <'finalidade_txt'>,
            'cliente_txt: <'cliente_txt'>',
            'ambiente_p44: <'ambiente_p44'>',}

        :raise InvalidParameterError: finalidade_txt and cliente_txt is null and invalid.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        vip_map = dict()
        vip_map['finalidade_txt'] = finalidade_txt
        vip_map['cliente_txt'] = cliente_txt

        url = 'environment-vip/get/ambiente_p44_txt/'

        code, xml = self.submit({'vip': vip_map}, 'POST', url)

        return self.response(code, xml)
