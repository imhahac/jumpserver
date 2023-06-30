# Generated by Django 3.2.19 on 2023-06-30 08:13

import django.db.models.deletion
from django.db import migrations, models


def add_chatgpt_platform(apps, schema_editor):
    platform_cls = apps.get_model('assets', 'Platform')
    automation_cls = apps.get_model('assets', 'PlatformAutomation')
    platform = platform_cls.objects.create(
        name='ChatGPT', internal=True, category='gpt', type='chatgpt',
        domain_enabled=False, su_enabled=False, comment='ChatGPT',
        created_by='System', updated_by='System',
    )
    platform.protocols.create(name='chatgpt', port=443, primary=True)
    automation_cls.objects.create(ansible_enabled=False, platform=platform)


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0119_assets_add_default_node'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPT',
            fields=[
                ('asset_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='assets.asset')),
                ('proxy', models.CharField(blank=True, default='', max_length=128, verbose_name='Proxy')),
            ],
            options={
                'verbose_name': 'Web',
            },
            bases=('assets.asset',),
        ),
        migrations.RunPython(add_chatgpt_platform)
    ]
