# Generated by Django 4.0.2 on 2022-02-05 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('peeringmanager', '0016_router_flag_emoji_alter_peering_bandwidth_community'),
    ]

    operations = [
        migrations.AddField(
            model_name='peering',
            name='mntner',
            field=models.CharField(default='LUTOMA-MNT', max_length=200, unique=True, verbose_name='Maintainer object'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='peering',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
    ]