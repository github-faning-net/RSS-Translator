# Generated by Django 5.0.1 on 2024-02-10 01:24

import encrypted_model_fields.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('translator', '0007_caiyuntranslator_max_characters_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeminiTranslator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('valid', models.BooleanField(null=True, verbose_name='Valid')),
                ('api_key', encrypted_model_fields.fields.EncryptedCharField(verbose_name='API Key')),
                ('model',
                 models.CharField(choices=[('gemini-pro', 'gemini-pro')], default='gemini-pro', max_length=100)),
                ('prompt', models.TextField(
                    default='Translate only the text from the following into {target_language},only returns translations.\n{text}')),
                ('temperature', models.FloatField(default=0.5)),
                ('top_p', models.FloatField(default=1)),
                ('top_k', models.IntegerField(default=1)),
                ('max_tokens', models.IntegerField(default=1000)),
            ],
            options={
                'verbose_name': 'Google Gemini',
                'verbose_name_plural': 'Google Gemini',
            },
        ),
    ]
