# Generated by Django 3.2.7 on 2021-09-03 18:47

import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='SomeOtherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=65)),
                ('other', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='someapp.someothermodel')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            managers=[
                ('on_site', django.contrib.sites.managers.CurrentSiteManager('site')),
            ],
        ),
    ]