# Generated by Django 5.0.3 on 2024-03-19 05:36

import encrypted_model_fields.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("translator", "0019_alter_openaitranslator_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="MoonshotAITranslator",
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
                (
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="Name"),
                ),
                ("valid", models.BooleanField(null=True, verbose_name="Valid")),
                (
                    "api_key",
                    encrypted_model_fields.fields.EncryptedCharField(
                        verbose_name="API Key"
                    ),
                ),
                (
                    "base_url",
                    models.URLField(
                        default="https://api.moonshot.cn/v1", verbose_name="API URL"
                    ),
                ),
                (
                    "model",
                    models.CharField(
                        choices=[
                            ("moonshot-v1-8k", "moonshot-v1-8k"),
                            ("moonshot-v1-32k", "moonshot-v1-32k"),
                            ("moonshot-v1-128k", "moonshot-v1-128k"),
                        ],
                        default="moonshot-v1-8k",
                        max_length=100,
                    ),
                ),
                (
                    "prompt",
                    models.TextField(
                        default="Translate only the text from the following into {target_language},only returns translations.\n{text}"
                    ),
                ),
                ("temperature", models.FloatField(default=0.5)),
                ("top_p", models.FloatField(default=0.95)),
                ("frequency_penalty", models.FloatField(default=0)),
                ("presence_penalty", models.FloatField(default=0)),
                ("max_tokens", models.IntegerField(default=1000)),
            ],
            options={
                "verbose_name": "Moonshot AI",
                "verbose_name_plural": "Moonshot AI",
            },
        ),
    ]
