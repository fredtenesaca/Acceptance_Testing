from main import ToDoListManager, Task
to_do_list= ToDoListManager()
@given('the to-do list is empty')
def step_impl(context):
# Set the to-do list as an empty list
    global to_do_list
    to_do_list.tasks = []
# Step 2: When the user adds a task "Buy groceries"
@when('the user adds a task "{name}" "{description}"')
def step_impl(context, name, description):
# Add the task to the to-do list
    global to_do_list
    to_do_list.add_task(name, description)
# Step 3: Then the to-do list should contain "Buy groceries"
@then('the to-do list should contain "{name}"')
def step_impl(context, name):
# Check if the task is in the to-do list
    global to_do_list
    assert any(task.name == name for task in to_do_list.tasks), f'Task "{name}" not found in the to-do list'
