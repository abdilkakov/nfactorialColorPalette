import colorsys
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from palette.models import PopularColor, UserColors


def index(request):
    return redirect('register')


def register(request):
    if request.method == 'POST':
        print(request.POST)
        print("request.POST")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        return redirect('login')
    return render(request, 'registration.html')


def profile_view(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


def hsl_to_rgb(h, s, l):
    h /= 360.0
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    rgb_hex = "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255),
                                           int(b * 255))
    return rgb_hex


def color_box_view(request):
    popular_colors = PopularColor.objects.filter(is_active=True)
    for p in popular_colors:
        p.color = hsl_to_rgb(h=p.hue, s=0.5, l=0.5)
    return render(request, "choose-color.html",
                  {
                      "popular_colors": popular_colors,
                      "page_name": "choose"
                  })


def color_box_view1(request):
    user_colors = UserColors.objects.filter(user=request.user)
    for t in user_colors:
        t.color = hsl_to_rgb(h=t.hue, s=t.sat, l=t.lightness)
    return render(request, "saved-colors.html",
                  {"user_colors": user_colors, "page_name": "usercolors"})


def generate_new_color(request, pk):
    user_color = UserColors.objects.filter(id=pk).first()

    return render(request, 'color-change.html', {'user_color': user_color})


def color_mix(request):
    return render(request, 'color-mix.html')
