from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    serialized_visits = []

    person_visits = Visit.objects.filter(passcard=passcard)


    for visit in person_visits:
        duration = visit.get_duration()
        format_time = visit.format_duration(duration)
        visit_long = visit.is_visit_long(58, duration)
        this_passcard_visits = {
            'entered_at': visit.entered_at,
            'duration': format_time,
            'is_strange': visit_long
        }
        serialized_visits.append(this_passcard_visits)

    context = {
        'passcard': passcard,
        'this_passcard_visits': serialized_visits
    }
    return render(request, 'passcard_info.html', context)
