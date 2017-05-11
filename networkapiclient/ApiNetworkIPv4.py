# -*- coding: utf-8 -*-
from networkapiclient.ApiGenericClient import ApiGenericClient
from networkapiclient.utils import build_uri_with_ids


class ApiNetworkIPv4(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiNetworkIPv4, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def deploy(self, id_networkv4):
        """Deploy network in equipments and set column 'active = 1' in tables redeipv4

        :param id_networkv4: ID for NetworkIPv4

        :return: Equipments configuration output
        """

        data = dict()
        uri = 'api/networkv4/%s/equipments/' % id_networkv4

        return super(ApiNetworkIPv4, self).post(uri, data=data)

    def get_by_id(self, id_networkv4):
        """Get IPv4 network

        :param id_networkv4: ID for NetworkIPv4

        :return: IPv4 Network
        """

        uri = 'api/networkv4/%s/' % id_networkv4

        return super(ApiNetworkIPv4, self).get(uri)

    def list(self, environment_vip=None):
        """List IPv4 networks

        :param environment_vip: environment vip to filter

        :return: IPv4 Networks
        """

        uri = 'api/networkv4/?'
        if environment_vip:
            uri += 'environment_vip=%s' % environment_vip

        return super(ApiNetworkIPv4, self).get(uri)

    def undeploy(self, id_networkv4):
        """Remove deployment of network in equipments and set column 'active = 0' in tables redeipv4 ]

        :param id_networkv4: ID for NetworkIPv4

        :return: Equipments configuration output
        """

        uri = 'api/networkv4/%s/equipments/' % id_networkv4

        return super(ApiNetworkIPv4, self).delete(uri)

    def check_vip_ip(self, ip, environment_vip):
        """
        Check available ip in environment vip
        """
        uri = 'api/ipv4/ip/%s/environment-vip/%s/' % (ip, environment_vip)

        return super(ApiNetworkIPv4, self).get(uri)

    def delete_ipv4(self, ipv4_id):
        """
        Delete ipv4
        """
        uri = 'api/ipv4/%s/' % (ipv4_id)

        return super(ApiNetworkIPv4, self).delete(uri)

    def search(self, **kwargs):
        """
        Method to search ipv4's based on extends search.

        :param search: Dict containing QuerySets to find ipv4's.
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields:  Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing ipv4's
        """

        return super(ApiNetworkIPv4, self).get(self.prepare_url('api/v3/networkv4/',
                                                                kwargs))

    def get(self, ids, **kwargs):
        """
        Method to get network-ipv4's by their ids

        :param ids: List containing identifiers of network-ipv4's
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields: Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing network-ipv4's
        """
        url = build_uri_with_ids('api/v3/networkv4/%s/', ids)

        return super(ApiNetworkIPv4, self).get(self.prepare_url(url, kwargs))

    def delete(self, ids):
        """
        Method to delete network-ipv4's by their ids

        :param ids: Identifiers of network-ipv4's
        :return: None
        """
        url = build_uri_with_ids('api/v3/networkv4/%s/', ids)

        return super(ApiNetworkIPv4, self).delete(url)

    def update(self, networkipv4s):
        """
        Method to update network-ipv4's

        :param networkipv4s: List containing network-ipv4's desired to updated
        :return: None
        """

        data = {'networks': networkipv4s}
        networkipv4s_ids = [str(networkipv4.get('id'))
                            for networkipv4 in networkipv4s]

        return super(ApiNetworkIPv4, self).put('api/v3/networkv4/%s/' %
                                               ';'.join(networkipv4s_ids), data)

    def create(self, networkipv4s):
        """
        Method to create network-ipv4's

        :param networkipv4s: List containing networkipv4's desired to be created on database
        :return: None
        """

        data = {'networks': networkipv4s}
        return super(ApiNetworkIPv4, self).post('api/v3/networkv4/', data)
