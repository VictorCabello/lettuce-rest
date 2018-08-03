import sure
from lettuce import world
from mock import patch, MagicMock, PropertyMock
from lettuce_rest import step_definition

SURE_VERSION = sure.version


def test_set_or_resolve_01():
    """
    test_set_or_resolve_01
    Verity static variable is assigned
    """
    step_definition.set_or_resolve('my_awsome_prop', 'super_value')

    result = world.my_awsome_prop

    result.should.be.equal('super_value')


def test_set_or_resolve_02():
    """
    test_set_or_resolve_02
    Verity dynimic variable is resolved and assigned
    """
    world.old_prop = 'this value was already defined'

    step_definition.set_or_resolve('my_awsome_prop', 'world.old_prop')

    result = world.my_awsome_prop

    result.should.be.equal('this value was already defined')


@patch('lettuce_rest.step_definition.set_or_resolve')
def test_set_base_url_01(set_or_resolve_mock):
    """
    test_set_base_url_01
    Verify that the function calls the set_or_resolve function as
    expected
    """
    step_definition.set_base_url(None, 'new_url')
    set_or_resolve_mock.assert_called_once_with('base_url', 'new_url')


def test_add_path_to_url_01():
    """
    test_add_path_to_url_01
    Verify that the function calls the set_or_resolve function as
    expected
    """
    world.base_url = 'http://fake.io'
    step_definition.add_path_to_url(None, 'appended_part')
    result = world.base_url

    result.should.be.equal('http://fake.io/appended_part')


def test_do_not_verify_ssl_certs_01():
    step_definition.do_not_verify_ssl_certs(None)
    result = world.verify_ssl

    result.should.be.equal(False)


def test_verify_ssl_certs():
    step_definition.verify_ssl_certs(None)
    result = world.verify_ssl

    result.should.be.equal(True)


def test_set_header_step_01():
    """
    test_set_header_step_01
    Verify default value
    """
    step_definition.init_lettuce_rest()
    result = world.headers

    result.should.be.equal({})


def test_set_header_step_02():
    """
    test_set_header_step_02
    Verify static value
    """
    step_definition.init_lettuce_rest()

    step_definition.set_header_step(None,
                                    'test_name',
                                    'test_value')

    result = world.headers

    result.should.be.equal({'test_name': 'test_value'})


def test_set_header_step_03():
    """
    test_set_header_step_03
    Verify dynimic value
    """
    step_definition.init_lettuce_rest()
    world.old_prop = 'this value was already defined'

    step_definition.set_header_step(None,
                                    'test_name',
                                    'world.old_prop')

    result = world.headers
    result.should.be.equal({'test_name': 'this value was already defined'})


def test_set_header_step_04():
    """
    test_set_header_step_04
    Set 2 headers
    """
    step_definition.init_lettuce_rest()

    step_definition.set_header_step(None, 'test_name_1', 'test_value_1')
    step_definition.set_header_step(None, 'test_name_2', 'test_value_2')

    result = world.headers

    result.should.be.equal({
        'test_name_1': 'test_value_1',
        'test_name_2': 'test_value_2'
    })


def test_set_header_step_05():
    """
    test_set_header_step_05
    Edit existing header
    """
    step_definition.init_lettuce_rest()

    step_definition.set_header_step(None, 'test_name_1', 'test_value_1')
    step_definition.set_header_step(None, 'test_name_1', 'test_value_2')

    result = world.headers

    result.should.be.equal({
        'test_name_1': 'test_value_2'
    })


def test_remove_header_01():
    step_definition.init_lettuce_rest()
    world.headers['test_name_1'] = 'test_value'
    world.headers['test_name_2'] = 'test_value'

    step_definition.remove_header(None, 'test_name_1')

    result = world.headers

    result.should.be.equal({'test_name_2': 'test_value'})


def test_remove_all_headers_01():
    step_definition.init_lettuce_rest()
    world.headers['test_name_1'] = 'test_value'
    world.headers['test_name_2'] = 'test_value'

    step_definition.remove_all_headers(None)

    result = world.headers

    result.should.be.equal({})


@patch('lettuce_rest.step_definition.requests')
def test_request_with_parameters_01(requests_mock):
    """
    request_with_parameters_01
    Verify request no headers, with ssl verification with static parameters
    """
    input_values = {
        'base_url': 'http://fake.io',
        'input_parameters': [{
            'param1':  'value1',
            'param2':  'value2',
        }],
        'request_verb': 'GET',
        'url_path_segment': 'api_name'
    }

    helper_request_with_parameters(**input_values)

    requests_mock.get.assert_called_once_with('http://fake.io/api_name',
                                              {
                                                  'param1': 'value1',
                                                  'param2': 'value2',
                                              },
                                              headers={},
                                              verify=True)


@patch('lettuce_rest.step_definition.requests')
def test_request_with_parameters_02(requests_mock):
    """
    request_with_parameters_02
    Verify request a header, without ssl verification with dynamic parameters
    """
    world.random_var = 'some_value'
    world.headers = {'header_1': 'value'}
    world.verify_ssl = False
    input_values = {
        'base_url': 'http://fake.io',
        'input_parameters': [{
            'param1':  'world.random_var',
            'param2':  'value2',
        }],
        'request_verb': 'GET',
        'url_path_segment': 'api_name'
    }

    helper_request_with_parameters(**input_values)

    requests_mock.get.assert_called_once_with('http://fake.io/api_name',
                                              {
                                                  'param1': 'some_value',
                                                  'param2': 'value2',
                                              },
                                              headers={'header_1': 'value'},
                                              verify=False)


def helper_request_with_parameters(base_url='',
                                   request_verb='',
                                   input_parameters=[],
                                   url_path_segment=''):
    world.base_url = base_url

    hasesh_mock = PropertyMock(return_value=input_parameters)
    step_mock = MagicMock()
    type(step_mock).hasesh = hasesh_mock

    step_definition.request_with_parameters(step_mock,
                                            request_verb,
                                            url_path_segment)

