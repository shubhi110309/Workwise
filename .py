print("===== WORKWISE AI =====")

tasks = []

n = int(input("Enter number of tasks: "))

for i in range(n):

    print("\nTask", i + 1)

    name = input("Enter task name: ")
    days = int(input("Days left: "))
    hours = int(input("Hours needed: "))
    importance = int(input("Importance (1-Low, 2-Medium, 3-High): "))

    score = 0

    # Check deadline
    if days <= 1:
        score += 3
    elif days <= 3:
        score += 2
    else:
        score += 1

    # Check importance
    score += importance

    # Check work required
    if hours >= 4:
        score += 2

    # Decide priority
    if score >= 7:
        priority = "HIGH"
    elif score >= 5:
        priority = "MEDIUM"
    else:
        priority = "LOW"

    tasks.append([name, priority, hours, score])


print("\n===== AI RECOMMENDATION =====")

# Show tasks
for task in tasks:
    print("\nTask:", task[0])
    print("Priority:", task[1])
    print("Hours:", task[2])

    if task[1] == "HIGH":
        print("Do this task first.")
    elif task[1] == "MEDIUM":
        print("Do this task after high priority tasks.")
    else:
        print("You can do this task later.")


# Workload
total_hours = 0

for task in tasks:
    total_hours += task[2]

print("\n===== WORKLOAD =====")
print("Total work:", total_hours, "hours")

if total_hours > 8:
    print("Warning: Your workload is high.")
else:
    print("Your workload is manageable.")
