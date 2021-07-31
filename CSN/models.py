# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import json
from json import JSONEncoder

class Addfriends(models.Model):
    addid = models.BigAutoField(primary_key=True)
    meid = models.BigIntegerField()
    friendid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'addfriends'


class Advertisement(models.Model):
    advertiseid = models.BigAutoField(primary_key=True)
    advertisename = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'advertisement'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class College(models.Model):
    collegeid = models.BigAutoField(primary_key=True)
    collegename = models.CharField(max_length=50)
    collegelocation = models.CharField(max_length=50)
    image = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'college'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Img(models.Model):
    imgid = models.BigAutoField(primary_key=True)
    imagname = models.CharField(max_length=20)
    imgcategory = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    uploadimage = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'img'


class Pracdemo(models.Model):
    videoid = models.BigAutoField(primary_key=True)
    videoname = models.CharField(max_length=25)
    videocategory = models.TextField()
    uploadvideo = models.TextField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'pracdemo'





class Qanswer(models.Model):
    qid = models.BigAutoField(primary_key=True)
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=70)
    option1 = models.CharField(max_length=70)
    option2 = models.CharField(max_length=70)
    option3 = models.CharField(max_length=70)
    option4 = models.CharField(max_length=70)
    visible = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'qanswer'


class Qpaper(models.Model):
    paperid = models.BigAutoField(primary_key=True)
    papername = models.CharField(max_length=25)
    subject = models.CharField(max_length=20)
    section = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    upload = models.CharField(max_length=50)
    uploadtext = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'qpaper'


class Result(models.Model):
    resid = models.BigAutoField(primary_key=True)
    collegename = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    result = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'result'


class Scrap(models.Model):
    scrapid = models.BigAutoField(primary_key=True)
    senderid = models.BigIntegerField()
    recieverid = models.BigIntegerField()
    smessage = models.CharField(max_length=500)
    time = models.CharField(max_length=50)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'scrap'


class Stuacc(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    confirmpassword = models.CharField(max_length=30)
    iam = models.CharField(max_length=10)
    dob = models.DateField()
    class Meta:
        managed = False
        db_table = 'stuacc'
# subclass JSONEncoder
    class StuaccEncoder(JSONEncoder):
            def default(self, o):
                return o.__dict__
        
class Profile(models.Model):
    profileid = models.BigAutoField(primary_key=True)
    userid = models.IntegerField()
    relstat = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    pincode = models.IntegerField()
    country = models.CharField(max_length=30)
    image = models.CharField(max_length=50)
    hschool = models.CharField(max_length=50)
    coluni = models.CharField(max_length=70)
    course = models.CharField(max_length=50)
    Stuacc = models.ForeignKey(Stuacc, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'profile'
           
    class ProfileEncoder(JSONEncoder):
            def default(self, o):
                return o.__dict__
            
class LoginModel(models.Model):
    email=models.CharField(max_length=30)
    password = models.CharField(max_length=30)