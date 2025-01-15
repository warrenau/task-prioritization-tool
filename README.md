# task-prioritization-tool

## requirements
- show how daily tasks contribute to overall progress
- prioritize tasks based on urgency and importance without user decision
- visual display of ranking
- easy interactive creation, editing, and deletion of tasks
- categories/tags to track work in different areas
- available/transferrable to all work/home computers

## inputs from user
- task name
- due date
- hours required for task to be completed
- hours spent working already
- progress
- importance
- category/tag

## program outputs
- table/list of all tasks in order of priority score
- calculate priority score from user inputs

The below shows an example of the output table list the user can interact with.

| Task Name | Due Date | Est Time to Completion | Progress | Importance | Tag
| --- | --- | --- | --- | --- | --- |
| Chapter 1 | 2024-09-30 | 6 hours | 30% | 80 | Dissertation |

## prioritization function
- must calculate priority score upon initial task creation
- must re-calculate priority score on edit
- the table must be resorted every time priority scores are calculated to rank from highest priority to lowest

This will probably take two functions?
1. one function to calc priority score
2. another function to update table and ranking on edit/new task

Calculation of priority and sorting functions should be called during new task creation and any time a task is edited. I don't think I will need to optimize the sorter very much. There should not be so many tasks that it is a problem for a modern computer.

## math
The priority score is based on the urgency (the time needed to complete the task compared to the time available until the task is due) and the importance of the task.

$$priority = f\left( t_{due}, t_{completion}, importance \right)$$

This calculation assumes that there are 4 productive hours in the work day. Some days will have more, some will have less. 

### Time

There are 3 conditions to consider for the time term:

1. The estimated time to completion is less than the time remaining before the due date,
2. the estimated time to completion is greater than the time remaining before the due date but the due date has not passed, and
3. the due date has passed.

For condition 1, the impact of time should increase as the difference gets smaller, thus squaring the difference. Not sure yet if this is the best way to do it. I don't think there is a way for all three cases to use the same math.

$$ \frac{1}{\left( t_{due}-t_{completion} \right)^2} $$

For condition 2, the impact of the time should be much greater than that of the importance. I am not sure yet how to handle that.

For condition 3, the impact of the time should be massive. However, a very low importance task that is overdue should not automatically rank higher priority than a high importance task. This should also cause a UI indicator, like coloring the background of the task row red or something.
