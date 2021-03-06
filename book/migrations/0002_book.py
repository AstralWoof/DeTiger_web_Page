# Generated by Django 3.0.8 on 2020-07-10 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=200)),
                ('date_published', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.Author')),
                ('published_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.Publisher')),
            ],
        ),
    ]
