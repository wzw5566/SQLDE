# Generated by Django 2.1.7 on 2019-02-22 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depat_name', models.CharField(help_text='部门名称', max_length=64, verbose_name='部门名称')),
            ],
            options={
                'verbose_name': '部门',
                'verbose_name_plural': '部门',
                'db_table': 'jt_department',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(help_text='角色名', max_length=100, verbose_name='角色名')),
            ],
            options={
                'verbose_name': '角色',
                'verbose_name_plural': '角色',
                'db_table': 'jt_role',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='姓名')),
                ('depat_id', models.IntegerField(verbose_name='部门id')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'jt_users',
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
                ('role_id', models.IntegerField(verbose_name='角色id')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否逻辑删除')),
            ],
            options={
                'verbose_name': '用户角色关系',
                'verbose_name_plural': '用户角色关系',
                'db_table': 'jt_user_role',
            },
        ),
    ]
