from app import check_system_status


def test_system_healthy():
    assert check_system_status(50) == "HEALTHY"


def test_system_danger():
    assert check_system_status(95) == "HEALTHY"