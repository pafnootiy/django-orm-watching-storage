from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    all_person_in_storage = []
    still_in_storage = Visit.objects.filter(leaved_at=None)
    for visit in still_in_storage:
        duration = visit.get_duration()
        format_time = visit.format_duration(duration)
        person_in_storage = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_time
        }

        all_person_in_storage.append(person_in_storage)
    context = {
        'all_person_in_storage': all_person_in_storage,
    }
    return render(request, 'storage_information.html', context)
