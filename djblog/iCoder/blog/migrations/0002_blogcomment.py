# Generated by Django 3.0.4 on 2016-07-31 02:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.expressions
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('timeStamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.expressions.Case, to='blog.BlogComment')),
                ('post', models.ForeignKey(on_delete=django.db.models.expressions.Case, to='blog.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.expressions.Case, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
