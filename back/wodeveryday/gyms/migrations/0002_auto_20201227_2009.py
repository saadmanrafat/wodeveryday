# Generated by Django 3.1.4 on 2020-12-27 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gyms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='gyms.region'),
        ),
    ]
