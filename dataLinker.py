import csv

# Create dictionaries 
student_data = {}
group_data = {}

# Read UCSCDATA.csv and store student information
with open("output.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        if len(row) >= 3:
            index_num = row[1]
            print(row)
            name = row[2]
            student_data[index_num] = name

# Read groupData.csv and store group information
with open("groupData.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        group_id = row[0]
        members = row[1:]
        group_data[group_id] = members

# Create a new CSV file 
with open("groups_with_names.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Group ID", "Student 1 Name", "Student 2 Name", "Student 3 Name", "Student 4 Name"])

    for group_id, members in group_data.items():
        row = [group_id]
        for index_num in members:
            name = student_data.get(index_num, "")  # Handle missing index numbers
            row.append(name)
        writer.writerow(row)

