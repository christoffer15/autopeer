# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peeringmanager', '0002_auto_20171101_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='peering',
            name='router',
            field=models.CharField(choices=[('at-grz.gw.lutoma.dn42', 'Graz, Austria'), ('de-scn.gw.lutoma.dn42', 'Saarbrücken, Germany'), ('ca-mon.gw.lutoma.dn42', 'Montréal, Canada'), ('us-lax.gw.lutoma.dn42', 'Los Angeles, USA')], default='de-scn.gw.lutoma.dn42', max_length=50, verbose_name='Local endpoint'),
            preserve_default=False,
        ),
    ]