# Generated by Django 4.1.1 on 2022-11-25 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carnet', '0006_alter_carnet_user_proprietaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carnet_user',
            name='proprietaire',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='carnet.user'),
            preserve_default=False,
        ),
    ]
