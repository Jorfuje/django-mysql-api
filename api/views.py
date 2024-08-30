from django.http.response import JsonResponse
from django.utils.decorators import method_decorator 
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json

# Create your views here.

class UserView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id = 0):
        if (id > 0):
            users = list(User.objects.filter(id = id).values())
            if len(users) > 0:
                user = users[0]
                datos = {'message': "Success", 'user': user}
            else:
                datos = {'message': "User not found..."}
            return JsonResponse(datos)
        else: 
            users = list(User.objects.values())
            if len(users) > 0:
                datos = {'message': "Success", 'users': users}
            else:
                datos = {'message': "Users not found..."}
            return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        User.objects.create(nombre = jd['nombre'], apellido = jd['apellido'], edad = jd['edad'], email = jd['email'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        users = list(User.objects.filter(id = id).values())
        if len(users) > 0:
            user = User.objects.get(id = id)
            user.nombre = jd['nombre']
            user.apellido = jd['apellido']
            user.edad = jd['edad']
            user.email = jd['email']
            user.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "User not found..."}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        users = list(User.objects.filter(id = id).values())
        if len(users) > 0:
            User.objects.filter(id = id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "User not found..."}
        return JsonResponse(datos)