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


class NetworkAPIClientError(Exception):

    def __init__(self, error):
        self.error = error

    def __str__(self):
        msg = u'%s' % (self.error)
        return msg.encode('utf-8', 'replace')


class DataBaseError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class XMLError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class ScriptError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class InvalidRequestError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, u'Chamada incorreta.')


class UserNotAuthenticatedError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(
            self,
            u'Usuário não autenticado. Usuário e/ou senha incorretos.')


class UserNotAuthorizedError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(
            self,
            u'Usuário não autorizado para executar a operação.')


class UrlNotFoundError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(
            self,
            u'Não encontrado. Uso de uma URL inválida.')


class NotImplementedError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, u'Chamada não implementada')


class TipoEquipamentoNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class ModeloEquipamentoNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class GrupoEquipamentoNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class InvalidParameterError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class EquipamentoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class EquipmentDontRemoveError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class GroupDontRemoveError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class VlanNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class EquipamentoNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class IPNaoDisponivelError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class IpError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class IpNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class HealthCheckExpectNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class HealthCheckExpectJaCadastradoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class VlanError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class ConfigEnvironmentInvalidError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class TipoRedeNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class AmbienteNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class InterfaceNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class RelacionamentoInterfaceEquipamentoNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class InterfaceInvalidBackFrontError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class InterfaceSwitchProtegidaError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class LigacaoFrontInterfaceNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class LigacaoFrontNaoTerminaSwitchError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class VipVersaoIPError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class VipError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class VipNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class VipAllreadyCreateError(VipError):

    def __init__(self, error):
        VipError.__init__(self, error)


class NomeTipoRoteiroDuplicadoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)

class NumeroRackDuplicadoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)

class NomeRackDuplicadoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)

class RackConfiguracaoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)

class RackAplicarError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)

class TipoRoteiroNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class RoteiroNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class RoteiroError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class EquipamentoRoteiroError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class EquipamentoRoteiroNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class MarcaNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)

class RackNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)

class MarcarError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)

class RacksError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)

class RackAllreadyConfigError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)

class ModeloEquipamentoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class ProtocoloTipoAcessoDuplicadoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class TipoAcessoNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class TipoAcessoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class EquipamentoAcessoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class EquipamentoAcessoNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class NomeInterfaceDuplicadoParaEquipamentoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class InterfaceError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class TipoRedeError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class NomeDivisaoDcDuplicadoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class DivisaoDcNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class DivisaoDcError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class NomeAmbienteLogicoDuplicadoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class AmbienteLogicoNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class AmbienteLogicoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class NomeGrupoL3DuplicadoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class GrupoL3NaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class GrupoL3Error(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class AmbienteDuplicadoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class AmbienteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class EquipamentoAmbienteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class EquipamentoAmbienteNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class UserUsuarioDuplicadoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class UsuarioNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class UsuarioError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class NomeGrupoUsuarioDuplicadoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class ValorIndicacaoPermissaoInvalidoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class GrupoUsuarioNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class UsuarioGrupoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class UsuarioGrupoNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class EquipamentoGrupoNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class PermissaoAdministrativaNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class NomeRoteiroDuplicadoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class NomeMarcaDuplicadoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)

class NomeMarcaModeloDuplicadoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class NomeTipoRedeDuplicadoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class NomeGrupoEquipamentoDuplicadoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class TipoRoteiroError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class PermissaoAdministrativaDuplicadaError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class DireitoGrupoEquipamentoNaoExisteError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class ValorIndicacaoDireitoInvalidoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class DireitoGrupoEquipamentoDuplicadoError(NetworkAPIClientError):

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class EnvironmentVipError(NetworkAPIClientError):

    """returns exception to environment vip."""

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class EnvironmentVipNotFoundError(NetworkAPIClientError):

    """returns exception to environment research by primary key."""

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class OptionVipError(NetworkAPIClientError):

    """returns exception to option vip."""

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class OptionVipNotFoundError(NetworkAPIClientError):

    """returns exception to option research by primary key."""

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class VlanAclExistenteError(VlanError):

    """returns exception to find a Vlan with a ACL-file that already exists."""

    def __init__(self, error):
        VlanError.__init__(self, error)


class VipIpError(VlanError):

    """returns exception to ip cant removed from vip."""

    def __init__(self, error):
        VlanError.__init__(self, error)


class DetailedEnvironmentError(NetworkAPIClientError):

    """returns exception to environment cant be removed because vlan has vip request association"""

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class InvalidTimeoutValueError(InvalidParameterError):

    """returns exception of invalid timeout value """

    def __init__(self, error):
        InvalidParameterError.__init__(self, error)


