#Create and store tasks
#Update tasks and mark them as completed
#Delete tasks

tasks = ["do this", "do that", "do those"]

start = input("Open list? [y] ")

while start == "y" or "Y":

    print("................................................................")
    print(f"Tasks: {tasks}")
    print("................................................................")
    print("[c] create a task, [x] delete a task, [e] edit task, [q] quit")
    choice = input()

    match choice:

        case "c" | "C":
            print("................................................................")
            newTask = input("Create task: ")
            tasks.append(newTask)
            start = "y"
        case "x" | "X":
            print("................................................................")
            removeTask = input("Delete task: ")
            if removeTask in tasks:
                tasks.remove(removeTask)
            start = "y"
        case "e" | "E":
            print("................................................................")
            updateTask = input("Update which task: ")
            if updateTask in tasks:
                tasks.remove(updateTask)
                updateTask = input("Update to: ")
                tasks.append(updateTask)
            else:
                print("Task not found")
                start = "y"
        case "q" | "Q":
            exit()
    
        

        
        

         
