import detector_anagrama


def test_anagrama_real():
    str1 = 'colinas'
    str2 = 'nicolas'
    assert True == detector_anagrama.detector_anagrama(str1, str2)


def test_anagrama_falso_mismo_tamano():
    str1 = 'job'
    str2 = 'boy'
    assert False == detector_anagrama.detector_anagrama(str1, str2)


def test_anagrama_falso_diferente_tamano():
    str1 = 'boy'
    str2 = 'tree'
    assert False == detector_anagrama.detector_anagrama(str1, str2)
