"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  : IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


label = input("Enter Hostname: ")
used_gb = float(input("Enter GB used: "))
total_gb = float (input("Enter Total GB used: "))

free_gb = total_gb - used_gb
percentage = used_gb/ total_gb * 100
projected_growth_monthly = used_gb * 0.15



# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign


print("=" * 50)
print(f"  RECORD CHECK  -  {label}")
print("=" * 50)

print(f"    Used    :{used_gb:>10.2f}")
print(f"    Total   :{total_gb:>10.2f}")
print(f"    Free    :{free_gb:>+10.2f}")
print(f"    Precent :{percentage:>10.2f}")
print(f"    Growth  :{projected_growth_monthly:>10.2f}%")

print("=" * 50)




