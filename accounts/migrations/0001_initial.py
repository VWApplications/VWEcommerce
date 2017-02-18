# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 00:55
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='O nome de usuário é um campo obrigatório de até 30 caracteres ou menos, entre eles letras e números', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@-_]+$', 32), 'O nome de usuário só pode conter letras, números e simbolos como @.-_', 'invalid')], verbose_name='Nome de Usuário')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='Nome')),
                ('date_of_birth', models.DateField(blank=True, verbose_name='Data de nascimento')),
                ('DDD', models.IntegerField(blank=True, verbose_name='DDD')),
                ('number', models.IntegerField(blank=True, verbose_name='Número')),
                ('phone', models.CharField(blank=True, max_length=30, verbose_name='Telefone')),
                ('country', models.CharField(blank=True, max_length=30, verbose_name='País')),
                ('city', models.CharField(blank=True, max_length=30, verbose_name='Cidade')),
                ('state', models.CharField(blank=True, max_length=30, verbose_name='Estado')),
                ('complement', models.CharField(blank=True, max_length=100, verbose_name='Complemento')),
                ('is_active', models.BooleanField(default=True, verbose_name='Está Ativo?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='É administrador?')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True, verbose_name='Chave')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('confirmed', models.BooleanField(default=False, verbose_name='Confirmado?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_resets', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Nova senha',
                'verbose_name_plural': 'Novas senhas',
                'ordering': ['-created_at'],
            },
        ),
    ]
