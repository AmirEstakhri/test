# Generated by Django 5.1.1 on 2024-11-18 22:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=50, unique=True)),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=50, unique=True)),
            ],
            options={
                "verbose_name": "Tag",
                "verbose_name_plural": "Tags",
            },
        ),
        migrations.CreateModel(
            name="CustomUser",
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
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("username", models.CharField(max_length=150, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("admin", "Admin"),
                            ("manager", "Manager"),
                            ("user", "User"),
                        ],
                        default="user",
                        max_length=20,
                    ),
                ),
                (
                    "sub_role",
                    models.CharField(
                        choices=[
                            ("none", "None"),
                            (
                                "user-access-to-all-users-with-role-user",
                                "User Access to All Users with Role User",
                            ),
                            (
                                "manager-access-to-all-users-with-role-manager",
                                "user Access to All Users with Role Manager",
                            ),
                        ],
                        default="none",
                        max_length=255,
                    ),
                ),
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
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
            },
        ),
        migrations.CreateModel(
            name="Form",
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
                ("title", models.CharField(max_length=255)),
                ("sender_signature", models.CharField(max_length=255)),
                ("receiver", models.CharField(max_length=255)),
                ("receiver_signature", models.CharField(blank=True, max_length=255)),
                ("content", models.TextField()),
                ("sender_name", models.CharField(max_length=255)),
                ("prioritize", models.BooleanField(default=False)),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("High", "High"),
                            ("Medium", "Medium"),
                            ("Low", "Low"),
                        ],
                        default="Medium",
                        max_length=100,
                    ),
                ),
                ("sender", models.CharField(max_length=100)),
                ("verified", models.BooleanField(default=False)),
                ("verified_at", models.DateTimeField(blank=True, null=True)),
                ("last_modified", models.DateTimeField(auto_now=True)),
                (
                    "allowed_managers",
                    models.ManyToManyField(
                        blank=True,
                        related_name="allowed_forms",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "assigned_managers",
                    models.ManyToManyField(
                        blank=True,
                        limit_choices_to={"role": "manager"},
                        related_name="assigned_forms",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "assigned_users",
                    models.ManyToManyField(
                        blank=True,
                        limit_choices_to={"role": "user"},
                        related_name="viewable_forms",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="forms",
                        to="app.category",
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
                ),
                (
                    "verified_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="verified_forms",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, related_name="forms", to="app.tag"
                    ),
                ),
            ],
            options={
                "verbose_name": "Form",
                "verbose_name_plural": "Forms",
            },
        ),
        migrations.CreateModel(
            name="FormVersion",
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
                ("version_number", models.IntegerField()),
                ("data", models.JSONField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="versions",
                        to="app.form",
                    ),
                ),
            ],
            options={
                "verbose_name": "Form Version",
                "verbose_name_plural": "Form Versions",
            },
        ),
    ]
