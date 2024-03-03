# Generated by Django 4.2.10 on 2024-03-03 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Application Submission Date')),
                ('position', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('enthusiasm', models.CharField(choices=[('1', '😐'), ('2', '😃'), ('3', '😍')], default='1', max_length=1)),
                ('workArrangement', models.CharField(choices=[('R', 'Remote'), ('H', 'Hybrid'), ('O', 'On-site')], default='R', max_length=1)),
                ('location', models.CharField(max_length=50)),
                ('techstack', models.TextField(max_length=100)),
                ('status', models.CharField(choices=[('A', 'Applied'), ('Y', 'Yet to Apply'), ('I', 'Interviewing'), ('N', 'Negotiating'), ('O', 'Accepted'), ('D', 'Decline'), ('R', 'Rejected')], default='A', max_length=1)),
                ('minsalary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('maxsalary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('notes', models.TextField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
