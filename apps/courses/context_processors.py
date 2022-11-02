from .models import Banner


def banner(request):
    return {"course_page_banner": Banner.load()}
