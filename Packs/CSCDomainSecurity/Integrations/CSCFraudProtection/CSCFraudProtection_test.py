import pytest
import io
from CommonServerPython import *
from CSCFraudProtection import (
    Client,
    fetchthephishkitdatawithticketid_command,
    fetchthescreenshotdatawithticketid_command,
    fetchtheticketdataandconverttopdf_command,
    gethtmlsourcecodeforaticket_command,
    listofworklogsforticketid_command,
    listtakedowneventswithfilters_command,
    updatetheactionwithticketid_command,
    getlistofbrands_command,
    getlistoffraudtypes_command,
    retrievelistofdetectionswithinspecifiedtimeframe_command,
    retrievefilteredlistofmonitoringresultswithinspecifiedtimeframe_command,
    retrievelistofmonitoringresultswithinspecifiedtimeframe_command,
    fetchthedetectiondataandconverttopdf_command,
    fetchthescreenshotdatawithticketid_command,
    gethtmlsourcecodeforaticket_command,
    listofworklogsforticketid_command,
    updatetheactionwithticketid_command,
    startorstopmonitoringforaspecificevent_command,
    listtakedownevents_command,
)

SERVER_URL = 'https://test_url.com'


def util_load_json(path):
    with io.open(path, mode='r', encoding='utf-8') as f:
        return json.loads(f.read())


@pytest.fixture()
def client():
    return Client(server_url=SERVER_URL, verify=None, proxy=None, headers=None, auth=None)


