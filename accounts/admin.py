from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'address')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    list_filter = ('birth_date',)
    readonly_fields = ('user',)
    fieldsets = (
        (None, {
            'fields': ('user', 'birth_date', 'address', 'profile_picture'),
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('user',)
        return self.readonly_fields


admin.site.register(Profile, ProfileAdmin)
