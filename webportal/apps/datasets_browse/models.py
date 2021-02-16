from django.db import models
from django.core.validators import ValidationError
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList, FieldPanel
# Register your models here.

@register_setting
class DatasetsBrowseSettings(BaseSetting):
   cmr_query = models.URLField(
      help_text="CMR Query API Endpoint",
      verbose_name="CMR Query API",
      blank=True
   )
   cmr_services = models.URLField(
      help_text="CMR Services Query API Endpoint",
      verbose_name="CMR Services API",
      blank=True
   )
   cmr_auth = models.URLField(
      help_text="CMR URS Authenticate API Endpoint",
      verbose_name="CMR Authentication API",
      blank=True
   )
   cmr_auth_enable = models.BooleanField(
      help_text="CMR Authentication On/Off Switch",
      verbose_name="Enable CMR Authentication",
      default=False
   )

   cmr_query_panel = [
      FieldPanel("cmr_query"),
      FieldPanel("cmr_services"),
   ]
   cmr_auth_panel = [
      FieldPanel("cmr_auth"),
      FieldPanel("cmr_auth_enable"),
   ]

   edit_handler = TabbedInterface([
      ObjectList(cmr_query_panel, heading="CMR Query Settings"),
      ObjectList(cmr_auth_panel, heading="CMR URS Settings"),
   ])

   # def clean(self):
   #    if self.cmr_auth_enable and self.cmr_auth == '':
   #       msg = BaseSetting.ValidationError("CMR URS Authentication API Endpoint is required.")
   #       self.add_error(field, msg)

   #    return self

   # def fields_required(self, fields):
   #    """Used for conditionally marking fields as rquired"""
   #    #cleaned_data = super().clean()
   #    for field in fields:
   #       print(self.field)
   #       if not self[field, '']:
   #          msg = forms.ValidationError("CMR URS Authentication API Endpoint is required.")
   #          self.add_error(field, msg)