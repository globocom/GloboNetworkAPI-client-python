# -*- coding: utf-8 -*-
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
import json
import logging

try:
    from urllib.parse import urlencode
except:
    from urllib import urlencode
import urllib
from io import BytesIO

import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError

from networkapiclient.exception import NetworkAPIClientError


class ApiGenericClient(object):

    """
        Class inherited by all NetworkAPI-Client classes
        who implements access methods to new pattern rest networkAPI.
    """

    def __init__(self, networkapi_url, user, password, user_ldap=None, log_level='INFO'):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        self.networkapi_url = networkapi_url
        self.user = user
        self.password = password
        self.user_ldap = user_ldap
        self.log_level = log_level

        logging.basicConfig(level=self.log_level, format='%(message)s')
        self.logger = logging.getLogger('networkapiclient')

    def get(self, uri):
        """
            Sends a GET request.

            @param uri: Uri of Service API.
            @param data: Requesting Data. Default: None

            @raise NetworkAPIClientError: Client failed to access the API.
        """
        try:

            request = requests.get(
                self._url(uri),
                auth=self._auth_basic(),
                headers=self._header()
            )

            request.raise_for_status()

            return request.json()

        except HTTPError:
            error = request.json()
            self.logger.error(error)
            raise NetworkAPIClientError(error.get('detail', ''))
        finally:
            self.logger.info('URI: %s', uri)
            self.logger.info('Status Code: %s',
                             request.status_code if request else '')
            self.logger.info('X-Request-Id: %s',
                             request.headers.get('x-request-id'))
            self.logger.info('X-Request-Context: %s',
                             request.headers.get('x-request-context'))

    def post(self, uri, data=None, files=None):
        """
            Sends a POST request.

            @param uri: Uri of Service API.
            @param data: Requesting Data. Default: None

            @raise NetworkAPIClientError: Client failed to access the API.
        """
        try:

            request = requests.post(
                self._url(uri),
                data=json.dumps(data),
                files=files,
                auth=self._auth_basic(),
                headers=self._header()
            )

            request.raise_for_status()

            return request.json()

        except HTTPError:
            error = request.json()
            self.logger.error(error)
            raise NetworkAPIClientError(error.get('detail', ''))
        finally:
            self.logger.info('URI: %s', uri)
            self.logger.info('Status Code: %s',
                             request.status_code if request else '')
            self.logger.info('X-Request-Id: %s',
                             request.headers.get('x-request-id'))
            self.logger.info('X-Request-Context: %s',
                             request.headers.get('x-request-context'))

    def put(self, uri, data=None):
        """
            Sends a PUT request.

            @param uri: Uri of Service API.
            @param data: Requesting Data. Default: None

            @raise NetworkAPIClientError: Client failed to access the API.
        """
        try:

            request = requests.put(
                self._url(uri),
                data=json.dumps(data),
                auth=self._auth_basic(),
                headers=self._header()
            )

            request.raise_for_status()

            return request.json()

        except HTTPError:
            error = request.json()
            self.logger.error(error)
            raise NetworkAPIClientError(error.get('detail', ''))
        finally:
            self.logger.info('URI: %s', uri)
            self.logger.info('Status Code: %s',
                             request.status_code if request else '')
            self.logger.info('X-Request-Id: %s',
                             request.headers.get('x-request-id'))
            self.logger.info('X-Request-Context: %s',
                             request.headers.get('x-request-context'))

    def delete(self, uri, data=None):
        """
            Sends a DELETE request.

            @param uri: Uri of Service API.

            @raise NetworkAPIClientError: Client failed to access the API.
        """
        try:

            request = requests.delete(
                self._url(uri),
                data=json.dumps(data),
                auth=self._auth_basic(),
                headers=self._header()
            )

            request.raise_for_status()

            return request.json()

        except HTTPError:
            error = request.json()
            self.logger.error(error)
            raise NetworkAPIClientError(error.get('detail', ''))
        finally:
            self.logger.info('URI: %s', uri)
            self.logger.info('Status Code: %s',
                             request.status_code if request else '')
            self.logger.info('X-Request-Id: %s',
                             request.headers.get('x-request-id'))
            self.logger.info('X-Request-Context: %s',
                             request.headers.get('x-request-context'))

    def _parse(self, content):
        """
            Parse data request to data from python.

            @param content: Context of request.

            @raise ParseError:
        """
        if content:

            stream = BytesIO(str(content))
            data = json.loads(stream.getvalue())

            return data

    def _url(self, uri):
        """Create Full URI To Send API.
        """

        return '%s%s' % (self.networkapi_url, uri)

    def _auth_basic(self):
        """Attaches HTTP Basic Authentication to the given Request object.
        """

        return HTTPBasicAuth(self.user, self.password)

    def _header(self):
        """Content Type For Header
        """

        headers = {
            'content-type': 'application/json',
        }

        return headers

    def prepare_url(self, uri, kwargs):
        """Convert dict for URL params
        """
        params = dict()
        for key in kwargs:
            if key in ('include', 'exclude', 'fields'):
                params.update({
                    key: ','.join(kwargs.get(key))
                })
            elif key in ('search', 'kind'):
                params.update({
                    key: kwargs.get(key)
                })

        if params:
            params = urlencode(params)
            uri = '%s?%s' % (uri, params)

        return uri
