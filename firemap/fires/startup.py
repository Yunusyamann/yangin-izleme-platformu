import os

def run_startup_task():
    # Sadece runserver komutunda çalıştır
    from django.core.management import commands
    if os.environ.get('RUN_MAIN', None) != 'true':
        # Django'nun otomatik yeniden başlatıcısında 2 kez çağrılmasını engeller
        return

    from fires.tasks import fetch_fire_data
    try:
        fetch_fire_data()
        print("🚨 Yangın verisi otomatik olarak çekildi!")
    except Exception as e:
        print(f"Hata: Otomatik veri çekilemedi -> {e}")

run_startup_task()
