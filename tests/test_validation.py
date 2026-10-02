from student_app.utils.validation import validate_marks, validate_name


def test_valid_name():
    assert validate_name("Ali") is True


def test_empty_name():
    assert validate_name("") is False


def test_blank_name():
    assert validate_name("   ") is False


def test_valid_marks():
    assert validate_marks(85) is True


def test_boundary_marks():
    assert validate_marks(0) is True
    assert validate_marks(100) is True


def test_marks_below_zero():
    assert validate_marks(-1) is False


def test_marks_above_hundred():
    assert validate_marks(101) is False
