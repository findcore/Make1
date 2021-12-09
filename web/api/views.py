import json
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pytz import unicode
from trans.models import FileUpload,CropImage

from PIL import Image
from media import img


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

def filecrop(request):
    if request.method == 'POST':
        # print(request.body)
        BODY=json.loads(request.body)
        # print(BODY)
        # print(BODY['bound'])
        simg = Image.open('./media/'+BODY['image'])
        wide2, height2= simg.size
        wide1, height1= BODY['bound']
        ratw=wide2/wide1
        rath=height2/height1
        # print(wide2,height2)
        left, upper, right, height=list(map(int,[BODY['select']['x']*ratw,BODY['select']['y']*rath,BODY['select']['x2']*ratw,BODY['select']['y2']*rath]))
        # print(left,upper,right,height)
        cropimg=simg.crop((left,upper,right,height))
        cropimg.save(output, format='JPEG', quality=85)
        output = io.BytesIO()
        output.seek(0)

        key=FileUpload.objects.last()

        cropobj=CropImage(fileupload=key,imgfile2=cropimg)


        cropobj.save()
