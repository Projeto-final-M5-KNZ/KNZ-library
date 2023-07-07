# Generated by Django 4.2.2 on 2023-07-07 16:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0005_alter_books_followers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=100)),
                ('published_date', models.DateField()),
                ('publishing_company', models.CharField(max_length=100)),
                ('availability', models.CharField(choices=[('unavaliable', 'Unavailable'), ('avaliable', 'Avaliable')], default='avaliable', max_length=255)),
                ('ranking', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('followers', models.ManyToManyField(related_name='Books', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]