"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd


import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the CSV file
df = pd.read_csv("storage_records.csv")

# 2. Calculate percentage
df["percent"] = (df["used_gb"] / df["total_gb"]) * 100

# 3. Create status using apply and lambda
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100
    else "WARNING" if p >= 90
    else "OK"
)

# 4. Print the full DataFrame
print("FULL STORAGE REPORT")
print(df)

# 5. Print rows that are not OK
print("\nSERVERS NEEDING ATTENTION")
print(df[df["status"] != "OK"])

# 6. Group by status and count records
print("\nSTATUS COUNTS")
print(df.groupby("status").size())

# 7. Save the full DataFrame
df.to_csv("storage_report.csv", index=False)

# 8. Create a bar chart
df["status"].value_counts().plot(kind="bar")

plt.title("Server Storage Status")
plt.xlabel("Status")
plt.ylabel("Number of Servers")

# 9. Save and display chart
plt.savefig("storage_status.png")
plt.show()


print(df)


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
