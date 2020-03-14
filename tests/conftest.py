import pytest


@pytest.fixture(name="response")
def response_fixture():
    return {
        "metadata": {
            "search": {
                "nbresults": 9414,
                "budget": {"min": "300000", "max": None},
                "surface": {"min": "35", "max": None},
                "commodites": [
                    {"name": "terrasse", "value": False},
                    {"name": "balcon", "value": True},
                ],
                "situation": [
                    {"name": "belleVue", "value": True},
                    {"name": "sansVisAVis", "value": False},
                ],
            },
            "summary": ["Achat", "Paris", "Appartement"],
        }
    }

