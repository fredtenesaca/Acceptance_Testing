Feature: Clear the entire to-do list.
 Scenario: Clear the entire to-do list
 Given the to-do list containing this tasks
  | Task | Description |
  | Buy groceries | I need to buy groceries |
  | Pay bills | I need to pay the bills |
 When the user clears the to-do list
 Then the to-do list should be empty