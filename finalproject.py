habits = []
quotes = [
    "Great job! Keep up the amazing work!",
    "You're one step closer to your goals!",
    "Small progress is still progress!",
    "Keep going; you're doing fantastic!",
    "Every habit checked off is a win!"
]

def add_habit():
    habit = input("Enter a new habit: ")
    habits.append([habit, False])
    print("Habit added!")

def mark_completed():
    print("Your habits:")
    for i in range(len(habits)):
        print(i + 1, habits[i][0], "- Completed" if habits[i][1] else "- Not Completed")
    choice = int(input("Enter the number of the habit you completed: ")) - 1
    if choice >= 0 and choice < len(habits) and not habits[choice][1]:
        habits[choice][1] = True
        print(quotes[choice % len(quotes)])
    else:
        print("Invalid choice or already completed.")

def show_habits():
    print("Your habits:")
    for i in range(len(habits)):
        print(habits[i][0], "- Completed" if habits[i][1] else "- Not Completed")

while True:
    print("Menu:")
    print("1. Add a habit")
    print("2. Mark a habit as completed")
    print("3. Show all habits")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_habit()
    elif choice == "2":
        mark_completed()
    elif choice == "3":
        show_habits()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
