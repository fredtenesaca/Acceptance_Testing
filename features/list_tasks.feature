Feature: List all tasks in the to-do list.
 Scenario: List all tasks in the to-do list
 Given the to-do list contains tasks
  | Task | Description |
  | Buy groceries | I need to buy groceries |
  | Pay bills | I need to pay the bills |
 When the user lists all tasks
 Then the output should contain tasks
  """
  Tasks:
  1. Name: Buy groceries, Description: I need to buy groceries, Status: Incomplete
  2. Name: Pay bills, Description: I need to pay the bills, Status: Incomplete
  """