import os, django, csv, sys, bcrypt

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "class200ok.settings")
django.setup()

from user.models    import *
from lecture.models import *


#User
CSV_PATH_PRODUCTS = 'class200ok_db/User.csv'

with open(CSV_PATH_PRODUCTS) as file:
    data_reader = csv.reader(file)
    next(file)
    for row in data_reader:
        if User.objects.filter(username=row[1], email=row[2],kakao_id=row[4]).exists():
            pass
        else:
            User.objects.create(
                username = row[1],
                email    = row[2],
                kakao_id = row[4],
            )

#Creator
CSV_PATH_PRODUCTS = 'class200ok_db/Creator.csv'

with open(CSV_PATH_PRODUCTS) as file:
    data_reader = csv.reader(file)
    next(file)
    for row in data_reader:
        if Creator.objects.filter(nickname=row[1], phonenumber=row[2], introduction=row[3], profile_image_url=row[4], user_id=row[6]).exists():
            pass
        else: 
            Creator.objects.create(
                nickname          = row[1],
                phonenumber       = row[2],
                introduction      = row[3],
                profile_image_url = row[4],
                user_id           = row[6],
            )

#Category
CSV_PATH_PRODUCTS = 'class200ok_db/Category.csv'

with open(CSV_PATH_PRODUCTS) as file:
    data_reader = csv.reader(file)
    next(file)
    for row in data_reader:
        if Category.objects.filter(name=row[1]).exists():
            pass
        else:
            Category.objects.create(
                name = row[1],
            )

#SubCategory
CSV_PATH_PRODUCTS = 'class200ok_db/SubCategory.csv'

with open(CSV_PATH_PRODUCTS) as file:
    data_reader = csv.reader(file)
    next(file)
    for row in data_reader:
        if SubCategory.objects.filter(name=row[1], category_id=row[2]).exists():
            pass
        else:
            SubCategory.objects.create(
                name        = row[1],
                category_id = row[2],
            )

#Difficulty
CSV_PATH_PRODUCTS = 'class200ok_db/Difficulty.csv'

with open(CSV_PATH_PRODUCTS) as file:
    data_reader = csv.reader(file)
    next(file)
    for row in data_reader:
        if Difficulty.objects.filter(level=row[1]).exists():
            pass
        else:            
            Difficulty.objects.create(
                level = row[1],
            )

#Hashtag
CSV_PATH_PRODUCTS = 'class200ok_db/Hashtag.csv'

with open(CSV_PATH_PRODUCTS) as file:
    data_reader = csv.reader(file)
    next(file)
    for row in data_reader:
        if Hashtag.objects.filter(tag=row[1]).exists():
            pass
        else:
            Hashtag.objects.create(
                tag = row[1],
            )

# Lecture
# CSV_PATH_PRODUCTS = 'class200ok_db/Lecture.csv'

# with open(CSV_PATH_PRODUCTS) as file:
#     data_reader = csv.reader(file)
#     next(file)
#     for row in data_reader:
#         if Lecture.objects.filter(title=row[1]).exists():
#             pass
#         else:            
#             Lecture.objects.create(
#                 title = row[1],
#             )

#PendingLecture
CSV_PATH_PRODUCTS = 'class200ok_db/PendingLecture.csv'

with open(CSV_PATH_PRODUCTS) as file:
    data_reader = csv.reader(file)
    next(file)
    for row in data_reader:
        if PendingLecture.objects.filter(title=row[1], cover_image_url=row[2], summary_image_url=row[3], detailed_category=row[4], user_id=row[7], category_id=row[8], sub_category_id=row[9], difficulty_id=row[10]).exists():
            pass
        else:
            PendingLecture.objects.create(
                title             = row[1],
                cover_image_url   = row[2],
                summary_image_url = row[3],
                detailed_category = row[4],
                user_id           = row[7],
                category_id       = row[8],
                sub_category_id   = row[9],
                difficulty_id     = row[10],
            )

#PendingLectureHashtag
CSV_PATH_PRODUCTS = 'class200ok_db/PendingLectureHashtag.csv'

with open(CSV_PATH_PRODUCTS) as file:
    data_reader = csv.reader(file)
    next(file)
    for row in data_reader:
        if PendingLectureHashtag.objects.filter(pending_lecture_id=row[1], hashtag_id=row[2]).exists():
            pass
        else:
            PendingLectureHashtag.objects.create(
                pending_lecture_id = row[1],
                hashtag_id         = row[2],
            )

#Introduction
CSV_PATH_PRODUCTS = 'class200ok_db/Introduction.csv'

with open(CSV_PATH_PRODUCTS) as file:
    data_reader = csv.reader(file)
    next(file)
    for row in data_reader:
        if Introduction.objects.filter(detail=row[1], image_url=row[2], pending_lecture_id=row[3]).exists():
            pass
        else:
            Introduction.objects.create(
                detail             = row[1],
                image_url          = row[2],
                pending_lecture_id = row[3],
            )

#Vote
CSV_PATH_PRODUCTS = 'class200ok_db/Vote.csv'

with open(CSV_PATH_PRODUCTS) as file:
    data_reader = csv.reader(file)
    next(file)
    for row in data_reader:
        if Vote.objects.filter(user_id=row[1], pending_lecture_id=row[2]).exists():
            pass
        else:
            Vote.objects.create(
                user_id            = row[1],
                pending_lecture_id = row[2],
            )