# Generated by Django 2.2 on 2019-12-05 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tom_dataproducts', '0007_manual_20191016_rename_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reduceddatum',
            options={'get_latest_by': ('timestamp',)},
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='data_product_type',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='reduceddatum',
            name='data_type',
            field=models.CharField(default='', max_length=100),
        ),
    ]