import pytest

from django_primer.models import Student


@pytest.mark.django_db
def test_create_student():
    # arrange
    student = Student(name='Petr', surname='Ivanov', email='sdd@sdf.com')

    # act
    student.save()

    # assert
    assert list(Student.objects.all()) == [student]


@pytest.mark.parametrize(
    'name, surname, expected',
    [
        ('Petr', 'Ivanov', 'Petr Ivanov'),
        ('', 'Ivanov', 'Ivanov'),
        ('Ivan', '', 'Ivan'),
        (None, 'Ivanov', 'Ivanov'),
        (None, None, None),
    ]
)
def test_student_fio(name, surname, expected):
    # arrange
    student = Student(name=name, surname=surname, email='sdd@sdf.com')

    # act & assert
    assert student.fio == expected
