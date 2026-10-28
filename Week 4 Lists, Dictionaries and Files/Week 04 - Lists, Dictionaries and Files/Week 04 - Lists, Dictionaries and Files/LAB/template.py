"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI       (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def check_record(value, limit):
    """Calculate the difference, percentage and status of a record."""
    difference = value - limit
    percent = (value / limit) * 100 if limit != 0 else 0

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print the report for one record."""
    print(f"{label}: {status}")
    print(f"  Value: {value:.1f}")
    print(f"  Limit: {limit:.1f}")
    print(f"  Difference: {difference:.1f}")
    print(f"  Percentage: {percent:.1f}%")


def load_records(path):
    """Load records from a file into a list of dictionaries."""
    records = []

    try:
        with open(path, "r") as file:
            next(file, None)

            for line in file:
                if line.strip():
                    label, value, limit = line.strip().split(",")

                    records.append({
                        "label": label,
                        "value": float(value),
                        "limit": float(limit)
                    })

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return []

    return records


try:
    with open("records_sample.txt", "x") as file:
        file.write("label,value,limit\n")
        file.write("R-001,87.0,100.0\n")
        file.write("R-002,120.0,100.0\n")
        file.write("R-003,45.0,100.0\n")
except FileExistsError:
    pass


records = load_records("records_sample.txt")

over_limit_count = 0

with open("results.txt", "w") as file:
    for record in records:
        difference, percent, status = check_record(
            record["value"],
            record["limit"]
        )

        print_report(
            record["label"],
            record["value"],
            record["limit"],
            difference,
            percent,
            status
        )

        file.write(f'{record["label"]},{status}\n')

        if status == "OVER LIMIT":
            over_limit_count += 1

print(f"\nTotal records OVER LIMIT: {over_limit_count}")

with open("results.txt", "r") as file:
    print("\nContents of results.txt:")
    print(file.read(), end="")




# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
