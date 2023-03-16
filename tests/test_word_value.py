from bstb.word_value import word_value


def test_word_value_OOC():
    value = word_value("OOC")

    assert value == 6
