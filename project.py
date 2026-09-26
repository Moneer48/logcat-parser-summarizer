import sys
import re


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python project.py [your_log_file]")

    log_file = sys.argv[1]

    try:
        with open(log_file) as file:
            lines = file.readlines()

    except FileNotFoundError:
        sys.exit("File not found!")

    parsed_items = [parse(line) for line in lines]
    valid_items = [item for item in parsed_items if item != None]

    # Get the error items to report
    errors = filter_errors(valid_items)

    report = generate_summary(errors)

    with open("report.md", "w") as output:
        output.write(report)


def parse(line):
    # Pattern for Android Logcat logs
    pattern = r"^.+([IWEVD])\s+\w+:\s*(.+)$"

    result = re.search(pattern, line.strip())

    if result:
        return {"level": result.group(1), "message": result.group(2)}
    else:
        return None


def filter_errors(items):
    return [item for item in items if item["level"] == 'E']


def generate_summary(items):
    total_errors = len(items)

    if total_errors == 0:
        return '# Logcat Crash Summary Report\nNo errors occurred!'

    error_counts = {}
    for item in items:
        msg = item["message"]
        error_counts[msg] = error_counts.get(msg, 0) + 1

    report = f'# Logcat Crash Summary Report\nTotal Errors Found: {total_errors}\n'
    report += '\n# Summary:\n'
    report += '| Occurences | Error Message |\n'
    report += '|---|---|\n'

    for msg, count in error_counts.items():
        report += f'|{count}|{msg}|\n'

    return report


if __name__ == "__main__":
    main()
