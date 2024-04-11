import colorsys

from django.shortcuts import render, redirect

from palette.models import UserColors


def hsl_to_hex(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h / 360.0, l / 100.0, s / 100.0)
    hex_color = "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255),
                                             int(b * 255))
    return hex_color


def save_color(request):
    if request.method == 'POST':
        print(request.POST)
        print("request.POST")
        hue = request.POST.get("hue")
        satturation = request.POST.get("satturation")
        lightness = request.POST.get("lightness")
        hex = hsl_to_hex(int(hue), int(satturation), int(lightness))
        print(hex, int(hue), int(satturation), int(lightness))
        UserColors.objects.create(
            hue=hue,
            user=request.user,
            sat=satturation,
            lightness=lightness,
            hex=hex
        )
    return redirect('color_list')


def save_color1(request):
    if request.method == 'POST':
        print(request.POST)
        print("request.POST")
        red = request.POST.get('red')
        green = request.POST.get('green')
        blue = request.POST.get('blue')
        hsl = rgb_to_hsl(int(red), int(green), int(blue))
        hex = hsl_to_hex(hsl[0], hsl[1], hsl[2])
        print(red, green, blue)
        UserColors.objects.create(
            hue=hsl[0],
            user=request.user,
            sat=hsl[1],
            lightness=hsl[2],
            hex=hex
        )
    return redirect('color_list')


def hsl_to_hex(h, s, l):
    h /= 360
    s /= 100
    l /= 100
    if s == 0:
        r = g = b = l
    else:
        def huetorgb(p, q, t):
            if t < 0:
                t += 1
            if t > 1:
                t -= 1
            if t < 1 / 6:
                return p + (q - p) * 6 * t
            if t < 1 / 2:
                return q
            if t < 2 / 3:
                return p + (q - p) * (2 / 3 - t) * 6
            return p

        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = huetorgb(p, q, h + 1 / 3)
        g = huetorgb(p, q, h)
        b = huetorgb(p, q, h - 1 / 3)

    return "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))



def rgb_to_hsl(r, g, b):
    r /= 255
    g /= 255
    b /= 255

    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin

    l = (cmax + cmin) / 2

    if delta == 0:
        h = 0
        s = 0
    else:
        if l < 0.5:
            s = delta / (cmax + cmin)
        else:
            s = delta / (2 - cmax - cmin)

        if cmax == r:
            h = (g - b) / delta + (6 if g < b else 0)
        elif cmax == g:
            h = (b - r) / delta + 2
        else:
            h = (r - g) / delta + 4

        h /= 6

    return h * 360, s * 100, l * 100


print
