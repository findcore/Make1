import json

from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pytz import unicode

from trans.models import FileUpload



@csrf_exempt
def fileUpload(request):
    if request.method == 'POST':
        title = 45
        img = request.FILES["image"]
        fileupload = FileUpload(
            title=title,
            imgfile=img,
        )
        fileupload.save()
        filesend = FileUpload.objects.get(title__contains=45)
        filesend2 = filesend.__dict__


        del(filesend2['_state'])
        filesend2=json.dumps(filesend2)
        return JsonResponse(data=filesend2, status=201,safe=False)
