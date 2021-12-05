# Generated by Django 3.2.9 on 2021-12-05 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='external_books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('isbn', models.TextField()),
                ('authors', models.CharField(max_length=250)),
                ('number_of_pages', models.IntegerField()),
                ('publisher', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('release_date', models.DateField()),
            ],
        ),
    ]
