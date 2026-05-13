import demistomock as demisto
from CommonServerPython import *


class Client(BaseClient):
    def __init__(self, server_url, verify, proxy, headers, auth):
        super().__init__(base_url=server_url, verify=verify, proxy=proxy, headers=headers, auth=auth)

    def controldetectionflowbyeventidandaction_request(self, action):
        params = assign_params(action=action)
        headers = self._headers

        response = self._http_request('put', 'detections/control', params=params, headers=headers)

        return response

    def performanactiononasingletarget_request(self, targetType,action,fraudType):
        params = assign_params(targetType=targetType, action=action, fraudType=fraudType)
        headers = self._headers

        response = self._http_request('post', 'actions/addone', params=params, headers=headers)

        return response

    def fetchthedetectiondataandconverttopdf_request(self, eventId):
        headers = self._headers

        response = self._http_request('get', f'detections/{eventId}/pdf', headers=headers)

        return response

    def retrieveeventscreenshotwitheventid_request(self, eventId):
        headers = self._headers

        response = self._http_request('get', f'detections/{eventId}/screenshot', headers=headers)

        return response

    def fetchthephishkitdatawithticketid_request(self, ticketId):
        headers = self._headers

        response = self._http_request('get', f'takedowns/{ticketId}/phishkit', headers=headers)

        return response

    def fetchthescreenshotdatawithticketid_request(self, ticketId):
        headers = self._headers

        response = self._http_request('get', f'takedowns/{ticketId}/screenshot', headers=headers)

        return response

    def fetchtheticketdataandconverttopdf_request(self, ticketId):
        headers = self._headers

        response = self._http_request('get', f'takedowns/{ticketId}/pdf', headers=headers)

        return response

    def gethtmlsourcecodeforaticket_request(self, ticketId):
        headers = self._headers

        response = self._http_request('get', f'takedowns/html/{ticketId}', headers=headers)

        return response

    def getlistofbrands_request(self):
        headers = self._headers

        response = self._http_request('get', 'brands', headers=headers)

        return response

    def getlistoffraudtypes_request(self):
        headers = self._headers

        response = self._http_request('get', 'fraud-types', headers=headers)

        return response

    def listofworklogsforticketid_request(self, ticketId):
        headers = self._headers

        response = self._http_request('get', f'takedowns/{ticketId}/worklogs', headers=headers)

        return response

    def listtakedownevents_request(self, fromDate, toDate, page, limit):
        params = assign_params(fromDate=fromDate, toDate=toDate, page=page, limit=limit)
        headers = self._headers

        response = self._http_request('get', 'takedowns/list', params=params, headers=headers)

        return response

    def listtakedowneventswithfilters_request(self, fromDate, toDate, _andId, fraudType, ticketStatus, DetectionDate, AuthorizationDate, CompletedDate, page, limit):
        params = assign_params(fromDate=fromDate, toDate=toDate, _andId=_andId, fraudType=fraudType, ticketStatus=ticketStatus, DetectionDate=DetectionDate, AuthorizationDate=AuthorizationDate, CompletedDate=CompletedDate, page=page, limit=limit)
        headers = self._headers

        response = self._http_request('get', 'takedowns/filtered-list', params=params, headers=headers)

        return response

    def performanactiononasingletarget_request(self, targetType, action, fraudType):
        params = assign_params(targetType=targetType, action=action, fraudType=fraudType)
        headers = self._headers

        response = self._http_request('post', 'actions/addone', params=params, headers=headers)

        return response

    def retrieveeventscreenshotwitheventid_request(self, eventId):
        headers = self._headers

        response = self._http_request('get', f'detections/{eventId}/screenshot', headers=headers)

        return response

    def retrievefilteredlistofmonitoringresultswithinspecifiedtimeframe_request(self, startDate, endDate, _andId, fraudType, monitoringStatus, page, limit):
        params = assign_params(startDate=startDate, endDate=endDate, _andId=_andId, fraudType=fraudType, monitoringStatus=monitoringStatus, page=page, limit=limit)
        headers = self._headers

        response = self._http_request('get', 'monitoring/filtered-list', params=params, headers=headers)

        return response

    def retrievelistofdetectionswithinspecifiedtimeframe_request(self, fromDate, toDate, scoreMin, ip, isp, registrar, monitoring, page, limit):
        params = assign_params(fromDate=fromDate, toDate=toDate, scoreMin=scoreMin, ip=ip, isp=isp, registrar=registrar, monitoring=monitoring, page=page, limit=limit)
        headers = self._headers

        response = self._http_request('get', 'detections/list', params=params, headers=headers)

        return response

    def retrievelistofmonitoringresultswithinspecifiedtimeframe_request(self, startDate, endDate, page, limit):
        params = assign_params(startDate=startDate, endDate=endDate, page=page, limit=limit)
        headers = self._headers

        response = self._http_request('get', 'monitoring/list', params=params, headers=headers)

        return response

    def retrievephishkitwitheventid_request(self, eventId):
        headers = self._headers

        response = self._http_request('get', f'detections/{eventId}/phishkit', headers=headers)

        return response

    def startorstopmonitoringforaspecificevent_request(self, action):
        params = assign_params(action=action)
        headers = self._headers

        response = self._http_request('put', 'monitoring/control', params=params, headers=headers)

        return response

    def updatetheactionwithticketid_request(self, action):
        params = assign_params(action=action)
        headers = self._headers

        response = self._http_request('put', 'takedowns/control', params=params, headers=headers)

        return response


