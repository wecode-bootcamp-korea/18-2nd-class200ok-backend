# Generated by Django 3.1.7 on 2021-04-05 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=45, null=True, unique=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('kakao_id', models.CharField(max_length=20, unique=True)),
                ('is_creator', models.BooleanField(default=False)),
                ('voting_power', models.IntegerField(default=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('phonenumber', models.CharField(max_length=13, unique=True)),
                ('introduction', models.CharField(max_length=200)),
                ('profile_image_url', models.CharField(max_length=2000)),
                ('image_url', models.CharField(max_length=2000, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user')),
            ],
            options={
                'db_table': 'creators',
            },
        ),
    ]
