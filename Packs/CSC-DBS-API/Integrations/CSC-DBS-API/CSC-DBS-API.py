import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401
from CommonServerUserPython import *  # noqa


class Client(BaseClient):
    def __init__(self, server_url, verify, proxy, headers, auth):
        super().__init__(base_url=server_url, verify=verify, proxy=proxy, headers=headers, auth=auth)

    def activateurlforwardingnode_request(self):
        headers = self._headers

        response = self._http_request('put', 'urlf/activate', headers=headers)

        return response

    def addonedsrecordtoadomain_request(self):
        headers = self._headers

        response = self._http_request('post', 'dsrecord', headers=headers)

        return response

    def addurlforwardingnode_request(self):
        headers = self._headers

        response = self._http_request('put', 'urlf', headers=headers)

        return response

    def cancelazoneeditwithafailedstatus_request(self, editID):
        headers = self._headers

        response = self._http_request('delete', f'zones/edits/{editID}', headers=headers)

        return response

    def checkregistrationavailabilityforoneormoredomainnames_request(self, qualifiedDomainNames):
        params = assign_params(qualifiedDomainNames=qualifiedDomainNames)
        headers = self._headers

        response = self._http_request('get', 'domains/availability', params=params, headers=headers)

        return response

    def deletealldsrecordsforthegivendomainname_request(self):
        headers = self._headers

        response = self._http_request('delete', 'dsrecord/all', headers=headers)

        return response

    def deleteasingledsrecordforadomain_request(self):
        headers = self._headers

        response = self._http_request('delete', 'dsrecord/single', headers=headers)

        return response

    def deleteurlforwardingbyqualifieddomainname_request(self, qualifiedDomainName):
        headers = self._headers

        response = self._http_request('delete', f'urlf/{qualifiedDomainName}', headers=headers)

        return response

    def deleteurlforwardingbyqualifieddomainnameandnodename_request(self, qualifiedDomainName, nodeName):
        headers = self._headers

        response = self._http_request('delete', f'urlf/{qualifiedDomainName}/node/{nodeName}', headers=headers)

        return response

    def getalldsrecordsforaqualifieddomainname_request(self, qualifiedDomainName):
        headers = self._headers

        response = self._http_request('get', f'dsrecord/{qualifiedDomainName}', headers=headers)

        return response

    def getasinglezoneeditbyitsuuid_request(self, editID):
        headers = self._headers

        response = self._http_request('get', f'zones/edits/{editID}', headers=headers)

        return response

    def getbusinessunitdata_request(self, filter_):
        params = assign_params(filter=filter_)
        headers = self._headers

        response = self._http_request('get', 'admin/businessunits', params=params, headers=headers)

        return response

    def getbusinessunitdatabybusinessunitname_request(self, businessUnitName):
        headers = self._headers

        response = self._http_request('get', f'admin/businessunits/{businessUnitName}', headers=headers)

        return response

    def getcertificatebyuuid_request(self, uuid):
        headers = self._headers

        response = self._http_request('get', f'tls/certificate/{uuid}', headers=headers)

        return response

    def getcustomfieldsforthisaccount_request(self, ):
        headers = self._headers

        response = self._http_request('get', 'admin/customfields', headers=headers)

        return response

    def getdomainconfigurationinformationforowneddomainswithoptionalfiltering_request(self, filter_ ):
        params = assign_params(filter=filter_)
        headers = self._headers

        response = self._http_request('get', 'domains/configuration', params=params, headers=headers)

        return response

    def getdomaindatabyqualifieddomainname_request(self, qualifiedDomainName):
        headers = self._headers

        response = self._http_request('get', f'domains/{qualifiedDomainName}', headers=headers)

        return response

    def getdomainportfoliodata_request(self, filter_):
        params = assign_params(filter=filter_)
        headers = self._headers

        response = self._http_request('get', 'domains', params=params, headers=headers)

        return response

    def getoneormorecertificates_request(self, filter_):
        params = assign_params(filter=filter_)
        headers = self._headers

        response = self._http_request('get', 'tls/certificate', params=params, headers=headers)

        return response

    def getoneormoreorders_request(self, filter_):
        params = assign_params(filter=filter_)
        headers = self._headers

        response = self._http_request('get', 'orderstatus', params=params, headers=headers)

        return response

    def getoneormoresecurityevents_request(self, filter_):
        params = assign_params(filter=filter_)
        headers = self._headers

        response = self._http_request('get', 'events', params=params, headers=headers)

        return response

    def getoneormorezoneedits_request(self, filter_):
        params = assign_params(filter=filter_)
        headers = self._headers

        response = self._http_request('get', 'zones/edits', params=params, headers=headers)

        return response

    def getordersbytheiruuid_request(self, orderUUID):
        headers = self._headers

        response = self._http_request('get', f'orderstatus/{orderUUID}', headers=headers)

        return response

    def getsecurityeventsbyid_request(self, eventID):
        headers = self._headers

        response = self._http_request('get', f'events/{eventID}', headers=headers)

        return response

    def getthecurrentstatusofazoneedit_request(self, editID):
        headers = self._headers

        response = self._http_request('get', f'zones/edits/status/{editID}', headers=headers)

        return response

    def geturlforwardingdatabyqualifieddomainname_request(self, qualifiedDomainName):
        headers = self._headers

        response = self._http_request('get', f'urlf/{qualifiedDomainName}', headers=headers)

        return response

    def getwhoiscontactprofiledata_request(self, filter_):
        params = assign_params(filter=filter_)
        headers = self._headers

        response = self._http_request('get', 'admin/whoiscontactprofiles', params=params, headers=headers)

        return response

    def getzonedatabyqualifiedzonename_request(self, zoneName, filter_):
        params = assign_params(filter=filter_)
        headers = self._headers

        response = self._http_request('get', f'zones/{zoneName}', params=params, headers=headers)

        return response

    def getzoneportfoliodata_request(self, filter_):
        params = assign_params(filter=filter_)
        headers = self._headers

        response = self._http_request('get', 'zones', params=params, headers=headers)

        return response

    def modifythebusinessunitassociatedwithadomain_request(self, businessUnitName, qualifiedDomainName):
        headers = self._headers

        response = self._http_request('put', f'admin/businessunit/{businessUnitName}/domain/{qualifiedDomainName}', headers=headers)

        return response

    def modifythecustomfieldsassociatedwithadomain_request(self):
        headers = self._headers

        response = self._http_request('put', 'admin/customfields', headers=headers)

        return response

    def placeadomainregistrationorder_request(self):
        headers = self._headers

        response = self._http_request('post', 'domains/registration', headers=headers)

        return response

    def placeansmodificationorder_request(self):
        headers = self._headers

        response = self._http_request('put', 'domains/nsmodification', headers=headers)

        return response

    def placeatlsregistrationorder_request(self):
        headers = self._headers

        response = self._http_request('post', 'tls/registration', headers=headers)

        return response

    def placeatlsreissueorder_request(self):
        headers = self._headers

        response = self._http_request('post', 'tls/reissue', headers=headers)

        return response

    def placeatlsrenewalorder_request(self):
        headers = self._headers

        response = self._http_request('post', 'tls/renewal', headers=headers)

        return response

    def placeawhoiscontactmodificationorder_request(self):
        headers = self._headers

        response = self._http_request('put', 'domains/whoiscontactmodification', headers=headers)

        return response

    def refreshexpiredtoken_request(self):
        headers = self._headers

        response = self._http_request('put', 'token/refresh', headers=headers)

        return response

    def submitandpublishoneormorezoneedits_request(self):
        headers = self._headers

        response = self._http_request('post', 'zones/edits', headers=headers)

        return response


