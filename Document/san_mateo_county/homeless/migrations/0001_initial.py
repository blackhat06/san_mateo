# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donators',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('contact_number', models.IntegerField(null=True, blank=True)),
                ('date', models.DateField()),
                ('email', models.EmailField(max_length=75)),
                ('category', models.CharField(max_length=50, choices=[(b'1', b'Individual Person'), (b'2', b'Individual Group'), (b'3', b'Organization')])),
                ('description_of_donation', models.TextField()),
                ('mode_of_donation', models.CharField(max_length=20, choices=[(b'1', b'delivery'), (b'2', b'pick-up')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HomelessPeople',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(max_length=30, choices=[(b'1', b'Male'), (b'2', b'Female'), (b'3', b'Prefer not to answer')])),
                ('address', models.TextField()),
                ('contact_number', models.IntegerField(null=True, blank=True)),
                ('higher_studies', models.CharField(max_length=20, choices=[(b'1', b'Uneducated'), (b'2', b'high school'), (b'3', b'college'), (b'4', b'Undergraduate'), (b'5', b'graduate'), (b'6', b'none of above')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
