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
    название = models.TextField(db_column='Название')  # Field name made lowercase.
    место = models.IntegerField(db_column='Место')  # Field name made lowercase.
    год = models.DateField(db_column='Год')  # Field name made lowercase.
    примечание = models.TextField(db_column='Примечание')  # Field name made lowercase.

    class Meta:
        
        db_table = 'выставка'


class group(models.Model):
    id = models.IntegerField(primary_key=True)
    наименование = models.TextField(db_column='Наименование')  # Field name made lowercase.
    примечание = models.TextField(db_column='Примечание')  # Field name made lowercase.

    class Meta:
        
        db_table = 'группа'


class learning(models.Model):
    инвентарный_номер = models.TextField(db_column='Инвентарный номер')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    легенда = models.TextField(db_column='Легенда')  # Field name made lowercase.
    персоналии_field = models.TextField(db_column='Персоналии(*)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    тематические_группы_field = models.IntegerField(db_column='Тематические группы(*)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    публикации_источники_информации_о_предмете_field = models.TextField(db_column='Публикации(источники информации о предмете)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    публикации_выступления_и_др_field = models.TextField(db_column='Публикации(выступления и др)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    участие_в_выставках = models.IntegerField(db_column='участие в выставках')  # Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = 'изучение'


class inventory_book (models.Model):
    инвентарный_номер = models.TextField(db_column='Инвентарный номер')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_книги_поступления = models.IntegerField(db_column='Номер книги поступления')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    сохранность = models.TextField(db_column='Сохранность')  # Field name made lowercase.
    материал_field = models.TextField(db_column='Материал(*)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    техника_field = models.TextField(db_column='Техника(*)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    количество_листов = models.IntegerField(db_column='Количество листов')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    нуждается_ли_в_реставрации = models.IntegerField(db_column='Нуждается ли в реставрации')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    условия_хранения = models.TextField(db_column='Условия хранения')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    внешний_вид = models.IntegerField(db_column='Внешний вид')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    сканы_для_текстовых_материалов_field = models.IntegerField(db_column='Сканы(для текстовых материалов)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        
        db_table = 'инвентарная книга'


class receipt_book (models.Model):
    id_номер_field = models.IntegerField(db_column='id(Номер)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    название = models.TextField(db_column='Название')  # Field name made lowercase.
    дата_поступления = models.DateField(db_column='Дата поступления')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    сдатчик_field = models.IntegerField(db_column='Сдатчик(*)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    датировка_дата_изготовления_нач_field = models.DateField(db_column='Датировка(дата изготовления)(нач)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    датировка_дата_изготовления_кон_field = models.DateField(db_column='Датировка(дата изготовления)(кон)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    размер_длина_field = models.IntegerField(db_column='Размер(длина)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    размер_ширина_field = models.IntegerField(db_column='Размер(ширина)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    размер_высота_field = models.IntegerField(db_column='Размер(высота)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    описание = models.TextField(db_column='Описание')  # Field name made lowercase.
    изображение_аватар_field = models.IntegerField(db_column='Изображение(аватар)(*)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    закупка_безвозмездная_передача = models.IntegerField(db_column='Закупка/безвозмездная передача')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    акт_поступления_ссылка_на_документ_field = models.TextField(db_column='Акт поступления (ссылка на документ)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        
        db_table = 'книга поступлений'


class material(models.Model):
    id = models.IntegerField(primary_key=True)
    наименование = models.TextField(db_column='Наименование')  # Field name made lowercase.
    примечание = models.TextField(db_column='Примечание')  # Field name made lowercase.

    class Meta:
        
        db_table = 'материал'


class organization(models.Model):
    id = models.IntegerField(primary_key=True)
    наименование = models.IntegerField(db_column='Наименование')  # Field name made lowercase.
    id_представителя = models.IntegerField(db_column='id представителя')  # Field renamed to remove unsuitable characters.
    примечание = models.TextField(db_column='Примечание')  # Field name made lowercase.

    class Meta:
        
        db_table = 'организация'


class person(models.Model):
    id = models.IntegerField(primary_key=True)
    фамилия = models.TextField(db_column='Фамилия')  # Field name made lowercase.
    имя = models.TextField(db_column='Имя')  # Field name made lowercase.
    отчество = models.TextField(db_column='Отчество')  # Field name made lowercase.
    примечание = models.TextField(db_column='Примечание')  # Field name made lowercase.

    class Meta:
        
        db_table = 'персона'


class subject_exhibition_source(models.Model):
    id_из_книги_поступлений = models.IntegerField(db_column='id из книги поступлений')  # Field renamed to remove unsuitable characters.
    id_выставки = models.IntegerField(db_column='id Выставки')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = 'предмет - выставка(источник)'


class subject_group(models.Model):
    id_из_книги_поступлений = models.IntegerField(db_column='id из книги поступлений')  # Field renamed to remove unsuitable characters.
    id_группы = models.IntegerField(db_column='id группы')  # Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = 'предмет - группа'


class subject_material(models.Model):
    id_из_книги_поступлений = models.IntegerField(db_column='id из книги поступлений')  # Field renamed to remove unsuitable characters.
    id_материала = models.IntegerField(db_column='id материала')  # Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = 'предмет - материал'


class subject_person(models.Model):
    id_из_книги_поступлений = models.IntegerField(db_column='id из книги поступлений')  # Field renamed to remove unsuitable characters.
    id_персоны = models.IntegerField(db_column='id Персоны')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = 'предмет - персона'


class subject_publication_speeches(models.Model):
    id_из_книги_поступлений = models.IntegerField(db_column='id из книги поступлений')  # Field renamed to remove unsuitable characters.
    id_публикации = models.IntegerField(db_column='id Публикации')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    место_в_публикации = models.IntegerField(db_column='Место в публикации')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = 'предмет - публикация(выступления)'


class subject_publication_source(models.Model):
    id_из_книги_поступлений = models.IntegerField(db_column='id из книги поступлений')  # Field renamed to remove unsuitable characters.
    id_публикации = models.IntegerField(db_column='id Публикации')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    место_в_публикации = models.IntegerField(db_column='Место в публикации')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = 'предмет - публикация(источник)'


class delivery_item(models.Model):
    id_из_книги_поступлений = models.IntegerField(db_column='id из книги поступлений')  # Field renamed to remove unsuitable characters.
    id_сдатчика = models.IntegerField(db_column='id сдатчика')  # Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = 'предмет - сдатчик'


class subject_scan(models.Model):
    id_из_книги_поступлений = models.IntegerField(db_column='id из книги поступлений')  # Field renamed to remove unsuitable characters.
    id_скана = models.IntegerField(db_column='id скана')  # Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = 'предмет - скан'


class subject_technique(models.Model):
    id_из_книги_поступлений = models.IntegerField(db_column='id из книги поступлений')  # Field renamed to remove unsuitable characters.
    id_техники = models.IntegerField(db_column='id техники')  # Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = 'предмет - техника'


class publication(models.Model):
    id = models.IntegerField(primary_key=True)
    название = models.TextField(db_column='Название')  # Field name made lowercase.
    издание = models.TextField(db_column='Издание')  # Field name made lowercase.
    издательство = models.TextField(db_column='Издательство')  # Field name made lowercase.
    год = models.DateField(db_column='Год')  # Field name made lowercase.

    class Meta:
        
        db_table = 'публикация'


class publication_speech(models.Model):
    id = models.IntegerField(primary_key=True)
    название = models.TextField(db_column='Название')  # Field name made lowercase.
    мероприятие = models.TextField(db_column='Мероприятие')  # Field name made lowercase.
    секция = models.TextField(db_column='Секция')  # Field name made lowercase.
    дата = models.DateField(db_column='Дата')  # Field name made lowercase.
    примечание = models.TextField(db_column='Примечание')  # Field name made lowercase.

    class Meta:
        
        db_table = 'публикация(выступление)'


class publication_printed(models.Model):
    id = models.IntegerField(primary_key=True)
    название = models.TextField(db_column='Название')  # Field name made lowercase.
    издание = models.TextField(db_column='Издание')  # Field name made lowercase.
    издательство = models.TextField(db_column='Издательство')  # Field name made lowercase.
    год = models.DateField(db_column='Год')  # Field name made lowercase.
    примечание = models.TextField(db_column='Примечание')  # Field name made lowercase.

    class Meta:
        
        db_table = 'публикация(печатная)'


class deliverer_person(models.Model):
    id = models.IntegerField(primary_key=True)
    фамилия = models.TextField(db_column='Фамилия')  # Field name made lowercase.
    имя = models.TextField(db_column='Имя')  # Field name made lowercase.
    отчество = models.TextField(db_column='Отчество')  # Field name made lowercase.
    паспортные_данные = models.IntegerField(db_column='Паспортные данные')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    примечание = models.TextField(db_column='Примечание')  # Field name made lowercase.

    class Meta:
        
        db_table = 'сдатчик(человек)'


class scan(models.Model):
    id = models.IntegerField(primary_key=True)
    ссылка_на_скан = models.CharField(db_column='Ссылка на скан', max_length=16000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    примечание_текст = models.TextField(db_column='Примечание/текст')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = 'скан'


class technic(models.Model):
    id = models.IntegerField(primary_key=True)
    наименование = models.TextField(db_column='Наименование')  # Field name made lowercase.
    примечание = models.TextField(db_column='Примечание')  # Field name made lowercase.

    class Meta:
        
        db_table = 'техника'


class photo(models.Model):
    id = models.IntegerField(primary_key=True)
    название = models.TextField(db_column='Название')  # Field name made lowercase.
    примечание = models.TextField(db_column='Примечание')  # Field name made lowercase.

    class Meta:
        
        db_table = 'фото'


class photo_subject(models.Model):
    id_из_книги_поступлений = models.IntegerField(db_column='id из книги поступлений')  # Field renamed to remove unsuitable characters.
    id_фото = models.IntegerField(db_column='id фото')  # Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = 'фото-предмет'
