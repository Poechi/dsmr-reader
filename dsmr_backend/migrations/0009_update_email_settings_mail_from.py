# Generated by Django 2.2.9 on 2020-01-03 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsmr_backend', '0008_scheduled_process_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailsettings',
            name='email_from',
            field=models.EmailField(blank=True, default=None, help_text='The email address you want to send any emails from', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='emailsettings',
            name='use_ssl',
            field=models.BooleanField(default=False, help_text='Optional: Whether to use an implicit TLS (secure) connection when talking to the SMTP server. In most email documentation this type of TLS connection is referred to as SSL. It is generally used on port 465', verbose_name='Use SSL'),
        ),
        migrations.AlterField(
            model_name='emailsettings',
            name='use_tls',
            field=models.BooleanField(default=False, help_text='Optional: Whether to use a TLS (secure) connection when talking to the SMTP server. This is used for explicit TLS connections, generally on port 587', verbose_name='Use TLS'),
        ),
    ]
