# pylint: disable=relative-beyond-top-level
from ..utils import get_metadata


def test_get_metadata(response):
    assert get_metadata(response) == """Hello"""
