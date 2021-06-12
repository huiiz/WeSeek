# Generated by Django 3.2.3 on 2021-06-09 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_title', models.CharField(default=None, max_length=32, null=True, verbose_name='消息标题')),
                ('message_content', models.CharField(max_length=1024, verbose_name='消息内容')),
                ('have_read', models.BooleanField(verbose_name='是否已读')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '加入队伍',
                'verbose_name_plural': '加入队伍',
            },
        ),
    ]