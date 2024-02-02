Feature: Delete a task in the to-do list.
 Scenario: Delete a task in the to-do list
 Given the to-do list contains this new tasks
  | Task | Description |
  | Buy groceries | I need to buy groceries |
  | Pay bills | I need to pay the bills |
 When the user marks task "Buy groceries" to be deleted from the to-do list
 Then the to-do list shouldnt show task "Buy groceries"
