from behave import *


@given(u'reverse_flask is set up')
def flask_is_setup(context):
    assert context.client


@when(u'we submit the form with the string "{string_input}"')
def submit_form(context, string_input):
    context.page = context.client.post('/', data=dict(input=string_input),follow_redirects=True)


@then(u'we should see the output "{output}"')
def output(context, output):
    assert output in context.page.data.decode()


@then(u'we should see the alert "{message}"')
def alert(context, message):
    assert message in context.page.data.decode()
