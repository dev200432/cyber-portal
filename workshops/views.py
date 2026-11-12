import resend
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from .forms import WorkshopRegistrationForm
from .models import Workshop

resend.api_key = settings.RESEND_API_KEY

def workshop_list(request):
    workshops = Workshop.objects.all().order_by('date')
    return render(request, 'workshops/index.html', {'workshops': workshops})

def register_workshop(request, workshop_id):
    workshop = get_object_or_404(Workshop, id=workshop_id)
    
    if request.method == 'POST':
        form = WorkshopRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.workshop = workshop
            registration.save()
            
            
            try:
                params = {
                    "from": "Cyber Security Portal <onboarding@resend.dev>",
                    "to": [registration.email],
                    "subject": f"Registration Confirmed: {workshop.title}",
                    "html": f"""
                        <div style="font-family: Arial, sans-serif; padding: 20px; color: #333;">
                            <h2>Badhai ho, {registration.full_name}!</h2>
                            <p>Aapka registration <strong>{workshop.title}</strong> ke liye successfully ho gaya hai.</p>
                            <p><strong>Workshop Date:</strong> {workshop.date}</p>
                            <p><strong>Speaker:</strong> {workshop.speaker}</p>
                            <br>
                            <p>Regards,<br><strong>Cyber Security Team</strong></p>
                        </div>
                    """
                }
                resend.Emails.send(params)
            except Exception as e:
                print(f"Email error: {e}")
                
            return redirect('workshop_success', registration_id=registration.id)
    else:
        form = WorkshopRegistrationForm()
        
    return render(request, 'workshops/register.html', {'form': form, 'workshop': workshop})

def workshop_success(request, registration_id):
    return render(request, 'workshops/success.html', {'registration_id': registration_id})