def test_fetchthephishkitdatawithticketid_command(client, requests_mock):
    args = {'ticketId': '123'}
    mock_response = util_load_json('./test_data/outputs/fetchthephishkitdatawithticketid_request.json')
    mock_results = util_load_json('./test_data/outputs/fetchthephishkitdatawithticketid_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = fetchthephishkitdatawithticketid_command(client, args)

    assert results.outputs == mock_results.get('outputs')


def test_fetchthescreenshotdatawithticketid_command(client, requests_mock):
    args = {'ticketId': '123'}
    mock_response = util_load_json('./test_data/outputs/fetchthescreenshotdatawithticketid_request.json')
    mock_results = util_load_json('./test_data/outputs/fetchthescreenshotdatawithticketid_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = fetchthescreenshotdatawithticketid_command(client, args)

    assert results.outputs == mock_results.get('outputs')


def test_fetchtheticketdataandconverttopdf_command(client, requests_mock):
    args = {'ticketId': '123'}
    mock_response = util_load_json('./test_data/outputs/fetchtheticketdataandconverttopdf_request.json')
    mock_results = util_load_json('./test_data/outputs/fetchtheticketdataandconverttopdf_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = fetchtheticketdataandconverttopdf_command(client, args)

    assert results.outputs == mock_results.get('outputs')


def test_gethtmlsourcecodeforaticket_command(client, requests_mock):
    args = {'ticketId': '123'}
    mock_response = util_load_json('./test_data/outputs/gethtmlsourcecodeforaticket_request.json')
    mock_results = util_load_json('./test_data/outputs/gethtmlsourcecodeforaticket_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = gethtmlsourcecodeforaticket_command(client, args)

    assert results.outputs == mock_results.get('outputs')


def test_listofworklogsforticketid_command(client, requests_mock):
    args = {'ticketId': '123'}
    mock_response = util_load_json('./test_data/outputs/listofworklogsforticketid_request.json')
    mock_results = util_load_json('./test_data/outputs/listofworklogsforticketid_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = listofworklogsforticketid_command(client, args)

    assert results.outputs == mock_results.get('outputs')


def test_listtakedowneventswithfilters_command(client, requests_mock):
    args = {'fromDate': '2026-01-01', 'toDate': '2026-03-01'}
    mock_response = util_load_json('./test_data/outputs/listtakedowneventswithfilters_request.json')
    mock_results = util_load_json('./test_data/outputs/listtakedowneventswithfilters_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = listtakedowneventswithfilters_command(client, args)

    assert results.outputs == mock_results.get('outputs')


def test_updatetheactionwithticketid_command(client, requests_mock):
    args = {'action': 'OPEN'}
    mock_response = util_load_json('./test_data/outputs/updatetheactionwithticketid_request.json')
    mock_results = util_load_json('./test_data/outputs/updatetheactionwithticketid_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = updatetheactionwithticketid_command(client, args)

    assert results.outputs == mock_results.get('outputs')


def test_getlistofbrands_command(client, requests_mock):
    mock_response = util_load_json('./test_data/outputs/getlistofbrands_request.json')
    mock_results = util_load_json('./test_data/outputs/getlistofbrands_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = getlistofbrands_command(client, {})

    assert results.outputs == mock_results.get('outputs')


def test_getlistoffraudtypes_command(client, requests_mock):
    mock_response = util_load_json('./test_data/outputs/getlistoffraudtypes_request.json')
    mock_results = util_load_json('./test_data/outputs/getlistoffraudtypes_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = getlistoffraudtypes_command(client, {})

    assert results.outputs == mock_results.get('outputs')


def test_retrievelistofdetectionswithinspecifiedtimeframe_command(client, requests_mock):
    args = {'fromDate': '2026-01-01', 'toDate': '2026-03-01'}
    mock_response = util_load_json('./test_data/outputs/retrievelistofdetectionswithinspecifiedtimeframe_request.json')
    mock_results = util_load_json('./test_data/outputs/retrievelistofdetectionswithinspecifiedtimeframe_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = retrievelistofdetectionswithinspecifiedtimeframe_command(client, args)

    assert results.outputs == mock_results.get('outputs')


def test_retrievefilteredlistofmonitoringresultswithinspecifiedtimeframe_command(client, requests_mock):
    args = {
        'fromDate': '2026-01-01',
        'toDate': '2026-03-01',
        'brand': 'BrandA',
        'fraudType': 'FraudTypeA'
    }
    mock_response = util_load_json('./test_data/outputs/retrievefilteredlistofmonitoringresultswithinspecifiedtimeframe_request.json')
    mock_results = util_load_json('./test_data/outputs/retrievefilteredlistofmonitoringresultswithinspecifiedtimeframe_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = retrievefilteredlistofmonitoringresultswithinspecifiedtimeframe_command(client, args)

    assert results.outputs == mock_results.get('outputs')


def test_retrievelistofmonitoringresultswithinspecifiedtimeframe_command(client, requests_mock):
    args = {'fromDate': '2026-01-01', 'toDate': '2026-03-01'}
    mock_response = util_load_json('./test_data/outputs/retrievelistofmonitoringresultswithinspecifiedtimeframe_request.json')
    mock_results = util_load_json('./test_data/outputs/retrievelistofmonitoringresultswithinspecifiedtimeframe_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = retrievelistofmonitoringresultswithinspecifiedtimeframe_command(client, args)

    assert results.outputs == mock_results.get('outputs')



def test_fetchthedetectiondataandconverttopdf_command(client, requests_mock):
    args = {'detectionId': '123'}
    mock_response = util_load_json('./test_data/outputs/fetchthedetectiondataandconverttopdf_request.json')
    mock_results = util_load_json('./test_data/outputs/fetchthedetectiondataandconverttopdf_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = fetchthedetectiondataandconverttopdf_command(client, args)

    assert results.outputs == mock_results.get('outputs')


def test_fetchthescreenshotdataforadetectionid_command(client, requests_mock):
    args = {'detectionId': '123'}
    mock_response = util_load_json('./test_data/outputs/fetchthescreenshotdataforadetectionid_request.json')
    mock_results = util_load_json('./test_data/outputs/fetchthescreenshotdataforadetectionid_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = fetchthescreenshotdatawithticketid_command(client, args)

    assert results.outputs == mock_results.get('outputs')


def test_gethtmlsourcecodeforadetectionid_command(client, requests_mock):
    args = {'detectionId': '123'}
    mock_response = util_load_json('./test_data/outputs/gethtmlsourcecodeforadetectionid_request.json')
    mock_results = util_load_json('./test_data/outputs/gethtmlsourcecodeforadetectionid_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = gethtmlsourcecodeforaticket_command(client, args)

    assert results.outputs == mock_results.get('outputs')


def test_listofworklogsfordetectionid_command(client, requests_mock):
    args = {'detectionId': '123'}
    mock_response = util_load_json('./test_data/outputs/listofworklogsfordetectionid_request.json')
    mock_results = util_load_json('./test_data/outputs/listofworklogsfordetectionid_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = listofworklogsforticketid_command(client, args)

    assert results.outputs == mock_results.get('outputs')


def test_updatetheactionfordetectionid_command(client, requests_mock):
    args = {'detectionId': '123', 'action': 'OPEN'}
    mock_response = util_load_json('./test_data/outputs/updatetheactionfordetectionid_request.json')
    mock_results = util_load_json('./test_data/outputs/updatetheactionfordetectionid_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = updatetheactionwithticketid_command(client, args)

    assert results.outputs == mock_results.get('outputs')


def test_startorstopmonitoringforaspecificevent_command(client, requests_mock):
    args = {'eventId': '123', 'action': 'START'}
    mock_response = util_load_json('./test_data/outputs/startorstopmonitoringforaspecificevent_request.json')
    mock_results = util_load_json('./test_data/outputs/startorstopmonitoringforaspecificevent_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = startorstopmonitoringforaspecificevent_command(client, args)

    assert results.outputs == mock_results.get('outputs')


def test_listtakedownevents_command(client, requests_mock):
    mock_response = util_load_json('./test_data/outputs/listtakedownevents_request.json')
    mock_results = util_load_json('./test_data/outputs/listtakedownevents_command.json')

    requests_mock.post(SERVER_URL, json=mock_response)
    results = listtakedownevents_command(client, {})

    assert results.outputs == mock_results.get('outputs')