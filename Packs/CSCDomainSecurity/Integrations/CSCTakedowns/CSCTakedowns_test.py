import pytest
import io
from CommonServerPython import *
from CSCTakedowns import Client, fetchthephishkitdatawithticketid_command, fetchthescreenshotdatawithticketid_command, fetchtheticketdataandconverttopdf_command, gethtmlsourcecodeforaticket_command, listofworklogsforticketid_command, listtakedownevents_command, listtakedowneventswithfilters_command, updatetheactionwithticketid_command
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
    mock_response_request = util_load_json(
        './test_data/outputs/fetchthephishkitdatawithticketid_request.json')
    mock_results = util_load_json(
        './test_data/outputs/fetchthephishkitdatawithticketid_command.json')
    requests_mock.post(SERVER_URL, json=mock_response_request)
    results = fetchthephishkitdatawithticketid_command(client=client, args=args
                                                       )
    assert results.outputs_prefix == 'CSCFraudProtection'
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
    mock_response_request = util_load_json(
        './test_data/outputs/fetchthescreenshotdatawithticketid_request.json')
    mock_results = util_load_json(
        './test_data/outputs/fetchthescreenshotdatawithticketid_command.json')
    requests_mock.post(SERVER_URL, json=mock_response_fetchthescreenshotdatawithticketid_request)
    results = fetchthescreenshotdatawithticketid_command(client=client, args=args
                                                       )
    assert results.outputs_prefix == 'CSCFraudProtection'
    assert results.outputs_key_field == ''
    assert results.outputs == mock_results.get('outputs')
    assert results.raw_response == mock_response_request

def test_fetchtheticketdataandconverttopdf_command(client, requests_mock):
    """
        When:
        Given:
        Then:
        """
    args = {'ticketId': '123'}
    mock_response_request = util_load_json(
        './test_data/outputs/fetchtheticketdataandconverttopdf_request.json')
    mock_results = util_load_json(
        './test_data/outputs/fetchtheticketdataandconverttopdf_command.json')
    requests_mock.post(SERVER_URL, json=mock_response_request)
    results = fetchtheticketdataandconverttopdf_command(client=client, args=args
                                                       )
    assert results.outputs_prefix == 'CSCFraudProtection'
    assert results.outputs_key_field == ''
    assert results.outputs == mock_results.get('outputs')
    assert results.raw_response == mock_response_request

def test_gethtmlsourcecodeforaticket_command(client, requests_mock):
    """
        When:
        Given:
        Then:
        """
    args = {'ticketId': '123'}
    mock_response_request = util_load_json(
        './test_data/outputs/gethtmlsourcecodeforaticket_request.json')
    mock_results = util_load_json(
        './test_data/outputs/gethtmlsourcecodeforaticket_command.json')
    requests_mock.post(SERVER_URL, json=mock_response_request)
    results = gethtmlsourcecodeforaticket_command(client=client, args=args
                                                       )
    assert results.outputs_prefix == 'CSCFraudProtection'
    assert results.outputs_key_field == ''
    assert results.outputs == mock_results.get('outputs')
    assert results.raw_response == mock_response_request

def test_listofworklogsforticketid_command(client, requests_mock):
    """
        When:
        Given:
        Then:
        """
    args = {'ticketId': '123'}
    mock_response_request = util_load_json(
        './test_data/outputs/listofworklogsforticketid_request.json')
    mock_results = util_load_json(
        './test_data/outputs/listofworklogsforticketid_command.json')
    requests_mock.post(SERVER_URL, json=mock_response_request)
    results = listofworklogsforticketid_command(client=client, args=args
                                                       )
    assert results.outputs_prefix == 'CSCFraudProtection'
    assert results.outputs_key_field == ''
    assert results.outputs == mock_results.get('outputs')
    assert results.raw_response == mock_response_request

    def test_listtakedowneventswithfilters_command(client, requests_mock):
        """
            When:
            Given:
            Then:
            """
        args = {'fromDate':'2026-01-01', 'toDate':'2026-03-01'}
        mock_response_request = util_load_json(
            './test_data/outputs/listtakedowneventswithfilters_request.json')
        mock_results = util_load_json(
            './test_data/outputs/listtakedowneventswithfilters_command.json')
        requests_mock.post(SERVER_URL, json=mock_response_request)
        results = listtakedowneventswithfilters_command(client=client, args=args
                                                           )
        assert results.outputs_prefix == 'CSCFraudProtection'
        assert results.outputs_key_field == ''
        assert results.outputs == mock_results.get('outputs')
        assert results.raw_response == mock_response_request

    def test_updatetheactionwithticketid_command(client, requests_mock):
        """
            When:
            Given:
            Then:
            """
        args = {'action':'OPEN'}
        mock_response_request = util_load_json(
            './test_data/outputs/updatetheactionwithticketid_request.json')
        mock_results = util_load_json(
            './test_data/outputs/updatetheactionwithticketid_command.json')
        requests_mock.post(SERVER_URL, json=mock_response_request)
        results = updatetheactionwithticketid_command(client=client, args=args
                                                           )
        assert results.outputs_prefix == 'CSCFraudProtection'
        assert results.outputs_key_field == ''
        assert results.outputs == mock_results.get('outputs')
        assert results.raw_response == mock_response_request

