# Generated by Django 4.0.1 on 2022-04-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adg', '0006_member_one_liner'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]