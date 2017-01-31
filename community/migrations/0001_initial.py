# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-30 21:05
from __future__ import unicode_literals

import community.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('display_name', models.CharField(max_length=25, unique=True)),
                ('grade', models.PositiveIntegerField()),
                ('published_date', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('show_full_name', models.BooleanField(default=False)),
                ('is_public', models.BooleanField(default=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=community.models.image_upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='StudentNeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.PositiveIntegerField()),
                ('achievement', models.PositiveIntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('measurement', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('published_date', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_verified', models.BooleanField(default=False)),
                ('district', models.CharField(choices=[('jhapa', 'Jhapa District'), ('ilam', 'Ilam District'), ('panchthar', 'Panchthar District'), ('taplejung', 'Taplejung District'), ('morang', 'Morang District'), ('sunsari', 'Sunsari District'), ('bhojpur', 'Bhojpur District'), ('dhankuta', 'Dhankuta District'), ('terhathum', 'Terhathum District'), ('sankhuwasabha', 'Sankhuwasabha District'), ('saptari', 'Saptari District'), ('siraha', 'Siraha District'), ('udayapur', 'Udayapur District'), ('khotang', 'Khotang District'), ('okhaldhunga', 'Okhaldhunga District'), ('solukhumbu', 'Solukhumbu District'), ('dhanusa', 'Dhanusa District'), ('mahottari', 'Mahottari District'), ('sarlahi', 'Sarlahi District'), ('sindhuli', 'Sindhuli District'), ('ramechhap', 'Ramechhap District'), ('dolakha', 'Dolakha District'), ('bhaktapur', 'Bhaktapur District'), ('dhading', 'Dhading District'), ('kathmandu', 'Kathmandu District'), ('kavrepalanchok', 'Kavrepalanchok District'), ('lalitpur', 'Lalitpur District'), ('nuwakot', 'Nuwakot District'), ('rasuwa', 'Rasuwa District'), ('sindhupalchok', 'Sindhupalchok District'), ('bara', 'Bara District'), ('parsa', 'Parsa District'), ('rautahat', 'Rautahat District'), ('chitwan', 'Chitwan District'), ('makwanpur', 'Makwanpur District'), ('gorkha', 'Gorkha District'), ('kaski', 'Kaski District'), ('lamjung', 'Lamjung District'), ('syangja', 'Syangja District'), ('tanahun', 'Tanahun District'), ('manang', 'Manang District'), ('kapilvastu', 'Kapilvastu District'), ('nawalparasi', 'Nawalparasi District'), ('rupandehi', 'Rupandehi District'), ('arghakhanchi', 'Arghakhanchi District'), ('gulmi', 'Gulmi District'), ('palpa', 'Palpa District'), ('baglung', 'Baglung District'), ('myagdi', 'Myagdi District'), ('parbat', 'Parbat District'), ('mustang', 'Mustang District'), ('dang', 'Dang Deukhuri District'), ('pyuthan', 'Pyuthan District'), ('rolpa', 'Rolpa District'), ('rukum', 'Rukum District'), ('salyan', 'Salyan District'), ('dolpa', 'Dolpa District'), ('humla', 'Humla District'), ('jumla', 'Jumla District'), ('kalikot', 'Kalikot District'), ('mugu', 'Mugu District'), ('banke', 'Banke District'), ('bardiya', 'Bardiya District'), ('surkhet', 'Surkhet District'), ('dailekh', 'Dailekh District'), ('jajarkot', 'Jajarkot District'), ('kailali', 'Kailali District'), ('achham', 'Achham District'), ('doti', 'Doti District'), ('bajhang', 'Bajhang District'), ('bajura', 'Bajura District'), ('kanchanpur', 'Kanchanpur District'), ('dadeldhura', 'Dadeldhura District'), ('baitadi', 'Baitadi District'), ('darchula', 'Darchula District')], default='taplejung', max_length=15)),
                ('description', models.TextField()),
            ],
        ),
    ]