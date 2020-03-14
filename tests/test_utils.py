from immo.utils import get_metadata


def test_get_metadata(response):
    assert get_metadata(response) == """Hello"""
