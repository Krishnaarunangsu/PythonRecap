import numpy as np


def curve(grades, curve_center: int):
    """
    Function to modify grades
    :type grades: object
    :param curve_center:
    :param grades:
    :return:
    """
    average = grades.mean()
    print(f' The mean is:\n{average}')
    change = CURVE_CENTER - average
    new_grades = grades + change
    print(f'Raw New Grades:{new_grades}')
    return np.clip(new_grades, grades, 100)


if __name__ == "__main__":
    CURVE_CENTER = 80
    grades = np.array([72, 35, 64, 88, 51, 90, 74, 12])
    print(f'Grades:\n{grades}')
    curve(grades, CURVE_CENTER)
