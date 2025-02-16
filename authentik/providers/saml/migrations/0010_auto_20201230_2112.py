# Generated by Django 3.1.4 on 2020-12-30 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_providers_saml", "0009_auto_20201112_2016"),
    ]

    operations = [
        migrations.AlterField(
            model_name="samlprovider",
            name="audience",
            field=models.TextField(
                blank=True,
                default="",
                help_text="Value of the audience restriction field of the assertion. When left empty, no audience restriction will be added.",
            ),
        ),
    ]
