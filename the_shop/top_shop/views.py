from django.shortcuts import render, redirect
from theorders.models import Order, Comment
from .forms import MessageForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User

# ToDo: 
 #    Create a separate file for such funcs
#       implement func across...already tested
def getTotalCurtItems(user: str):
    order, created = Order.objects.get_or_create(user=user, complete=False)
    return order.get_cart_items


def home(request):
    # # Get the latest shoes for each brand
    # latest_shoes = Product.objects.filter(
    #     brand=OuterRef('brand')
    # ).order_by('-shoe_time_added')
    #
    # # Get the distinct brands with their latest shoes
    # distinct_brands_with_latest_shoes = Product.objects.filter(
    #     shoe_time_added__lte=datetime.now(),  # To avoid future timestamps if any
    # ).annotate(
    #     latest_shoe_id=Subquery(latest_shoes.values('id')[:1])
    # ).values('latest_shoe_id')
    #
    # # Fetch the final queryset with the latest shoes for each brand
    # popular_products = Product.objects.select_related('brand').filter(id__in=distinct_brands_with_latest_shoes.values('latest_shoe_id'))
    shop_testimonies = Comment.objects.all()
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'home-shop.html', {"order": order, "shop_testimonies": shop_testimonies})
    else:
        return render(request, 'home-shop.html', {"shop_testimonies": shop_testimonies})


def about(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'about-shop.html', {"order": order})
    else:
        return render(request, 'about-shop.html')


def contacts(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            name = "Zebbylion"
            form.save()

            template = render_to_string('message_added_email.html', {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "name": name,
                "message": message
            })
            sent_email = EmailMessage(
                'New message from Top Gz users',
                template,
                settings.EMAIL_HOST_USER,
                ['zebbynjau@gmail.com']
            )
            sent_email.fail_silently = False
            sent_email.send()
            # Email to be sent to message sender
            template2 = render_to_string('message_sent_email.html', {
                "first_name": first_name,
                "message": message,
                "email": email
            })
            sent_email2 = EmailMessage(
                'Your message has been received',
                template2,
                settings.EMAIL_HOST_USER,
                [email]
            )
            sent_email2.fail_silently = False
            sent_email2.send()
            return redirect('introPage:home-page')
    else:
        form = MessageForm()
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'contacts.html', {"order": order, "form": form})
    else:
        return render(request, 'contacts.html', {"form": form})


def team(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user=customer, complete=False)
        return render(request, 'team.html', {"order": order})
    else:
        return render(request, 'team.html')


# def testimonies(request):
#     shop_testimonies = Comment.objects.all()
#     return render(request, 'testimonies.html', {"shop_testimonies": shop_testimonies})
