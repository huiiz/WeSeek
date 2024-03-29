# Generated by Django 3.2.3 on 2021-06-09 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='预约人数')),
                ('title', models.CharField(default='', max_length=64, null=True, verbose_name='活动主题')),
                ('content', models.TextField(default='', null=True, verbose_name='活动内容')),
                ('from_time', models.DateTimeField(verbose_name='预约开始时间')),
                ('to_time', models.DateTimeField(verbose_name='预约结束时间')),
                ('remarks', models.CharField(default='', max_length=512, null=True, verbose_name='备注')),
                ('response', models.CharField(default='', max_length=512, verbose_name='回复')),
                ('name', models.CharField(default='', max_length=8, verbose_name='姓名')),
                ('phone', models.CharField(default=None, max_length=20, null=True, verbose_name='手机号')),
                ('status', models.BooleanField(default=False, verbose_name='状态，False为还未成功')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('delete_time', models.DateTimeField(default=None, null=True, verbose_name='删除时间')),
            ],
            options={
                'verbose_name': '预约信息',
                'verbose_name_plural': '预约信息',
            },
        ),
    ]
