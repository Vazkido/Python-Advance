# THIS ASSIGNMENT SAY TO REMODIFY THE CLASS WORK FOR 18 DECEMBER CLASS
class DuplicateVisitorsError(Exception):
    pass 

try:
    with open("visitors.txt", "r") as f:
        content = f.readlines()
    visitors_name = input("Enter visitors name: ")      
    if not content:
        content += 1
        with open("visitors.txt", "w") as f:
            f.write(visitors_name)
            print("Name Added Successfully.")
    elif content:
        # content += 1
        last_line = len(content[-1])
        if last_line == visitors_name:
            raise DuplicateVisitorsError("Duplicate Visitors Name!")
        else:
            with open("visitors.txt", "w") as f:
                f.write(visitors_name) + 1
                print("Name Added Successfully.")
except FileNotFoundError:
    print("This File wasn't found" )
    with open("visitors.txt", "x" ) as f:
        pass

