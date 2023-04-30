# Generated by Django 4.1.8 on 2023-04-29 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0049_alter_event_id_alter_event_category_name_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("booking", "0004_remove_ticket_guest_id_booking"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "full_price",
                    models.DecimalField(decimal_places=2, max_digits=8, null=True),
                ),
                ("fee", models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                (
                    "total",
                    models.DecimalField(decimal_places=2, max_digits=8, null=True),
                ),
                ("is_validated", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("quantity", models.PositiveIntegerField()),
                ("ticket_price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("currency", models.CharField(default="USD", max_length=10)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="booking.order"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TicketClass",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
                ("price", models.FloatField()),
                ("capacity", models.IntegerField()),
                ("quantity_sold", models.IntegerField()),
                (
                    "ticket_type",
                    models.CharField(
                        choices=[
                            ("Free", "Free"),
                            ("Paid", "Paind"),
                            ("Donation", "Donation"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "Absorb_fees",
                    models.CharField(
                        choices=[("t", "true"), ("f", "false")], max_length=1
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="event.event"
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="ticket",
            name="event",
        ),
        # migrations.RemoveField(
        #     model_name="discount",
        #     name="ID",
        # ),
        # migrations.AlterField(
        #     model_name="discount",
        #     name="EVENT_ID",
        #     field=models.ForeignKey(
        #         on_delete=django.db.models.deletion.CASCADE, to="event.event"
        #     ),
        # ),
        # migrations.AlterField(
        #     model_name="discount",
        #     name="id",
        #     field=models.IntegerField(primary_key=True, serialize=False),
        # ),
        migrations.DeleteModel(
            name="Booking",
        ),
        migrations.DeleteModel(
            name="Ticket",
        ),
        migrations.AddField(
            model_name="orderitem",
            name="ticket_class",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="booking.ticketclass"
            ),
        ),
        # migrations.AddField(
        #     model_name="order",
        #     name="discount",
        #     field=models.ForeignKey(
        #         null=True,
        #         on_delete=django.db.models.deletion.CASCADE,
        #         to="booking.discount",
        #     ),
        # ),
        migrations.AddField(
            model_name="order",
            name="event",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="event.event"
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        # migrations.AddField(
        #     model_name="discount",
        #     name="ticket_class",
        #     field=models.ForeignKey(
        #         default=1,
        #         on_delete=django.db.models.deletion.CASCADE,
        #         to="booking.ticketclass",
        #     ),
        #     preserve_default=False,
        # ),
    ]
