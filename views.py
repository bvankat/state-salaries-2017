from models import *
from django.shortcuts import *
from django.db.models import *
from salaries2017.models import *
from django.http import HttpResponse

CURRENT_FISCAL = 2017
all = Salary.objects.all().order_by('-gross_pay')
agencies = Agency.objects.all().order_by('agency_name')
allcount = all.count()
    
def Main(request):
    top10 = all[:10]
    agencycount = agencies.count()
    topagencies = Agency.objects.order_by('-grand_total')[:10]
    agencysort = agencies.order_by('-grand_total')
    dictionaries = {'allcount':allcount, 'top10':top10, 'agencies': agencies, 'agencycount': agencycount, 'agencysort': agencysort, 'topagencies':topagencies, 'CURRENT_FISCAL':CURRENT_FISCAL,}
    return render_to_response('salaries2017/main.html', dictionaries)
    
def AgencyPage(request, company):
    agency = Agency.objects.get(agency_code=company)
    people = all.filter(agency_code=company)
    count = people.count()
    top100 = people[:100]
    dictionaries = { 'agency': agency, 'people':people, 'count': count, 'top100':top100, 'agencies':agencies, 'allcount':allcount,'CURRENT_FISCAL':CURRENT_FISCAL,}
    return render_to_response('salaries2017/agency.html', dictionaries)
    
def PersonPage(request, id, name_slug):
    person = Salary.objects.get(id=id, name_slug=name_slug)
    dictionaries = { 'person': person, }
    return render_to_response('salaries2017/person.html', dictionaries)
    
def Search(request):
    query = request.GET.get('q', '')
    exploded = query.split(" ")
    q_objects = Q()
    for term in exploded:
        q_objects &= Q(full_name__icontains=term)

    if query:
        qset = (
            q_objects
        )
        results = Salary.objects.filter(qset).order_by('last_name', '-gross_pay')
    else:
        results = []

    dictionaries = { 'results': results, 'query': query, 'agencies':agencies, 'allcount':allcount,}
    return render_to_response('salaries2017/search.html', dictionaries)
    
def About(request):
    MINUS_ONE = int(CURRENT_FISCAL) - 1
    dictionaries = {'agencies':agencies, 'allcount':allcount,'CURRENT_FISCAL':CURRENT_FISCAL, 'MINUS_ONE':MINUS_ONE,}
    return render_to_response('salaries2017/about.html', dictionaries)

def Maint(request):
    return render_to_response('salaries2017/maint.html')