class InvalidBalMethodValueError(InvalidParameterError):

    """returns exception of invalid balancing method value """

    def __init__(self, error):
        InvalidParameterError.__init__(self, error)


class InvalidCacheValueError(InvalidParameterError):

    """returns exception of invalid cache value """

    def __init__(self, error):
        InvalidParameterError.__init__(self, error)


class InvalidFinalityValueError(InvalidParameterError):

    """returns exception of invalid finality value """

    def __init__(self, error):
        InvalidParameterError.__init__(self, error)


class InvalidPersistenceValueError(InvalidParameterError):

    """returns exception of invalid persistence value """

    def __init__(self, error):
        InvalidParameterError.__init__(self, error)


class InvalidPriorityValueError(InvalidParameterError):

    """returns exception of invalid priority value """

    def __init__(self, error):
        InvalidParameterError.__init__(self, error)


class IpEquipmentError(NetworkAPIClientError):

    """returns exception of invalid ip and equipment association"""

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class RealServerPriorityError(InvalidParameterError):

    """returns exception of invalid real server priority list"""

    def __init__(self, error):
        InvalidParameterError.__init__(self, error)


class RealServerWeightError(InvalidParameterError):

    """returns exception of invalid real server weight list"""

    def __init__(self, error):
        InvalidParameterError.__init__(self, error)


class RealServerPortError(InvalidParameterError):

    """returns exception of invalid real server port list"""

    def __init__(self, error):
        InvalidParameterError.__init__(self, error)


class RealParameterValueError(InvalidParameterError):

    """returns exception of invalid real server parameter"""

    def __init__(self, error):
        InvalidParameterError.__init__(self, error)


class RealServerScriptError(NetworkAPIClientError):

    """returns exception of real server script error"""

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class IpNotFoundByEquipAndVipError(NetworkAPIClientError):

    """returns exception of real server error"""

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class FilterNotFoundError(NetworkAPIClientError):

    """returns exception of filter search"""

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class FilterEqTypeAssociationError(NetworkAPIClientError):

    """returns exception of filter and equip type already exist"""

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class FilterDuplicateError(NetworkAPIClientError):

    """returns exception of filter name already exist"""

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class PermissionNotFoundError(NetworkAPIClientError):

    """returns exception of filter search"""

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class NetworkIPRangeEnvError(NetworkAPIClientError):

    """returns exception of two environments having the same ip range"""

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class IpRangeAlreadyAssociation(NetworkAPIClientError):

    """returns exception whey trying to associate ip and equipment, and equipment having another ip in the same ip range"""

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class CantDissociateError(NetworkAPIClientError):

    """returns exception whey trying to dissociate filter and equipment type, and some environment is using the filter"""

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class IpEquipCantDissociateFromVip(NetworkAPIClientError):

    """Returns exception when trying to dissociate ip and equipment, but equipment is the last balancer for Vip Request"""

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class VipRequestNoBlockInRule(NetworkAPIClientError):

    """Returns exception when trying to add a block in rule vip that doesn't has any block"""

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class VipRequestBlockAlreadyInRule(NetworkAPIClientError):

    """Returns exception when trying to add a block that already exists in rule vip"""

    def __init__(self, error):
        NetworkAPIClientError.__init__(self, error)


