# from django.core.exceptions import ValidationError
# from django.core.validators import MinLengthValidator, MinValueValidator
# from django.db import models
#
#
# def validate_username(username):
#     is_valid = all(ch.isalnum() or ch == '_' for ch in username)
#     if not is_valid:
#         raise ValidationError("Username must contain only letters, digits, and underscores!")
#
#
# class Profile(models.Model):
#     MIN_USERNAME_LENGTH = 3
#     MAX_USERNAME_LENGTH = 15
#     MIN_AGE_REQUIREMENT = 21
#     MAX_PASSWORD_LENGTH = 20
#     MAX_FIRST_NAME_LENGTH = 25
#     MAX_LAST_NAME_LENGTH = 25
#
#     username = models.CharField(
#         max_length=MAX_USERNAME_LENGTH,
#         validators=[
#             MinLengthValidator(MIN_USERNAME_LENGTH, message="Username must be at least 3 characters long!"),
#         ],
#         null=False,
#         blank=False,
#     )
#
#     email = models.EmailField(
#         null=False,
#         blank=False,
#     )
#
#     age = models.PositiveIntegerField(
#         null=False,
#         blank=False,
#         validators=[MinValueValidator(MIN_AGE_REQUIREMENT),],
#         help_text="Age requirement: 21 years and above."
#     )
#
#     password = models.CharField(
#         max_length=MAX_PASSWORD_LENGTH,
#         null=False,
#         blank=False,
#     )
#
#     first_name = models.CharField(
#         max_length=MAX_FIRST_NAME_LENGTH,
#         null=True,
#         blank=True,
#     )
#
#     last_name = models.CharField(
#         max_length=MAX_LAST_NAME_LENGTH,
#         null=True,
#         blank=True,
#     )
#
#     profile_picture = models.ImageField(
#         null=True,
#         blank=True,
#     )

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

# from exam_music_app.profiles.validators import validate_username


def validate_username(username):  # IF we use it from validators.py we should remove this code
    is_valid = all(ch.isalnum() or ch == '_' for ch in username)

    if not is_valid:
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 15

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_USERNAME_LENGTH),
            # validate_username, # -> ADDING THIS IF WE USE THE VALIDATOR FROM OUR validators.py
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
