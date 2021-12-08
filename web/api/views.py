import json

from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pytz import unicode

from trans.models import FileUpload



def fileUpload(request):
    if request.method == 'POST':
        num=FileUpload.objects.values_list('title',flat=True)
        num=list(map(int,num))
        num.sort()
        number=num[-1]+1
        print(number)
        title = number
        img = request.FILES["image"]
        fileupload = FileUpload(
            title=title,
            imgfile=img,
        )
        fileupload.save()
        filesend = FileUpload.objects.get(title__contains=number)
        filesend2 = filesend.__dict__


        del(filesend2['_state'])
        filesend2=json.dumps(filesend2)
        return JsonResponse(data=filesend2, status=201,safe=False)