class ErrorHandler(object):

    '''Classe que trata os códigos de erros retornados pela networkAPI e lança a exceção
    correspondente na networkAPI-Client.
    '''
    # Mapa com todos os erros retornados pela networkAPI.
    errors = {1: DataBaseError,
              2: ScriptError,
              3: XMLError,
              4: XMLError,
              100: TipoEquipamentoNaoExisteError,
              101: ModeloEquipamentoNaoExisteError,
              102: GrupoEquipamentoNaoExisteError,
              103: InvalidParameterError,
              104: InvalidParameterError,
              105: InvalidParameterError,
              106: InvalidParameterError,
              107: EquipamentoError,
              108: VlanError,
              109: VlanError,
              110: VlanError,
              111: TipoRedeNaoExisteError,
              112: AmbienteNaoExisteError,
              113: InvalidParameterError,
              114: InvalidParameterError,
              115: InvalidParameterError,
              116: VlanNaoExisteError,
              117: EquipamentoNaoExisteError,
              118: IpError,
              119: IpNaoExisteError,
              120: IpError,
              121: VlanError,
              122: VlanError,
              123: InvalidParameterError,
              124: HealthCheckExpectNaoExisteError,
              125: InvalidFinalityValueError,
              126: InvalidParameterError,
              127: InvalidParameterError,
              128: InvalidCacheValueError,
              129: InvalidParameterError,
              130: InvalidParameterError,
              131: InvalidBalMethodValueError,
              132: InvalidPersistenceValueError,
              133: InvalidParameterError,
              134: InvalidParameterError,
              135: InvalidTimeoutValueError,
              136: InvalidParameterError,
              137: InvalidParameterError,
              138: InvalidParameterError,
              139: LigacaoFrontInterfaceNaoExisteError,
              140: InvalidParameterError,
              141: InterfaceNaoExisteError,
              142: RelacionamentoInterfaceEquipamentoNaoExisteError,
              143: InterfaceSwitchProtegidaError,
              144: LigacaoFrontNaoTerminaSwitchError,
              145: InvalidParameterError,
              146: EquipamentoError,
              147: InvalidParameterError,
              148: EquipamentoError,
              149: EquipamentoError,
              150: IPNaoDisponivelError,
              151: InvalidParameterError,
              152: VipNaoExisteError,
              153: IpNaoExisteError,
              154: InvalidParameterError,
              156: EquipamentoAmbienteError,
              157: EquipamentoAmbienteNaoExisteError,
              158: TipoRoteiroNaoExisteError,
              159: InvalidParameterError,
              160: GrupoL3NaoExisteError,
              161: InvalidParameterError,
              162: AmbienteLogicoNaoExisteError,
              163: InvalidParameterError,
              164: DivisaoDcNaoExisteError,
              165: RoteiroNaoExisteError,
              166: InvalidParameterError,
              167: MarcaNaoExisteError,
              168: InvalidParameterError,
              169: NomeGrupoL3DuplicadoError,
              170: InvalidParameterError,
              171: TipoAcessoNaoExisteError,
              172: InvalidParameterError,
              173: NomeAmbienteLogicoDuplicadoError,
              174: InvalidParameterError,
              175: NomeDivisaoDcDuplicadoError,
              176: InvalidParameterError,
              177: UsuarioNaoExisteError,
              178: InvalidParameterError,
              179: UserUsuarioDuplicadoError,
              180: GrupoUsuarioNaoExisteError,
              181: InvalidParameterError,
              182: NomeGrupoUsuarioDuplicadoError,
              183: UsuarioGrupoError,
              184: UsuarioGrupoNaoExisteError,
              185: EquipamentoGrupoNaoExisteError,
              186: VipError,
              187: NomeInterfaceDuplicadoParaEquipamentoError,
              189: PermissaoAdministrativaNaoExisteError,
              190: EquipamentoRoteiroNaoExisteError,
              191: VipError,
              192: VipAllreadyCreateError,
              193: NomeTipoRoteiroDuplicadoError,
              194: InvalidParameterError,
              195: InvalidParameterError,
              196: TipoRoteiroError,
              197: RoteiroError,
              198: EquipamentoRoteiroError,
              199: MarcarError,
              200: InvalidParameterError,
              201: InvalidParameterError,
              202: ModeloEquipamentoError,
              203: ProtocoloTipoAcessoDuplicadoError,
              204: TipoAcessoError,
              205: InvalidParameterError,
              206: InvalidParameterError,
              207: InvalidParameterError,
              208: InvalidParameterError,
              209: EquipamentoAcessoNaoExisteError,
              210: InvalidParameterError,
              211: InvalidParameterError,
              212: InterfaceNaoExisteError,
              213: InterfaceNaoExisteError,
              214: InterfaceError,
              215: TipoRedeError,
              216: DivisaoDcError,
              217: AmbienteLogicoError,
              218: GrupoL3Error,
              219: AmbienteDuplicadoError,
              220: AmbienteError,
              221: InvalidParameterError,
              222: InvalidParameterError,
              223: InvalidParameterError,
              224: UsuarioError,
              225: InvalidParameterError,
              226: InvalidParameterError,
              227: InvalidParameterError,
              228: InvalidParameterError,
              229: ValorIndicacaoPermissaoInvalidoError,
              230: ValorIndicacaoPermissaoInvalidoError,
              231: ValorIndicacaoPermissaoInvalidoError,
              232: ValorIndicacaoPermissaoInvalidoError,
              233: InvalidParameterError,
              234: InvalidParameterError,
              235: InvalidParameterError,
              236: InvalidParameterError,
              237: InvalidParameterError,
              238: InvalidParameterError,
              239: InvalidParameterError,
              240: ValorIndicacaoPermissaoInvalidoError,
              241: ValorIndicacaoPermissaoInvalidoError,
              242: EquipamentoAcessoError,
              243: InvalidParameterError,
              244: InvalidParameterError,
              245: InvalidParameterError,
              246: InvalidParameterError,
              247: InvalidParameterError,
              248: InvalidParameterError,
              249: InvalidParameterError,
              250: NomeRoteiroDuplicadoError,
              251: NomeMarcaDuplicadoError,
              252: NomeMarcaModeloDuplicadoError,
              253: NomeTipoRedeDuplicadoError,
              254: NomeGrupoEquipamentoDuplicadoError,
              255: InvalidParameterError,
              256: InvalidParameterError,
              257: PermissaoAdministrativaDuplicadaError,
              258: DireitoGrupoEquipamentoNaoExisteError,
              259: InvalidParameterError,
              260: InvalidParameterError,
              261: InvalidParameterError,
              262: InvalidParameterError,
              263: ValorIndicacaoDireitoInvalidoError,
              264: ValorIndicacaoDireitoInvalidoError,
              265: ValorIndicacaoDireitoInvalidoError,
              266: ValorIndicacaoDireitoInvalidoError,
              267: DireitoGrupoEquipamentoDuplicadoError,
              268: InvalidParameterError,
              269: InvalidParameterError,
              270: InvalidParameterError,
              271: InvalidParameterError,
              272: InvalidParameterError,
              273: DataBaseError,
              274: InvalidParameterError,
              275: InvalidParameterError,
              276: InvalidParameterError,
              277: InvalidParameterError,
              278: InvalidParameterError,
              279: InvalidParameterError,
              280: InvalidParameterError,
              281: InvalidParameterError,
              282: InvalidParameterError,
              283: EnvironmentVipNotFoundError,
              284: EnvironmentVipError,
              285: EnvironmentVipError,
              286: InvalidParameterError,
              287: InvalidParameterError,
              288: IpError,
              289: OptionVipNotFoundError,
              290: OptionVipError,
              291: OptionVipError,
              292: IpNaoExisteError,
              293: VlanError,
              294: ConfigEnvironmentInvalidError,
              295: IPNaoDisponivelError,
              296: IPNaoDisponivelError,
              297: VipError,
              298: VipError,
              307: InterfaceInvalidBackFrontError,
              309: EquipmentDontRemoveError,
              310: GroupDontRemoveError,
              315: VlanError,
              400: InvalidRequestError,
              401: UserNotAuthenticatedError,
              402: UserNotAuthorizedError,
              404: UrlNotFoundError,
              501: NotImplementedError,
              311: VlanAclExistenteError,
              312: EquipamentoError,
              313: HealthCheckExpectJaCadastradoError,
              314: VlanError,
              316: EnvironmentVipNotFoundError,
              317: IpError,
              318: VipError,
              319: VipIpError,
              320: EquipamentoAmbienteError,
              321: EnvironmentVipError,
              322: VipError,
              323: DetailedEnvironmentError,
              324: DetailedEnvironmentError,
              325: InvalidPriorityValueError,
              326: EquipamentoNaoExisteError,
              327: IpEquipmentError,
              328: IpError,
              329: RealServerPriorityError,
              330: RealServerWeightError,
              331: RealServerPortError,
              332: RealParameterValueError,
              333: RealServerScriptError,
              334: IpNotFoundByEquipAndVipError,
              335: IPNaoDisponivelError,
              336: VipIpError,
              337: InvalidParameterError,
              338: DataBaseError,
              339: FilterNotFoundError,
              340: DataBaseError,
              341: DataBaseError,
              342: TipoEquipamentoNaoExisteError,
              343: FilterEqTypeAssociationError,
              344: FilterDuplicateError,
              345: VipError,
              346: NetworkIPRangeEnvError,
              347: IpRangeAlreadyAssociation,
              348: CantDissociateError,
              350: PermissionNotFoundError,
              351: PermissaoAdministrativaDuplicadaError,
              352: IpEquipCantDissociateFromVip,
              354: VipIpError,
              355: VipIpError,
              356: VipIpError,
              357: EnvironmentVipError,
              358: InvalidParameterError,
              376: NumeroRackDuplicadoError,
              378: RacksError,
              379: RackNaoExisteError,
              380: RackAllreadyConfigError,
              381: NomeRackDuplicadoError,
              382: RackConfiguracaoError,
              383: RackAplicarError
              }

    @classmethod
    def handle(cls, code, description):
        '''Recebe o código e a descrição do erro da networkAPI e lança a exceção correspondente.

        :param code: Código de erro retornado pela networkAPI.
        :param description: Descrição do erro.

        :return: None
        '''
        if code is None:
            raise NetworkAPIClientError(description)

        if int(code) in cls.errors:
            raise cls.errors[int(code)](description)
        else:
            raise NetworkAPIClientError(description)
