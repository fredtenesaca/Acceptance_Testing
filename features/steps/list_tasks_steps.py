from main import ToDoListManager, Task

to_do_list= ToDoListManager()
@given('the to-do list contains tasks')
def step_impl(context):
    for row in context.table:
        to_do_list.add_task(row['Task'], row['Description'])

@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    # Puedes imprimir la lista de tareas o realizar la lógica de la aplicación aquí
    context.actual_output= to_do_list.list_tasks()

@then('the output should contain tasks')
def step_then_output_should_contain(context):
    expected_output = context.text
    expected_output_string= ''.join(expected_output.splitlines())
    assert context.actual_output == expected_output_string, f"Expected: {expected_output_string}, Actual: {context.actual_output}"

