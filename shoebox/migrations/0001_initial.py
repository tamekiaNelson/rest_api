# Generated by Django 3.0.2 on 2020-01-09 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.URLField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('Red', 'Red'), ('Orange', 'Orange'), ('Yello', 'Yello'), ('Green', 'Green'), ('Blue', 'Blue'), ('Indigo', 'Indigo'), ('Violet', 'Violet'), ('White', 'White'), ('Black', 'Black')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(choices=[('sneaker', 'sneaker'), ('boot', 'boot'), ('sandal', 'sandal'), ('dress', 'dress'), ('other', 'other')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(default=0)),
                ('brand', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=100)),
                ('fasten_type', models.CharField(max_length=100)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoebox.ShoeColor')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoebox.Manufacturer')),
                ('shoe_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoebox.ShoeType')),
            ],
        ),
    ]
