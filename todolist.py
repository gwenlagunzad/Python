def display_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Done")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print(f'Task "{task}" added.')

def view_tasks(tasks):
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i}. {task['task']} - {status}")

def mark_as_done(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]["done"] = True
        print(f'Task "{tasks[task_number]["task"]}" marked as done.')
    else:
        print("Invalid task number.")

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as f:
        for task in tasks:
            status = "1" if task["done"] else "0"
            f.write(f"{task['task']}|{status}\n")

def load_tasks(filename="tasks.txt"):
    tasks = []
    try:
        with open(filename, "r") as f:
            for line in f:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "done": status == "1"})
    except FileNotFoundError:
        pass
    return tasks

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_as_done(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() # Simple To-Do List Application
