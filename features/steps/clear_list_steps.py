from main import ToDoListManager, Task

to_do_list= ToDoListManager()
@given('the to-do list containing this tasks')
def step_impl(context):
    for row in context.table:
        to_do_list.add_task(row['Task'], row['Description'])

@when('the user clears the to-do list')
def step_impl(context):
    to_do_list.clear_all_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert to_do_list.tasks == [], f"Expected tasks: [], Actual tasks: {to_do_list.tasks}"