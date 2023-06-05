from django.core.exceptions import ValidationError
from datetime import datetime


def validate_timestamp(value):
    today = datetime.now().date()

    if value < today:
        raise ValidationError("Timestamp must be today or next days")
