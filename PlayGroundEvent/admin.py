from pyexpat.errors import messages

from django.contrib import admin
from PlayGroundEvent.models import Company, Ticket, Event
from django.contrib import messages




class ticket_admin(admin.ModelAdmin):
    list_display = ('vip', 'user', 'number')
    list_filter = ['vip']
    search_fields = ('event__title', 'event__user')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    def get_username(self, obj: Ticket):
        username = getattr(obj.user)

    def save_model(self, request, obj, form, change):
        if form.cleaned_data["ticket_count"] < form.initial["ticket_count"]:
            messages.warning(
                request,
                f"Ticket count should be greater than initial value, so we set it to {form.initial['ticket_count']}",
            )
        super().save_model(request, obj, form, change)



admin.site.register(Ticket, ticket_admin)
admin.site.register(Company)






