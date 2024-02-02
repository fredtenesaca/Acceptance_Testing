Feature: Mark a task as completed.
 Scenario: Mark a task as completed
 Given the to-do list contains the following tasks
  | Task | Description |
  | Buy groceries | I need to buy groceries |
 When the user marks task "Buy groceries" as completed
 Then the to-do list should show task "Buy groceries" as completed