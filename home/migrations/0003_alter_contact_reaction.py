# Generated by Django 4.1.6 on 2023-02-06 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_contact_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="reaction",
            field=models.IntegerField(
                choices=[(1, "Awful"), (2, "Bad"), (3, "Meh"), (4, "Good"), (5, "Rad")]
            ),
        ),
    ]
