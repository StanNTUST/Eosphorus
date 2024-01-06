# Generated by Django 4.2.1 on 2023-11-24 01:02

import base.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("bio", models.TextField(blank=True, null=True)),
                ("nickname", models.CharField(max_length=20, null=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "avatar",
                    models.ImageField(default="avatar.png", null=True, upload_to=""),
                ),
                (
                    "line_user_id",
                    models.CharField(blank=True, default="", max_length=80, null=True),
                ),
                ("is_staff", models.BooleanField(default=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_superuser", models.BooleanField(default=False)),
                (
                    "persona",
                    models.ImageField(
                        default="loading.gif",
                        storage=base.models.OverwriteStorage(),
                        upload_to="persona",
                    ),
                ),
                ("artifacts", models.TextField(blank=True, null=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
            ],
            options={"verbose_name": "User", "verbose_name_plural": "Users",},
            managers=[("objects", base.models.CustomUserManager()),],
        ),
        migrations.CreateModel(
            name="ActivityTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="CompetitionTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="OurTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag_name", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=400)),
                ("emb", models.TextField(null=True)),
                ("emb_org", models.TextField(null=True)),
                ("ord", models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Topic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField(blank=True, null=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("pin_mode", models.BooleanField(default=False)),
                (
                    "host",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        default=0, related_name="likes", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "participants",
                    models.ManyToManyField(
                        blank=True,
                        related_name="participants",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "topic",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="base.topic",
                    ),
                ),
            ],
            options={"ordering": ["-updated", "-created"],},
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("body", models.TextField()),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.room"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Competition",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                ("url", models.URLField(null=True)),
                ("cover_img_url", models.URLField(null=True)),
                ("start_time", models.DateTimeField(null=True)),
                ("end_time", models.DateTimeField(null=True)),
                ("guide_line_html", models.TextField(null=True)),
                ("organizer_title", models.TextField(null=True)),
                ("page_views", models.IntegerField(null=True)),
                ("contact_email", models.EmailField(max_length=254, null=True)),
                ("contact_name", models.TextField(null=True)),
                ("contact_phone", models.TextField(null=True)),
                ("limit_highschool", models.BooleanField(null=True)),
                ("limit_none", models.BooleanField(null=True)),
                ("limit_other", models.BooleanField(null=True)),
                ("emb", models.CharField(max_length=800, null=True)),
                ("our_tags", models.ManyToManyField(blank=True, to="base.ourtag")),
                ("tags", models.ManyToManyField(blank=True, to="base.competitiontag")),
            ],
        ),
        migrations.CreateModel(
            name="Activity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                ("eventIdNumber", models.TextField(null=True)),
                ("start_time", models.DateTimeField(null=True)),
                ("end_time", models.DateTimeField(null=True)),
                ("eventPlaceType", models.TextField(null=True)),
                ("location", models.TextField(null=True)),
                ("likeCount", models.IntegerField(null=True)),
                ("page_views", models.IntegerField(null=True)),
                ("isAD", models.BooleanField(null=True)),
                ("cover_img_url", models.URLField(null=True)),
                ("url", models.URLField(null=True)),
                ("guide_line_html", models.TextField(null=True)),
                ("summary", models.TextField(null=True)),
                ("precise_location", models.TextField(null=True)),
                ("longitude_and_latitude", models.TextField(null=True)),
                ("add_to_calendar", models.URLField(null=True)),
                ("agency_title", models.TextField(null=True)),
                ("emb", models.TextField(null=True)),
                ("our_tags", models.ManyToManyField(blank=True, to="base.ourtag")),
                ("tags", models.ManyToManyField(blank=True, to="base.activitytag")),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="love_activity",
            field=models.ManyToManyField(
                blank=True, related_name="love_activity", to="base.activity"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="love_comp",
            field=models.ManyToManyField(
                blank=True, related_name="love_comp", to="base.competition"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="nope_activity",
            field=models.ManyToManyField(
                blank=True, related_name="nope_activity", to="base.activity"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="nope_comp",
            field=models.ManyToManyField(
                blank=True, related_name="nope_comp", to="base.competition"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="top3",
            field=models.ManyToManyField(
                blank=True, related_name="top3", to="base.ourtag"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]
