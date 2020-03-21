#!/bin/python3

class Task:
    """ Task class: Attributes: task_name, priority"""
    def __init__(self, task_name, priority):
        self.task_name = task_name
        self.priority = priority

    def __str__(self):
        return "{}: {}".format(self.task_name, self.priority)

class Scheduler:
    """Schedules list of task by priority"""
    def __init__(self, num_task, task_list=None, low=0, high=100):
        self.num_task = num_task
        self.low = low
        self.high = high
        self.num_task = num_task
        self.task_list = self.build_task_list(task_list)

    def schedule(self):
        self.task_list.sort(key = lambda task: task.priority, reverse=True)

    def build_task_list(self, task_list):
        tasks = []
        for task in task_list:
            task_name, priority = task.split(' ')
            priority = int(priority)
            if (priority >= self.low) and (priority <= self.high):
                new_task = Task(task_name, priority)
                tasks.append(new_task)
        return tasks

    def __str__(self):
        return '>'.join(map(lambda x: x.task_name, self.task_list))

# Main
if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        text = f.read()

    lines_stack = text.split('\n')
    num_test = int(lines_stack.pop(0))
    output = []

    for _ in range(num_test): # Iterate for all test cases
        low, high = list(map(int, lines_stack.pop(0).split(' ')))
        number_of_tasks = int(lines_stack.pop(0))
        task_list = lines_stack[0:number_of_tasks]
        # Build Scheduler
        our_scheduler = Scheduler(number_of_tasks, task_list, low, 55)
        our_scheduler.schedule()
        
        output.append(f"{our_scheduler}")
        del lines_stack[0: number_of_tasks] #already read

    with open('output.txt', 'w') as f:
        for i in range(len(output)):
            f.write(f"Case {i+1}: {output[i]}\n")
