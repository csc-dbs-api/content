import pytest
import io
from CommonServerPython import *
from CSCTakedowns import Client, controldetectionflowbyeventidandaction_command, fetchthedetectiondataandconverttopdf_command, fetchthephishkitdatawithticketid_command, fetchthescreenshotdatawithticketid_command, fetchtheticketdataandconverttopdf_command, gethtmlsourcecodeforaticket_command, getlistofands_command, getlistoffraudtypes_command, listofworklogsforticketid_command, listtakedownevents_command, listtakedowneventswithfilters_command, performanactiononasingletarget_command, retrieveeventscreenshotwitheventid_command, retrievefilteredlistofmonitoringresultswithinspecifiedtimeframe_command, retrievelistofdetectionswithinspecifiedtimeframe_command, retrievelistofmonitoringresultswithinspecifiedtimeframe_command, retrievephishkitwitheventid_command, startorstopmonitoringforaspecificevent_command, updatetheactionwithticketid_command
SERVER_URL = 'https://test_url.com'


def util_load_json(path):
    with io.open(path, mode='r', encoding='utf-8') as f:
        return json.loads(f.read())


@pytest.fixture()
def client():
    return Client(server_url=SERVER_URL, verify=None, proxy=None, headers=None, auth=None)


def test_fetchthephishkitdatawithticketid_command(client, requests_mock):
    """
        When:
        Given:
        Then:
        """
    args = {'ticketId': '123'}
    mock_response_fetchthephishkitdatawithticketid_request = util_load_json(
        './test_data/outputs/fetchthephishkitdatawithticketid_request.json')
    mock_results = util_load_json(
        './test_data/outputs/fetchthephishkitdatawithticketid_command.json')
    requests_mock.post(SERVER_URL, json=mock_response_fetchthephishkitdatawithticketid_request)
    results = fetchthephishkitdatawithticketid_command(client=client, args=args
                                                       )
    assert results.outputs_prefix == ''
    assert results.outputs_key_field == ''
    assert results.outputs == mock_results.get('outputs')
    assert results.raw_response == mock_response_fetchthephishkitdatawithticketid_request


def test_fetchthescreenshotdatawithticketid_command(client, requests_mock):
    """
        When:
        Given:
        Then:
        """
    args = {'ticketId': '123'}
    mock_response_fetchthescreenshotdatawithticketid_request = util_load_json(
        './test_data/outputs/fetchthescreenshotdatawithticketid_request.json')
    mock_results = util_load_json(
        './test_data/outputs/fetchthescreenshotdatawithticketid_command.json')
    requests_mock.post(SERVER_URL, json=mock_response_fetchthescreenshotdatawithticketid_request)
    results = fetchthescreenshotdatawithticketid_command(client=client,
                                                         args=args)
    assert results.outputs_prefix == ''
    assert results.outputs_key_field == ''
    assert results.outputs == mock_results.get('outputs')
    assert results.raw_response == mock_response_fetchthescreenshotdatawithticketid_request
