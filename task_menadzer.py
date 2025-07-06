import argparse
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

# ======= Helpers =======
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# ======= Core Functions =======
def add_task(description, due=None, priority="medium"):
    tasks = load_tasks()
    task = {
        "description": description,
        "done": False,
        "due": due,
        "priority": priority.lower()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Dodano zadanie: {description}")

def list_tasks(filter_done=None, filter_priority=None):
    tasks = load_tasks()
    if not tasks:
        print("Brak zadań.")
        return

    print("\nTwoje zadania:")
    print("Nr | Opis | Status | Termin | Priorytet")
    print("---|------|--------|--------|-----------")

    for idx, task in enumerate(tasks, 1):
        if filter_done is not None and task["done"] != filter_done:
            continue
        if filter_priority and task["priority"] != filter_priority:
            continue

        status = "✔️" if task["done"] else "❌"
        due = task.get("due") or "-"
        priority = task.get("priority", "medium")

        if due != "-":
            try:
                due_date = datetime.strptime(due, "%Y-%m-%d").date()
                today = datetime.today().date()
                if due_date < today:
                    due += " (po terminie)"
                elif due_date == today:
                    due += " (dzisiaj)"
                else:
                    due += " (w terminie)"
            except ValueError:
                pass

        print(f"{idx} | {task['description']} | {status} | {due} | {priority}")

def mark_done(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        print(f"Zadanie {task_number} oznaczone jako wykonane.")
    else:
        print("Nieprawidłowy numer zadania.")

def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Usunięto: {removed_task['description']}")
    else:
        print("Nieprawidłowy numer zadania.")

def clear_done():
    tasks = load_tasks()
    tasks = [t for t in tasks if not t["done"]]
    save_tasks(tasks)
    print("Wszystkie wykonane zadania zostały usunięte.")

# ======= CLI Parser =======
def main():
    parser = argparse.ArgumentParser(description="Menadżer zadań CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Dodaj nowe zadanie")
    add_parser.add_argument("description", help="Opis zadania")
    add_parser.add_argument("--due", help="Termin (YYYY-MM-DD)", default=None)
    add_parser.add_argument("--priority", choices=["low", "medium", "high"], default="medium", help="Priorytet")

    list_parser = subparsers.add_parser("list", help="Wyświetl listę zadań")
    list_parser.add_argument("--done", action="store_true", help="Pokaż tylko wykonane")
    list_parser.add_argument("--undone", action="store_true", help="Pokaż tylko niewykonane")
    list_parser.add_argument("--priority", choices=["low", "medium", "high"], help="Filtruj po priorytecie")

    done_parser = subparsers.add_parser("done", help="Oznacz zadanie jako wykonane")
    done_parser.add_argument("number", type=int, help="Numer zadania")

    delete_parser = subparsers.add_parser("delete", help="Usuń zadanie")
    delete_parser.add_argument("number", type=int, help="Numer zadania")

    subparsers.add_parser("clear_done", help="Usuń wszystkie wykonane zadania")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description, args.due, args.priority)
    elif args.command == "list":
        done_filter = True if args.done else False if args.undone else None
        list_tasks(filter_done=done_filter, filter_priority=args.priority)
    elif args.command == "done":
        mark_done(args.number)
    elif args.command == "delete":
        delete_task(args.number)
    elif args.command == "clear_done":
        clear_done()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
