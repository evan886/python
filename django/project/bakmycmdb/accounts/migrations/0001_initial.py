# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django.core.validators
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('menuAuth', '0001_initial'),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='myUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('wechat', models.CharField(max_length=50, null=True, verbose_name='\u5fae\u4fe1', blank=True)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u624b\u673a', validators=[django.core.validators.RegexValidator(b'^[0-9+()-]+$', b'\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe6\x9c\x89\xe6\x95\x88\xe7\x9a\x84\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81\xe3\x80\x82', b'invalid')])),
                ('qq', models.CharField(max_length=50, null=True, verbose_name='QQ', blank=True)),
                ('availabity', models.BigIntegerField(default=0)),
                ('auth', models.ManyToManyField(to='menuAuth.menu', blank=True)),
            ],
            options={
                'db_table': 'myUser',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departmentName', models.CharField(max_length=64, verbose_name='\u90e8\u95e8\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u4ecb\u7ecd', blank=True)),
                ('availabity', models.BigIntegerField(default=1, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('auth', models.ManyToManyField(to='menuAuth.menu', blank=True)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.AddField(
            model_name='myuser',
            name='department',
            field=models.ForeignKey(verbose_name='\u90e8\u95e8', to='accounts.department', null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='department',
            unique_together=set([('departmentName', 'availabity')]),
        ),
        migrations.AlterUniqueTogether(
            name='myuser',
            unique_together=set([('username', 'availabity')]),
        ),
    ]
