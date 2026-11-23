# Simple log analysis script
# Counts failed login attempts in a log file

def count_failed_logins(log_file):
    count = 0
    with open(log_file, "r") as f:
        for line in f:
            if "failed login" in line.lower():
                count += 1
    return count

if __name__ == "__main__":
    total = count_failed_logins("sample.log")
    print(f"Failed login attempts found: {total}")