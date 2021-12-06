from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from trans.models import FileUpload



@csrf_exempt
def fileUpload(request):
    if request.method == 'POST':
        title = 11
        img = request.FILES["image"]
        fileupload = FileUpload(
            title=title,
            imgfile=img,
        )
        fileupload.save()
        filesend=FileUpload.objects.filter(title__contains=10).first()
        filesend2=model_to_dict(filesend)

        return JsonResponse(data=filesend2, status=201)
