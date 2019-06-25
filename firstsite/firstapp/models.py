from django.db import models

# Create your models here.
from mongoengine import *
import mongoengine

class tag_user(mongoengine.Document):
    _id = ObjectIdField(required=True)
    user = StringField(required=True)
    influences = IntField(required=True)
    code_infor = DictField(required=True)
    good_languages = ListField(required=True)
    informations = DictField(required=True)
    repo_lables_join = ListField(required=True)
    friends = ListField(required=True)
    lable = ListField(required=True)
    commits = IntField(required=True)
    score = FloatField(required=True)
    meta = {'collection':'tag_user'}

class user_3(mongoengine.Document):
    _id = ObjectIdField(required=True)
    name = StringField(required=True)
    login = StringField(required=True)
    type = StringField(required=True)
    company = ListField(required=True)
    location = ListField(required=True)
    organizations = IntField(required=True)
    followers = IntField(required=True)
    commits = IntField(required=True)
    public_repos = IntField(required=True)
    num_languages = IntField(required=True)
    issues = IntField(required=True)
    time = IntField(required=True)
    meta = {'collection':'user_2'}
class rank_all(mongoengine.Document):
    _id = ObjectIdField(required=True)
    login = StringField(required=True)
    score_rank = IntField(required=True)
    commit_rank = IntField(required=True)
    follow_rank = IntField(required=True)
    issue_rank = IntField(required=True)
    languages_rank = IntField(required=True)
    repos_rank = IntField(required=True)
    meta = {'collection':'rank'}

class User_image(mongoengine.Document):
    _id = ObjectIdField(required=True)
    login = StringField(required=True)
    imgage = StringField(required=True)
    meta = {'collection':'User_image'}

class blog(mongoengine.Document):
    _id = ObjectIdField(required=True)
    login = StringField(required=True)
    blog = StringField(required=True)
    meta = {'collection':'blog'}

class user_analyze3(mongoengine.Document):
    _id = ObjectIdField(required=True)
    login = StringField(required=True)
    commit = FloatField(required=True)
    issue = FloatField(required=True)
    follower = FloatField(required=True)
    repos = FloatField(required=True)
    languages = FloatField(required=True)
    score = FloatField(required=True)
    rank = IntField(required=True)
    meta = {'collection':'user_analyze3'}

class items(mongoengine.Document):
    _id = ObjectIdField(required=True)
    item_name = StringField(required=True)
    full_name = StringField(required=True)
    owner = StringField(required=True)
    description = ListField(required=True)
    language = ListField(required=True)
    size = IntField(required=True)
    watchers_count = IntField(required=True)
    forks_count = IntField(required=True)
    parent_name = StringField(required=True)
    parent_fork = ListField(required=True)
    updated_time = StringField(required=True)
    contributors = ListField(required=True)
    commit = ListField(required=True)
    content = ListField(required=True)
    meta = {'collection':'items'}
# for i in tag_user.objects[:2]:
#     print(i.good_languages)



