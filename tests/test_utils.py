from immo.utils import get_metadata


def test_get_metadata(response):
    expected = "\nFetched 9414 results in Achat > Paris > Appartement."
    expected += "\n\t- commodites: balcon"
    expected += "\n\t- situation: belleVue, sansVisAVis"
    expected += "\n\t- budget: [300000, 700000]"
    expected += "\n\t- surface: [35, ]\n"

    assert get_metadata(response) == expected
