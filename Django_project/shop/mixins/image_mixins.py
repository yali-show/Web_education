from django.utils.safestring import mark_safe


class ImageChange:
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if type(readonly_fields) is list:
            readonly_fields.append('image_field')
        elif type(readonly_fields) is tuple:
            readonly_fields += ('image_field',)
        return readonly_fields

    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        if type(list_display) is list:
            list_display.insert(0, 'image_field')
        elif type(list_display) is tuple:
            # list_display += ('image_field',)
            list_display = ('image_field',) + list_display
        return list_display

    @mark_safe
    def image_field(self, obj):
        if not obj.image:
            return 'No image'
        return f'<img src="{obj.image.url}" width="64" height="64"/>'

