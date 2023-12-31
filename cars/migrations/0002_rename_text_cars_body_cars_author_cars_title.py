# Generated by Django 4.0.10 on 2023-05-09 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars',
            old_name='text',
            new_name='body',
        ),
        migrations.AddField(
            model_name='cars',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cars',
            name='title',
            field=models.CharField(default='Azbel', max_length=2000),
            preserve_default=False,
        ),
    ]
