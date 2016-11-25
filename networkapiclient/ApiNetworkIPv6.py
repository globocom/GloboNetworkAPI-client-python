# -*- coding: utf-8 -*-
from networkapiclient.ApiGenericClient import ApiGenericClient
from networkapiclient.utils import build_uri_with_ids


class ApiNetworkIPv6(ApiGenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """

        super(ApiNetworkIPv6, self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap
        )

    def deploy(self, id_networkv6):
        """Deploy network in equipments and set column 'active = 1' in tables redeipv6 ]

        :param id_networkv6: ID for NetworkIPv6

        :return: Equipments configuration output
        """

        data = dict()
        uri = 'api/networkv6/%s/equipments/' % id_networkv6

        return super(ApiNetworkIPv6, self).post(uri, data=data)

    def get_by_id(self, id_networkv6):
        """Get IPv6 network

        :param id_networkv4: ID for NetworkIPv6

        :return: IPv6 Network
        """

        uri = 'api/networkv4/%s/' % id_networkv6
        return super(ApiNetworkIPv6, self).get(uri)

    def list(self, environment_vip=None):
        """List networks redeipv6 ]

        :param environment_vip: environment vip to filter

        :return: IPv6 Networks
        """

        uri = 'api/networkv6/?'
        if environment_vip:
            uri += 'environment_vip=%s' % environment_vip

        return super(ApiNetworkIPv6, self).get(uri)

    def undeploy(self, id_networkv6):
        """Remove deployment of network in equipments and set column 'active = 0' in tables redeipv6 ]

        :param id_networkv6: ID for NetworkIPv6

        :return: Equipments configuration output
        """

        uri = 'api/networkv6/%s/equipments/' % id_networkv6
        return super(ApiNetworkIPv6, self).delete(uri)

    def check_vip_ip(self, ip, environment_vip):
        """
        Check available ipv6 in environment vip
        """
        uri = 'api/ipv6/ip/%s/environment-vip/%s/' % (ip, environment_vip)

        return super(ApiNetworkIPv6, self).get(uri)

    def delete_ipv6(self, ipv6_id):
        """
        Delete ipv6
        """
        uri = 'api/ipv6/%s/' % (ipv6_id)

        return super(ApiNetworkIPv6, self).delete(uri)

    def search(self, **kwargs):
        """
        Method to search ipv6's based on extends search.

        :param search: Dict containing QuerySets to find ipv6's.
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields:  Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing ipv6's
        """

        return super(ApiNetworkIPv6, self).get(self.prepare_url('api/v3/networkv6/',
                                                                kwargs))

    def get(self, ids, **kwargs):
        """
        Method to get network-ipv6's by their ids

        :param ids: List containing identifiers of network-ipv6's
        :param include: Array containing fields to include on response.
        :param exclude: Array containing fields to exclude on response.
        :param fields: Array containing fields to override default fields.
        :param kind: Determine if result will be detailed ('detail') or basic ('basic').
        :return: Dict containing network-ipv6's
        """
        url = build_uri_with_ids('api/v3/networkv6/%s/', ids)

        return super(ApiNetworkIPv6, self).get(self.prepare_url(url, kwargs))

    def delete(self, ids):
        """
        Method to delete network-ipv6's by their ids

        :param ids: Identifiers of network-ipv6's
        :return: None
        """
        url = build_uri_with_ids('api/v3/networkv6/%s/', ids)

        return super(ApiNetworkIPv6, self).delete(url)

    def update(self, networkipv6s):
        """
        Method to update network-ipv6's

        :param networkipv6s: List containing network-ipv6's desired to updated
        :return: None
        """

        data = {'networks': networkipv6s}
        networkipv6s_ids = [str(networkipv6.get('id'))
                            for networkipv6 in networkipv6s]

        return super(ApiNetworkIPv6, self).put('api/v3/networkv6/%s/' %
                                               ';'.join(networkipv6s_ids), data)

    def create(self, networkipv6s):
        """
        Method to create network-ipv6's

        :param networkipv6s: List containing networkipv6's desired to be created on database
        :return: None
        """

        data = {'networks': networkipv6s}
        return super(ApiNetworkIPv6, self).post('api/v3/networkv6/', data)
