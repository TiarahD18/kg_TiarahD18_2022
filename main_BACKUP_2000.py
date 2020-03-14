<<<<<<< HEAD
def isIsomorphic(str1, str2):
    iso_str1 = {}
    iso_str2 = {}

    for i, value in enumerate(str1):
        iso_str1[value] = iso_str1.get(value, []) + [i]

    for k, value in enumerate(str2):
        iso_str2[value] = iso_str2.get(value, []) + [k]

    if sorted(iso_str1.values()) == sorted(iso_str2.values()):
        return True

    else:
=======
def isIsomorphic(str1, str2):
    iso_str1 = {}
    iso_str2 = {}

    for i, value in enumerate(str1):
        iso_str1[value] = iso_str1.get(value, []) + [i]

    for k, value in enumerate(str2):
        iso_str2[value] = iso_str2.get(value, []) + [k]

    if sorted(iso_str1.values()) == sorted(iso_str2.values()):
        return True

    else:
>>>>>>> origin
        return False