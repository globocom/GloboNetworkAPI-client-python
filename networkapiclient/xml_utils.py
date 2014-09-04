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

from xml.dom import InvalidCharacterErr
from xml.dom.minidom import *
from xml.dom.minicompat import StringTypes
import re


class XMLErrorUtils(Exception):

    """Representa um erro ocorrido durante o marshall ou unmarshall do XML."""

    def __init__(self, cause, message):
        self.cause = cause
        self.message = message

    def __str__(self):
        msg = u'Erro ao criar ou ler o XML: Causa: %s, Mensagem: %s' % (
            self.cause, self.message)
        return msg.encode('utf-8')


class InvalidNodeNameXMLError(XMLErrorUtils):

    """Nome inválido para representá-lo como uma TAG de XML."""

    def __init__(self, cause, message):
        XMLErrorUtils.__init__(self, cause, message)


class InvalidNodeTypeXMLError(XMLErrorUtils):

    """Tipo inválido para o conteúdo de uma TAG de XML."""

    def __init__(self, cause, message):
        XMLErrorUtils.__init__(self, cause, message)


def _add_text_node(value, node, doc):
    if value is None:
        return

    if not isinstance(value, StringTypes):
        text = r'%s' % unicode(value)
    else:
        text = r'%s' % value.replace('%', '%%')

    try:
        textNode = doc.createTextNode(text)
        node.appendChild(textNode)
    except TypeError as t:
        raise InvalidNodeTypeXMLError(
            t,
            u'Conteúdo de um Nó do XML com tipo de dado inválido: %s ' %
            value)


def _add_list_node(nodeName, list, parent, doc):
    for value in list:
        node = doc.createElement(nodeName)
        parent.appendChild(node)
        if isinstance(value, dict):
            _add_nodes_to_parent(value, node, doc)
        else:
            _add_text_node(value, node, doc)


def _add_nodes_to_parent(map, parent, doc):
    if map is None:
        return

    for key, value in map.iteritems():
        try:
            if isinstance(value, dict):
                node = doc.createElement(key)
                parent.appendChild(node)
                _add_nodes_to_parent(value, node, doc)
            elif isinstance(value, type([])):
                _add_list_node(key, value, parent, doc)
            else:
                node = doc.createElement(key)
                parent.appendChild(node)
                _add_text_node(value, node, doc)

        except InvalidCharacterErr as i:
            raise InvalidNodeNameXMLError(
                i,
                u'Valor inválido para nome de uma TAG de XML: %s' %
                key)


