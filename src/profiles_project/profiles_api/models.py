from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        BaseUserManager)


class UserProfileManager(BaseUserManager):
    """
    Works with custom UserProfile.
    """

    def create_user(self, email, name, password):
        """Create new UserProfile"""
        if not email:
            raise ValueError('User must have an email!')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """
        Create and save superuser.
        """
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Represents a user profile.
    """

    email = models.EmailField(max_length=128, unique=True)
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a user's full name."""
        return self.name

    def get_short_name(self):
        """Used to get a user's full name."""
        return self.name

    def __str__(self):
        """
        String representation of object.
        """
        return self.email
