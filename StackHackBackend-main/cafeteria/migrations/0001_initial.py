# Generated by Django 3.1.3 on 2021-01-11 17:28

import cafeteria.models
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
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_code', models.CharField(max_length=20, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=300, null=True)),
                ('price', models.IntegerField(null=True)),
                ('image_url', models.URLField(null=True)),
                ('image', models.ImageField(null=True, upload_to=cafeteria.models.content_file_name)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
        ),
    ]