def dumps(map, root_name, root_attributes=None):
    """Cria um string no formato XML a partir dos elementos do map.

    Os elementos do mapa serão nós filhos do root_name.

    Cada chave do map será um Nó no XML. E o valor da chave será o conteúdo do Nó.

    Exemplos:

    ::

        - Mapa: {'networkapi':1}
          XML: &lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;networkapi&gt;1&lt;/networkapi&gt;

        - Mapa: {'networkapi':{'teste':1}}
          XML:  &lt;?xml version="1.0" encoding="UTF-8"?&gt;
          &lt;networkapi&gt;
          &lt;teste&gt;1&lt;/teste&gt;
          &lt;/networkapi&gt;

        - Mapa: {'networkapi':{'teste01':01, 'teste02':02}}
          XML: &lt;?xml version="1.0" encoding="UTF-8"?&gt;
          &lt;networkapi&gt;
          &lt;teste01&gt;01&lt;/teste01&gt;
          &lt;teste02&gt;02&lt;/teste02&gt;
          &lt;/networkapi&gt;

        - Mapa: {'networkapi':{'teste01':01, 'teste02':[02,03,04]}}
          XML: &lt;?xml version="1.0" encoding="UTF-8"?&gt;
          &lt;networkapi&gt;
          &lt;teste01&gt;01&lt;/teste01&gt;
          &lt;teste02&gt;02&lt;/teste02&gt;
          &lt;teste02&gt;03&lt;/teste02&gt;
          &lt;teste02&gt;04&lt;/teste02&gt;
          &lt;/networkapi&gt;

        - Mapa: {'networkapi':{'teste01':01, 'teste02':{'a':1, 'b':2}}}
          XML: &lt;?xml version="1.0" encoding="UTF-8"?&gt;
          &lt;networkapi&gt;
          &lt;teste01&gt;01&lt;/teste01&gt;
          &lt;teste02&gt;
          &lt;a&gt;1&lt;/a&gt;
          &lt;b&gt;2&lt;/b&gt;
          &lt;/teste02&gt;
          &lt;/networkapi&gt;

    :param map: Dicionário com os dados para serem convertidos em XML.
    :param root_name: Nome do nó root do XML.
    :param root_attributes: Dicionário com valores para serem adicionados como atributos
        para o nó root.

    :return: XML

    :raise XMLErrorUtils: Representa um erro ocorrido durante o marshall ou unmarshall do XML.
    :raise InvalidNodeNameXMLError: Nome inválido para representá-lo como uma TAG de XML.
    :raise InvalidNodeTypeXMLError: "Tipo inválido para o conteúdo de uma TAG de XML.
    """
    xml = ''
    try:
        implementation = getDOMImplementation()
    except ImportError as i:
        raise XMLErrorUtils(i, u'Erro ao obter o DOMImplementation')

    doc = implementation.createDocument(None, root_name, None)

    try:
        root = doc.documentElement

        if (root_attributes is not None):
            for key, value in root_attributes.iteritems():
                attribute = doc.createAttribute(key)
                attribute.nodeValue = value
                root.setAttributeNode(attribute)

        _add_nodes_to_parent(map, root, doc)

        xml = doc.toxml('UTF-8')
    except InvalidCharacterErr as i:
        raise InvalidNodeNameXMLError(
            i,
            u'Valor inválido para nome de uma TAG de XML: %s' %
            root_name)
    finally:
        doc.unlink()

    return xml


def dumps_networkapi(map, version='1.0'):
    """Idem ao método dump, porém, define que o nó root é o valor 'networkapi'.

    :param map: Dicionário com os dados para serem convertidos em XML.
    :param version: Versão do nó networkapi. A versão será adicionada como atributo do nó.

    :return: XML

    :raise XMLErrorUtils: Representa um erro ocorrido durante o marshall ou unmarshall do XML.
    :raise InvalidNodeNameXMLError: Nome inválido para representá-lo como uma TAG de XML.
    :raise InvalidNodeTypeXMLError: "Tipo inválido para o conteúdo de uma TAG de XML.
    """
    return dumps(map, 'networkapi', {'versao': version})


def _create_childs_map(parent, force_list):
    if parent is None:
        return None

    if parent.hasChildNodes():
        childs = parent.childNodes
        childs_map = dict()
        childs_values = []
        for i in range(childs.length):
            child = childs.item(i)
            if child.nodeType == Node.ELEMENT_NODE:
                if child.nodeName in childs_map:
                    child_value = _create_childs_map(child, force_list)
                    if child_value is not None:
                        value = childs_map[child.nodeName]
                        if not isinstance(value, type([])):
                            value = [value]
                        value.append(child_value)
                        childs_map[child.nodeName] = value
                elif child.nodeName in force_list:
                    child_value = _create_childs_map(child, force_list)
                    if child_value is None:
                        child_value = []
                    else:
                        child_value = [child_value]
                    childs_map[child.nodeName] = child_value
                else:
                    childs_map[
                        child.nodeName] = _create_childs_map(
                        child,
                        force_list)
            elif child.nodeType == Node.TEXT_NODE or child.nodeType == Node.CDATA_SECTION_NODE:
                if child.data.strip() != '':
                    childs_values.append(child.data.replace('%%', '%'))

        if len(childs_values) == 0 and len(childs_map) == 0:
            return None
        if len(childs_values) != 0 and len(childs_map) != 0:
            childs_values.append(childs_map)
            return childs_values
        if len(childs_values) != 0:
            if len(childs_values) == 1:
                return childs_values[0]
            return childs_values
        return childs_map
    elif parent.nodeType == Node.TEXT_NODE or parent.nodeType == Node.CDATA_SECTION_NODE:
        if parent.data.strip() != '':
            return parent.data

    return None


