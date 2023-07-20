# Generated by Django 4.1.5 on 2023-01-24 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('pages', models.CharField(max_length=100)),
                ('rate', models.CharField(choices=[('g', 'Good'), ('m', 'Medium'), ('b', 'Bad'), ('nr', 'Not Rated')], default='NR', max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.customuser')),
            ],
        ),
    ]
