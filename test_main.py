"""
Test goes here

"""

import subprocess


def test_extract():
    """tests extract()"""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_transform_load():
    """tests transfrom_load"""
    result = subprocess.run(
        ["python", "main.py", "transform"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


def test_update_record():
    """tests update"""
    result = subprocess.run(
        ["python", "main.py", "update", "3", "country_A", "10", "10", "10", "10"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_delete_record():
    """tests delete"""
    result = subprocess.run(
        ["python", "main.py", "delete", "1"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_create_record():
    """tests create"""
    result = subprocess.run(
        ["python", "main.py", "update", "1000", "country_A", "1", "1", "1", "1.1"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_read_data():
    """tests read_data"""
    result = subprocess.run(
        ["python", "main.py", "read_data"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_create_record()
    test_read_data()
    test_update_record()
    test_delete_record()
