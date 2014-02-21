from django.contrib import admin
from django.forms import Textarea
from django.db import models

from models import JsonEndpoint
import reversion

class JsonEndpointAdmin(reversion.VersionAdmin):
	model = JsonEndpoint
	readonly_fields = ('slug',)
	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':40, 'cols':200})},
    }


admin.site.register(JsonEndpoint, JsonEndpointAdmin)
