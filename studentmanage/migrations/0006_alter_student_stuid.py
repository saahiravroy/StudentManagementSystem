# Generated by Django 3.2.12 on 2022-02-13 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentmanage', '0005_alter_student_stuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='StuID',
            field=models.IntegerField(null=True),
        ),
    ]
