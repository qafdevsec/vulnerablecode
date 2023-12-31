# Generated by Django 4.0.7 on 2023-01-01 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulnerabilities', '0036_alter_package_package_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisory',
            name='weaknesses',
            field=models.JSONField(blank=True, default=list, help_text='A list of CWE ids'),
        ),
        migrations.CreateModel(
            name='Weakness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cwe_id', models.IntegerField(help_text='CWE id')),
                ('vulnerabilities', models.ManyToManyField(related_name='weaknesses', to='vulnerabilities.vulnerability')),
            ],
        ),
    ]
