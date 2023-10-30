from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Master, MasterAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(MasterRating, MasterRatingAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Article, ArticleAdmin)