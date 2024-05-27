# views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, PropertyForm
from .models import UserProfile, Property, InterestedBuyer, PropertyLike

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, phone_number=form.cleaned_data['phone_number'], is_seller=form.cleaned_data['is_seller'])
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def seller_property_list(request):
    user_profile = UserProfile.objects.get(user=request.user)
    properties = Property.objects.filter(seller=user_profile)
    return render(request, 'seller_property_list.html', {'properties': properties})

@login_required
def add_property(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.is_seller:
        if request.method == 'POST':
            form = PropertyForm(request.POST)
            if form.is_valid():
                property = form.save(commit=False)
                property.seller = user_profile
                property.save()
                return redirect('seller_property_list')
        else:
            form = PropertyForm()
        return render(request, 'add_property.html', {'form': form})
    else:
        return redirect('property_list')

def property_list(request):
    properties = Property.objects.all()
    paginator = Paginator(properties, 10)  # Show 10 properties per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    for property in page_obj:
        property.like_count = PropertyLike.objects.filter(property=property).count()

    return render(request, 'property_list.html', {'page_obj': page_obj})

@login_required
def interested_property(request, property_id):
    user_profile = UserProfile.objects.get(user=request.user)
    property = Property.objects.get(id=property_id)
    InterestedBuyer.objects.create(buyer=user_profile, property=property)

    # Send email to buyer
    buyer_email = user_profile.user.email
    seller_name = property.seller.user.get_full_name()
    seller_email = property.seller.user.email
    seller_phone = property.seller.phone_number
    subject = 'Property Details'
    message = f'You have shown interest in the property listed by {seller_name}. Here are their contact details:\n\nEmail: {seller_email}\nPhone: {seller_phone}'
    send_mail(subject, message, 'noreply@example.com', [buyer_email])

    # Send email to seller
    buyer_name = user_profile.user.get_full_name()
    buyer_email = user_profile.user.email
    buyer_phone = user_profile.phone_number
    subject = 'Interested Buyer'
    message = f'{buyer_name} has shown interest in your property located at {property.place}. Here are their contact details:\n\nEmail: {buyer_email}\nPhone:{buyer_phone}'
    send_mail(subject, message, 'noreply@example.com', [property.seller.user.email])

    return render(request, 'seller_details.html', {'seller': property.seller})

@login_required
def like_property(request, property_id):
    user_profile = UserProfile.objects.get(user=request.user)
    property = Property.objects.get(id=property_id)

    try:
        like = PropertyLike.objects.get(buyer=user_profile, property=property)
        like.delete()
    except PropertyLike.DoesNotExist:
        PropertyLike.objects.create(buyer=user_profile, property=property)

    return redirect('property_list')

def home(request):
    return render(request, 'home.html')
from django.contrib.auth.views import LoginView

def login_view(request):
    return render(request,'login.html')

