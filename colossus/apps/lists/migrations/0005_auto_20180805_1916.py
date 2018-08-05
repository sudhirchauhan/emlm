# Generated by Django 2.1 on 2018-08-05 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20180729_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriberimport',
            name='update_or_create',
            field=models.BooleanField(default=True, help_text='If the email address is already subscribed to the list, the entry will be updated with data fromthe CSV file. If this option is left unchecked, only new email addresses will be created.', verbose_name='update or create subscriber'),
        ),
        migrations.AlterField(
            model_name='mailinglist',
            name='forms_custom_header',
            field=models.TextField(blank=True, help_text='Header displayed on all subscription form pages. Accepts HTML.If empty, the name of the mailing list will be used.', verbose_name='custom header'),
        ),
        migrations.AlterField(
            model_name='mailinglist',
            name='list_manager',
            field=models.EmailField(blank=True, help_text='Email address to handle subscribe/unsubscribe requests.It can be a real email address or an automated route to handle callbacks/webhooks.', max_length=254, verbose_name='list manager'),
        ),
    ]