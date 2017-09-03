from django.utils import timezone
from haystack import indexes
from .models import Product
import datetime


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(date_upload__lte=datetime.datetime.now())
