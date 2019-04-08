# Generated by Django 2.1.5 on 2019-01-10 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_name', models.CharField(max_length=20, unique=True, verbose_name='登录账号')),
                ('name', models.CharField(max_length=20, verbose_name='用户昵称')),
                ('password', models.CharField(max_length=30, verbose_name='用户密码')),
                ('tel', models.CharField(max_length=11, null=True, unique=True, verbose_name='用户电话')),
            ],
        ),
    ]