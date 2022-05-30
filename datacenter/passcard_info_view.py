from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import Duration
from datacenter.models import Format
from datacenter.models import VisitLong


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()[0]
    person_passcard = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in person_passcard:
        duration = Duration(visit).get_duration(visit)
        format_time = Format(duration).format_duration(duration)
        visit_long = VisitLong(visit, 58, duration).is_visit_long(visit, 58, duration)
        person_in = {
            'entered_at': visit.entered_at,
            'duration': format_time,
            'is_strange': visit_long
        }
        this_passcard_visits.append(person_in)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
