# Generated by Django 5.1.2 on 2024-12-02 06:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0013_alter_allproduct_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='allproduct',
            name='status',
            field=models.CharField(choices=[('Not orderd', 'Not Ordered'), ('Pending', 'Pending'), ('Ready for ship', 'Ready for ship'), ('Order shipped', 'Order shipped'), ('Out of delivery', 'Out of delivery'), ('Delivered', 'Delivered')], default='', max_length=50),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cartitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.allproduct')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.cart')),
            ],
        ),
    ]