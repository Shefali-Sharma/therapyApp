import pdb
from django.http import HttpResponse
from .serializers import *
from django.http import JsonResponse
import logging

logger = logging.getLogger('main')

def loghttprequest(request):
    logger.debug(" Request received from : " + request.META['REMOTE_ADDR'] + "\tPath: " + request.path)


def index(request):
    """
    Index Page of main app
    :param request: HTTPREQUEST Object
    :return:
    """
    loghttprequest(request)
    #print ("Module name : " + str(__name__))
    responseString = "<h3>API Documentation: </h3>" \
                     "<h4>1. Get all Folders: http://161.85.98.97:8000/main/folders</h4>" \
                     "<h4>2. Get All Videos: http://161.85.98.97:8000/main/videos</h4>" \
                     "<h4>3. Get Children Folders of a folder: http://161.85.98.97:8000/main/children/folder/{parent-id}</h4>" \
                     "<h4>4. Get Children Videos of a folder: http://161.85.98.97:8000/main/children/video/{parent-id}</h4>"
    #pdb.set_trace()
    return HttpResponse(responseString)

def get_all_folders(request):
    """
    To get all folders from current DB
    :param request: HTTPREQUEST Object
    :return: list of folders in JSON Format
    """
    loghttprequest(request)
    folders = Folder.objects.all()
    serializer = FolderSerializer(folders, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_all_videos(request):
    """
    To get all videos from current DB
    :param request: HTTPREQUEST Object
    :return: list of videos in JSON Format
    """
    loghttprequest(request)
    videos = Video.objects.all()
    serializer = VideoSerializer(videos, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_children(request,type,parent):
    """
    Getting children of a folder with id @parent
    :param request:  HTTPREQUEST Object
    :param type: 'video' or 'folder'
    :param parent: parent id of folder
    :return: videos or folders of a parent folder
    """

    loghttprequest(request)

    if  type == 'video':
        videosids = Video_folder_mapping.objects.filter(folder_id=parent)
        videos = Video.objects.filter(video_folder_mapping__folder_id__exact=parent)
        serializer = VideoSerializer(videos, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif type == 'folder':
        folders = Folder.objects.filter(parent_id=parent)
        serializer = FolderSerializer(folders, many=True)
        resultJson =  JsonResponse(serializer.data, safe=False)
        #resultJson['path'] = "Dummy"
        return resultJson
    else:
        return HttpResponse("Unknown type:" + "\t" + type)


def test(request):
    pass