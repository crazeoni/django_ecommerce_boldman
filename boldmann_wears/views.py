from django.shortcuts import render
from boldmann_wears.models import Bolducts, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
#from django.views.generic import View
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from boldmann_wears.forms import BolductsForm

# Create your views here.
def home(request):
	return render(request, 'boldmann_wears/home.html')

class HomeView(ListView):
	model = Bolducts
	extra_context={'boots': Bolducts.objects.filter(category='Boots')}
	template_name = "boldmann_wears/product_listing.html"

class ProductView(DetailView):
    model = Bolducts
    template_name = "boldmann_wears/product.html"

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object' : order
            }
            return render(self.request, 'boldmann_wears/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("/")


@login_required	
def products(request):
	shoes = Bolducts.objects.all().order_by('-date_added')
	context = {'shoes': shoes}
	return render(request, 'boldmann_wears/product_listing.html', context)

# def product_overview(request, product_id):
	# shoes = Bolducts.objects.get(id=product_id)
	# context = {'shoes': shoes}
	# return render(request, 'boldmann_wears/product_overview.html', context)

@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Bolducts, pk=pk )
    order_item, created = OrderItem.objects.get_or_create(
        item = item,
        user = request.user,
        ordered = False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Added quantity Item")
            return redirect("boldmann_wears:order_summary")
        else:
            order.items.add(order_item)
            messages.info(request, "Item added to your cart")
            return redirect("boldmann_wears:order_summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item added to your cart")
        return redirect("boldmann_wears:order_summary")

@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(Item, pk=pk )
    order_qs = Order.objects.filter(
        user=request.user, 
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order_item.delete()
            messages.info(request, "Item \""+order_item.item.item_name+"\" remove from your cart")
            return redirect("boldmann_wears:order_summary")
        else:
            messages.info(request, "This Item not in your cart")
            return redirect("boldmann_wears:order_summary")
    else:
        #add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("boldmann_wears:order_summary")


@login_required
def reduce_quantity_item(request, pk):
    item = get_object_or_404(Bolducts, pk=pk )
    order_qs = Order.objects.filter(
        user = request.user, 
        ordered = False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists() :
            order_item = OrderItem.objects.filter(
                item = item,
                user = request.user,
                ordered = False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            messages.info(request, "Item quantity was updated")
            return redirect("boldmann_wears:order_summary")
        else:
            messages.info(request, "This Item not in your cart")
            return redirect("boldmann_wears:order_summary")
    else:
        #add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("boldmann_wears:order_summary")

def boots(request):
	boots = Bolducts.objects.filter(category='Boots')
	context = {'boots': boots}
	return render(request, 'boldmann_wears/boot.html', context)

def monkstrap(request):
	monkstrap = Bolducts.objects.filter(category='Monkstrap')
	context = {'monkstrap': monkstrap}
	return render(request, 'boldmann_wears/monkstrap.html', context)

def loafers(request):
	loafers = Bolducts.objects.filter(category='Loafers')
	context = {'loafers': loafers}
	return render(request, 'boldmann_wears/loafers.html', context)

def brogues(request):
	brogues = Bolducts.objects.filter(category='Brogues')
	context = {'brogues': brogues}
	return render(request, 'boldmann_wears/brogues.html', context)

def leather_slides(request):
	leather_slides = Bolducts.objects.filter(category='Leather slides')
	context = {'leather_slides': leather_slides}
	return render(request, 'boldmann_wears/leather_slides.html', context)

def leather_mules(request):
	leather_mules = Bolducts.objects.filter(category='Leather mules')
	context = {'leather_mules': leather_mules}
	return render(request, 'boldmann_wears/leather_mules.html', context)

def oxfords(request):
	oxfords = Bolducts.objects.filter(category='Oxfords')
	context = {'oxfords': oxfords}
	return render(request, 'boldmann_wears/oxfords.html', context)

def category(request):
	boots = Bolducts.objects.filter(category='Boots')
	monkstrap = Bolducts.objects.filter(category='Monkstrap')
	brogues = Bolducts.objects.filter(category='Brogues')
	leather_slides = Bolducts.objects.filter(category='Leather slides')
	oxfords = Bolducts.objects.filter(category='Oxfords')
	loafers = Bolducts.objects.filter(category='Loafers')
	leather_mules = Bolducts.objects.filter(category='Leather mules')
	context = {'boots': boots, 'monkstrap': monkstrap, 'brogues': brogues, 'leather_slides': leather_slides, 'oxfords': oxfords, 'loafers': loafers, 'leather_mules': leather_mules}
	return render(request, 'boldmann_wears/categories.html', context)


def new_topic(request):
	"""Add a new topic."""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = BolductsForm()
	else:
		# POST data submitted; process data.
		form = BolductsForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('boldmann_wears:products'))
	context = {'form': form}
	return render(request, 'learning_logs/produc_listing.html', context)
