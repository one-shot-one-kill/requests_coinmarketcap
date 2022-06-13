# Generated by Django 4.0.5 on 2022-06-13 14:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_coinname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coinname',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='coinname',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]