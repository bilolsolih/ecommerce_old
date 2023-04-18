# Generated by Django 4.2 on 2023-04-18 16:58

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=128, unique=True, verbose_name='Username')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='UZ', unique=True, verbose_name='Phone number')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('first_name', models.CharField(max_length=124, verbose_name='First name')),
                ('last_name', models.CharField(max_length=124, verbose_name='Last name')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='images/accounts/profile/%Y/%m/%d/', verbose_name='Profile photo')),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='m', max_length=1, verbose_name='Gender')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is staff?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active?')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Is superuser?')),
                ('groups', models.ManyToManyField(blank=True, related_name='users', to='auth.group', verbose_name='Groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
