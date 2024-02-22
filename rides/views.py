from django.shortcuts import render

from .models import Person

# relative import of forms
from .forms import RideForm

# Create your views here.
def about(request):
    # Your logic here
    return render(request, 'about.html')

def index(request):

  context = {}
  
  # Initialize variables for city and state searches
  search_city_origin = request.GET.get('search_origin', '').strip()
  search_city_destination = request.GET.get('search_destination', '').strip()
  search_state = request.GET.get('searchstate', '').strip().upper()  # Convert to uppercase for case insensitivity
    
  # If either city or state search is provided, filter the Person objects

  if search_city_origin or search_city_destination or search_state:

     # Start with all Person objects
    queryset = Person.objects.all()
        
    # Filter by city if search_city is provided
    if search_city_origin:
      queryset = queryset.filter(origination__icontains=search_city_origin) 
    
    if search_city_destination:
      queryset = queryset.filter(destination_city__icontains=search_city_destination)
        
  
    # Filter by state if search_state is provided
    if search_state:
      queryset = queryset.filter(destination_state__iexact=search_state)
        
    # Update the context with the filtered queryset
    context['people'] = queryset


  '''
  if "search" in request.GET or "search2" in request.GET:

    # Get the city and remove white spaces
    search = request.GET.get('search', '').strip()

    # Get the state and remove white spaces, convert to upper case
    search2 = request.GET.get('search2', '').strip().upper()

    people = Person.objects.all()

    # Search by city if given
    if search:
      people = people.filter(destination_city__icontains=search)

    # Search by state if given
    if search2:
      people = people.filter(destination_state__icontains=search2)

    context['people'] = people 
  '''
  
  '''
  if "search" in request.GET:
    search = request.GET["search"]

    context["people"] = Person.objects.filter(
        origination__icontains=search) | Person.objects.filter(destination_city__icontains=search)

  if "searchstate" in request.GET:
    search2 = request.GET['searchstate'].upper()

    context["people"] = Person.objects.filter(
        destination_state__icontains=search2)

  '''


  context["form"] = RideForm()

  return render(request, "index_view.html", context)