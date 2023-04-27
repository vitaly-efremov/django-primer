from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass

from django_primer.models import Score


@dataclass
class Statistics:
    subjects: list[str]
    student_statistics: list[dict]


class StatisticsCollector:
    def __init__(self, db_repository, calculate_function):
        self._db_repository = db_repository or Score.objects.all
        self._calculate_function = calculate_function or calculate_statistics

    def collect(self):
        scores = self._db_repository()
        return self._calculate_function(scores)


def calculate_all_statistics() -> Statistics:
    scores = Score.objects.all()
    return calculate_statistics(scores)


def calculate_statistics(scores: Iterable[Score]) -> Statistics:
    student_scores = defaultdict(dict)
    subjects = set()
    for score in scores:
        subject_name = score.subject.name
        subjects.add(subject_name)
        student_scores[score.student][subject_name] = score.value

    subjects = sorted(subjects)
    student_statistics = [
        {
            'student': student,
            'scores': [f'{scores[subject]:.1f}' for subject in subjects]
        }
        for student, scores in student_scores.items()
    ]
    return Statistics(subjects=subjects, student_statistics=student_statistics)
