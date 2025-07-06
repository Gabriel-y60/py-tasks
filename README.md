# Task menadżer commends

how to add task

-py task_menadzer.py add "kup mleko"

how to chek whats on the list

-py task_menadzer.py list

how to mark done the task

-py task_menadzer.py done 1

how to delete task

-py task_menadzer.py delete 1

how to add task with date and type of priority

-py task_menadzer.py add "Opis zadania" --due 2025-07-10 --priority high/medium/low

how to filtr a list:

-by only done - py task_menadzer.py list --done

-by olny undone - py task_menadzer.py list --undone

-by priority - py task_menadzer.py list --priority high/medium/low

and comends can be combained

-example - py task_menadzer.py list --undone --priority high

how to clear done tasks

-py task menadzer.py clear_done

how to ask for help with commends

-py tasks_manadzer.py --help
