# -*- coding: utf-8 -*-
from collections import defaultdict

from django.views.generic.base import TemplateView

from .models import Score
from .service.student_statistics import calculate_all_statistics


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        statistics = calculate_all_statistics()
        context.update({
            'subjects': statistics.subjects,
            'student_statistics': statistics.student_statistics
        })
        return context
