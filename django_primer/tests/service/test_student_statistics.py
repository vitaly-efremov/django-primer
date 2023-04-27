from unittest.mock import Mock

import pytest

from django_primer.models import Student, Score, Subject
from django_primer.service.student_statistics import calculate_statistics, Statistics, calculate_all_statistics, \
    StatisticsCollector


def test_student_statistics():
    # arrange
    subject = Subject(id=1, name='subject')
    subject2 = Subject(id=2, name='subject2')
    student = Student(id=1, name='name', surname='surname', email='sdd@sdf.com')
    score = Score(id=1, subject=subject, student=student, value=4)
    score2 = Score(id=2, subject=subject2, student=student, value=5)

    # act
    statistics = calculate_statistics([score, score2])

    # assert
    assert statistics == Statistics(
        subjects=['subject', 'subject2'],
        student_statistics=[{'scores': ['4.0', '5.0'], 'student': student}]
    )


@pytest.mark.django_db
def test_student_all_statistics():
    # arrange
    subject = Subject(name='subject')
    student = Student(name='name', surname='surname', email='sdd@sdf.com')
    subject.save()
    student.save()
    score = Score(subject=subject, student=student, value=4)
    score.save()

    # act
    statistics = calculate_all_statistics()

    # assert
    assert statistics == Statistics(
        subjects=['subject'],
        student_statistics=[{'scores': ['4.0'], 'student': student}]
    )


def test_student_statistics_collector():
    # arrange
    scores = [Mock(spec=Score)]
    statistics_stub = Mock(spec=Statistics)

    repository_stub = Mock(return_value=scores)
    statistics_function_stub = Mock(return_value=statistics_stub)
    collector = StatisticsCollector(db_repository=repository_stub, calculate_function=statistics_function_stub)

    # act
    statistics = collector.collect()

    # assert
    repository_stub.assert_called_once()
    statistics_function_stub.assert_called_once_with(scores)
    assert statistics == statistics_stub


