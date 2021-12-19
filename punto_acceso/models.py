# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EmpresaCliente(models.Model):
    id_c = models.AutoField(primary_key=True)
    nit_c = models.IntegerField(blank=True, null=True)
    nombre_empresa_c = models.TextField(blank=True, null=True)
    nombre_comercial_c = models.TextField(blank=True, null=True)
    telefono_c = models.TextField(blank=True, null=True)
    direccion_c = models.TextField(blank=True, null=True)
    user_admin_c = models.TextField(blank=True, null=True)
    email_c = models.TextField(blank=True, null=True)
    web_c = models.TextField(blank=True, null=True)
    pais_c = models.TextField(blank=True, null=True)
    estado_c = models.TextField(blank=True, null=True)
    ciudad_c = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESA_CLIENTE'


class EmpresaPropietario(models.Model):
    id_p = models.AutoField(primary_key=True)
    nit_p = models.IntegerField(blank=True, null=True)
    nombre_empresa_p = models.TextField(blank=True, null=True)
    nombre_comercial_p = models.TextField(blank=True, null=True)
    telefono_p = models.TextField(blank=True, null=True)
    direccion_p = models.TextField(blank=True, null=True)
    user_admin_p = models.TextField(blank=True, null=True)
    email_p = models.TextField(blank=True, null=True)
    web_p = models.TextField(blank=True, null=True)
    pais_p = models.TextField(blank=True, null=True)
    estado_p = models.TextField(blank=True, null=True)
    ciudad_p = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESA_PROPIETARIO'


class PuntoAcceso(models.Model):
    id_access = models.AutoField(primary_key=True)
    nombre_empresa = models.TextField(blank=True, null=True)
    geolocalizacion = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PUNTO_ACCESO'


class UsuarioPropietario(models.Model):
    id_propietario = models.AutoField(primary_key=True)
    cedula_propietario = models.IntegerField(blank=True, null=True)
    nombre_propietario = models.TextField(blank=True, null=True)
    email_propietario = models.TextField(blank=True, null=True)
    usuario_propietario = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    telefono_propietario = models.TextField(blank=True, null=True)
    last_login = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'USUARIO_PROPIETARIO'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
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
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

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
