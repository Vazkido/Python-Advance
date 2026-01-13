# THIS ASSIGNMENT SAY TO REMODIFY THE CLASS WORK FOR 18 DECEMBER CLASS
from datetime import datetime

class DuplicateVisitorsError(Exception):
    pass 

class WaitTimeError(Exception):
    pass 

visitors_name = input("Enter visitors name: ").lower().strip()

try:
    with open("visitors.txt", "r") as f:
        content = f.readlines()
    if not content:
        with open("visitors.txt", "w") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{visitors_name} - {timestamp}")
            print("Name Added Successfully.")
    else:
        last_line_original = content[-1].strip()  # Don't lowercase yet!
        last_timestamp_str = last_line_original.split(" - ")[1]
        last_line_lower = last_line_original.lower()  # Lowercase for name comparison
        
        
        #Here we check for Wait time Error.
        last_timestamp_str = last_line_original.split(" - ")[1]
        
        
        if visitors_name == last_line_lower.split(" - ")[0]:
            raise DuplicateVisitorsError("Duplicate Visitors, Name not added")
        #If we get  here, add the name.
        else:
            with open("visitors.txt", "a") as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"\n{visitors_name} - {timestamp}")
                print("Name Added Successfully.")
        
# Here we handle file not found error.
except FileNotFoundError:
    print("This File wasn't found, it has been created." )
    with open("visitors.txt", "x" ) as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{visitors_name} - {timestamp}")
    print("Name Added Successfully.")

# Here we handle duplicate visitor found error.
except DuplicateVisitorsError as e:
    print(f"Error: {e}")
    print("This visitor already signed in!")