from django.shortcuts import render, redirect
from .models import Expenses
from django.db.models import Q


def index(request):
    somedata = 'HI THERE'
    return render(request, 'budget/index.html', context={'data': somedata})


# VIEW Budgets
def budget_list(request):
    budget_list = Expenses.objects.all()
    return render(request, 'budget/budget_list.html', context={'budget_data': budget_list})


# VIEW Budget
def budget_detail(request, budget_index):
    budget_to_view = Expenses.objects.get(pk=budget_index)
    return render(request, 'budget/budget_detail.html', context={'budget': budget_to_view})

# CREATE budget
def budget_add(request):
    new_expense = Expenses()
    if request.method == 'POST':
       
        new_expense.title = request.POST['title']
        new_expense.amount = request.POST['amount']
        new_expense.category = request.POST['category']
        new_expense.description = request.POST['description']
        new_expense.date_added = request.POST['date_added']
        new_expense.date_completed = request.POST['date_completed']
        new_expense.save()
        return redirect('list')
    return render(request, 'budget/add_budget.html', context={'budget':new_expense})


# UPDATE BUDGET
def budget_update(request, budget_index):
    budget_to_update = Expenses.objects.get(pk=budget_index)

    if request.method == 'POST':
        budget_to_update.title = request.POST['title']
        budget_to_update.amount = request.POST['amount']
        budget_to_update.description=request.POST['description']
        budget_to_update.category=request.POST['category']
        budget_to_update.date_added=request.POST['date_added']
        budget_to_update.date_completed=request.POST['date_completed']
        budget_to_update.save()
        return redirect('list')
    return render(request, 'budget/update_budget.html',context={'budget':budget_to_update})


# DELETE BUDGET
def budget_delete(request, budget_index):
    budget_to_delete = Expenses.objects.get(pk=budget_index)
    if request.method == 'POST':
        budget_to_delete.delete()
        return redirect('list')
    return render(request, 'budget/delete_budget.html', context={'budget': budget_to_delete})



# Existing views...

def search(request):
    query = request.GET.get('q', '')
    if query:
        budgets = Expenses.objects.filter(
            Q(title__icontains=query) |
            Q(category__icontains=query) |
            Q(description__icontains=query) |
            Q(date_added__icontains=query) |
            Q(date_completed__icontains=query) |
            Q(amount__icontains=query)
        )
    else:
        budgets = Expenses.objects.none()

    return render(request, 'budget/search.html', {'budgets': budgets})



