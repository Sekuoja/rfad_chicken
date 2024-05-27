from django.contrib import admin
from rfad.models import Race
from django.utils.safestring import mark_safe


@admin.register(Race)
class AdminRace(admin.ModelAdmin):
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f"<img src='{obj.art.url}'>")


admin.site.site_header = "RfadAdmin"

admin.site.site_title = "Врата балдура"

admin.site.index_title = "Добро пожаловать в царство Шеогората"