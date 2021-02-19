import pytest
"""
если тест должен упасть, а он выполнился успешно, то высветится ошибка
"""
@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False