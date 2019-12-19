# Generated by Django 2.0.3 on 2019-10-10 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Future_Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('surname', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('pin_code', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('highest_degree_obtained', models.CharField(blank=True, max_length=50, null=True)),
                ('grades_obtained', models.CharField(blank=True, max_length=3, null=True)),
                ('max_grades', models.CharField(blank=True, max_length=3, null=True)),
                ('is_active', models.BooleanField(default=1)),
                ('time_stamp', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.Country')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('surname', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('pin_code', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('programme_studied', models.CharField(max_length=500)),
                ('grades_obtained', models.CharField(blank=True, max_length=3, null=True)),
                ('max_grades', models.CharField(blank=True, max_length=3, null=True)),
                ('year_of_study', models.IntegerField()),
                ('is_active', models.BooleanField(default=1)),
                ('time_stamp', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.Country')),
                ('industry_interested', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Industry')),
                ('skills_interested', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Skills')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('surname', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('position_in_company', models.CharField(blank=True, max_length=50, null=True)),
                ('working_years', models.IntegerField(default=0)),
                ('no_of_employees', models.IntegerField()),
                ('website_url', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('company_registration_number', models.CharField(blank=True, max_length=500, null=True)),
                ('is_active', models.BooleanField(default=1)),
                ('time_stamp', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.Country')),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Industry')),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Skills')),
                ('user_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.UserType')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]