import time

while True:
    a = int(input("1. Show students \n2. Add student \n3. Update student \n4. Delete student \n5. Exit \nChoose: "))
    if a == 1:
        with open("students.txt", "r") as file:
            print(file.read())

    elif a == 2:
        b = input("Add a name: ")
        x = int(input("Add student's age: "))
        with open("students.txt", "a") as file:
            file.write(f"\n{b}, {x}")
        print("Successfully added")

    elif a == 3:
        c = input("Whose name do you want to update: ")
        d = input("Put in the updated name: ")
        e = int(input("Put in the updated age: "))
        with open("students.txt", "r") as file:
            lines = file.readlines()
        updated_lines = []
        for line in lines:
            name, age = line.strip().split(",")
            if name == c:
                updated_lines.append(f"{d}, {e}\n")
            else:
                updated_lines.append(line)
        with open("students.txt", "w") as file:
            file.writelines(updated_lines)
        print("Successfully updated!")

    elif a == 4:
        e = input("Which student do you want to delete: ")
        with open("students.txt", "r") as file:
            lines = file.readlines()
        with open("students.txt", "w") as file:
            for line in lines:
                if not line.startswith(e):
                    file.write(line)
        print("Successfully deleted!")
    elif a ==5:
        break
    time.sleep(2)
    print("\n")