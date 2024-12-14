# Generated by Django 5.1.4 on 2024-12-14 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('open', 'open'), ('in-progress', 'in-progress'), ('pending', 'pending'), ('closed', 'closed')], default='open', max_length=100)),
                ('remarks', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
