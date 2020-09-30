# Generated by Django 3.0.6 on 2020-05-19 22:08

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("passbook_flows", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="InvitationStage",
            fields=[
                (
                    "stage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="passbook_flows.Stage",
                    ),
                ),
                (
                    "continue_flow_without_invitation",
                    models.BooleanField(
                        default=False,
                        help_text="If this flag is set, this Stage will jump to the next Stage when no Invitation is given. By default this Stage will cancel the Flow when no invitation is given.",
                    ),
                ),
            ],
            options={
                "verbose_name": "Invitation Stage",
                "verbose_name_plural": "Invitation Stages",
            },
            bases=("passbook_flows.stage",),
        ),
        migrations.CreateModel(
            name="Invitation",
            fields=[
                (
                    "invite_uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("expires", models.DateTimeField(blank=True, default=None, null=True)),
                (
                    "fixed_data",
                    models.JSONField(default=dict),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Invitation",
                "verbose_name_plural": "Invitations",
            },
        ),
    ]
