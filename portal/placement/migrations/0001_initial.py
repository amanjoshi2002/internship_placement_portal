# Generated by Django 5.0.4 on 2024-05-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('slots', models.IntegerField()),
                ('link', models.URLField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='internship_logos/')),
                ('last_date_to_apply', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('slots', models.IntegerField()),
                ('link', models.URLField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='placement_logos/')),
                ('last_date_to_apply', models.DateField()),
            ],
        ),
    ]
