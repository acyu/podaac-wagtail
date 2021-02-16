from django.http import HttpResponse, JsonResponse
from apps.datasets_browse.models import DatasetsBrowseSettings

#dataset browse api call
def datasets_browse_cmr_query(request, include_facets=False, provider=[], query_parameters=[], format='json'):
   datasets_browse_settings = DatasetsBrowseSettings.for_request(request)
   return datasets_browse_settings.cmr_query