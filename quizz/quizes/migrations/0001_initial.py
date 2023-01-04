# Generated by Django 4.1.4 on 2023-01-04 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('topic', models.CharField(max_length=120)),
                ('nombre_de_question', models.IntegerField()),
                ('temps', models.IntegerField(help_text='temps du quiz')),
                ('score_passe', models.IntegerField(help_text='score demander en %')),
                ('niveau', models.CharField(choices=[('facile', 'facile'), ('moyen', 'moyen'), ('difficile', 'difficile')], max_length=15)),
            ],
        ),
    ]