def controldetectionflowbyeventidandaction_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    action = str(args.get('action', ''))

    response = client.controldetectionflowbyeventidandaction_request(action)
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def fetchthedetectiondataandconverttopdf_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    eventId = args.get('eventId', None)

    response = client.fetchthedetectiondataandconverttopdf_request(eventId)
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def fetchthephishkitdatawithticketid_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    ticketId = args.get('ticketId', None)

    response = client.fetchthephishkitdatawithticketid_request(ticketId)
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def fetchthescreenshotdatawithticketid_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    ticketId = args.get('ticketId', None)

    response = client.fetchthescreenshotdatawithticketid_request(ticketId)
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def fetchtheticketdataandconverttopdf_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    ticketId = args.get('ticketId', None)

    response = client.fetchtheticketdataandconverttopdf_request(ticketId)
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def gethtmlsourcecodeforaticket_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    ticketId = args.get('ticketId', None)

    response = client.gethtmlsourcecodeforaticket_request(ticketId)
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getlistofbrands_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.getlistofbrands_request()
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def getlistoffraudtypes_command(client: Client, args: Dict[str, Any]) -> CommandResults:

    response = client.getlistoffraudtypes_request()
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def listofworklogsforticketid_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    ticketId = args.get('ticketId', None)

    response = client.listofworklogsforticketid_request(ticketId)
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def listtakedownevents_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    fromDate = str(args.get('fromDate', ''))
    toDate = str(args.get('toDate', ''))
    page = args.get('page', None)
    limit = args.get('limit', None)

    response = client.listtakedownevents_request(fromDate, toDate, page, limit)
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def listtakedowneventswithfilters_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    fromDate = str(args.get('fromDate', ''))
    toDate = str(args.get('toDate', ''))
    _andId = args.get('_andId', None)
    fraudType = str(args.get('fraudType', ''))
    ticketStatus = str(args.get('ticketStatus', ''))
    DetectionDate = argToBoolean(args.get('DetectionDate', False))
    AuthorizationDate = argToBoolean(args.get('AuthorizationDate', False))
    CompletedDate = argToBoolean(args.get('CompletedDate', False))
    page = args.get('page', None)
    limit = args.get('limit', None)

    response = client.listtakedowneventswithfilters_request(fromDate, toDate, _andId, fraudType, ticketStatus, DetectionDate, AuthorizationDate, CompletedDate, page, limit)
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def performanactiononasingletarget_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    targetType = str(args.get('targetType', ''))
    action = str(args.get('action', ''))
    fraudType = str(args.get('fraudType', ''))

    response = client.performanactiononasingletarget_request(targetType, action, fraudType)
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def retrieveeventscreenshotwitheventid_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    eventId = args.get('eventId', None)

    response = client.retrieveeventscreenshotwitheventid_request(eventId)
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def retrievefilteredlistofmonitoringresultswithinspecifiedtimeframe_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    startDate = str(args.get('startDate', ''))
    endDate = str(args.get('endDate', ''))
    _andId = args.get('_andId', None)
    fraudType = str(args.get('fraudType', ''))
    monitoringStatus = str(args.get('monitoringStatus', ''))
    page = args.get('page', None)
    limit = args.get('limit', None)

    response = client.retrievefilteredlistofmonitoringresultswithinspecifiedtimeframe_request(startDate, endDate, _andId, fraudType, monitoringStatus, page, limit)
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def retrievelistofdetectionswithinspecifiedtimeframe_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    fromDate = str(args.get('fromDate', ''))
    toDate = str(args.get('toDate', ''))
    scoreMin = args.get('scoreMin', None)
    ip = str(args.get('ip', ''))
    isp = str(args.get('isp', ''))
    registrar = str(args.get('registrar', ''))
    monitoring = str(args.get('monitoring', ''))
    page = args.get('page', None)
    limit = args.get('limit', None)

    response = client.retrievelistofdetectionswithinspecifiedtimeframe_request(fromDate, toDate, scoreMin, ip, isp, registrar, monitoring, page, limit)
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def retrievelistofmonitoringresultswithinspecifiedtimeframe_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    startDate = str(args.get('startDate', ''))
    endDate = str(args.get('endDate', ''))
    page = args.get('page', None)
    limit = args.get('limit', None)

    response = client.retrievelistofmonitoringresultswithinspecifiedtimeframe_request(startDate, endDate, page, limit)
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def retrievephishkitwitheventid_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    eventId = args.get('eventId', None)

    response = client.retrievephishkitwitheventid_request(eventId)
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def startorstopmonitoringforaspecificevent_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    action = str(args.get('action', ''))

    response = client.startorstopmonitoringforaspecificevent_request(action)
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
        outputs_key_field='',
        outputs=response,
        raw_response=response
    )

    return command_results


