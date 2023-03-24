import os

from bstb.logo import moluk


def test_01(tmp_path):
    assert os.path.isdir(tmp_path)

    moluk(tmp_path)

    filename = os.path.join(tmp_path, "moluk.svg")

    assert os.path.isfile(filename)
