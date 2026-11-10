"""
RECORD CHECK  -  my version
===========================

Name  :Mohammed Subhaan
Lane  :   IT      (delete two)
Date  : 10/11/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = []   # replace with your code


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

for raw_record in raw_records:
    pass   # replace with your code


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring




"""
RECORD CHECK  -  my version
===========================

Name  : Subhaan 
Lane  : IT
Date  : 2026-11-10
"""

# =================================================================== FUNCTIONS
def parse_line(raw_line):
    """Parse a raw, messy infrastructure log line into a normalized dictionary."""
    line = raw_line.strip()
    if not line:
        raise ValueError("Empty line")
        
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip().lower()
    
    record = {"hostname": hostname}
    for pair in rest.split(","):
        if "=" not in pair:
            continue
        key, value = pair.split("=", 1)
        record[key.strip().lower()] = float(value.strip())
        
    return record


def status_of(record):
    """Determine server usage status based on used vs total metrics."""
    ratio = record["used"] / record["total"]
    if ratio >= 1.0:
        return "OVER LIMIT"
    elif ratio >= 0.9:
        return "WARNING"
    else:
        return "OK"


# ====================================================================== INPUT
# Excellent tier: Load raw messy records from an external file
filename = "messy_lines.txt"

# (Optional helper to ensure messy_lines.txt exists with at least 5 messy lines)
sample_data = [
    "  Srv-01 , used=45 , total=100  ",
    "SRV-02,USED=105,TOTAL=100",
    "   srv-03  ,  used=70   , total=100",
    "srv-04,used=92,total=100",
    "  SRV-05 , used=unknown , total=100  ",  # Deliberate malformed value to test error handling
    "srv-06,used=50,total=50"
]

# Write sample data to file if running standalone
with open(filename, "w") as f:
    for line in sample_data:
        f.write(line + "\n")


# =============================================================== PROCESS + OUTPUT
total_records = 0
flagged_records = 0

with open(filename, "r") as f:
    for raw_record in f:
        try:
            parsed = parse_line(raw_record)
            total_records += 1
            
            status = status_of(parsed)
            if status in ("OVER LIMIT", "WARNING"):
                flagged_records += 1
                
            print(f"Record: {parsed['hostname']} | Status: {status}")
            
        except (ValueError, IndexError):
            print(f"Could not parse: {raw_record.strip()}")

print(f"\nSummary: Processed {total_records} valid records, {flagged_records} flagged for attention.")
