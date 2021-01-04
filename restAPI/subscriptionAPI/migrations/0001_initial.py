# Generated by Django 3.1.4 on 2021-01-04 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerDetails',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=512)),
                ('address', models.CharField(max_length=1000)),
                ('dob', models.DateField()),
                ('company', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionDetails',
            fields=[
                ('sub_id', models.IntegerField(primary_key=True, serialize=False)),
                ('subscription_name', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=17)),
                ('amount', models.IntegerField()),
                ('date_time', models.DateTimeField()),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptionAPI.managerdetails')),
                ('sub_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptionAPI.subscriptiondetails')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=17)),
                ('expire_month', models.CharField(max_length=2)),
                ('expire_year', models.CharField(max_length=2)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptionAPI.managerdetails')),
            ],
        ),
    ]