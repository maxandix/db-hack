from datacenter.models import Mark, Chastisement, Schoolkid, Subject, Lesson, Commendation
from datacenter.models import Commendation
import random
from django.core.exceptions import ObjectDoesNotExist

possible_commendations = ['Молодец!',
                          'Отлично!',
                          'Хорошо!',
                          'Гораздо лучше, чем я ожидал!',
                          'Ты меня приятно удивил!',
                          'Великолепно!',
                          'Прекрасно!',
                          'Ты меня очень обрадовал!',
                          'Именно этого я давно ждал от тебя!',
                          'Сказано здорово – просто и ясно!',
                          'Ты, как всегда, точен!',
                          'Очень хороший ответ!',
                          'Талантливо!',
                          'Ты сегодня прыгнул выше головы!',
                          'Я поражен!',
                          'Уже существенно лучше!',
                          'Потрясающе!',
                          'Замечательно!',
                          'Прекрасное начало!',
                          'Так держать!',
                          'Ты на верном пути!',
                          'Здорово!',
                          'Это как раз то, что нужно!',
                          'Я тобой горжусь!',
                          'С каждым разом у тебя получается всё лучше!',
                          'Мы с тобой не зря поработали!',
                          'Я вижу, как ты стараешься!',
                          'Ты растешь над собой!',
                          'Ты многое сделал, я это вижу!',
                          'Теперь у тебя точно все получится!']


def fix_marks(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.MultipleObjectsReturned:
        print(f'Найдено больше одного ученика с именем {schoolkid_name}')
        return
    except ObjectDoesNotExist:
        print(F'Не найдено учеников с именем {schoolkid_name}')
        return

    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for mark in marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.MultipleObjectsReturned:
        print(f'Найдено больше одного ученика с именем {schoolkid_name}')
        return
    except ObjectDoesNotExist:
        print(F'Не найдено учеников с именем {schoolkid_name}')
        return

    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for chastisement in chastisements:
        print('deleting', chastisement)
        chastisement.delete()


def create_commendation(schoolkid_name, subject_title):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.MultipleObjectsReturned:
        print(f'Найдено больше одного ученика с именем {schoolkid_name}')
        return
    except ObjectDoesNotExist:
        print(F'Не найдено учеников с именем {schoolkid_name}')
        return

    try:
        subject = Subject.objects.get(title=subject_title, year_of_study=schoolkid.year_of_study)
    except Subject.MultipleObjectsReturned:
        print(f'Найдено больше одного предмета с названием {subject_title}')
        return
    except ObjectDoesNotExist:
        print(f'Не найдено предметов с названием {subject_title}')
        return

    last_lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter,
                                        subject=subject).order_by('-date', '-timeslot').first()
    commendation = Commendation.objects.create(
        text=random.choice(possible_commendations),
        schoolkid=schoolkid,
        subject=subject,
        teacher=last_lesson.teacher,
        created=last_lesson.date
    )
    print(f'commendation for {schoolkid} created.')
