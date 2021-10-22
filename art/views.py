from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    get_list_or_404,
    HttpResponse,
    reverse,
)
from chat.models import Message, Artist
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
from chat.views import (
    chatSend,
    get_ip,
    numberOfMessages,
    chatMessages,
    addNewMessage,
)
from .forms import ArtForm
from .models import Art
from chat.models import Message, Artist


# error handling
def error_404(request, exception):
    return render(request, "404.html", status=404)


def error_500(request):
    return render(request, "500.html", status=500)


def art(request):
    """
    this view will load the home page with the art for sale shown
    remove old messages if ip not in session for that ip so chatbox
    is new everytime user accesses site
    """
    if "ip_address" not in request.session:
        ip = get_ip(request)
        if Message.objects.filter(chat_session=ip).exists():
            Message.objects.filter(chat_session=ip).delete()

    artCollection = Art.objects.all()
    context = {"artCollection": artCollection}
    return render(request, "art.html", context)


def addArt(request):
    """
    This view will give the artist a form to add a new piece of art
    to sell on a get request. When the view recieves a post request
    it will add the new art to the database and redirect to the home page
    """
    if request.method == "POST":
        form = ArtForm(request.POST, request.FILES)
        if form.is_valid():
            art = form.save()
            messages.success(request, "Art added")
            return redirect("art")
    else:
        form = ArtForm()
        context = {
            "form": form,
        }
        return render(request, "artAdd.html", context)


def editArt(request, id):
    """
    This view will allow the artist to edit a current art piece
    """
    art = get_object_or_404(Art, pk=id)

    if request.method == "POST":
        form = ArtForm(request.POST, request.FILES, instance=art)
        if form.is_valid():
            form.save()
            messages.success(request, "Art details updated.")
            return redirect("art")
        else:
            messages.error(
                request, "Issue updating art piece, please try again later."
            )
            return redirect("art")

    else:
        form = ArtForm(instance=art)
        context = {
            "form": form,
            "id": id,
        }
        return render(request, "artEdit.html", context)


def deleteArt(request, id):
    """
    This view allows an artist to delete an art piece from the home page
    """
    art = get_object_or_404(Art, pk=id)
    art.delete()
    messages.success(request, "Art piece deleted")
    return redirect(reverse("art"))


def artDetails(request, id):
    """
    This view renders the art piece in more detail
    """
    art = get_object_or_404(Art, pk=id)
    context = {
        "art": art,
    }
    return render(request, "artDetails.html", context)
