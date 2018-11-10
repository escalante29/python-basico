def detector_anagrama(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    result = False
    # at this point we know the strings are of same length
    for char in str_1:
        if char in str_2:
            result = True
        else:
            result = False
            break

    print(f'Es anagrama ({str_1, str_2})? {result}')

    return result


detector_anagrama('orb', 'bro')
detector_anagrama('car', 'arc')
detector_anagrama('necrofila', 'florencia')
detector_anagrama('alvaro', 'valora')

