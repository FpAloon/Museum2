from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class test(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class RecordPost(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'record_post'


class RecordTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'record_test'


class Wh(models.Model):
    num = models.IntegerField()
    txt = models.TextField()
    dat = models.DateField()
    url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'wh'


class exhibition (models.Model):
    id = models.IntegerField(primary_key=True)
    ???????????????? = models.TextField(db_column='????????????????')  # Field name made lowercase.
    ?????????? = models.IntegerField(db_column='??????????')  # Field name made lowercase.
    ?????? = models.DateField(db_column='??????')  # Field name made lowercase.
    ???????????????????? = models.TextField(db_column='????????????????????')  # Field name made lowercase.

    class Meta:
        
        db_table = '????????????????'


class group(models.Model):
    id = models.IntegerField(primary_key=True)
    ???????????????????????? = models.TextField(db_column='????????????????????????')  # Field name made lowercase.
    ???????????????????? = models.TextField(db_column='????????????????????')  # Field name made lowercase.

    class Meta:
        
        db_table = '????????????'


class learning(models.Model):
    ??????????????????????_?????????? = models.TextField(db_column='?????????????????????? ??????????')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ?????????????? = models.TextField(db_column='??????????????')  # Field name made lowercase.
    ????????????????????_field = models.TextField(db_column='????????????????????(*)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ????????????????????????_????????????_field = models.IntegerField(db_column='???????????????????????? ????????????(*)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ????????????????????_??????????????????_????????????????????_??_????????????????_field = models.TextField(db_column='????????????????????(?????????????????? ???????????????????? ?? ????????????????)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ????????????????????_??????????????????????_??_????_field = models.TextField(db_column='????????????????????(?????????????????????? ?? ????)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ??????????????_??_?????????????????? = models.IntegerField(db_column='?????????????? ?? ??????????????????')  # Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = '????????????????'


class inventory_book (models.Model):
    ??????????????????????_?????????? = models.TextField(db_column='?????????????????????? ??????????')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ??????????_??????????_?????????????????????? = models.IntegerField(db_column='?????????? ?????????? ??????????????????????')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ?????????????????????? = models.TextField(db_column='??????????????????????')  # Field name made lowercase.
    ????????????????_field = models.TextField(db_column='????????????????(*)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ??????????????_field = models.TextField(db_column='??????????????(*)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ????????????????????_???????????? = models.IntegerField(db_column='???????????????????? ????????????')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ??????????????????_????_??_?????????????????????? = models.IntegerField(db_column='?????????????????? ???? ?? ??????????????????????')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ??????????????_???????????????? = models.TextField(db_column='?????????????? ????????????????')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ??????????????_?????? = models.IntegerField(db_column='?????????????? ??????')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ??????????_??????_??????????????????_????????????????????_field = models.IntegerField(db_column='??????????(?????? ?????????????????? ????????????????????)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        
        db_table = '?????????????????????? ??????????'


class receipt_book (models.Model):
    id_??????????_field = models.IntegerField(db_column='id(??????????)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ???????????????? = models.TextField(db_column='????????????????')  # Field name made lowercase.
    ????????_?????????????????????? = models.DateField(db_column='???????? ??????????????????????')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ??????????????_field = models.IntegerField(db_column='??????????????(*)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ??????????????????_????????_????????????????????????_??????_field = models.DateField(db_column='??????????????????(???????? ????????????????????????)(??????)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ??????????????????_????????_????????????????????????_??????_field = models.DateField(db_column='??????????????????(???????? ????????????????????????)(??????)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ????????????_??????????_field = models.IntegerField(db_column='????????????(??????????)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ????????????_????????????_field = models.IntegerField(db_column='????????????(????????????)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ????????????_????????????_field = models.IntegerField(db_column='????????????(????????????)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ???????????????? = models.TextField(db_column='????????????????')  # Field name made lowercase.
    ??????????????????????_????????????_field = models.IntegerField(db_column='??????????????????????(????????????)(*)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ??????????????_??????????????????????????_???????????????? = models.IntegerField(db_column='??????????????/?????????????????????????? ????????????????')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ??????_??????????????????????_????????????_????_????????????????_field = models.TextField(db_column='?????? ?????????????????????? (???????????? ???? ????????????????)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        
        db_table = '?????????? ??????????????????????'


class material(models.Model):
    id = models.IntegerField(primary_key=True)
    ???????????????????????? = models.TextField(db_column='????????????????????????')  # Field name made lowercase.
    ???????????????????? = models.TextField(db_column='????????????????????')  # Field name made lowercase.

    class Meta:
        
        db_table = '????????????????'


class organization(models.Model):
    id = models.IntegerField(primary_key=True)
    ???????????????????????? = models.IntegerField(db_column='????????????????????????')  # Field name made lowercase.
    id_?????????????????????????? = models.IntegerField(db_column='id ??????????????????????????')  # Field renamed to remove unsuitable characters.
    ???????????????????? = models.TextField(db_column='????????????????????')  # Field name made lowercase.

    class Meta:
        
        db_table = '??????????????????????'


class person(models.Model):
    id = models.IntegerField(primary_key=True)
    ?????????????? = models.TextField(db_column='??????????????')  # Field name made lowercase.
    ?????? = models.TextField(db_column='??????')  # Field name made lowercase.
    ???????????????? = models.TextField(db_column='????????????????')  # Field name made lowercase.
    ???????????????????? = models.TextField(db_column='????????????????????')  # Field name made lowercase.

    class Meta:
        
        db_table = '??????????????'


class subject_exhibition_source(models.Model):
    id_????_??????????_?????????????????????? = models.IntegerField(db_column='id ???? ?????????? ??????????????????????')  # Field renamed to remove unsuitable characters.
    id_???????????????? = models.IntegerField(db_column='id ????????????????')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = '?????????????? - ????????????????(????????????????)'


class subject_group(models.Model):
    id_????_??????????_?????????????????????? = models.IntegerField(db_column='id ???? ?????????? ??????????????????????')  # Field renamed to remove unsuitable characters.
    id_???????????? = models.IntegerField(db_column='id ????????????')  # Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = '?????????????? - ????????????'


class subject_material(models.Model):
    id_????_??????????_?????????????????????? = models.IntegerField(db_column='id ???? ?????????? ??????????????????????')  # Field renamed to remove unsuitable characters.
    id_?????????????????? = models.IntegerField(db_column='id ??????????????????')  # Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = '?????????????? - ????????????????'


class subject_person(models.Model):
    id_????_??????????_?????????????????????? = models.IntegerField(db_column='id ???? ?????????? ??????????????????????')  # Field renamed to remove unsuitable characters.
    id_?????????????? = models.IntegerField(db_column='id ??????????????')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = '?????????????? - ??????????????'


class subject_publication_speeches(models.Model):
    id_????_??????????_?????????????????????? = models.IntegerField(db_column='id ???? ?????????? ??????????????????????')  # Field renamed to remove unsuitable characters.
    id_???????????????????? = models.IntegerField(db_column='id ????????????????????')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ??????????_??_???????????????????? = models.IntegerField(db_column='?????????? ?? ????????????????????')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = '?????????????? - ????????????????????(??????????????????????)'


class subject_publication_source(models.Model):
    id_????_??????????_?????????????????????? = models.IntegerField(db_column='id ???? ?????????? ??????????????????????')  # Field renamed to remove unsuitable characters.
    id_???????????????????? = models.IntegerField(db_column='id ????????????????????')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ??????????_??_???????????????????? = models.IntegerField(db_column='?????????? ?? ????????????????????')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = '?????????????? - ????????????????????(????????????????)'


class delivery_item(models.Model):
    id_????_??????????_?????????????????????? = models.IntegerField(db_column='id ???? ?????????? ??????????????????????')  # Field renamed to remove unsuitable characters.
    id_???????????????? = models.IntegerField(db_column='id ????????????????')  # Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = '?????????????? - ??????????????'


class subject_scan(models.Model):
    id_????_??????????_?????????????????????? = models.IntegerField(db_column='id ???? ?????????? ??????????????????????')  # Field renamed to remove unsuitable characters.
    id_?????????? = models.IntegerField(db_column='id ??????????')  # Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = '?????????????? - ????????'


class subject_technique(models.Model):
    id_????_??????????_?????????????????????? = models.IntegerField(db_column='id ???? ?????????? ??????????????????????')  # Field renamed to remove unsuitable characters.
    id_?????????????? = models.IntegerField(db_column='id ??????????????')  # Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = '?????????????? - ??????????????'


class publication(models.Model):
    id = models.IntegerField(primary_key=True)
    ???????????????? = models.TextField(db_column='????????????????')  # Field name made lowercase.
    ?????????????? = models.TextField(db_column='??????????????')  # Field name made lowercase.
    ???????????????????????? = models.TextField(db_column='????????????????????????')  # Field name made lowercase.
    ?????? = models.DateField(db_column='??????')  # Field name made lowercase.

    class Meta:
        
        db_table = '????????????????????'


class publication_speech(models.Model):
    id = models.IntegerField(primary_key=True)
    ???????????????? = models.TextField(db_column='????????????????')  # Field name made lowercase.
    ?????????????????????? = models.TextField(db_column='??????????????????????')  # Field name made lowercase.
    ???????????? = models.TextField(db_column='????????????')  # Field name made lowercase.
    ???????? = models.DateField(db_column='????????')  # Field name made lowercase.
    ???????????????????? = models.TextField(db_column='????????????????????')  # Field name made lowercase.

    class Meta:
        
        db_table = '????????????????????(??????????????????????)'


class publication_printed(models.Model):
    id = models.IntegerField(primary_key=True)
    ???????????????? = models.TextField(db_column='????????????????')  # Field name made lowercase.
    ?????????????? = models.TextField(db_column='??????????????')  # Field name made lowercase.
    ???????????????????????? = models.TextField(db_column='????????????????????????')  # Field name made lowercase.
    ?????? = models.DateField(db_column='??????')  # Field name made lowercase.
    ???????????????????? = models.TextField(db_column='????????????????????')  # Field name made lowercase.

    class Meta:
        
        db_table = '????????????????????(????????????????)'


class deliverer_person(models.Model):
    id = models.IntegerField(primary_key=True)
    ?????????????? = models.TextField(db_column='??????????????')  # Field name made lowercase.
    ?????? = models.TextField(db_column='??????')  # Field name made lowercase.
    ???????????????? = models.TextField(db_column='????????????????')  # Field name made lowercase.
    ????????????????????_???????????? = models.IntegerField(db_column='???????????????????? ????????????')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ???????????????????? = models.TextField(db_column='????????????????????')  # Field name made lowercase.

    class Meta:
        
        db_table = '??????????????(??????????????)'


class scan(models.Model):
    id = models.IntegerField(primary_key=True)
    ????????????_????_???????? = models.CharField(db_column='???????????? ???? ????????', max_length=16000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ????????????????????_?????????? = models.TextField(db_column='????????????????????/??????????')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = '????????'


class technic(models.Model):
    id = models.IntegerField(primary_key=True)
    ???????????????????????? = models.TextField(db_column='????????????????????????')  # Field name made lowercase.
    ???????????????????? = models.TextField(db_column='????????????????????')  # Field name made lowercase.

    class Meta:
        
        db_table = '??????????????'


class photo(models.Model):
    id = models.IntegerField(primary_key=True)
    ???????????????? = models.TextField(db_column='????????????????')  # Field name made lowercase.
    ???????????????????? = models.TextField(db_column='????????????????????')  # Field name made lowercase.

    class Meta:
        
        db_table = '????????'


class photo_subject(models.Model):
    id_????_??????????_?????????????????????? = models.IntegerField(db_column='id ???? ?????????? ??????????????????????')  # Field renamed to remove unsuitable characters.
    id_???????? = models.IntegerField(db_column='id ????????')  # Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = '????????-??????????????'
