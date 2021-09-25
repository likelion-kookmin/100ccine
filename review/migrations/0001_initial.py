# Generated by Django 3.2.7 on 2021-09-25 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=30, null=True, verbose_name='작성자')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('pub_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=30, null=True, verbose_name='작성자')),
                ('text', models.CharField(max_length=100, null=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('board', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='review.review')),
            ],
        ),
    ]
