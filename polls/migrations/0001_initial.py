# Generated by Django 3.1.6 on 2021-12-14 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Choice_text', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128)),
                ('start_date', models.DateTimeField(verbose_name='Date published')),
                ('end_date', models.DateTimeField(verbose_name='Date published')),
                ('description', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=300)),
                ('question_type', models.CharField(choices=[('TEXT', 'TEXT'), ('CHOICE', 'CHOICE'), ('MULTICHOICE', 'MULTICHOICE')], default='TEXT', max_length=200)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='polls.poll')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('Choice_text', models.CharField(max_length=300, null=True)),
                ('Choice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Choice', to='polls.choice')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='poll', to='polls.poll')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='question', to='polls.question')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question'),
        ),
    ]
