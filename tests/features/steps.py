from lettuce import step, world
import sure

sure.version


@step(u'I set the property "([^"]*)" of the world to "([^"]*)"')
def set_prop(step, property_name, value):
    setattr(world, property_name, value)


@step(u'the property "([^"]*)" of the world should be "([^"]*)"')
def check_prop(step, property_name, value):
    result = getattr(world, property_name)

    str(result).should.be.equal(value)
