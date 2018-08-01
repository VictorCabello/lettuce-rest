import sure
from lettuce import world
from mock import patch
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
