from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record, Complaint, Customer
from django.core.paginator import Paginator
from .forms import AddCustomerForm, AddRecordForm, AddComplaintForm

# Вход/Домашняя страница
def home(request):
    records = Record.objects.all()

    # Если пользователь входит в систему
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Аутентификация
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "При входе произошла ошибка, попробуйте еще раз")
            return redirect('home')
    else:
        return render(request, 'home.html', { 'records': records })

# Выход из системы
def logout_user(request):
    logout(request)
    messages.success(request, "Вы вышли из системы")
    return redirect('home')

# Клиенты
def customer(request):
    customers = Customer.objects.all().order_by('id').values()
    return render(request, 'customer.html', { 'customers': customers })

def customer_info(request, pk):
    if request.user.is_authenticated:
        customer_info = Customer.objects.get(id=pk)
        return render(request, 'customer_info.html', { 'customer_info': customer_info })
    else:
        messages.success(request, "Вы должны войти в систему, чтобы просмотреть эту страницу")
        return redirect('home')

def delete_customer(request, pk):
    if request.user.is_authenticated:
        delete_it = Customer.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Клиент успешно удален")
        return redirect('customer')
    else:
        messages.success(request, "Вы должны войти в систему, чтобы просмотреть эту страницу")
        return redirect('home')

def add_customer(request):
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_customer= form.save()
                messages.success(request, "Клиент добавлен")
                return redirect('customer')
        return render(request, 'add_customer.html', { 'form':form })
    else:
        messages.success(request, "Вы должны войти в систему, чтобы просмотреть эту страницу")
        return redirect('home')

def update_customer(request, pk):
    if request.user.is_authenticated:
        current_customer = Customer.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=current_customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Клиент успешно обновлен")
            return redirect('customer')
        return render(request, 'update_customer.html', { 'form':form })
    else:
        messages.success(request, "Вы должны войти в систему, чтобы просмотреть эту страницу")
        return redirect('home')

# Обращения
def record(request):
    records = Record.objects.all().order_by('id').values()
    
    # paginator = Paginator(records, 5)  # Number of items per page
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    return render(request, 'record.html', { 'records': records })

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'customer_record.html', { 'customer_record': customer_record })
    else:
        messages.success(request, "Вы должны войти в систему, чтобы просмотреть эту страницу")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Обращение успешно удалено")
        return redirect('record')
    else:
        messages.success(request, "Вы должны войти в систему, чтобы просмотреть эту страницу")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None, user=request.user)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Обращение добавлено")
                return redirect('record')
        return render(request, 'add_record.html', { 'form':form })
    else:
        messages.success(request, "Вы должны войти в систему, чтобы просмотреть эту страницу")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, user=request.user, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Обращение успешно обновлено")
            return redirect('record')
        return render(request, 'update_record.html', { 'form':form })
    else:
        messages.success(request, "Вы должны войти в систему, чтобы просмотреть эту страницу")
        return redirect('home')

# Жалобы
def complaint(request):
    complaints = Complaint.objects.all().order_by('id').values()
    return render(request, 'complaint.html', { 'complaints': complaints })

def customer_complaint(request, pk):
    if request.user.is_authenticated:
        customer_complaint = Complaint.objects.get(id=pk)
        return render(request, 'customer_complaint.html', { 'customer_complaint': customer_complaint })
    else:
        messages.success(request, "Вы должны войти в систему, чтобы просмотреть эту страницу")
        return redirect('home')

def delete_complaint(request, pk):
    if request.user.is_authenticated:
        delete_it = Complaint.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Жалоба успешно удалена")
        return redirect('complaint')
    else:
        messages.success(request, "Вы должны войти в систему, чтобы просмотреть эту страницу")
        return redirect('home')

def add_complaint(request):
    form = AddComplaintForm(request.POST or None, user=request.user)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_complaint = form.save()
                messages.success(request, "Жалоба добавлена")
                return redirect('complaint')
        return render(request, 'add_complaint.html', { 'form':form })
    else:
        messages.success(request, "Вы должны войти в систему, чтобы просмотреть эту страницу")
        return redirect('home')

def update_complaint(request, pk):
    if request.user.is_authenticated:
        current_complaint = Complaint.objects.get(id=pk)
        form = AddComplaintForm(request.POST or None, user=request.user, instance=current_complaint)
        if form.is_valid():
            form.save()
            messages.success(request, "Обращение успешно обновлено")
            return redirect('complaint')
        return render(request, 'update_complaint.html', { 'form':form })
    else:
        messages.success(request, "Вы должны войти в систему, чтобы просмотреть эту страницу")
        return redirect('home')
