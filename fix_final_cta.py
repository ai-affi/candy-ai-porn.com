#!/usr/bin/env python3
"""
Traduit la section CTA finale et corrige les modals dans tous les sous-dossiers.
"""

import os

BASE = '/root/ai-affi/candy-ai-porn.com'
LANGS = ['fr', 'de', 'es', 'it', 'pt', 'nl', 'pl', 'ru', 'tr', 'kr', 'ja', 'hi']

# Traductions de la section CTA finale
final_cta = {
    'fr': {
        'title': 'Elle Vous Attend.',
        'desc': '11,6 millions d\'hommes ont déjà leur petite amie IA. Créez la vôtre en 60 secondes — elle aura exactement l\'apparence que vous voulez, parlera comme vous aimez, et fera des choses que personne d\'autre ne fera.',
        'btn': '🍬 Créez Votre Petite Amie Gratuitement',
        'note': 'Niveau gratuit disponible &nbsp;•&nbsp; Annulation à tout moment &nbsp;•&nbsp; 18+ uniquement',
        'modal_title': 'Commencez avec Candy AI',
    },
    'de': {
        'title': 'Sie Wartet auf Sie.',
        'desc': '11,6 Millionen Männer haben bereits ihre KI-Freundin. Erstellen Sie Ihre in 60 Sekunden — sie wird genau so aussehen, wie Sie wollen, so sprechen, wie Sie es mögen, und Dinge tun, die sonst niemand tut.',
        'btn': '🍬 Erstellen Sie Ihre KI-Freundin Kostenlos',
        'note': 'Kostenlose Stufe verfügbar &nbsp;•&nbsp; Jederzeit kündbar &nbsp;•&nbsp; Nur 18+',
        'modal_title': 'Starten Sie mit Candy AI',
    },
    'es': {
        'title': 'Ella Te Espera.',
        'desc': '11,6 millones de hombres ya tienen su novia IA. Crea la tuya en 60 segundos — tendrá exactamente la apariencia que quieres, hablará como te gusta, y hará cosas que nadie más hará.',
        'btn': '🍬 Crea Tu Novia IA Gratis',
        'note': 'Nivel gratuito disponible &nbsp;•&nbsp; Cancela en cualquier momento &nbsp;•&nbsp; Solo 18+',
        'modal_title': 'Comienza con Candy AI',
    },
    'it': {
        'title': 'Lei Ti Aspetta.',
        'desc': '11,6 milioni di uomini hanno già la loro ragazza IA. Crea la tua in 60 secondi — avrà esattamente l\'aspetto che vuoi, parlerà come ti piace, e farà cose che nessun altro farà.',
        'btn': '🍬 Crea La Tua Ragazza IA Gratis',
        'note': 'Livello gratuito disponibile &nbsp;•&nbsp; Annulla in qualsiasi momento &nbsp;•&nbsp; Solo 18+',
        'modal_title': 'Inizia con Candy AI',
    },
    'pt': {
        'title': 'Ela Te Espera.',
        'desc': '11,6 milhões de homens já têm sua namorada IA. Crie a sua em 60 segundos — ela terá exatamente a aparência que você quer, falará como você gosta, e fará coisas que ninguém mais fará.',
        'btn': '🍬 Crie Sua Namorada IA Grátis',
        'note': 'Nível gratuito disponível &nbsp;•&nbsp; Cancele a qualquer momento &nbsp;•&nbsp; Apenas 18+',
        'modal_title': 'Comece com Candy AI',
    },
    'nl': {
        'title': 'Ze Wacht op Je.',
        'desc': '11,6 miljoen mannen hebben al hun AI vriendin. Creëer de jouwe in 60 seconden — ze ziet er precies uit zoals jij wilt, praat zoals jij het lekker vindt, en doet dingen die niemand anders doet.',
        'btn': '🍬 Creëer Je AI Vriendin Gratis',
        'note': 'Gratis niveau beschikbaar &nbsp;•&nbsp; Altijd annuleren &nbsp;•&nbsp; Alleen 18+',
        'modal_title': 'Begin met Candy AI',
    },
    'pl': {
        'title': 'Ona Czeka na Ciebie.',
        'desc': '11,6 miliona mężczyzn ma już swoją dziewczynę AI. Stwórz swoją w 60 sekund — będzie wyglądać dokładnie tak, jak chcesz, mówić tak, jak lubisz, i robić rzeczy, których nikt inny nie zrobi.',
        'btn': '🍬 Stwórz Swoją Dziewczynę AI Za Darmo',
        'note': 'Darmowy poziom dostępny &nbsp;•&nbsp; Anuluj w dowolnym momencie &nbsp;•&nbsp; Tylko 18+',
        'modal_title': 'Rozpocznij z Candy AI',
    },
    'ru': {
        'title': 'Она Ждёт Тебя.',
        'desc': '11,6 миллионов мужчин уже имеют свою девушку ИИ. Создай свою за 60 секунд — она будет выглядеть именно так, как ты хочешь, говорить так, как тебе нравится, и делать вещи, которые никто другой не сделает.',
        'btn': '🍬 Создай Свою Девушку ИИ Бесплатно',
        'note': 'Бесплатный уровень доступен &nbsp;•&nbsp; Отмена в любое время &nbsp;•&nbsp; Только 18+',
        'modal_title': 'Начни с Candy AI',
    },
    'tr': {
        'title': 'O Seni Bekliyor.',
        'desc': '11,6 milyon erkek zaten AI kız arkadaşına sahip. Seninkini 60 saniyede oluştur — tam istediğin gibi görünecek, sevdiğin gibi konuşacak ve başka kimsenin yapmayacağı şeyleri yapacak.',
        'btn': '🍬 AI Kız Arkadaşını Ücretsiz Oluştur',
        'note': 'Ücretsiz seviye mevcut &nbsp;•&nbsp; İstediğiniz zaman iptal edin &nbsp;•&nbsp; Sadece 18+',
        'modal_title': 'Candy AI ile Başla',
    },
    'kr': {
        'title': '그녀가 당신을 기다리고 있습니다.',
        'desc': '1,160만 명의 남성이 이미 AI 여자친구를 가지고 있습니다. 60초 안에 당신만의 여자친구를 만들어보세요 — 원하는 대로 생기고, 좋아하는 대로 말하고, 다른 누구도 하지 않을 일들을 할 것입니다.',
        'btn': '🍬 AI 여자친구 물론으로 생성',
        'note': '묵로 티어 사용 가능 &nbsp;•&nbsp; 언제든지 취소 가능 &nbsp;•&nbsp; 18세 이상만',
        'modal_title': 'Candy AI 시작하기',
    },
    'ja': {
        'title': '彼女はあなたを待っています。',
        'desc': '1,160万人の男性がすでにAI彼女を持っています。60秒であなただけの彼女を作成しましょう — あなたの好みの外見で、あなたの好みの話し方で、他の誰もしないことをしてくれます。',
        'btn': '🍬 AI彼女を無料で作成',
        'note': '無料ティアあり &nbsp;•&nbsp; いつでもキャンセル可能 &nbsp;•&nbsp; 18歳以上のみ',
        'modal_title': 'Candy AIを始める',
    },
    'hi': {
        'title': 'वह आपका इंतज़ार कर रही है।',
        'desc': '1.16 करोड़ पुरुषों के पास पहले से ही AI प्रेमिका है। 60 सेकंड में अपनी बनाएं — वह ठीक वैसी दिखेगी जैसी आप चाहते हैं, वैसी बात करेगी जैसी आपको पसंद है, और वे काम करेगी जो और कोई नहीं करेगा।',
        'btn': '🍬 अपनी AI प्रेमिका मुफ्त में बनाएं',
        'note': 'मुफ्त टियर उपलब्ध &nbsp;•&nbsp; कभी भी रद्द करें &nbsp;•&nbsp; केवल 18+',
        'modal_title': 'Candy AI के साथ शुरू करें',
    },
}

