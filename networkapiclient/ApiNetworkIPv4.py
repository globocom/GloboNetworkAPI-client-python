from networkapiclient.ApiGenericClient import ApiGenericClient


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
        uri = "api/networkv4/%s/equipments/" % id_networkv4
        return self.post(uri, data=data)

    def get_by_id(self, id_networkv4):
        """Get IPv4 network

        :param id_networkv4: ID for NetworkIPv4

        :return: IPv4 Network
        """

        uri = "api/networkv4/%s/" % id_networkv4
        return self.get(uri)

    def list(self, environment_vip=None):
        """List IPv4 networks

        :param environment_vip: environment vip to filter

        :return: IPv4 Networks
        """

        uri = "api/networkv4/?"
        if environment_vip:
            uri += "environment_vip=%s" % environment_vip

        return self.get(uri)

    def undeploy(self, id_networkv4):
        """Remove deployment of network in equipments and set column 'active = 0' in tables redeipv4 ]

        :param id_networkv4: ID for NetworkIPv4

        :return: Equipments configuration output
        """

        uri = "api/networkv4/%s/equipments/" % id_networkv4
        return self.delete(uri)

    def check_vip_ip(self, ip, environment_vip):
        """
        Check available ip in environment vip
        """
        uri = "api/ipv4/ip/%s/environment-vip/%s/" % (ip, environment_vip)

        return self.get(uri)

    def delete_ipv4(self, ipv4_id):
        """
        Delete ipv4
        """
        uri = "api/ipv4/%s/" % (ipv4_id)

        return self.delete(uri)
