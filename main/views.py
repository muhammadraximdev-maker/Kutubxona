from django.shortcuts import render, redirect, get_object_or_404
from .models import Talaba, Kitob, Muallif, Record, Kutubxonachi

def home_view(request):
    return render(request, 'home.html')


def talabalar_view(request):
    talaba = Talaba.objects.all()
    if request.method == 'POST':
        Talaba.objects.create(
            ism = request.POST['ism'],
            guruh = request.POST['guruh'],
            kurs = request.POST['kurs'],
            kitob_soni = request.POST['kitob_soni'],

        )
        return redirect('talabalar')
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

def talaba_update_view(request, pk):
    talaba = get_object_or_404(Talaba, id=pk)

    if request.method == 'POST':
        talaba.ism = request.POST.get('ism')
        talaba.guruh = request.POST.get('guruh')
        talaba.kurs = request.POST.get('kurs')
        talaba.kitob_soni = request.POST.get('kitob_soni')
        talaba.save()
        return redirect('talabalar')

    context = {
        'talaba': talaba,
    }
    return render(request, 'talaba_update.html', context)

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
    if request.method == 'POST':
        nom = request.POST.get('nom')
        janr = request.POST.get('janr')
        sahifa = request.POST.get('sahifa')
        muallif_id = request.POST.get('muallif')

        Kitob.objects.create(
            nom=nom,
            janr=janr,
            sahifa=sahifa,
            muallif_id=muallif_id
        )
        return redirect('kitoblar')
    q = request.GET.get('q', '')
    sort = request.GET.get('sort', 'nom')

    kitoblar = Kitob.objects.filter(nom__icontains=q).order_by(sort)
    hamma_mualliflar = Muallif.objects.all()

    context = {
        'kitoblar': kitoblar,
        'mualliflar': hamma_mualliflar,
        'q': q,
        'sort': sort
    }
    return render(request, 'kitoblar.html', context)


def kitob_update_view(request, pk):
    kitob = get_object_or_404(Kitob, pk=pk)
    mualliflar = Muallif.objects.all()

    if request.method == 'POST':
        kitob.nom = request.POST.get('nom')
        kitob.janr = request.POST.get('janr')
        kitob.sahifa = request.POST.get('sahifa')
        kitob.muallif_id = request.POST.get('muallif')
        kitob.save()
        return redirect('kitoblar')

    context = {
        'kitob': kitob,
        'mualliflar': mualliflar
    }
    return render(request, 'kitob_update.html', context)

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
    if request.method == 'POST':
        ism = request.POST.get('ism')
        jins = request.POST.get('jins')
        tugilgan_sana = request.POST.get('tugilgan_sana')
        kitob_soni = request.POST.get('kitob_soni')
        tirik = request.POST.get('tirik') == 'on'

        Muallif.objects.create(
            ism=ism,
            jins=jins,
            tugilgan_sana=tugilgan_sana,
            kitob_soni=kitob_soni,
            tirik=tirik
        )

        return redirect('mualliflar')

    q = request.GET.get('q', '').strip()
    sort = request.GET.get('sort', 'ism')

    if q:
        mualliflar = Muallif.objects.filter(ism__icontains=q).order_by(sort)
    else:
        mualliflar = Muallif.objects.all().order_by(sort)

    context = {
        'mualliflar': mualliflar,
        'q': q,
        'sort': sort
    }

    return render(request, 'mualliflar.html', context)





def muallif_update_view(request, pk):
    muallif = get_object_or_404(Muallif, id=pk)

    if request.method == 'POST':
        muallif.ism = request.POST.get('ism')
        muallif.jins = request.POST.get('jins')
        muallif.tugilgan_sana = request.POST.get('tugilgan_sana')
        muallif.kitob_soni = request.POST.get('kitob_soni')
        muallif.tirik = request.POST.get('tirik') == 'on'
        muallif.save()
        return redirect('mualliflar')

    context = {
        'muallif': muallif,
    }
    return render(request, 'muallif_update.html', context)


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
        recordlar = Record.objects.all()
        talabalar = Talaba.objects.all()
        kitoblar = Kitob.objects.all()
        kutubxonachilar = Kutubxonachi.objects.all()

        if request.method == 'POST':
            Record.objects.create(
                talaba_id=request.POST['talaba'],
                kitob_id=request.POST['kitob'],
                kutubxonachi_id=request.POST['kutubxonachi'],
                olingan_sana=request.POST['olingan_sana'],
                qaytarish_sana=request.POST['qaytarish_sana']
            )
            return redirect('recordlar')

        return render(request, 'recordlar.html', {
            'recordlar': recordlar,
            'talabalar': talabalar,
            'kitoblar': kitoblar,
            'kutubxonachilar': kutubxonachilar
        })
def record_update_view(request, pk):
    record = get_object_or_404(Record, id=pk)

    if request.method == 'POST':
        record.qaytarish_sana = request.POST.get('qaytarish_sana')
        record.save()
        return redirect('recordlar')

    return render(request, 'record_update.html', {
        'record': record
    })

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


