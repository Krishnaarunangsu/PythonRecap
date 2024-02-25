def what_tech_they_use(**kwargs):
    """

    Args:
        **kwargs:

    Returns:

    """
    result = []
    for key, value in kwargs.items():
        # result.append("{} uses {}".format(key, value))
        result.append(f'{key} uses {value}')
    return result

print(what_tech_they_use(Google='Angular', Facebook='react', Microsoft='.NET'))


print(what_tech_they_use(Krishna='Mahabharat', Ram='Ramayana'))