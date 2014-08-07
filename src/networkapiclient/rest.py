# -*- coding:utf-8 -*-
'''
Title: Infrastructure NetworkAPI
Author: globo.com / TQI
Copyright: ( c )  2009 globo.com todos os direitos reservados.
'''

import logging
from urllib2 import *
from httplib import *
from urlparse import urlparse
from networkapiclient.xml_utils import dumps_networkapi, loads

LOG = logging.getLogger('networkapiclient.rest')

class RestError(Exception):
    """Representa um erro ocorrido durante uma requisão REST."""
    def __init__(self, cause, message):
        self.cause = cause
        self.message = message
        
    def __str__(self):
        msg = u'Erro ao realizar requisição REST: Causa: %s, Mensagem: %s' % (self.cause, self.message)
        return msg.encode('utf-8')

class ConnectionError(RestError):
    """Caso ocorra algum erro de conexão com a NetworkAPI."""
    def __init__(self, cause):
        super(ConnectionError, self).__init__(cause, u'Falha na conexão com a NetworkAPI.')

class Rest:
    """Classe utilitária para chamada de webservices REST.
        
    Implementa métodos utilitários para realizações de chamadas a webservices
    REST. 
    """
    
    def __init__(self):
        proxy_support = ProxyHandler({})
        opener = build_opener(proxy_support)
        install_opener(opener)

    
    def get(self, url, auth_map=None):
        """Envia uma requisição GET para a URL informada.
        
        Se auth_map é diferente de None, então deverá conter as 
        chaves NETWORKAPI_PASSWORD e NETWORKAPI_USERNAME para realizar
        a autenticação na networkAPI.
        As chaves e os seus valores são enviados no header da requisição.
        
        :param url: URL para enviar a requisição HTTP.
        :param auth_map: Dicionário com as informações para autenticação na networkAPI. 
        
        :return: Retorna uma tupla contendo:
            (< código de resposta http >, < corpo da resposta >).
        
        :raise ConnectionError: Falha na conexão com a networkAPI.
        :raise RestError: Falha no acesso à networkAPI.
        """
        try:
            LOG.debug('GET %s', url)
            request = Request(url)
            if auth_map is not None:
                for key in auth_map.iterkeys():
                    request.add_header(key, auth_map[key])
                #request.add_header('NETWORKAPI_PASSWORD', auth_map['NETWORKAPI_PASSWORD'])
                #request.add_header('NETWORKAPI_USERNAME', auth_map['NETWORKAPI_USERNAME'])
            content = urlopen(request).read()
            response_code = 200
            LOG.debug('GET %s returns %s\n%s', url, response_code, content)
            return response_code, content
        except HTTPError, e:
            response_code = e.code
            content = ''
            if int(e.code) == 500:
                content = e.read()
            LOG.debug('GET %s returns %s\n%s', url, response_code, content)
            return response_code, content
        except URLError, e:
            raise ConnectionError(e)
        except Exception, e:
            raise RestError(e, e.message)
    
    def post(self, url, request_data, content_type=None, auth_map=None):
        """Envia uma requisição POST para a URL informada.
        
        Se auth_map é diferente de None, então deverá conter as 
            chaves NETWORKAPI_PASSWORD e NETWORKAPI_USERNAME para realizar
            a autenticação na networkAPI.

        As chaves e os seus valores são enviados no header da requisição.
        
        :param url: URL para enviar a requisição HTTP.
        :param request_data: Descrição para enviar no corpo da requisição HTTP.
        :param content_type: Tipo do conteúdo enviado em request_data. O valor deste
            parâmetro será adicionado no header "Content-Type" da requisição.
        :param auth_map: Dicionário com as informações para autenticação na networkAPI.
        
        :return: Retorna uma tupla contendo:

        ::

            (< código de resposta http >, < corpo da resposta >).
        
        :raise ConnectionError: Falha na conexão com a networkAPI.
        :raise RestError: Falha no acesso à networkAPI.
        """
        try:
            LOG.debug("POST %s\n%s", url, request_data)
            request = Request(url);
            request.add_data(request_data)
            #print request_data
            if auth_map is not None:
                
                for key in auth_map.iterkeys():
                    request.add_header(key, auth_map[key])
                
                #request.add_header('NETWORKAPI_PASSWORD', auth_map['NETWORKAPI_PASSWORD'])
                #request.add_header('NETWORKAPI_USERNAME', auth_map['NETWORKAPI_USERNAME'])
            if content_type != None:
                request.add_header('Content-Type', content_type)                
            content = urlopen(request).read()
            response_code = 200
            LOG.debug('POST %s returns %s\n%s', url, response_code, content)
            return response_code, content
        except HTTPError, e:
            response_code = e.code
            content = ''
            if int(e.code) == 500:
                content = e.read()
            LOG.debug('POST %s returns %s\n%s', url, response_code, content)
            return response_code, content
        except URLError, e:
            raise ConnectionError(e)
        except Exception, e:
            raise RestError(e, e.message)
    
    def delete(self, url, request_data, content_type=None, auth_map=None):
        """Envia uma requisição DELETE para a URL informada.
        
        Se auth_map é diferente de None, então deverá conter as 
            chaves NETWORKAPI_PASSWORD e NETWORKAPI_USERNAME para realizar
            a autenticação na networkAPI.

        As chaves e os seus valores são enviados no header da requisição.
        
        :param url: URL para enviar a requisição HTTP.
        :param request_data: Descrição para enviar no corpo da requisição HTTP.
        :param content_type: Tipo do conteúdo enviado em request_data. O valor deste
            parâmetro será adicionado no header "Content-Type" da requisição.
        :param auth_map: Dicionário com as informações para autenticação na networkAPI.
        
        :return: Retorna uma tupla contendo: 
            (< código de resposta http >, < corpo da resposta >).
        
        :raise ConnectionError: Falha na conexão com a networkAPI.
        :raise RestError: Falha no acesso à networkAPI.
        """
        try:
            LOG.debug("DELETE %s", url)
            parsed_url = urlparse(url)
            if parsed_url.scheme == 'https':
                connection = HTTPSConnection(parsed_url.hostname, parsed_url.port)
            else:
                connection = HTTPConnection(parsed_url.hostname, parsed_url.port)
            
            try:
                headers_map = dict()
                if auth_map is not None:
                    headers_map.update(auth_map)
                
                if content_type is not None:
                    headers_map['Content-Type'] = content_type
                    
                connection.request("DELETE", parsed_url.path, request_data, headers_map)
                
                response = connection.getresponse()
                body = response.read()
                LOG.debug('DELETE %s returns %s\n%s', url, response.status, body)
                return response.status, body
            finally:
                connection.close()
        except URLError, e:
            raise ConnectionError(e)
        except Exception, e:
            raise RestError(e, e.message)
        

    def put(self, url, request_data, content_type=None, auth_map=None):
        """Envia uma requisição PUT para a URL informada.
        
        Se auth_map é diferente de None, então deverá conter as 
            chaves NETWORKAPI_PASSWORD e NETWORKAPI_USERNAME para realizar
            a autenticação na networkAPI.

        As chaves e os seus valores são enviados no header da requisição.
        
        :param url: URL para enviar a requisição HTTP.
        :param request_data: Descrição para enviar no corpo da requisição HTTP.
        :param content_type: Tipo do conteúdo enviado em request_data. O valor deste
            parâmetro será adicionado no header "Content-Type" da requisição.
        :param auth_map: Dicionário com as informações para autenticação na networkAPI.
        
        :return: Retorna uma tupla contendo:

        ::

            (< código de resposta http >, < corpo da resposta >).
        
        :raise ConnectionError: Falha na conexão com a networkAPI.
        :raise RestError: Falha no acesso à networkAPI.
        """
        try:
            LOG.debug("PUT %s\n%s", url, request_data)
            parsed_url = urlparse(url)
            if parsed_url.scheme == 'https':
                connection = HTTPSConnection(parsed_url.hostname, parsed_url.port)
            else:
                connection = HTTPConnection(parsed_url.hostname, parsed_url.port)
            
            try:
                headers_map = dict()
                if auth_map is not None:
                    headers_map.update(auth_map)
                
                if content_type is not None:
                    headers_map['Content-Type'] = content_type
                    
                connection.request("PUT", parsed_url.path, request_data, headers_map)
                
                response = connection.getresponse()
                body = response.read()
                LOG.debug('PUT %s returns %s\n%s', url, response.status, body)
                return response.status, body
            finally:
                connection.close()
        except URLError, e:
            raise ConnectionError(e)
        except Exception, e:
            raise RestError(e, e.message)
            
            
    def post_map(self, url, map, auth_map=None):
        """Gera um XML a partir dos dados do dicionário e o envia através de uma requisição POST.
        
        :param url: URL para enviar a requisição HTTP.
        :param map: Dicionário com os dados do corpo da requisição HTTP.
        :param auth_map: Dicionário com as informações para autenticação na networkAPI. 
        
        :return: Retorna uma tupla contendo: 
            (< código de resposta http >, < corpo da resposta >).
        
        :raise ConnectionError: Falha na conexão com a networkAPI.
        :raise RestError: Falha no acesso à networkAPI.
        """
        xml = dumps_networkapi(map)
        response_code, content = self.post(url, xml, 'text/plain', auth_map)
        return response_code, content
    
    def put_map(self, url, map, auth_map=None):
        """Gera um XML a partir dos dados do dicionário e o envia através de uma requisição PUT.
        
        :param url: URL para enviar a requisição HTTP.
        :param map: Dicionário com os dados do corpo da requisição HTTP.
        :param auth_map: Dicionário com as informações para autenticação na networkAPI. 
        
        :return: Retorna uma tupla contendo: 
            (< código de resposta http>, < corpo da resposta>).
        
        :raise ConnectionError: Falha na conexão com a networkAPI.
        :raise RestError: Falha no acesso à networkAPI.
        """
        xml = dumps_networkapi(map)
        response_code, content = self.put(url, xml, 'text/plain', auth_map)
        return response_code, content
    
    def get_map(self, url, auth_map=None):
        """Envia uma requisição GET.
        
        :param url: URL para enviar a requisição HTTP.
        :param auth_map: Dicionário com as informações para autenticação na networkAPI. 
        
        :return: Retorna uma tupla contendo: 
            (< código de resposta http >, < corpo da resposta >).
        
        :raise ConnectionError: Falha na conexão com a networkAPI.
        :raise RestError: Falha no acesso à networkAPI.
        """
        response_code, content = self.get(url, auth_map)
        return response_code, content
    
    def delete_map(self, url, map=None, auth_map=None):
        """Gera um XML a partir dos dados do dicionário e o envia através de uma requisição DELETE.
        
        :param url: URL para enviar a requisição HTTP.
        :param map: Dicionário com os dados do corpo da requisição HTTP.
        :param auth_map: Dicionário com as informações para autenticação na networkAPI. 
        
        :return: Retorna uma tupla contendo: 
            (< código de resposta http >, < corpo da resposta >).
        
        :raise ConnectionError: Falha na conexão com a networkAPI.
        :raise RestError: Falha no acesso à networkAPI.
        """
        xml = None
        if map != None:
            xml = dumps_networkapi(map)
        response_code, content = self.delete(url, xml, 'text/plain', auth_map)
        return response_code, content
    
    def unmarshall(self, content):
        try:
            return loads(content)
        except Exception, e:
            raise RestError(e, u'Erro ao gerar o mapa de resposta!\n'\
                            u'Conteúdo recebido:\n%s' % content)


