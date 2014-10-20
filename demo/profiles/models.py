from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    greatest_fear = models.CharField(
        blank=True,
        null=True,
        max_length=100,
    )
    home = models.TextField(
        blank=True,
        null=True,
    )

    def get_short_name(self):
        return self.user

    def get_absolute_url(self):
        return reverse('profile-detail', args=[str(self.user.slug)])

    def __unicode__(self):
        return unicode(self.get_short_name())