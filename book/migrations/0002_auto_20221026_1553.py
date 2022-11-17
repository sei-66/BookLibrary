# Generated by Django 3.2 on 2022-10-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=100)),
                ("text", models.TextField()),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("business", "ビジネス"),
                            ("life", "生活"),
                            ("manga", "マンガ"),
                            ("other", "その他"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="SampleModel",
        ),
    ]