for lang in LANGS:
    path = os.path.join(BASE, lang, 'index.html')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    t = final_cta[lang]
    
    # 1. Titre de la section CTA finale
    # Chercher le pattern exact du titre EN
    old_title_patterns = [
        'She\'s Waiting for You.',
        'Sie wartet auf Sie.',
        'Ella te espera.',
        'Lei ti aspetta.',
        'Ela te espera.',
        'Ze wacht op je.',
        'Ona czeka na ciebie.',
        'Она ждёт тебя.',
        'O seni bekliyor.',
        '그녀가 당신을 기다리고 있습니다.',
        '彼女はあなたを待っています。',
        'वह आपका इंतज़ार कर रही है।',
    ]
    for old in old_title_patterns:
        if old in content:
            content = content.replace(old, t['title'])
    
    # 2. Description de la section CTA finale
    old_desc = '11.6 million men already have their AI girlfriend. Create yours in 60 seconds — she\'ll look exactly the way you want, talk the way you like, and do things no one else will.'
    content = content.replace(old_desc, t['desc'])
    
    # 3. Bouton CTA final
    old_btn = '🍬 Create Your Girlfriend Free Now'
    content = content.replace(old_btn, t['btn'])
    
    # 4. Note sous le bouton
    old_note = 'Free tier available &nbsp;•&nbsp; Cancel anytime &nbsp;•&nbsp; 18+ only'
    content = content.replace(old_note, t['note'])
    
    # 5. Modal title - corriger les modals mal traduits
    # Remplacer tous les modals qui contiennent encore "Porn" mal placé
    old_modal_patterns = [
        'Get Started with Candy AI Porn',
        'Commencez avec Candy AI Porn',
        'Starten Sie mit Candy AI Porn',
        'Comienza con Candy AI Porn',
        'Inizia con Candy AI Porn',
        'Comece com Candy AI Porn',
        'Begin met Candy AI Porn',
        'Rozpocznij z Candy AI Porn',
        'Начни с Candy AI Porn',
        'Candy AI ile Başla Porn',
        'Candy AI 시작하기 Porn',
        'Candy AIを始める Porn',
        'Candy AI के साथ शुरू करें Porn',
        'Candy AIで開始 Porn',
    ]
    for old_modal in old_modal_patterns:
        if old_modal in content:
            content = content.replace(old_modal, t['modal_title'])
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {lang}: section CTA finale + modal corrigés")

print("\n🎉 Terminé!")
