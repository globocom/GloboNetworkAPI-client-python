from networkapiclient.ApiGenericClient import ApiGenericClient


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
        uri = "api/networkv6/%s/equipments/" % id_networkv6
        return self.post(uri, data=data)

    def get_by_id(self, id_networkv6):
        """Get IPv6 network

        :param id_networkv4: ID for NetworkIPv6

        :return: IPv6 Network
        """

        uri = "api/networkv4/%s/" % id_networkv6
        return self.get(uri)

    def list(self, environment_vip=None):
        """List networks redeipv6 ]

        :param environment_vip: environment vip to filter

        :return: IPv6 Networks
        """

        uri = "api/networkv6/?"
        if environment_vip:
            uri += "environment_vip=%s" % environment_vip

        return self.get(uri)

    def undeploy(self, id_networkv6):
        """Remove deployment of network in equipments and set column 'active = 0' in tables redeipv6 ]

        :param id_networkv6: ID for NetworkIPv6

        :return: Equipments configuration output
        """

        uri = "api/networkv6/%s/equipments/" % id_networkv6
        return self.delete(uri)

    def check_vip_ip(self, ip, environment_vip):
        """
        Check available ipv6 in environment vip
        """
        uri = "api/ipv6/ip/%s/environment-vip/%s/" % (ip, environment_vip)

        return self.get(uri)

    def delete_ipv6(self, ipv6_id):
        """
        Delete ipv6
        """
        uri = "api/ipv6/%s/" % (ipv6_id)

        return self.delete(uri)
