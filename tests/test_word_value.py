from bstb.word_value import word_value


def test_word_value_OOC():
    value = word_value("OOC")

    assert value == 6


def test_GC6BAPN():
    assert 6 == word_value("OOC")
    assert 4 == word_value("D")
    assert 2 == word_value("VDL")
    assert 7 == word_value("NYD")
    assert 9 == word_value("GONYB")
    assert 2 == word_value("WO")
    assert 8 == word_value("SIAMYCGOO")
    assert 4 == word_value("EBTTRT")
    assert 1 == word_value("1")
    assert 5 == word_value("WOWY")
    assert 9 == word_value("MLK")
    assert 5 == word_value("P(ITNOL)")
    assert 8 == word_value("TF")
