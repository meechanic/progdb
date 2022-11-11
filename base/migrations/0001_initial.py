# Generated by Django 3.0 on 2022-11-11 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('human_description', models.TextField(blank=True)),
                ('machine_description', models.TextField(blank=True)),
                ('edition_number', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('human_description', models.TextField(blank=True)),
                ('machine_description', models.TextField(blank=True)),
                ('main_prog_language', models.TextField(blank=True)),
                ('supercategory', models.TextField(blank=True)),
                ('category', models.TextField(blank=True)),
                ('subcategory', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(unique=True)),
                ('human_description', models.TextField(blank=True)),
                ('machine_description', models.TextField(blank=True)),
                ('scheme', models.TextField(blank=True)),
                ('host', models.TextField(blank=True)),
                ('full_path', models.TextField(blank=True)),
                ('dirname', models.TextField(blank=True)),
                ('basename', models.TextField(blank=True)),
                ('supercollection', models.TextField(blank=True)),
                ('collection', models.TextField(blank=True)),
                ('subcollection', models.TextField(blank=True)),
                ('is_installation', models.BooleanField(default=False)),
                ('is_source', models.BooleanField(default=False)),
                ('edition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resource_edition', to='base.Edition')),
            ],
            options={
                'ordering': ['text'],
            },
        ),
        migrations.AddField(
            model_name='edition',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replica_package', to='base.Package'),
        ),
    ]
