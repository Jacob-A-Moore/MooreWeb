from django.contrib import messages
from django.shortcuts import render
from .models import Bio, Education, Experience, Skill, Hobby, Interest


def about(request):
    bio = Bio.objects.first()  # since there is only one bio instance FIXME I would grab by ID.
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills = Skill.objects.all()
    hobbies = Hobby.objects.all()
    interests = Interest.objects.all()

    context = {
        'bio': bio,
        'education': education,
        'experience': experience,
        'skills': skills,
        'hobbies': hobbies,
        'interests': interests,
        'messages': messages.get_messages(request),
    }
    return render(request, 'about/index.html', context)
