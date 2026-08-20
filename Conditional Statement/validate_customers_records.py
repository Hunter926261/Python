# Validate customer records
# Fields -> Age, Salary, Gender, Department, Joining Date

# Validation
# Age > 0
# Salary > 0
# Gender => [Male,Female,Other]
# Department not null or empty
# Joining Date => yyyy-MM-dd format

import csv
from datetime import datetime

def validate_row(row):

    # Validate the Data
    errors = []
    # Age
    try:
        age = int(row["Age"])
        if age <= 0:
            errors.append("Invalid Age")
    except (ValueError,TypeError):
        errors.append("Invalid Age")

    # Salary
    try:
        salary = float(row["Salary"])
        if salary <= 0:
            errors.append("Invalid Salary")
    except (ValueError,TypeError):
        errors.append("Invalid Salary")

    # Gender
    if (row["Gender"].strip()).capitalize() not in ["Male","Female","Other"]:
        errors.append("Invalid Gender")

    # Department
    if not row["Department"].strip():
        errors.append("Invalid Department")

    # Joining Date
    try:
        datetime.strptime((row["Joining Date"]).strip(),"%Y-%m-%d")
    except (ValueError,TypeError):
        errors.append("Invalid Joining Date")

    # if error in row
    if errors:
        row["Error"] = ",".join(errors)
        return False, row

    # if no error in row
    return True, row

def read_customer_data(customer_data_path):
    # Store Data as Valid & Invalid
    valid_customer_data = []
    invalid_customer_data = []

    with open(customer_data_path,"r",newline="") as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            is_valid, validated_row = validate_row(row)

            if is_valid:
                valid_customer_data.append(validated_row)
            else:
                invalid_customer_data.append(validated_row)

    # Return the Valid & Invalid customer data
    return valid_customer_data, invalid_customer_data


def load_validated_data(file_path,records,header):
    with open(file_path,"w",newline="") as file:
        csv_writer = csv.DictWriter(file,fieldnames=header)

        csv_writer.writeheader()
        csv_writer.writerows(records)


def main():
    customer_record_path = "Conditional Statement/customer_record.csv"

    valid_customer_record_path = "Conditional Statement/valid_customer_record.csv"

    invalid_customer_record_path = "Conditional Statement/invalid_customer_record.csv"

    valid_customer_data, invalid_customer_data = read_customer_data(customer_record_path)

    load_validated_data(valid_customer_record_path,valid_customer_data,["Age","Salary","Gender","Department","Joining Date"])

    load_validated_data(invalid_customer_record_path,invalid_customer_data,["Age","Salary","Gender","Department","Joining Date","Error"])


if __name__ == "__main__":
    main()