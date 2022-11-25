# Generated by Django 4.1.1 on 2022-11-25 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carnet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carnet_user',
            name='id',
        ),
        migrations.AddField(
            model_name='carnet_user',
            name='proprietaire',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='carnet.user'),
            preserve_default=False,
        ),
    ]
