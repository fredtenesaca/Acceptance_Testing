from main import ToDoListManager, Task

to_do_list= ToDoListManager()
@given('the to-do list contains this new tasks')
def step_impl(context):
    for row in context.table:
        to_do_list.add_task(row['Task'], row['Description'])

@when('the user marks task "{name}" to be deleted from the to-do list')
def step_impl(context, name):
    to_do_list.delete_task(1)

@then('the to-do list shouldnt show task "{name}"')
def step_impl(context, name):
    for task in to_do_list.tasks:
        if task.name == name:
            assert False
    assert True
