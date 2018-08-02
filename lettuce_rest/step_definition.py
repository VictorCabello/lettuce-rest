from lettuce import step, world, before

__all__ = [
    'set_base_url',
    'add_path_to_url',
    'do_not_verify_ssl_certs',
    'verify_ssl_certs',
    'set_header_step',
    'remove_header'
]

WORLD_PREFIX = 'world'


@before.all
def init_lettuce_rest():
    world.headers = {}
    world.base_url = ''
    world.verify_ssl = True


def set_or_resolve(property_name, new_value, special_setter=None):
    """
    This function sets a value for a world property but
    it the value starts with the WORLD_PREFIX then it will
    remove that prefix and try to get the value from the worl
    """
    value_to_set = new_value

    if new_value.startswith(WORLD_PREFIX):
        value_to_set = getattr(world, new_value[len(WORLD_PREFIX) + 1:])

    if special_setter:
        special_setter(value_to_set)
    else:
        setattr(world, property_name, value_to_set)


class SetHeaderHandler:

    def __init__(self, header_name):
        self.header_name = header_name

    def __call__(self, value):
        world.headers[self.header_name] = value


@step('I set base URL to "([^"]*)"')
def set_base_url(step, base_url):
    set_or_resolve('base_url', base_url)


@step('I add path "([^"]*)" to base URL')
def add_path_to_url(step, path):
    world.base_url += "/" + path


@step('I do not want to verify SSL certs')
def do_not_verify_ssl_certs(step):
    world.verify_ssl = False


@step('I want to verify SSL certs')
def verify_ssl_certs(step):
    world.verify_ssl = True


@step('I set "([^"]*)" header to "([^"]*)"')
def set_header_step(step, header_name, header_value):
    header_name = header_name.encode('ascii')
    header_value = header_value.encode('ascii')

    set_header_handler = SetHeaderHandler(header_name)
    set_or_resolve('headers', header_value, set_header_handler)


@step('I clear "([^"]*)" header')
def remove_header(step, header_name):
    world.headers.pop(header_name, None)


@step('I clear all headers')
def remove_all_headers(step):
    world.headers.clear()
