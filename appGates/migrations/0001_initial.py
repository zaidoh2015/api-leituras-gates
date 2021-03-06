# Generated by Django 2.1.2 on 2018-10-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('BLQ-01', 'E-001'), ('BLQ-02', 'E-002'), ('BLQ-03', 'E-003'), ('BLQ-04', 'E-004'), ('BLQ-05', 'E-005'), ('BLQ-06', 'E-006'), ('BLQ-07', 'E-007'), ('BLQ-08', 'E-008'), ('BLQ-09', 'E-009'), ('BLQ-11', 'E-011'), ('BLQ-12', 'E-012'), ('BLQ-01', 'M-001'), ('BLQ-02', 'M-002'), ('BLQ-03', 'M-003'), ('BLQ-04', 'M-004'), ('BLQ-05', 'M-005'), ('BLQ-06', 'M-006'), ('BLQ-07', 'M-007'), ('BLQ-08', 'M-008'), ('BLQ-09', 'M-019'), ('BLQ-10', 'M-010'), ('BLQ-11', 'M-011'), ('BLQ-12', 'M-012')], max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
