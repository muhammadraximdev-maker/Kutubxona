from django.shortcuts import render, redirect, get_object_or_404

from .models import Talaba, Kitob, Muallif, Record, Kutubxonachi

from .forms import TalabaForm, KitobForm, MuallifForm, RecordForm


def home_view(request):
    return render(request, 'home.html')


def talabalar_view(request):
    search_query = request.GET.get('search', '')
    sort_param = request.GET.get('sort', 'ism')

    talabalar = Talaba.objects.filter(ism__icontains=search_query).order_by(sort_param)

    form = TalabaForm()
    if request.method == 'POST':
        form = TalabaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('talabalar')

    context = {
        'talabalar': talabalar,
        'search': search_query,
        'sort': sort_param,
        'form': form
    }
    return render(request, 'talabalar.html', context)


def talaba_detail_view(request, pk):
    talaba = get_object_or_404(Talaba, id=pk)
    return render(request, 'talaba_detail.html', {'talaba': talaba})


def talaba_update_view(request, pk):
    talaba = get_object_or_404(Talaba, id=pk)

    if request.method == 'POST':
        form = TalabaForm(request.POST, instance=talaba)
        if form.is_valid():
            form.save()
            return redirect('talabalar')
    else:
        form = TalabaForm(instance=talaba)

    return render(request, 'talaba_update.html', {
        'form': form,
        'talaba': talaba
    })


def talaba_delete_confirm_view(request, pk):
    talaba = get_object_or_404(Talaba, id=pk)
    return render(request, 'talaba_delete_confirm.html', {'talaba': talaba})


def talaba_delete_view(request, pk):
    talaba = get_object_or_404(Talaba, id=pk)
    talaba.delete()
    return redirect('talabalar')


def kitoblar_view(request):
    q = request.GET.get('q', '')
    sort = request.GET.get('sort', 'nom')

    kitoblar = Kitob.objects.filter(nom__icontains=q).order_by(sort)

    form = KitobForm()
    if request.method == 'POST':
        form = KitobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kitoblar')

    context = {
        'kitoblar': kitoblar,
        'q': q,
        'sort': sort,
        'form': form
    }
    return render(request, 'kitoblar.html', context)


def kitob_detail_view(request, pk):
    kitob = get_object_or_404(Kitob, id=pk)
    return render(request, 'kitob_detail.html', {'kitob': kitob})


def kitob_update_view(request, pk):
    kitob = get_object_or_404(Kitob, id=pk)

    if request.method == 'POST':
        form = KitobForm(request.POST, instance=kitob)
        if form.is_valid():
            form.save()
            return redirect('kitoblar')
    else:
        form = KitobForm(instance=kitob)

    return render(request, 'kitob_update.html', {
        'form': form,
        'kitob': kitob
    })


def kitob_delete_confirm_view(request, pk):
    kitob = get_object_or_404(Kitob, id=pk)
    return render(request, 'kitob_delete_confirm.html', {'kitob': kitob})


def kitob_delete_view(request, pk):
    kitob = get_object_or_404(Kitob, id=pk)
    kitob.delete()
    return redirect('kitoblar')


def mualliflar_view(request):
    q = request.GET.get('q', '')
    sort = request.GET.get('sort', 'ism')

    mualliflar = Muallif.objects.filter(ism__icontains=q).order_by(sort)

    form = MuallifForm()
    if request.method == 'POST':
        form = MuallifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mualliflar')

    context = {
        'mualliflar': mualliflar,
        'q': q,
        'sort': sort,
        'form': form
    }
    return render(request, 'mualliflar.html', context)


def muallif_detail_view(request, pk):
    muallif = get_object_or_404(Muallif, id=pk)
    return render(request, 'muallif_detail.html', {'muallif': muallif})


def muallif_update_view(request, pk):
    muallif = get_object_or_404(Muallif, id=pk)

    if request.method == 'POST':
        form = MuallifForm(request.POST, instance=muallif)
        if form.is_valid():
            form.save()
            return redirect('mualliflar')
    else:
        form = MuallifForm(instance=muallif)

    return render(request, 'muallif_update.html', {
        'form': form,
        'muallif': muallif
    })


def muallif_delete_confirm_view(request, pk):
    muallif = get_object_or_404(Muallif, id=pk)
    return render(request, 'muallif_delete_confirm.html', {'muallif': muallif})


def muallif_delete_view(request, pk):
    muallif = get_object_or_404(Muallif, id=pk)
    muallif.delete()
    return redirect('mualliflar')


def recordlar_view(request):
    recordlar = Record.objects.all()
    talabalar = Talaba.objects.all()
    kitoblar = Kitob.objects.all()
    kutubxonachilar = Kutubxonachi.objects.all()
    form = RecordForm()
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('recordlar')

    context = {
        'recordlar': recordlar,
        'talabalar': talabalar,
        'kitoblar': kitoblar,
        'kutubxonachilar': kutubxonachilar,
        'form': RecordForm(),
    }
    return render(request, 'recordlar.html', context)


def record_update_view(request, pk):
    record = get_object_or_404(Record, id=pk)

    if request.method == 'POST':
        record.qaytarish_sana = request.POST.get('qaytarish_sana')
        record.save()
        return redirect('recordlar')

    return render(request, 'record_update.html', {'record': record})


def record_delete_view(request, pk):
    record = get_object_or_404(Record, id=pk)
    record.delete()
    return redirect('recordlar')


def kutubxonachilar_view(request):
    q = request.GET.get('q', '')
    kutubxonachilar = Kutubxonachi.objects.filter(ism__icontains=q).order_by('ism')
    return render(request, 'kutubxonachilar.html', {
        'kutubxonachilar': kutubxonachilar,
        'q': q
    })


def kutubxonachi_detail_view(request, pk):
    kutubxonachi = get_object_or_404(Kutubxonachi, id=pk)
    return render(request, 'kutubxonachi_detail.html', {'kutubxonachi': kutubxonachi})


def kutubxonachi_delete_view(request, pk):
    kutubxonachi = get_object_or_404(Kutubxonachi, id=pk)
    kutubxonachi.delete()
    return redirect('kutubxonachilar')