def loads(xml, force_list=None):
    """Cria um dicionário com os dados do XML.

    O dicionário terá como chave o nome do nó root e como valor o conteúdo do nó root.
    Quando o conteúdo de um nó é uma lista de nós então o valor do nó será
    um dicionário com uma chave para cada nó.
    Entretanto, se existir nós, de um mesmo pai, com o mesmo nome, então eles serão
    armazenados em uma mesma chave do dicionário que terá como valor uma lista.

    O force_list deverá ter nomes de nós do XML que necessariamente terão seus
    valores armazenados em uma lista no dicionário de retorno.


    ::
        Por exemplo:
        xml_1 = &lt;?xml version="1.0" encoding="UTF-8"?&gt;
        &lt;networkapi versao="1.0"&gt;
        &lt;testes&gt;
        &lt;teste&gt;1&lt;teste&gt;
        &lt;teste&gt;2&lt;teste&gt;
        &lt;/testes&gt;
        &lt;/networkapi&gt;

        A chamada loads(xml_1), irá gerar o dicionário: {'networkapi':{'testes':{'teste':[1,2]}}}

        xml_2 = &lt;?xml version="1.0" encoding="UTF-8"?&gt;
        &lt;networkapi versao="1.0"&gt;
        &lt;testes&gt;
        &lt;teste&gt;1&lt;teste&gt;
        &lt;/testes&gt;
        &lt;/networkapi&gt;

        A chamada loads(xml_2), irá gerar o dicionário: {'networkapi':{'testes':{'teste':1}}}

        A chamada loads(xml_2, ['teste']), irá gerar o dicionário: {'networkapi':{'testes':{'teste':[1]}}}

        Ou seja, o XML_2 tem apenas um nó 'teste', porém, ao informar o parâmetro 'force_list'
        com o valor ['teste'], a chave 'teste', no dicionário, terá o valor dentro de uma lista.

    :param xml: XML
    :param force_list: Lista com os nomes dos nós do XML que deverão ter seus valores
        armazenados em lista dentro da chave do dicionário de retorno.

    :return: Dicionário com os nós do XML.

    :raise XMLErrorUtils: Representa um erro ocorrido durante o marshall ou unmarshall do XML.
    """
    if force_list is None:
        force_list = []

    try:
        xml = remove_illegal_characters(xml)
        doc = parseString(xml)
    except Exception as e:
        raise XMLErrorUtils(e, u'Falha ao realizar o parse do xml.')

    root = doc.documentElement

    map = dict()
    attrs_map = dict()

    if root.hasAttributes():
        attributes = root.attributes
        for i in range(attributes.length):
            attr = attributes.item(i)
            attrs_map[attr.nodeName] = attr.nodeValue

    map[root.nodeName] = _create_childs_map(root, force_list)

    return map


def remove_illegal_characters(xml):
    RE_XML_ILLEGAL = u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' + \
                     u'|' + \
                     u'([%s-%s][^%s-%s])|([^%s-%s][%s-%s])|([%s-%s]$)|(^[%s-%s])' % \
        (unichr(0xd800), unichr(0xdbff), unichr(0xdc00), unichr(0xdfff),
         unichr(0xd800), unichr(0xdbff), unichr(0xdc00), unichr(0xdfff),
         unichr(0xd800), unichr(0xdbff), unichr(0xdc00), unichr(0xdfff))

    xml = re.sub(RE_XML_ILLEGAL, "?", xml)
    return xml
