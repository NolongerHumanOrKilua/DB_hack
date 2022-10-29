import random

commendations = [
    "Ты меня приятно удивил!",
    "Сказано здорово – просто и ясно!",
    "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится!",
    "Здорово!",
    "Талантливо!",
]
subject_name = "Музыка"
schoolkid = "Фролов Иван"


def fix_marks(schoolkid):
    child = Schoolkid.objects.get(full_name__contains=schoolkid)
    marks = Mark.objects.filter(
        schoolkid=child, points__in=[2, 3]
        ).update(points=5)


def remove_chastisements(schoolkid):
    child = Schoolkid.objects.get(full_name__contains=schoolkid)
    chastisement = Chastisement.objects.filter(schoolkid=child)
    chastisement.delete()


def create_commendation(schoolkid, subject_name):
    child = Schoolkid.objects.get(full_name__contains=schoolkid)
    subject = Subject.objects.get(
    title__contains=subject_name, year_of_study=child.year_of_study)
    lesson = Lesson.objects.filter(
        group_letter=child.group_letter, subject=subject
    ).order_by("?")[0]
    teacher = lesson.teacher
    subject = lesson.subject
    date = lesson.date
    Commendation.objects.create(
        text=random.choise(commendations),
        created=date,
        schoolkid=child,
        subject=subject,
        teacher=teacher
     )
