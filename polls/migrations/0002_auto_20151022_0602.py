# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Poll',
            new_name='Question',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='poll',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='question_text',
        ),
    ]
