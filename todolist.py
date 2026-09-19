#Create and store tasks
#Update tasks and mark them as completed
#Delete tasks
import json 

tasks = {"1": "do this", "2": "do that", "3": "do those"}

with open('tasks.json', 'r') as file:
    tasks = json.load(file)


def save():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, sort_keys=True, indent=4)


def updateTasks(task): 

    for slot in tasks:
        if tasks[slot] == None:
            tasks[slot] = task
            return
        else:
            n = str(len(tasks) + 1)

            if n in tasks.keys():
                n = int(n)
                n += 1
                n = str(n)
            tasks.update({n: task})
            return

def deleteTask(task):

    for slot in tasks: 
        
        if tasks[slot] == task:
            tasks.pop(slot)
            return

def clear():

    print("\033[H\033[J", end="")

clear()
start = input("Open list? [y] ")



while start == "y" or "Y":

    clear()


    print("................................................................")

    b = str(tasks.values())
    print(f"Tasks: {b[11:]}")

    print("................................................................")
    print("[c] create a task, [x] delete a task, [e] edit task, [q] quit")
    choice = input()

    match choice:

        case "c" | "C":
            print("................................................................")
            newTask = input("Create task: ")
            updateTasks(newTask)

            save()

            start = "y"
        case "x" | "X":
            print("................................................................")
            removeTask = input("Delete task: ")
            if removeTask in tasks.values():
                deleteTask(removeTask)

            save()

            start = "y"
        case "e" | "E":
            print("................................................................")
            updateTask = input("Update which task: ")
            if updateTask in tasks.values():
                deleteTask(updateTask)
                updateTask = input("Update to: ")
                updateTasks(updateTask)

            else:
                print("Task not found") 
                start = "y"

            save()

        case "q" | "Q":
            exit()
    
        

        
        

         
