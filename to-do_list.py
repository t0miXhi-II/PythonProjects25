def main():
    task_list = []

    while True:
        task = input("Enter task (or type 'done' to stop): ")

        if task.lower() == "done":
            break
        else:
            task_list.append(task)

    view_tasks(task_list)
    save_quesion(task_list)


def view_tasks(task_list):
    for i, task in enumerate(task_list):
        print(f"{i + 1}) {task}")


def save_quesion(task_list):
    ans = input("Do you wnat to save to file? y/n:  ")
    match ans.lower():
        case "y" | "yes":
            save_to_file(task_list)
            print("Task List successfully saved to file - task_list.txt")
        case "n" | "no":
            print("Task List is NOT saved to file")
        case _:
            print("Invalid Input!") 


def save_to_file(task_list):
    with open("task_list.txt", "a") as file:
        for i, task in enumerate(task_list):
            file.write(f"\n{i + 1}) {task}")

if __name__ == "__main__":
    main()