from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from App1.models import *
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.views.decorators.http import require_http_methods
import json

# Create your views here.
def test1(request):
    return HttpResponse("Hello, this is test1")

def add_data(request):
    # 创建用户
    user1 = Users.objects.create(username='john', email='john@example.com', password='password123')
    user2 = Users.objects.create(username='admin', email='admin@example.com', password='password123', is_staff=True)

    # 创建书籍
    book1 = Books.objects.create(title='Book One', author='Author A', isbn='1234567890123', price=19.99)
    book2 = Books.objects.create(title='Book Two', author='Author B', isbn='9876543210987', price=29.99)

    # 创建订单
    order1 = Orders.objects.create(user_id=user1, status='Pending')

    # 创建订单详情
    OrdersDetails.objects.create(order_id=order1, book_id=book1, quantity=2, price=19.99)
    OrdersDetails.objects.create(order_id=order1, book_id=book2, quantity=1, price=29.99)
    return HttpResponse("Hello, this is add_data")


def add_books(request):
    import time
    time.sleep(5)
    Books.objects.create(title='Book Three', author='Author C', isbn='123456789065', price=19.89)
    return HttpResponse("Hello, this is add_books")


@csrf_exempt
# @require_http_methods(['POST'])
def task1_u(request):
    if request.method == 'POST':
        try:
            data=json.loads(request.body)
            print(data)
            id=data.get("id")
            username=data.get("username")
            email=data.get("email")
            password=data.get("password")
            # is_staff=data.get('is_staff')
            Users.objects.create(id=id,username=username,email=email,password=password)
            return JsonResponse({'message': 'Data inserted successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': 'An error occurred', 'details': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
# @require_http_methods(['POST'])
def task2(request):
    all_book_info=Books.objects.all()
    # print(all_book_info)
    lis=[]
    for b in all_book_info:
        data={
            "id":b.id,
            "title":b.title,
            "author":b.author,
            "price":b.price,
            "publish_date":b.publish_date
            }
        lis.append(data)
    return JsonResponse({'books': lis}, status=200)


@csrf_exempt
# @require_http_methods(['POST'])
def task3(request):
    u_name=request.GET.get("name")
    u_id=Users.objects.filter(username=u_name)[0].id
    o_lis=Orders.objects.filter(user_id=u_id)
    print(o_lis)
    return HttpResponse("Hello, this is task3")
    
    
@csrf_exempt
# @require_http_methods(['POST'])
def task3_2(request):
    b_name=request.GET.get("name")
    if Books.objects.filter(title=b_name).exists():
        Books.objects.filter(title=b_name).delete()
        return HttpResponse("Hello, this is task3_2")
    else:
        return HttpResponse("No such book")
    
    


