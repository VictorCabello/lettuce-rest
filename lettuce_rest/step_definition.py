from lettuce import step, world

__all__ = [
    'set_base_url',
    'add_path_to_url'
]

WORLD_PREFIX = 'world'


def set_or_resolve(property_name, new_value):
    """
    This function sets a value for a world property but
    it the value starts with the WORLD_PREFIX then it will
    remove that prefix and try to get the value from the worl
    """
    value_to_set = new_value

    if new_value.startswith(WORLD_PREFIX):
        value_to_set = getattr(world, new_value[len(WORLD_PREFIX) + 1:])

    setattr(world, property_name, value_to_set)


@step('I set base URL to "([^"]*)"')
def set_base_url(step, base_url):
    set_or_resolve('base_url', base_url)


@step('I add path "([^"]*)" to base URL')
def add_path_to_url(step, path):
    world.base_url += "/" + path