def activateurlforwardingnode_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.activateurlforwardingnode_request()
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.UrlForwardingActivateResult',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def addonedsrecordtoadomain_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.addonedsrecordtoadomain_request()
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def addurlforwardingnode_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.addurlforwardingnode_request()
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.UrlForwardingResult',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def cancelazoneeditwithafailedstatus_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    editID = str(args.get('editID', ''))

    response = client.cancelazoneeditwithafailedstatus_request(editID)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def checkregistrationavailabilityforoneormoredomainnames_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    qualifiedDomainNames = str(args.get('qualifiedDomainNames', ''))

    response = client.checkregistrationavailabilityforoneormoredomainnames_request(qualifiedDomainNames)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.RegistrationAvailabilityResult',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def deletealldsrecordsforthegivendomainname_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.deletealldsrecordsforthegivendomainname_request()
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def deleteasingledsrecordforadomain_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.deleteasingledsrecordforadomain_request()
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def deleteurlforwardingbyqualifieddomainname_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    qualifiedDomainName = str(args.get('qualifiedDomainName', ''))

    response = client.deleteurlforwardingbyqualifieddomainname_request(qualifiedDomainName)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.UrlForwardingDeleteAllResult',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def deleteurlforwardingbyqualifieddomainnameandnodename_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    qualifiedDomainName = str(args.get('qualifiedDomainName', ''))
    nodeName = str(args.get('nodeName', ''))

    response = client.deleteurlforwardingbyqualifieddomainnameandnodename_request(qualifiedDomainName, nodeName)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.UrlForwardingDeleteResult',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getalldsrecordsforaqualifieddomainname_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    qualifiedDomainName = str(args.get('qualifiedDomainName', ''))

    response = client.getalldsrecordsforaqualifieddomainname_request(qualifiedDomainName)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getasinglezoneeditbyitsuuid_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    editID = str(args.get('editID', ''))

    response = client.getasinglezoneeditbyitsuuid_request(editID)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.ZoneEdit',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getbusinessunitdata_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    filter_ = str(args.get('filter_', ''))


    response = client.getbusinessunitdata_request(filter_)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.PagedBusinessUnitResponse',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getbusinessunitdatabybusinessunitname_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    businessUnitName = str(args.get('businessUnitName', ''))

    response = client.getbusinessunitdatabybusinessunitname_request(businessUnitName)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.BusinessUnit',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getcertificatebyuuid_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    uuid = str(args.get('uuid', ''))

    response = client.getcertificatebyuuid_request(uuid)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.TlsOrderResponse',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getcustomfieldsforthisaccount_command(client: Client, args: Dict[str, Any]) -> CommandResults:


    response = client.getcustomfieldsforthisaccount_request()
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.AccountCustomFields',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getdomainconfigurationinformationforowneddomainswithoptionalfiltering_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    filter_ = str(args.get('filter_', ''))
    response = client.getdomainconfigurationinformationforowneddomainswithoptionalfiltering_request(filter_)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.ConfigurationCallSuccess',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getdomaindatabyqualifieddomainname_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    qualifiedDomainName = str(args.get('qualifiedDomainName', ''))

    response = client.getdomaindatabyqualifieddomainname_request(qualifiedDomainName)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.Domain',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getdomainportfoliodata_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    filter_ = str(args.get('filter_', ''))


    response = client.getdomainportfoliodata_request(filter_)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.PagedDomainResponse',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getoneormorecertificates_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    filter_ = str(args.get('filter_', ''))

    response = client.getoneormorecertificates_request(filter_)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.MultiTlsRetrieveResponse',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getoneormoreorders_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    filter_ = str(args.get('filter_', ''))

    response = client.getoneormoreorders_request(filter_)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.MultiOrderResponse',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getoneormoresecurityevents_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    filter_ = str(args.get('filter_', ''))


    response = client.getoneormoresecurityevents_request(filter_)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.PagedEventResponse',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getoneormorezoneedits_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    filter_ = str(args.get('filter_', ''))


    response = client.getoneormorezoneedits_request(filter_)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.PagedZoneEditResponse',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getordersbytheiruuid_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    orderUUID = str(args.get('orderUUID', ''))

    response = client.getordersbytheiruuid_request(orderUUID)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.Order',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getsecurityeventsbyid_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    eventID = str(args.get('eventID', ''))

    response = client.getsecurityeventsbyid_request(eventID)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.SecurityEvent',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getthecurrentstatusofazoneedit_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    editID = str(args.get('editID', ''))

    response = client.getthecurrentstatusofazoneedit_request(editID)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.ZoneEditStatusResult',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def geturlforwardingdatabyqualifieddomainname_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    qualifiedDomainName = str(args.get('qualifiedDomainName', ''))

    response = client.geturlforwardingdatabyqualifieddomainname_request(qualifiedDomainName)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.UrlForwardingRecords',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getwhoiscontactprofiledata_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    filter_ = str(args.get('filter_', ''))


    response = client.getwhoiscontactprofiledata_request(filter_)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.WhoisContactProfilePagedResource',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getzonedatabyqualifiedzonename_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    zoneName = str(args.get('zoneName', ''))
    filter_ = str(args.get('filter_', ''))

    response = client.getzonedatabyqualifiedzonename_request(zoneName, filter_)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.Zone',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getzoneportfoliodata_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    filter_ = str(args.get('filter_', ''))

    response = client.getzoneportfoliodata_request(filter_)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.PagedZoneResponse',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def modifythebusinessunitassociatedwithadomain_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    businessUnitName = str(args.get('businessUnitName', ''))
    qualifiedDomainName = str(args.get('qualifiedDomainName', ''))

    response = client.modifythebusinessunitassociatedwithadomain_request(businessUnitName, qualifiedDomainName)
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.businessUnitModResult',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def modifythecustomfieldsassociatedwithadomain_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.modifythecustomfieldsassociatedwithadomain_request()
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.customFieldModResult',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def placeadomainregistrationorder_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.placeadomainregistrationorder_request()
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def placeansmodificationorder_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.placeansmodificationorder_request()
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.NsModRequestResult',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def placeatlsregistrationorder_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.placeatlsregistrationorder_request()
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.TlsResponse',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def placeatlsreissueorder_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.placeatlsreissueorder_request()
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.TlsResponseEV',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def placeatlsrenewalorder_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.placeatlsrenewalorder_request()
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API.TlsResponseUCC',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def placeawhoiscontactmodificationorder_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.placeawhoiscontactmodificationorder_request()
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def refreshexpiredtoken_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.refreshexpiredtoken_request()
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def submitandpublishoneormorezoneedits_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.submitandpublishoneormorezoneedits_request()
    command_results = CommandResults(
        outputs_prefix='CSC-DBS-API',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def test_module(client: Client) -> None:
    # Test functions here
    return_results('ok')


def main() -> None:

    params: Dict[str, Any] = demisto.params()
    args: Dict[str, Any] = demisto.args()
    url = params.get('url')
    verify_certificate: bool = not params.get('insecure', False)
    proxy = params.get('proxy', False)
    # Extract token and api_key securely from credential fields (type: 9)
    token_creds = params.get('token', {}) or {}
    api_key_creds = params.get('api_key', {}) or {}

    token = token_creds.get('password')
    api_key = api_key_creds.get('password')

    headers = {
        "Authorization": f"Bearer {token}",  # Or just token if your API doesn’t need “Bearer”
        "apikey": api_key
    }

    command = demisto.command()
    demisto.debug(f'Command being called is {command}')

    try:
        requests.packages.urllib3.disable_warnings()
        client: Client = Client(urljoin(url, ''), verify_certificate, proxy, headers=headers, auth=None)
        
        commands = {
    		'csc-dbs-api-activateurlforwardingnode': activateurlforwardingnode_command,
			'csc-dbs-api-addonedsrecordtoadomain': addonedsrecordtoadomain_command,
			'csc-dbs-api-addurlforwardingnode': addurlforwardingnode_command,
			'csc-dbs-api-cancelazoneeditwithafailedstatus': cancelazoneeditwithafailedstatus_command,
			'csc-dbs-api-checkregistrationavailabilityforoneormoredomainnames': checkregistrationavailabilityforoneormoredomainnames_command,
			'csc-dbs-api-deletealldsrecordsforthegivendomainname': deletealldsrecordsforthegivendomainname_command,
			'csc-dbs-api-deleteasingledsrecordforadomain': deleteasingledsrecordforadomain_command,
			'csc-dbs-api-deleteurlforwardingbyqualifieddomainname': deleteurlforwardingbyqualifieddomainname_command,
			'csc-dbs-api-deleteurlforwardingbyqualifieddomainnameandnodename': deleteurlforwardingbyqualifieddomainnameandnodename_command,
			'csc-dbs-api-getalldsrecordsforaqualifieddomainname': getalldsrecordsforaqualifieddomainname_command,
			'csc-dbs-api-getasinglezoneeditbyitsuuid': getasinglezoneeditbyitsuuid_command,
			'csc-dbs-api-getbusinessunitdata': getbusinessunitdata_command,
			'csc-dbs-api-getbusinessunitdatabybusinessunitname': getbusinessunitdatabybusinessunitname_command,
			'csc-dbs-api-getcertificatebyuuid': getcertificatebyuuid_command,
			'csc-dbs-api-getcustomfieldsforthisaccount': getcustomfieldsforthisaccount_command,
			'csc-dbs-api-getdomainconfigurationinformationforowneddomainswithoptionalfiltering': getdomainconfigurationinformationforowneddomainswithoptionalfiltering_command,
			'csc-dbs-api-getdomaindatabyqualifieddomainname': getdomaindatabyqualifieddomainname_command,
			'csc-dbs-api-getdomainportfoliodata': getdomainportfoliodata_command,
			'csc-dbs-api-getoneormorecertificates': getoneormorecertificates_command,
			'csc-dbs-api-getoneormoreorders': getoneormoreorders_command,
			'csc-dbs-api-getoneormoresecurityevents': getoneormoresecurityevents_command,
			'csc-dbs-api-getoneormorezoneedits': getoneormorezoneedits_command,
			'csc-dbs-api-getordersbytheiruuid': getordersbytheiruuid_command,
			'csc-dbs-api-getsecurityeventsbyid': getsecurityeventsbyid_command,
			'csc-dbs-api-getthecurrentstatusofazoneedit': getthecurrentstatusofazoneedit_command,
			'csc-dbs-api-geturlforwardingdatabyqualifieddomainname': geturlforwardingdatabyqualifieddomainname_command,
			'csc-dbs-api-getwhoiscontactprofiledata': getwhoiscontactprofiledata_command,
			'csc-dbs-api-getzonedatabyqualifiedzonename': getzonedatabyqualifiedzonename_command,
			'csc-dbs-api-getzoneportfoliodata': getzoneportfoliodata_command,
			'csc-dbs-api-modifythebusinessunitassociatedwithadomain': modifythebusinessunitassociatedwithadomain_command,
			'csc-dbs-api-modifythecustomfieldsassociatedwithadomain': modifythecustomfieldsassociatedwithadomain_command,
			'csc-dbs-api-placeadomainregistrationorder': placeadomainregistrationorder_command,
			'csc-dbs-api-placeansmodificationorder': placeansmodificationorder_command,
			'csc-dbs-api-placeatlsregistrationorder': placeatlsregistrationorder_command,
			'csc-dbs-api-placeatlsreissueorder': placeatlsreissueorder_command,
			'csc-dbs-api-placeatlsrenewalorder': placeatlsrenewalorder_command,
			'csc-dbs-api-placeawhoiscontactmodificationorder': placeawhoiscontactmodificationorder_command,
			'csc-dbs-api-refreshexpiredtoken': refreshexpiredtoken_command,
			'csc-dbs-api-submitandpublishoneormorezoneedits': submitandpublishoneormorezoneedits_command,
        }

        if command == 'test-module':
            test_module(client)
        elif command in commands:
            return_results(commands[command](client, args))
        else:
            raise NotImplementedError(f'{command} command is not implemented.')

    except Exception as e:
        return_error(str(e))


if __name__ in ['__main__', 'builtin', 'builtins']:
    main()
