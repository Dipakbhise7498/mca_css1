from django import template
from farmerapp.models import *
register = template.Library()

@register.simple_tag
def getquantity(obj, bookid, pid):
    print(obj)
    book = Booking.objects.get(id=bookid)
    proid = (book.booking_id).split('.')[1:]
    myindex = proid.index(str(pid))
    li = (book.quantity).split(',')
    print(li)
    return li[myindex]