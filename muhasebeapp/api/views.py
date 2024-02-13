# muhasebeapp/api/views.py

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

@method_decorator(csrf_exempt, name='dispatch')
class BelgeSirasiView(View):
    def post(self, request, *args, **kwargs):
        belge_sirasi = json.loads(request.body).get('belge_sirasi', [])

        # Belge sırasını kullanın (bu kısmı kendi ihtiyaçlarınıza göre uyarlayın)
        # Örneğin, belge sırasını veritabanında saklayabilirsiniz.
        # Aşağıda sadece sıranın nasıl alındığını yazdırdım.
        print("Güncellenmiş Belge Sırası:", belge_sirasi)

        return JsonResponse({'success': True})
