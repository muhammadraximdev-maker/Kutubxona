from django.shortcuts import render, redirect
from .models import Talaba, Kitob, Muallif, Record, Kutubxonachi

def home_view(request):
    return render(request, 'home.html')


def talabalar_view(request):
    search_query = request.GET.get('search', '')
    sort_param = request.GET.get('sort', 'ism')

    if search_query:
        talabalar = Talaba.objects.filter(ism__icontains=search_query)
    else:
        talabalar = Talaba.objects.all()

    talabalar = talabalar.order_by(sort_param)

    return render(request, 'talabalar.html', {
        'talabalar': talabalar,
        'search': search_query,
        'sort': sort_param
    })
def talaba_detail_view(request, pk):
    talaba = Talaba.objects.get(id=pk)
    return render(request, 'talaba_detail.html', {'talaba': talaba})
def talaba_delete_view(request, pk):
    talaba = Talaba.objects.get(id=pk)
    talaba.delete()
    return redirect('talabalar')
def talaba_delete_confirm_view(request, pk):
    talaba = Talaba.objects.get(id=pk)
    context = {'talaba': talaba}
    return render(request, 'talaba_delete_confirm.html', context)

def kitoblar_view(request):
    q = request.GET.get('q', '')
    sort = request.GET.get('sort', 'nom')
    kitoblar = Kitob.objects.filter(nom__icontains=q).order_by(sort)
    return render(request, 'kitoblar.html', {'kitoblar': kitoblar, 'q': q, 'sort': sort})

def kitob_detail_view(request, pk):
    kitob = Kitob.objects.get(id=pk)
    return render(request, 'kitob_detail.html', {'kitob': kitob})

def kitob_delete_view(request, pk):
    kitob = Kitob.objects.get(id=pk)
    kitob.delete()
    return redirect('kitoblar')

def kitob_delete_confirm_view(request, pk):
    kitob = Kitob.objects.get(id=pk)
    return render(request, 'kitob_delete_confirm.html', {'kitob': kitob})


def mualliflar_view(request):
    q = request.GET.get('q', '')
    sort = request.GET.get('sort', 'ism')  # Ism bo'yicha saralash qo'shildi

    mualliflar = Muallif.objects.filter(ism__icontains=q).order_by(sort)

    return render(request, 'mualliflar.html', {
        'mualliflar': mualliflar,
        'q': q,
        'sort': sort
    })
def muallif_delete_confirm_view(request, pk):
    muallif = Muallif.objects.get(id=pk)
    return render(request, 'muallif_delete_confirm.html', {'muallif': muallif})

def muallif_detail_view(request, pk):
    muallif = Muallif.objects.get(id=pk)
    return render(request, 'muallif_detail.html', {'muallif': muallif})

def muallif_delete_view(request, pk):
    muallif = Muallif.objects.get(id=pk)
    muallif.delete()
    return redirect('mualliflar')

def recordlar_view(request):
    q = request.GET.get('q', '')
    recordlar = Record.objects.filter(kitob__nom__icontains=q).order_by('-id')
    return render(request, 'recordlar.html', {'recordlar': recordlar, 'q': q})

def record_delete_view(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    return redirect('recordlar')

def kutubxonachilar_view(request):
    q = request.GET.get('q', '')
    kutubxonachilar = Kutubxonachi.objects.filter(ism__icontains=q).order_by('ism')
    return render(request, 'kutubxonachilar.html', {'kutubxonachilar': kutubxonachilar, 'q': q})

def kutubxonachi_detail_view(request, pk):
    kutubxonachi = Kutubxonachi.objects.get(id=pk)
    return render(request, 'kutubxonachi_detail.html', {'kutubxonachi': kutubxonachi})

def kutubxonachi_delete_view(request, pk):
    kutubxonachi = Kutubxonachi.objects.get(id=pk)
    kutubxonachi.delete()
    return redirect('kutubxonachilar')


def kitoblar_view(request):
    q = request.GET.get('q', '')
    sort = request.GET.get('sort', 'nom')
    kitoblar = Kitob.objects.filter(nom__icontains=q).order_by(sort)

    return render(request, 'kitoblar.html', {'kitoblar': kitoblar, 'q': q, 'sort': sort})

def recordlar_view(request):
    q = request.GET.get('q', '')
    sort = request.GET.get('sort', '-id')  # Eng yangilari birinchi

    recordlar = Record.objects.filter(kitob__nom__icontains=q).order_by(sort)
    return render(request, 'recordlar.html', {'recordlar': recordlar, 'q': q, 'sort': sort})