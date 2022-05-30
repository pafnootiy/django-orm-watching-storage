from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import Duration
from datacenter.models import Format
from datacenter.models import VisitLong

from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []
    all_visits = Visit.objects.all()
    for visit in all_visits:
        if visit.leaved_at:
            duration = Duration(visit).get_time_in_storage(visit)
            format_time = Format(duration).format_duration(duration)
            continue
        else:
            person_in_storage = {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': format_time

            }
            non_closed_visits.append(person_in_storage)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
