from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()[9]
    person_passcard = Visit.objects.filter(passcard=passcard)
    serialized_visits = []
    for visit in person_passcard:
        if visit.leaved_at:
            duration = Visit(visit).get_duration(visit)
            format_time = Visit(duration).format_duration(duration)
            visit_long = Visit(visit, 58, duration).is_visit_long(visit, 58, duration)
            person_in = {
                'entered_at': visit.entered_at,
                'duration': format_time,
                'is_strange': visit_long
            }
            serialized_visits.append(person_in)
        else:
            duration = Visit(visit).get_time_in_storage(visit)
            format_time = Visit(duration).format_duration(duration)
            visit_long = Visit(visit, 58, duration).is_visit_long(visit, 58, duration)
            person_in = {
                'entered_at': visit.entered_at,
                'duration': format_time,
                'is_strange': visit_long
            }
            serialized_visits.append(person_in)

    context = {
        'passcard': passcard,
        'this_passcard_visits': serialized_visits
    }
    return render(request, 'passcard_info.html', context)
