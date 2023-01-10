# Generated by Django 4.1.4 on 2023-01-09 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App_auth', '0002_companymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionDuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveIntegerField()),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_subscription.subscriptionplan')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('duration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_subscription.subscriptionduration')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_subscription.subscriptionplan')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriberModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=255)),
                ('payment_status', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stripe_customer_id', models.CharField(blank=True, max_length=255)),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriber_company', to='App_auth.companymodel')),
                ('subscription_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_plan', to='App_subscription.subscription')),
            ],
        ),
    ]
