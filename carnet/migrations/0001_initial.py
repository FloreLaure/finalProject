# Generated by Django 4.1.1 on 2022-12-15 13:18

import datetime
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
            name='ajouAutre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('Episode_essentiels_de_maladie', models.TextField()),
                ('Prescription_Observations', models.TextField()),
                ('Prescripteur', models.CharField(max_length=30)),
                ('lieu', models.CharField(default='hopital', max_length=30)),
                ('fichier', models.FileField(upload_to='upload/')),
                ('autr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='vaccinal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('Vaccin', models.CharField(max_length=30)),
                ('Prescription_Observations', models.TextField()),
                ('Prescripteur', models.CharField(max_length=30)),
                ('lieu', models.CharField(default='hopital', max_length=30)),
                ('fichier', models.FileField(upload_to='upload/')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=30, null=True)),
                ('Prenom', models.CharField(max_length=40, null=True)),
                ('Profession', models.CharField(max_length=30, null=True)),
                ('Date_de_naissance', models.DateField(default=datetime.datetime.now)),
                ('Secteur_ou_village', models.CharField(max_length=30, null=True)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], default='M', max_length=6, null=True)),
                ('photo', models.ImageField(upload_to='upload/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='familiaux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('Tare', models.CharField(max_length=30)),
                ('Prescription_Observations', models.TextField()),
                ('Prescripteur', models.CharField(max_length=30)),
                ('lieu', models.CharField(default='hopital', max_length=30)),
                ('fichier', models.FileField(upload_to='upload/')),
                ('famille', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='carnetUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserProfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carnet.userprofil')),
                ('autre', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='carnet.ajouautre')),
                ('familiaux', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='carnet.familiaux')),
                ('vaccinal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='carnet.vaccinal')),
            ],
        ),
    ]
