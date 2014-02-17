from django.contrib import admin
from models import JsonEndpoint
import reversion

class JsonEndpointAdmin(reversion.VersionAdmin):
	model = JsonEndpoint
	readonly_fields = ('slug',)

admin.site.register(JsonEndpoint, JsonEndpointAdmin)
