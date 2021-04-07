# Generated by Django 3.1.7 on 2021-04-07 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('lecture', '0002_auto_20210406_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendinglecture',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user', unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='pendinglecture',
            unique_together=set(),
        ),
    ]
