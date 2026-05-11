import json
import os
import re
from datetime import datetime

class Task:
    """Represents a single task in the system."""
    def __init__(self, task_id, title, priority="Medium", due_date=None, completed=False):
        self.task_id = task_id
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


class TaskManager:
    """Handles the collection of tasks and file operations."""
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [Task.from_dict(t) for t in data]
        except (json.JSONDecodeError, IOError):
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)

    def add_task(self, title, priority, due_date):
        task_id = max([t.task_id for t in self.tasks], default=0) + 1
        new_task = Task(task_id, title, priority, due_date)
        self.tasks.append(new_task)
        self.save_tasks()
        return task_id

    def delete_task(self, task_id):
        original_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.task_id != task_id]
        self.save_tasks()
        return len(self.tasks) < original_count

    def toggle_task(self, task_id):
        for t in self.tasks:
            if t.task_id == task_id:
                t.completed = not t.completed
                self.save_tasks()
                return True
        return False

    def get_filtered_tasks(self, filter_type='all'):
        if filter_type == 'pending':
            return [t for t in self.tasks if not t.completed]
        if filter_type == 'completed':
            return [t for t in self.tasks if t.completed]
        return self.tasks


class CLI:
    """The User Interface layer."""
    def __init__(self):
        self.manager = TaskManager()
        self.date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_header(self):
        print("=" * 60)
        print(f"{'PYTHON TASK MASTER 3000':^60}")
        print("=" * 60)

    def validate_date(self, date_str):
        if not date_str: return "N/A"
        if self.date_pattern.match(date_str):
            return date_str
        return None

    def display_tasks(self, filter_type='all'):
        tasks = self.manager.get_filtered_tasks(filter_type)
        self.draw_header()
        print(f" Showing: {filter_type.upper()} TASKS")
        print("-" * 60)
        print(f"{'ID':<4} {'Status':<10} {'Priority':<10} {'Due Date':<12} {'Title'}")
        print("-" * 60)
        
        for t in tasks:
            status = "[DONE]" if t.completed else "[ ]"
            print(f"{t.task_id:<4} {status:<10} {t.priority:<10} {t.due_date:<12} {t.title}")
        
        if not tasks:
            print(f"\n{'No tasks found.':^60}")
        print("-" * 60)

    def menu(self):
        while True:
            self.display_tasks()
            print("\nCommands: [a] Add | [d] Delete | [c] Complete | [f] Filter | [q] Quit")
            choice = input("Select an option: ").lower().strip()

            if choice == 'a':
                title = input("Enter Task Title: ")
                priority = input("Priority (Low/Med/High): ").capitalize() or "Medium"
                due = input("Due Date (YYYY-MM-DD) or enter to skip: ")
                if due and not self.validate_date(due):
                    print("Invalid date format!")
                    input("Press Enter to continue...")
                    continue
                self.manager.add_task(title, priority, due or "N/A")

            elif choice == 'd':
                try:
                    tid = int(input("Enter Task ID to delete: "))
                    if not self.manager.delete_task(tid):
                        print("Task ID not found.")
                        input("Press Enter...")
                except ValueError:
                    print("Please enter a valid number.")

            elif choice == 'c':
                try:
                    tid = int(input("Enter Task ID to toggle status: "))
                    if not self.manager.toggle_task(tid):
                        print("Task ID not found.")
                        input("Press Enter...")
                except ValueError:
                    print("Please enter a valid number.")

            elif choice == 'f':
                f_type = input("Filter by (all/pending/completed): ").lower()
                self.display_tasks(f_type)
                input("\nShowing filtered results. Press Enter to return to main menu...")

            elif choice == 'q':
                print("Goodbye!")
                break
            
            self.clear_screen()

# --- Entry Point ---
# This block ensures the code runs only if executed directly.
# This pushes us towards a robust, production-style script structure.

if __name__ == "__main__":
    app = CLI()
    try:
        app.menu()
    except KeyboardInterrupt:
        print("\nProgram exited safely.")

# --- Future Extension Ideas ---
# 1. Add categories/tags for tasks.
# 2. Add a search function to find tasks by keyword.
# 3. Implement a sorting algorithm by due date or priority.
# 4. Integrate a notification system for overdue tasks.
# 5. Use a SQLite database instead of a JSON file for scalability.
# 6. Add a "Pomodoro Timer" feature to help focus on tasks.
# 7. Export tasks to a CSV or PDF format.
# 8. Create a GUI using Tkinter or PyQt.
# 9. Sync tasks with an online API or cloud storage.
# 10. Add color-coded priorities in the terminal using ANSI codes.
# 11. Implement user authentication for multiple users.
# 12. Track time spent on each task.
# 13. Generate weekly productivity reports.
# 14. Add sub-tasks or "Checklists" within a main task.
# 15. Create a 'trash' system to restore deleted tasks.
# 16. Implement "Natural Language Processing" to parse task dates.
# 17. Add a calendar view.
# 18. Build a web-based dashboard using Flask or Django.
# 19. Add dark mode/light mode terminal themes.
# 20. Optimize the loading process for thousands of tasks.