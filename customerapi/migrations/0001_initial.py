# Generated by Django 4.1.7 on 2023-07-14 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('Invoice_no', models.IntegerField(primary_key=True, serialize=False)),
                ('Date', models.DateField()),
                ('Customer_Name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit_price', models.IntegerField()),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('Invoice_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerapi.invoice')),
            ],
        ),
    ]
