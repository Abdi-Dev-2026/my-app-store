from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, DownloadRequest, UserPoints, Favorite
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib.auth.models import User

# Home Page - Show all products with search & category filter
def home(request):
    products = Product.objects.all()

    # Search functionality
    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query)

    # Category filter
    category = request.GET.get('category')
    if category:
        products = products.filter(category=category)

    return render(request, 'home.html', {
        'products': products,
        'query': query,
        'selected_category': category
    })

# Product detail view
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    is_approved = False

    if request.user.is_authenticated:
        is_approved = DownloadRequest.objects.filter(
            user=request.user, 
            product=product, 
            status='approved'
        ).exists()

    return render(request, 'detail.html', {
        'product': product, 
        'is_approved': is_approved
    })

# Request download (Payment or Points)
@login_required
def request_download(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        phone = request.POST.get('phone')
        DownloadRequest.objects.create(
            user=request.user,
            product=product,
            phone_number=phone
        )
        return render(request, 'payment_success.html', {'product': product})

    return render(request, 'payment.html', {'product': product})

# User's purchased apps
@login_required
def my_apps(request):
    approved_requests = DownloadRequest.objects.filter(
        user=request.user,
        status='approved'
    ).select_related('product')

    total_spent = approved_requests.aggregate(total=Sum('product__price'))['total'] or 0
    
    user_points = int(total_spent * 10) 
    balance = user_points * 0.01 

    return render(request, 'my_apps.html', {
        'requests': approved_requests,
        'user_points': user_points,
        'balance': balance
    })

# Buy product with points
@login_required
def buy_with_points(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user_points, created = UserPoints.objects.get_or_create(user=request.user)

    cost_points = int(product.price * 100) 

    if user_points.points >= cost_points:
        user_points.points -= cost_points
        user_points.save()

        DownloadRequest.objects.create(
            user=request.user,
            product=product,
            phone_number="Wallet/Points",
            status='approved'
        )
        return redirect('my_apps')
    else:
        return redirect('product_detail', id=product.id)

# Toggle Favorite
@login_required
def toggle_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    fav, created = Favorite.objects.get_or_create(user=request.user, product=product)
    if not created:
        fav.delete()
    return redirect(request.META.get('HTTP_REFERER', 'home'))

# View user's favorites
@login_required
def my_favorites(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('product')
    return render(request, 'favorites.html', {'favorites': favorites})

# Admin Dashboard
@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('home')

    total_earnings = DownloadRequest.objects.filter(status='approved').aggregate(Sum('product__price'))['product__price__sum'] or 0
    total_users = User.objects.count()
    total_downloads = DownloadRequest.objects.filter(status='approved').count()

    return render(request, 'admin_dashboard.html', {
        'total_earnings': total_earnings,
        'total_users': total_users,
        'total_downloads': total_downloads
    })