from main import ToDoListManager, Task

to_do_list= ToDoListManager()
@given('the to-do list contains the following incomplete tasks')
def step_impl(context):
    for row in context.table:
        to_do_list.add_task(row['Task'], row['Description'])

@when('the user marks task "{name}" as delayed')
def step_impl(context, name):
    print(name)
    to_do_list.mark_delayed(1)

@then('the to-do list should show task "{name}" as delayed')
def step_impl(context, name):
    for task in to_do_list.tasks:
        if task.name == name:
            assert task.status == 'Delayed', f"Expected status: Delayed, Actual status: {task.status}"
            break