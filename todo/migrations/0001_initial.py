# Generated by Django 3.2.2 on 2021-05-12 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('time', models.DateTimeField(verbose_name='last updated time')),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]