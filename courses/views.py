from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Group
from django.utils import timezone
from .utils import redistribute_groups


def find_group_to_add_user(groups):
    available_groups = [group for group in groups if group.students.count() < group.max_users]
    if available_groups:
        return available_groups[0]
    else:
        return None

def distribute_users_to_groups(product_id, user_id):
    product = Product.objects.get(id=product_id)
    groups = Group.objects.filter(product=product)

    total_groups = groups.count()
    total_users = product.users.count()
    users_per_group = total_users // total_groups

    if product.start_date < timezone.now():
        redistribute_groups(groups, total_users, users_per_group)

    group_to_add_user = find_group_to_add_user(groups)

    group_to_add_user.students.add(user_id)
    group_to_add_user.save()

    return HttpResponse("Пользователь успешно добавлен в группу")

def distribute_users_to_groups_view(request):
    product_id = request.POST.get('product_id')
    user_id = request.POST.get('user_id')

    distribute_users_to_groups(product_id, user_id)

    return HttpResponse("Пользователь успешно добавлен в группу")
