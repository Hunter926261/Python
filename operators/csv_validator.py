# A company has received employee data in a CSV file. Before loading the data into the database, the data must be validated.
# Write a Python program to validate each record in the CSV file.

# Validation Rules
# •	Age >0 
# •	Salary >0 
# •	Experience>=0 

import csv

def validate_csv(row):
    # If data in csv is words (eg. Twenty)
    try:
        age = int(row["Age"])
        salary = float(row["Salary"])
        experience = int(row["Experience"])
    except ValueError:
        row["Error"] = "Invalid Data Type"
        return False,row

    # if not valid numbers
    errors = []

    if age <= 0:
        errors.append("Invalid Age")
    if salary <= 0:
        errors.append("Invalid Salary")
    if experience < 0:
        errors.append("Invalid Experience")

    # if errors exist
    if errors:
        row["Error"]=", ".join(errors)
        return False, row
    
    # if no errors
    return True, row

def read_csv(file_name):

    # Store data as Valid & Invalid
    Valid_records = []
    Invalid_records = []

    with open(file_name,"r",newline='') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            
            # check the isValid & Validated row
            isValid,validated_row = validate_csv(row)

            if isValid:
                Valid_records.append(validated_row)
            else:
                Invalid_records.append(validated_row)

    return Valid_records,Invalid_records


def write_csv(file_name,records,headers):

    with open(file_name,"w",newline="") as file:
        csv_writer = csv.DictWriter(file,fieldnames=headers)

        csv_writer.writeheader()

        csv_writer.writerows(records)

# main function which combines the row validation,reading rows & writing valid & Invalid csv

def main():

    valid_record, Invalid_record = read_csv("operators/employees.csv")

    write_csv("operators/valid_records.csv",valid_record,["Age","Salary","Experience"])

    write_csv("operators/Invalid_records.csv",Invalid_record,["Age","Salary","Experience","Error"])

    total_records = len(valid_record) + len(Invalid_record)

    print(f"Total Records: {total_records}")
    print(f"Valid Records: {len(valid_record)}")
    print(f"Invalid Record: {len(Invalid_record)}")


if __name__ == "__main__":
    main()    