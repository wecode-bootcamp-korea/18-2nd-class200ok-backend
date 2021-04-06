# Generated by Django 3.1.7 on 2021-04-06 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'difficulties',
            },
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'hashtags',
            },
        ),
        migrations.CreateModel(
            name='PendingLecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('cover_image_url', models.CharField(max_length=2000, null=True)),
                ('summary_image_url', models.CharField(max_length=2000, null=True)),
                ('detailed_category', models.CharField(max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lecture.category')),
                ('difficulty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lecture.difficulty')),
            ],
            options={
                'db_table': 'pending_lectures',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pending_lecture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lecture.pendinglecture')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user')),
            ],
            options={
                'db_table': 'votes',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecture.category')),
            ],
            options={
                'db_table': 'subcategories',
            },
        ),
        migrations.CreateModel(
            name='PendingLectureHashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lecture.hashtag')),
                ('pending_lecture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lecture.pendinglecture')),
            ],
            options={
                'db_table': 'pending_lectures_hashtags',
                'unique_together': {('pending_lecture', 'hashtag')},
            },
        ),
        migrations.AddField(
            model_name='pendinglecture',
            name='hashtags',
            field=models.ManyToManyField(through='lecture.PendingLectureHashtag', to='lecture.Hashtag'),
        ),
        migrations.AddField(
            model_name='pendinglecture',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lecture.subcategory'),
        ),
        migrations.AddField(
            model_name='pendinglecture',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user'),
        ),
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=300, null=True)),
                ('image_url', models.CharField(max_length=2000)),
                ('pending_lecture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lecture.pendinglecture')),
            ],
            options={
                'db_table': 'introductions',
            },
        ),
        migrations.AlterUniqueTogether(
            name='pendinglecture',
            unique_together={('user', 'title')},
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('discount_rate', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('description', models.TextField(default='HTML')),
                ('down_payment', models.DecimalField(decimal_places=0, default=5, max_digits=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lecture.category')),
                ('difficulty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lecture.difficulty')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lecture.subcategory')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user')),
            ],
            options={
                'db_table': 'lectures',
                'unique_together': {('user', 'title')},
            },
        ),
    ]
