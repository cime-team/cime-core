import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils import timezone


class CimeUserManager(BaseUserManager):
    """
    Administrador de usuarios de la aplicación, tiene los métodos para crear
    usuarios y administradores.
    """
    def create_user(self, email, name, password=None, **extra_fields):
        """
        Crea y almacena un nuevo usuario con el correo y el password indicado.
        """
        if not email:
            raise ValueError('El usuario debe tener un correo')
        email = self.normalize_email(email)
        user = self.model(email = email, name = name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password, **extra_fields):
        """
        Crea un usuario que tiene todos los privilegios de acceso por defecto,
        necesario para poder crear usuarios por linea de comandos.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe ser administrador')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Estás tratando de crear un superusuario no súper?')
        return self.create_user(email, name, password, **extra_fields)


class CimeUser(AbstractBaseUser, PermissionsMixin):
    """
    Representa a un usuario dentro de la aplicación, emula el comportamiento de
    django.contrib.auth.models.User, pero los usuarios están indexados por email
    y por un id único no secuencial.

    Atención: Para evitar acoplamiento, este módulo no se debería ocupar
    directamente cuando sea posible, es preferible rescatar el usuario desde la
    configuración:

        from django.conf import settings
        class MiClase(models.Model):
            usuario = models.ForeignKey(settings.AUTH_USER_MODEL, ...)

    """
    # Identificación
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True,
        help_text = 'el correo del usuario debe corresponder a un dominio'
        '@cime.cl, @alumnos.usm.cl, o a @sansano.usm.cl')
    name = models.CharField('nombre', max_length=255,
        help_text='nombre natural del usuario.')

    # Fechas
    date_joined = models.DateTimeField('creado', default = timezone.now)

    # Datos Académicos
    # TODO: Vincular a las claves foraneas de la organización.
    # Podría estar en un modelo 1 a 1 en organización, para que no se acoplen.
    # campus = models.ForeignKey('Campus', null=True, blank=True)
    # career = models.ForeignKey('Career', null=True, blank=True)
    # plan = models.ForeignKey('Plan', null=True, blank=True)

    is_staff = models.BooleanField('es staff', default = False,
        help_text="define si el usuario es administrador")

    is_active = models.BooleanField('activo', default = True,
        help_text="define si el usuario es una cuenta activa o está eliminado")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',]

    objects = CimeUserManager()

    class Meta:
        verbose_name = 'usuario'

    def __str__(self):
        return '{0} <{1}>'.format(self.name, self.email)

    def get_short_name(self):
        return self.name


@receiver(post_save, sender=CimeUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
