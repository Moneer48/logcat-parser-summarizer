# Logcat Parser and Summarizer
#### Video Demo:  https://youtu.be/Yo8yz9DFqas
#### Description:
As Android developers get exposed to thousands of log lines that make debugging tedious and time-consuming.
For this, this project is a great approach that any developer can use in order to solve this problem.

The tool processes raw text logs, extracts structured log components using Python's Regular Expressions ('re' library), summarizes the errors of a log file by listing each error along with its number of occurrences there, and it outputs the summary report in a markdown (.md) file.

### Project Structure & Functions
The project consists of `project.py` (the primary application) and `test_project.py` (unit tests).

The core functionality is divided into 3 function alongside `main()`:

* **`main():`**
    Handles command-line arguments using `sys.argv`. It safely opens the specified log file, call the parsing and filtering functions, and ultimately saves the final summary report to `report.md`.

* **`parse(line):`**
    Takes a single line from a log file from `main()` and applies a Regular Expression by a pattern using `re.search()`. It extracts the level of the report (e.g `E` for Error or `W` for Warning) with the error message and returns them as a dictionary.

* **`filter_errors(items):`**
    Takes a list of dictionaries as input passed by `main()` and filters each dictionary to finally return a list of dictionaries only containing the level `E`.

* **`generate_summary(items):`**
    Takes a list of dictionaries and constructs `report.md` by returning `report` string variable.

### Usage & Testing
To run the tool on a log file:
```
python project.py sample.log
```
To run the tool's unit tests:
```
pytest test_project.py
```
