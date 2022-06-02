from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []
    all_visits_in_storage = Visit.objects.filter(leaved_at=None)
    for visit in all_visits_in_storage:
        duration = Visit(visit).get_time_in_storage(visit)
        format_time = Visit(duration).format_duration(duration)
        person_in_storage = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_time
        }

        non_closed_visits.append(person_in_storage)
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
