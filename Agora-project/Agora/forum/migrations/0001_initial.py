# Generated by Django 3.1 on 2020-08-07 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=80)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('creatore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussioni', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Discussione',
                'verbose_name_plural': 'Discussioni',
            },
        ),
        migrations.CreateModel(
            name='Sezione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=80)),
                ('descrizione', models.CharField(blank=True, max_length=150, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Sezione',
                'verbose_name_plural': 'Sezioni',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testo', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('creatore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('discussione_appartenenza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.discussione')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.AddField(
            model_name='discussione',
            name='sezione_appartenenza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.sezione'),
        ),
    ]
