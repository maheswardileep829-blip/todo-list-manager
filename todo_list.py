import json
# TODO List Manager - Project #9
try:
    with open('todos.txt', 'r') as file:
        todos = json.load(file)
    print("✓ Loaded previous tasks!")
except:
    todos = []
    print("Starting fresh!")

def show_menu():
    print("\n" + "="*50)
    print("TODO LIST MANAGER")
    print("="*50)
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Save and quit")
    print("="*50)

# Main loop
while True:
    show_menu()
    choice = input("\nChoose option (1-5): ")
    
    if choice == '1':
        if len(todos) == 0:
            print("ERROR! You don't have anything on your list yet!")
        else:
            print("\nYOUR TASKS:")
            for i, task in enumerate(todos, 1):
                status = "✓" if task['complete'] else "○"
                print(f"{i}. [{status}] {task['task']}")
        
    elif choice == '2':
        task = input("What is the task you want to add? ")
        new_task = {
            'task' : task,
            'complete' : False
        }
        todos.append(new_task)
        print(f"✓ Added {task}")
    
    elif choice == '3':
        if len(todos) == 0:
            print("No tasks to mark complete!")
        else:
            print("\nYOUR TASKS:")
            for i, task in enumerate(todos, 1):
                status = "✓" if task['complete'] else "○"
            print(f"{i}. [{status}] {task['task']}")
        
        # Ask which one
        task_num = int(input("\nWhich task number to mark complete? "))
        
        # Mark it complete
        todos[task_num - 1]['complete'] = True
        print(f"✓ Marked task {task_num} as complete!")
    
    elif choice == '4':
        if len(todos) == 0:
            print("No tasks to delete!")
        else:
            print ("\n YOUR TASKS:")
        for i, task in enumerate(todos, 1):
            status = "✓" if task['complete'] else "○"
            print(f"{i}. [{status}] {task['task']}")
        delete = int(input ("Which task do you want to delete (Numbers only)?"))
        todos.pop(delete - 1)
        print(f"✓ Deleted task {delete}!")
    
    elif choice == '5':
        with open('todos.txt', 'w') as file:
            json.dump(todos, file)
        print("\n✓ Tasks saved! Goodbye!")
        break
    
    else:
        print("\nInvalid choice! Try again.")