from django.contrib import admin
from django.forms import Textarea
from django.db import models

from models import JsonEndpoint, AuthEndpoint, MockObjectClass, MockObject
import reversion

class JsonEndpointAdmin(reversion.VersionAdmin):
	model = JsonEndpoint
	readonly_fields = ('slug',)
	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':40, 'cols':200})},
    }


class MockObjectAdmin(admin.StackedInline):
    model = MockObject
    extra = 1


class MockObjectClassAdmin(reversion.VersionAdmin):
    model = MockObjectClass
    inlines = [MockObjectAdmin]


admin.site.register(JsonEndpoint, JsonEndpointAdmin)
admin.site.register(AuthEndpoint)
admin.site.register(MockObjectClass, MockObjectClassAdmin)
# admin.site.register(MockObject)