class RestRequest:
    """Classe básica para requisições webservices REST à networkAPI"""
    
    def __init__(self, url, method, user, password, user_ldap=None):
        '''Construtor da classe.
        
        :param url: URL para enviar a requisição HTTP.
        :param method: Método da requisição ('POST', 'PUT', 'GET' ou 'DELETE').
        :param user: Usuário para autenticação na networkAPI.
        :param password: Senha para autenticação na networkAPI. 
        '''
        self.url = url
        self.method = method
        self.auth_map = dict()
        self.auth_map['NETWORKAPI_USERNAME'] = user
        self.auth_map['NETWORKAPI_PASSWORD'] = password
         
        if user_ldap is not None: 
            self.auth_map['NETWORKAPI_USERLDAP'] = user_ldap

    def submit(self, map):
        '''Envia a requisição HTTP de acordo com os parâmetros informados no construtor.
        
        :param map: Dicionário com os dados do corpo da requisição.
        
        :return: Retorna uma tupla contendo: 
            (< código de resposta http >, < corpo da resposta >).
        
        :raise ConnectionError: Falha na conexão com a networkAPI.
        :raise RestError: Falha no acesso à networkAPI.
        '''
        # print "Requição em %s %s com corpo: %s" % (self.method, self.url, map)
        rest = Rest()
        if self.method == 'POST':
            code, response = rest.post_map(self.url, map, self.auth_map)
        elif self.method == 'PUT':
            code, response = rest.put_map(self.url, map, self.auth_map)
        elif self.method == 'GET':
            code, response = rest.get_map(self.url, self.auth_map)
        elif self.method == 'DELETE':
            code, response = rest.delete_map(self.url, map, self.auth_map)           
        
        return code, response
