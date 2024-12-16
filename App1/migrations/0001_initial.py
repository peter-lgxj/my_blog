# Generated by Django 5.1.4 on 2024-12-12 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Books",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("isbn", models.CharField(max_length=255, unique=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("publish_date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Orders",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("order_date", models.DateTimeField(auto_now_add=True)),
                ("status", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=255, unique=True)),
                ("email", models.CharField(max_length=255, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("is_staff", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="OrdersDetails",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("quantity", models.IntegerField(default=1)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "book_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="App1.books"
                    ),
                ),
                (
                    "order_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="App1.orders"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="orders",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="App1.users"
            ),
        ),
    ]