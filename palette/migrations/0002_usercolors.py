# Generated by Django 4.2.11 on 2024-04-08 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('palette', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserColors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hue', models.IntegerField()),
                ('sat', models.IntegerField()),
                ('lightness', models.IntegerField()),
                ('hex', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
