# Generated by Django 3.1.5 on 2021-10-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='number',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='댓글 번호'),
        ),
    ]
