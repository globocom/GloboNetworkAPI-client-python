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


class BlockRule(GenericClient):

    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(
            BlockRule,
            self).__init__(
            networkapi_url,
            user,
            password,
            user_ldap)

    def get_rule_by_id(self, rule_id):
        """Get rule by indentifier.

        :param rule_id: Rule identifier

        :return: Dictionary with the following structure:

        ::

            {'rule': {'environment': < environment_id >,
            'content': < content >,
            'custom': < custom >,
            'id': < id >,
            'name': < name >}}

        :raise UserNotAuthorizedError: User dont have permition.
        :raise InvalidParameterError: RULE identifier is null or invalid.
        :raise DataBaseError: Can't connect to networkapi database.
        """

        url = "rule/get_by_id/" + str(rule_id)

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml, ['rule_contents', 'rule_blocks'])
