import time
while True:
    
    a = int(input("1. Show students \n2. Add student \n3. Update student \n4. Delete student \n5. Exit \nChoose: "))
    
    if a == 1:
        with open("miu.txt", "r") as file:
            print(file.read())

    elif a == 2:
        b = int(input("Add Student's ID: "))
        c = input("Add Student's First Name: ")
        d = input("Add Student's Last Name: ")
        e = input("Add Student's Email: ")
        f = int(input("Add Student's Phone Number: "))
        with open("miu.txt", "a") as file:
            file.write(f"\n{b}, {c}, {d}, {e}, {f}")
        print("Successfully added")

    elif a == 3:
        g = input("Put in the ID of the Student you want to update: ")
        h = int(input("Put in the updated ID: "))
        i = input("Put in the updated First Name: ")
        j = input("Put in the updated Last Name: ")
        k = input("Put in the updated Email: ")
        l = int(input("Put in the updated Phone Number: "))
        with open("miu.txt", "r") as file:
            lines = file.readlines()
        updated_lines = []
        for line in lines:
            if line.startswith(g):
                updated_lines.append(f"{h}, {i}, {j}, {k}, {l}\n")
            else:
                updated_lines.append(line)
        with open("miu.txt", "w") as file:
            file.writelines(updated_lines)
        print("Successfully updated!")

    elif a == 4:
        e = input("Put in the ID of the Student you want to delete: ")
        with open("miu.txt", "r") as file:
            lines = file.readlines()
        with open("miu.txt", "w") as file:
            for line in lines:
                if not line.startswith(e):
                    file.write(line)
        print("Successfully deleted!")
        
    elif a ==5:
        break
    time.sleep(2)
    print("\n")