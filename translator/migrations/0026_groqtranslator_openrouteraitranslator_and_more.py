# Generated by Django 5.0.3 on 2024-04-24 22:21

import encrypted_model_fields.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0025_remove_azureaitranslator_deloyment_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroqTranslator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('valid', models.BooleanField(null=True, verbose_name='Valid')),
                ('is_ai', models.BooleanField(default=True, editable=False)),
                ('api_key', encrypted_model_fields.fields.EncryptedCharField(verbose_name='API Key')),
                ('translate_prompt', models.TextField(default='Translate only the text into {target_language},only returns translations.')),
                ('temperature', models.FloatField(default=0.5)),
                ('top_p', models.FloatField(default=0.95)),
                ('frequency_penalty', models.FloatField(default=0)),
                ('presence_penalty', models.FloatField(default=0)),
                ('max_tokens', models.IntegerField(default=1000)),
                ('summary_prompt', models.TextField(default='Summarize the following text in {target_language}.')),
                ('base_url', models.URLField(default='https://api.groq.com/openai/v1', verbose_name='API URL')),
                ('model', models.CharField(default='llama3-8b-8192', help_text='More models can be found at https://console.groq.com/docs/models', max_length=100)),
            ],
            options={
                'verbose_name': 'Groq',
                'verbose_name_plural': 'Groq',
            },
        ),
        migrations.CreateModel(
            name='OpenRouterAITranslator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('valid', models.BooleanField(null=True, verbose_name='Valid')),
                ('is_ai', models.BooleanField(default=True, editable=False)),
                ('api_key', encrypted_model_fields.fields.EncryptedCharField(verbose_name='API Key')),
                ('translate_prompt', models.TextField(default='Translate only the text into {target_language},only returns translations.')),
                ('temperature', models.FloatField(default=0.5)),
                ('top_p', models.FloatField(default=0.95)),
                ('frequency_penalty', models.FloatField(default=0)),
                ('presence_penalty', models.FloatField(default=0)),
                ('max_tokens', models.IntegerField(default=1000)),
                ('summary_prompt', models.TextField(default='Summarize the following text in {target_language}.')),
                ('base_url', models.URLField(default='https://openrouter.ai/api/v1', verbose_name='API URL')),
                ('model', models.CharField(default='openai/gpt-3.5-turbo', help_text='More models can be found at https://openrouter.ai/docs#models', max_length=100)),
            ],
            options={
                'verbose_name': 'OpenRouter AI',
                'verbose_name_plural': 'OpenRouter AI',
            },
        ),
        migrations.CreateModel(
            name='TogetherAITranslator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('valid', models.BooleanField(null=True, verbose_name='Valid')),
                ('is_ai', models.BooleanField(default=True, editable=False)),
                ('api_key', encrypted_model_fields.fields.EncryptedCharField(verbose_name='API Key')),
                ('translate_prompt', models.TextField(default='Translate only the text into {target_language},only returns translations.')),
                ('temperature', models.FloatField(default=0.5)),
                ('top_p', models.FloatField(default=0.95)),
                ('frequency_penalty', models.FloatField(default=0)),
                ('presence_penalty', models.FloatField(default=0)),
                ('max_tokens', models.IntegerField(default=1000)),
                ('summary_prompt', models.TextField(default='Summarize the following text in {target_language}.')),
                ('base_url', models.URLField(default='https://api.together.xyz/v1', verbose_name='API URL')),
                ('model', models.CharField(default='mistralai/Mixtral-8x7B-Instruct-v0.1', help_text='More models can be found at https://docs.together.ai/docs/inference-models#chat-models', max_length=100)),
            ],
            options={
                'verbose_name': 'Together AI',
                'verbose_name_plural': 'Together AI',
            },
        ),
    ]
