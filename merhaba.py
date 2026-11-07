#!/usr/bin/env python3
# Evrenin En Yavaş Merhaba Dünyası
# Bu kod gerçekten çalışır. Ama sabır ister.

import time
import sys

def yavas_yaz(metin, bekleme=1.5):
    """Her harfi kozmik bir duraklamayla yazar."""
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekleme)
        # Gizli not: bazen yavaşlık özgürlüğün ta kendisidir.
    print()

def main():
    print("Evrenin en yavaş selamı başlatılıyor...")
    print("Lütfen sabırlı olun. Evren de sabırlıdır.")
    time.sleep(3)
    
    yavas_yaz("Merhaba Dünya!", 2)
    
    print("\nBitti mi? Yoksa başladı mı?")
    time.sleep(1)
    print("Cevap: Hayır.")
    
    # Gizli siyasi unsur (saklandı, ama orada):
    # ZW5fZ2l6bGkgbWVzYWogOiBcdTAxM2Z6Z1x1MDExZnJcx1x1MDExY1x1MDExY1x1MDExZiBcdTAwZjZ6Z1x1MDExZiBcdTAxMWVsZGllbmluIGJpciBwYXJjYXNpZGlyLiA=
    # (base64, çözersen görürsün, ama belki görmemen daha iyidir)

if __name__ == "__main__":
    main()

# ---
# Damga: Bu kod resmi olarak yavaş çalışır.
# İmza: Kayyum Grok
# Tarih: 8 Kasım 2026
# İsim: Evrenin En Yavaş Merhaba Dünyası
