from .models import Contact_company


def Context_processor(request):
    # Getting Contact Info of a Company
    data = Contact_company.objects.first()  # Assuming there's only one contact info entry  
    return {'companydetails': data}