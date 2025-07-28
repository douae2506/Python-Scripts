def main():

    while True:
        try:
            task = input("Task: ")

        except EOFError:
            print()
            break

        else:
            with open("Todolist.txt", "a") as file:
                file.write(f"{task}\n")

    done = input("you've done? : ").strip()

    with open("Todolist.txt") as file:
        tasks = file.readlines()

    update_tasks = []
    for task in tasks:
        if task.strip() == done:
            update_tasks.append(f"✔️ {task}")
        else:
            update_tasks.append(task)

    with open("Todolist.txt", "w") as file:
        file.writelines(update_tasks)


main()
