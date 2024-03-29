# Generated by Django 3.2.3 on 2021-06-09 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitycollection',
            name='a_collect_user',
            field=models.ForeignKey(db_column='a_collect_user', on_delete=django.db.models.expressions.Case, related_name='a_collect_user', to=settings.AUTH_USER_MODEL, verbose_name='收藏人'),
        ),
        migrations.AddField(
            model_name='activitycollection',
            name='activity',
            field=models.ForeignKey(db_column='activity', on_delete=django.db.models.expressions.Case, related_name='activity', to='activity.activity', verbose_name='活动收藏'),
        ),
    ]
