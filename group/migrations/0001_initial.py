# Generated by Django 3.2.3 on 2021-06-09 13:33

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InitialiseGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=5, verbose_name='招募队员数量')),
                ('requirement', models.TextField(default=None, null=True, verbose_name='期望队友要求')),
                ('allow_time', models.DateTimeField(default=None, null=True, verbose_name='截止招募时间')),
                ('remarks', models.TextField(default=None, null=True, verbose_name='备注')),
                ('success', models.BooleanField(default=False, verbose_name='组队成功')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '新建组队',
                'verbose_name_plural': '新建组队',
            },
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_time', models.DateTimeField(auto_now_add=True, verbose_name='请求加入时间')),
                ('allowed_time', models.DateTimeField(blank=True, null=True, verbose_name='允许时间')),
                ('refused', models.BooleanField(default=False, verbose_name='是否被发起人拒绝')),
                ('cancel', models.BooleanField(default=False, verbose_name='是否取消申请')),
                ('group_id', models.ForeignKey(db_column='group_id', on_delete=django.db.models.expressions.Case, related_name='group_id', to='group.initialisegroup', verbose_name='队伍')),
            ],
            options={
                'verbose_name': '加入队伍',
                'verbose_name_plural': '加入队伍',
            },
        ),
    ]
