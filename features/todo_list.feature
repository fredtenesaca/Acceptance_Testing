Feature: Add a task to the to-do list.
 Scenario: Adding a task
 Given the To-Do list is empty
 When the user adds a task "Buy groceries" "I need to buy groceries"
 Then the to-do list should contain "Buy groceries"



