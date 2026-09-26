from project import parse, filter_errors, generate_summary


def test_parse():
    valid_line = "05-26 11:32:01.412 10123 10123 E AndroidRuntime: java.lang.NullPointerException"
    invalid_line = "This was Moneer's CS50 Final Project"
    assert parse(valid_line) == {"level": "E", "message": "java.lang.NullPointerException"}
    assert parse(invalid_line) == None


def test_filter_errors():
    errors = [
        {"level": "I", "message": "Initializing"},
        {"level": "W", "message": "Warning"},
        {"level": "E", "message": "Error"}
    ]

    assert filter_errors(errors) == [{"level": 'E', "message": 'Error'}]


def test_generate_summary():
    assert "No errors occurred!" in generate_summary([])

    errors = [
        {"level": "E", "message": "Error1"},
        {"level": "E", "message": "Error2"}
    ]

    summary = generate_summary(errors)

    assert "Total Errors Found: 2" in summary
    assert "|1|Error1|" in summary
    assert "|1|Error2|" in summary
