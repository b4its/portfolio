from django.shortcuts import render

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def indexe(request):
    return render(request, 'index.html')

def stone(request):
    return render(request, 'stone.html')