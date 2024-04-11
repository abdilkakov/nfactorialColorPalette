# Generated by Django 4.2.11 on 2024-04-07 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PopularColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('hue', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
