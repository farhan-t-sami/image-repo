import django_filters
from upload.models import Images

class TypeFilter(django_filters.FilterSet):
    class Meta:
        model = Images
        fields = ['image_type']

    # Overrides the default empty placeholder to 'All'
    def __init__(self, *args, **kwargs):
        super(TypeFilter, self).__init__(*args, **kwargs)
        self.filters['image_type'].extra.update(
            {'empty_label': 'All'})