def updatetheactionwithticketid_command(client: Client, args: Dict[str, Any]) -> CommandResults:
    action = str(args.get('action', ''))

    response = client.updatetheactionwithticketid_request(action)
    command_results = CommandResults(
        outputs_prefix='CSCFraudProtection',
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
    headers = {}
    headers['APIKey'] = params['api_key']

    command = demisto.command()
    demisto.debug(f'Command being called is {command}')

    try:
        requests.packages.urllib3.disable_warnings()
        client: Client = Client(urljoin(url, ''), verify_certificate, proxy, headers=headers, auth=None)
        
        commands = {
    		'csc-controldetectionflowbyeventidandaction': controldetectionflowbyeventidandaction_command,
			'csc-fetchthedetectiondataandconverttopdf': fetchthedetectiondataandconverttopdf_command,
			'csc-fetchthephishkitdatawithticketid': fetchthephishkitdatawithticketid_command,
			'csc-fetchthescreenshotdatawithticketid': fetchthescreenshotdatawithticketid_command,
			'csc-fetchtheticketdataandconverttopdf': fetchtheticketdataandconverttopdf_command,
			'csc-gethtmlsourcecodeforaticket': gethtmlsourcecodeforaticket_command,
			'csc-getlistofbrands': getlistofbrands_command,
			'csc-getlistoffraudtypes': getlistoffraudtypes_command,
			'csc-listofworklogsforticketid': listofworklogsforticketid_command,
			'csc-listtakedownevents': listtakedownevents_command,
			'csc-listtakedowneventswithfilters': listtakedowneventswithfilters_command,
			'csc-performanactiononasingletarget': performanactiononasingletarget_command,
			'csc-retrieveeventscreenshotwitheventid': retrieveeventscreenshotwitheventid_command,
			'csc-retrievefilteredlistofmonitoringresultswithinspecifiedtimeframe': retrievefilteredlistofmonitoringresultswithinspecifiedtimeframe_command,
			'csc-retrievelistofdetectionswithinspecifiedtimeframe': retrievelistofdetectionswithinspecifiedtimeframe_command,
			'csc-retrievelistofmonitoringresultswithinspecifiedtimeframe': retrievelistofmonitoringresultswithinspecifiedtimeframe_command,
			'csc-retrievephishkitwitheventid': retrievephishkitwitheventid_command,
			'csc-startorstopmonitoringforaspecificevent': startorstopmonitoringforaspecificevent_command,
			'csc-updatetheactionwithticketid': updatetheactionwithticketid_command,
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
