# Generated by Django 3.2.9 on 2021-11-20 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_sl', '0003_auto_20211116_0810'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='stories_user',
        ),
        migrations.CreateModel(
            name='presents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stories', models.IntegerField(blank=True)),
                ('poems', models.IntegerField(blank=True)),
                ('novels', models.IntegerField(blank=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presents', to='user_sl.user')),
            ],
            options={
                'db_table': 'presents',
            },
        ),
    ]
