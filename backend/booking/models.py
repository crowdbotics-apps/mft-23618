from django.conf import settings
from django.db import models


class Message(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "taxi_profile.UserProfile",
        on_delete=models.CASCADE,
        related_name="message_user",
    )
    driver = models.ForeignKey(
        "taxi_profile.DriverProfile",
        on_delete=models.CASCADE,
        related_name="message_driver",
    )
    message = models.TextField()
    timestamp_created = models.DateTimeField(
        auto_now_add=True,
    )
    booking = models.ForeignKey(
        "booking.BookingTransaction",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="message_booking",
    )


class Rating(models.Model):
    "Generated Model"
    driver = models.ForeignKey(
        "taxi_profile.DriverProfile",
        on_delete=models.CASCADE,
        related_name="rating_driver",
    )
    rating = models.FloatField()
    timestamp_created = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        "taxi_profile.UserProfile",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rating_user",
    )
    review = models.TextField(
        null=True,
        blank=True,
    )


class BookingTransaction(models.Model):
    "Generated Model"
    distance = models.FloatField()
    price = models.FloatField()
    status = models.CharField(
        max_length=10,
    )
    timestamp_created = models.DateTimeField(
        auto_now_add=True,
    )
    timestamp_depart = models.DateTimeField()
    timestamp_arrive = models.DateTimeField()
    user = models.ForeignKey(
        "taxi_profile.UserProfile",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_user",
    )
    driver = models.ForeignKey(
        "taxi_profile.DriverProfile",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_driver",
    )
    pickup = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_pickup",
    )
    dropoff = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff",
    )
    tip = models.FloatField(
        null=True,
        blank=True,
    )
    dropoff2 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff2",
    )
    dropoff3 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff3",
    )
    dropoff4 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff4",
    )
    dropoff5 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff5",
    )
    dropoff6 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff6",
    )
    dropoff7 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff7",
    )
    dropoff8 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff8",
    )
    dropoff9 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff9",
    )
    dropoff10 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff10",
    )
    dropoff11 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff11",
    )
    dropoff12 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff12",
    )
    dropoff13 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff13",
    )
    dropoff14 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff14",
    )
    dropoff15 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff15",
    )
    dropoff16 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff16",
    )
    dropoff17 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff17",
    )
    dropoff18 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff18",
    )
    dropoff19 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff19",
    )
    dropoff20 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff20",
    )
    dropoff21 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff21",
    )
    dropoff22 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff22",
    )
    dropoff23 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff23",
    )
    dropoff24 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff24",
    )
    dropoff25 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff25",
    )
    dropoff26 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff26",
    )
    dropoff27 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff27",
    )
    dropoff28 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff28",
    )
    dropoff29 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff29",
    )
    dropoff30 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff30",
    )
    dropoff31 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff31",
    )
    dropoff32 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff32",
    )
    dropoff33 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff33",
    )
    dropoff34 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff34",
    )
    dropoff35 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff35",
    )
    dropoff36 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff36",
    )
    dropoff37 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff37",
    )
    dropoff38 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff38",
    )
    dropoff39 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff39",
    )
    dropoff40 = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff40",
    )
    dropoff41 = models.ForeignKey(
        "location.MapLocation",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookingtransaction_dropoff41",
    )
    dropoff42 = models.ForeignKey(
        "location.MapLocation",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookingtransaction_dropoff42",
    )
    dropoff43 = models.ForeignKey(
        "location.MapLocation",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookingtransaction_dropoff43",
    )
    dropoff44 = models.ForeignKey(
        "location.MapLocation",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookingtransaction_dropoff44",
    )
    dropoff45 = models.ForeignKey(
        "location.MapLocation",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookingtransaction_dropoff45",
    )
    dropoff46 = models.ForeignKey(
        "location.MapLocation",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookingtransaction_dropoff46",
    )
    dropoff47 = models.ForeignKey(
        "location.MapLocation",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookingtransaction_dropoff47",
    )
    dropoff48 = models.ForeignKey(
        "location.MapLocation",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookingtransaction_dropoff48",
    )
    dropoff49 = models.ForeignKey(
        "location.MapLocation",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookingtransaction_dropoff49",
    )
    dropoff50 = models.ForeignKey(
        "location.MapLocation",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookingtransaction_dropoff50",
    )


# Create your models here.
