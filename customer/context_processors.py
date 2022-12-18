from owner.models import Carts
def cart_count(request): #take request as arg and return a dict
    cnt=Carts.objects.filter(status="in-cart").count()
    return {"cnt":cnt}  #we can access this dict in all templates



