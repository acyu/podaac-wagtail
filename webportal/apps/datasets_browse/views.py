from django.shortcuts import render
from apps.datasets_browse.utilities import datasets_browse_cmr_query

# Create your views here.
def datasets_browses_list(request):
   #print(datasets_browse_settings.cmr_query)
   print(datasets_browse_cmr_query(request))
   return render(request, 'datasets_browse/datasets_browse_list.html')

def datasets_browse_dataset(request, dataset_id):
   return render(request, 'datasets_browse/datasets_browse_dataset.html')