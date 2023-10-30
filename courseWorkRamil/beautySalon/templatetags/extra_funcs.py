from django import template
from datetime import datetime, time, timedelta

from ..models import MasterRating, Master, Appointment, Comment

register = template.Library()


@register.simple_tag()
def get_current_date():
    return datetime.today().strftime('%Y-%m-%d')


@register.simple_tag()
def get_current_time():
    return datetime.now().strftime("%H:%M:%S")


@register.simple_tag()
def get_all_specs(master):
    return master.specialization.all()


@register.simple_tag()
def get_rating(master):
    all_scores = MasterRating.objects.filter(evaluated_id=master.id)
    master_rating = 0 + sum([record.value for record in all_scores])
    return master_rating


@register.simple_tag()
def get_score(master, user):
    if user.is_authenticated:
        if MasterRating.objects.filter(evaluating_id=user.id, evaluated_id=master.id).exists():
            score = MasterRating.objects.get(evaluating_id=user.id, evaluated_id=master.id)
            return score.value
    return 0


@register.simple_tag()
def get_time_for_service(service):
    duration = timedelta(hours=service.duration // 60, minutes=service.duration % 60)
    time_start = timedelta(hours=9, minutes=0, seconds=0)
    time_end = timedelta(hours=23, minutes=0, seconds=0)

    all_times = []

    while time_start + duration < time_end:
        all_times.append(time_start)
        time_start += duration

    return all_times


@register.simple_tag()
def get_masters_for_service(service, user):
    all_masters = Master.objects.all()
    need_masters = []

    for master in all_masters:
        if service.specialization in master.specialization.all():
            if master.user.id != user.id:
                need_masters.append(master)

    return need_masters


@register.simple_tag()
def get_appointments_for_user(user):
    all_appointments = Appointment.objects.filter(user_id=user.id, status=False)
    return all_appointments


@register.simple_tag()
def get_appointments_for_master(master):
    all_appointments = Appointment.objects.filter(master_id=master.id, status=False)
    return all_appointments


@register.simple_tag()
def get_comments_for_master(master):
    all_comments = Comment.objects.filter(master_id=master.id)
    return all_comments

