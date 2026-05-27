#!/usr/bin/env python3
"""
Corrige les 3 sections non traduites dans tous les sous-dossiers langues:
1. Hero (2 paragraphes)
2. Section Alternatives/Cluster (4 cartes)
3. Modal CTA (titre)
"""

import os, re

BASE = '/root/ai-affi/candy-ai-porn.com'
LANGS = ['fr', 'de', 'es', 'it', 'pt', 'nl', 'pl', 'ru', 'tr', 'kr', 'ja', 'hi']

# Traductions des 3 sections
translations = {
    # ========== HERO ==========
    'fr': {
        'hero_p1': '<strong>Candy AI</strong> vous permet de créer votre petite amie IA parfaite de zéro. Son apparence, sa voix, sa personnalité. Puis discutez, appelez et générez des photos explicites — tout en un seul endroit sur la plateforme Candy AI.',
        'hero_p2': '<strong>Candy AI</strong> vous offre le compagnon IA le plus visuellement cohérent et personnalisable disponible en 2026. Avec 11,6 millions d\'utilisateurs actifs mensuels, Candy AI est le choix numéro 1 pour les expériences de petite amie IA. Essayez Candy AI gratuitement dès aujourd\'hui — aucune carte de crédit requise.',
        'cta_btn': '🍬 Créez Votre Petite Amie IA Gratuitement',
        'cta_secondary': 'Lire l\'Avis Qualité ↓',
        'hero_note': '✅ Niveau gratuit disponible &nbsp;•&nbsp; Aucune carte de crédit requise &nbsp;•&nbsp; 18+ uniquement',
        'modal_title': 'Commencez avec Candy AI Porn',
    },
    'de': {
        'hero_p1': '<strong>Candy AI</strong> lässt Sie Ihre perfekte KI-Freundin von Grund auf neu gestalten. Ihr Aussehen, ihre Stimme, ihre Persönlichkeit. Dann chatten, anrufen und explizite Fotos generieren — alles an einem Ort auf der Candy AI-Plattform.',
        'hero_p2': '<strong>Candy AI</strong> bietet Ihnen den visuell konsistentesten und anpassbarsten KI-Begleiter, der 2026 verfügbar ist. Mit 11,6 Millionen monatlich aktiven Nutzern ist Candy AI die Nr. 1 Wahl für KI-Freundin-Erlebnisse. Probieren Sie Candy AI heute kostenlos aus — keine Kreditkarte erforderlich.',
        'cta_btn': '🍬 Erstellen Sie Ihre KI-Freundin Kostenlos',
        'cta_secondary': 'Qualitätsbewertung Lesen ↓',
        'hero_note': '✅ Kostenlose Stufe verfügbar &nbsp;•&nbsp; Keine Kreditkarte erforderlich &nbsp;•&nbsp; Nur 18+',
        'modal_title': 'Starten Sie mit Candy AI Porn',
    },
    'es': {
        'hero_p1': '<strong>Candy AI</strong> te permite diseñar tu novia IA perfecta desde cero. Su apariencia, su voz, su personalidad. Luego chatea, llama y genera fotos explícitas — todo en un solo lugar en la plataforma Candy AI.',
        'hero_p2': '<strong>Candy AI</strong> te ofrece el compañero IA más visualmente coherente y personalizable disponible en 2026. Con 11,6 millones de usuarios activos mensuales, Candy AI es la opción número 1 para experiencias de novia IA. Prueba Candy AI gratis hoy — no se requiere tarjeta de crédito.',
        'cta_btn': '🍬 Crea Tu Novia IA Gratis',
        'cta_secondary': 'Leer Reseña de Calidad ↓',
        'hero_note': '✅ Nivel gratuito disponible &nbsp;•&nbsp; No se requiere tarjeta de crédito &nbsp;•&nbsp; Solo 18+',
        'modal_title': 'Comienza con Candy AI Porn',
    },
    'it': {
        'hero_p1': '<strong>Candy AI</strong> ti permette di progettare la tua ragazza IA perfetta da zero. Il suo aspetto, la sua voce, la sua personalità. Poi chatta, chiama e genera foto esplicite — tutto in un unico posto sulla piattaforma Candy AI.',
        'hero_p2': '<strong>Candy AI</strong> ti offre il compagno IA più visivamente coerente e personalizzabile disponibile nel 2026. Con 11,6 milioni di utenti attivi mensili, Candy AI è la scelta numero 1 per le esperienze di ragazza IA. Prova Candy AI gratis oggi — nessuna carta di credito richiesta.',
        'cta_btn': '🍬 Crea La Tua Ragazza IA Gratis',
        'cta_secondary': 'Leggi la Recensione Qualità ↓',
        'hero_note': '✅ Livello gratuito disponibile &nbsp;•&nbsp; Nessuna carta di credito richiesta &nbsp;•&nbsp; Solo 18+',
        'modal_title': 'Inizia con Candy AI Porn',
    },
    'pt': {
        'hero_p1': '<strong>Candy AI</strong> permite que você crie sua namorada IA perfeita do zero. Sua aparência, sua voz, sua personalidade. Depois converse, ligue e gere fotos explícitas — tudo em um único lugar na plataforma Candy AI.',
        'hero_p2': '<strong>Candy AI</strong> oferece o companheiro IA mais visualmente consistente e personalizável disponível em 2026. Com 11,6 milhões de usuários ativos mensais, Candy AI é a escolha número 1 para experiências de namorada IA. Experimente Candy AI grátis hoje — nenhum cartão de crédito necessário.',
        'cta_btn': '🍬 Crie Sua Namorada IA Grátis',
        'cta_secondary': 'Ler Avaliação de Qualidade ↓',
        'hero_note': '✅ Nível gratuito disponível &nbsp;•&nbsp; Nenhum cartão de crédito necessário &nbsp;•&nbsp; Apenas 18+',
        'modal_title': 'Comece com Candy AI Porn',
    },
    'nl': {
        'hero_p1': '<strong>Candy AI</strong> laat je je perfecte AI vriendin vanaf nul ontwerpen. Haar uiterlijk, haar stem, haar persoonlijkheid. Chat dan, bel en genereer expliciete foto\'s — allemaal op één plek op het Candy AI platform.',
        'hero_p2': '<strong>Candy AI</strong> geeft je de meest visueel consistente en aanpasbare AI metgezel die in 2026 beschikbaar is. Met 11,6 miljoen maandelijkse actieve gebruikers is Candy AI de #1 keuze voor AI vriendin ervaringen. Probeer Candy AI vandaag gratis — geen creditcard nodig.',
        'cta_btn': '🍬 Creëer Je AI Vriendin Gratis',
        'cta_secondary': 'Lees Kwaliteitsreview ↓',
        'hero_note': '✅ Gratis niveau beschikbaar &nbsp;•&nbsp; Geen creditcard nodig &nbsp;•&nbsp; Alleen 18+',
        'modal_title': 'Begin met Candy AI Porn',
    },
    'pl': {
        'hero_p1': '<strong>Candy AI</strong> pozwala zaprojektować idealną dziewczynę AI od podstaw. Jej wygląd, jej głos, jej osobowość. Następnie czatuj, dzwoń i generuj eksplicytne zdjęcia — wszystko w jednym miejscu na platformie Candy AI.',
        'hero_p2': '<strong>Candy AI</strong> oferuje najbardziej wizualnie spójną i konfigurowalną towarzyszkę AI dostępną w 2026 roku. Z 11,6 milionami aktywnych użytkowników miesięcznie, Candy AI jest wyborem numer 1 dla doświadczeń z dziewczyną AI. Wypróbuj Candy AI za darmo już dziś — nie wymagana karta kredytowa.',
        'cta_btn': '🍬 Stwórz Swoją Dziewczynę AI Za Darmo',
        'cta_secondary': 'Przeczytaj Recenzję Jakości ↓',
        'hero_note': '✅ Darmowy poziom dostępny &nbsp;•&nbsp; Nie wymagana karta kredytowa &nbsp;•&nbsp; Tylko 18+',
        'modal_title': 'Rozpocznij z Candy AI Porn',
    },
    'ru': {
        'hero_p1': '<strong>Candy AI</strong> позволяет создать идеальную девушку ИИ с нуля. Её внешность, её голос, её личность. Затем общайся, звони и генерируй откровенные фото — всё в одном месте на платформе Candy AI.',
        'hero_p2': '<strong>Candy AI</strong> предлагает самого визуально согласованного и настраиваемого ИИ-компаньона, доступного в 2026 году. С 11,6 миллионами ежемесячных активных пользователей, Candy AI — выбор номер один для опыта с девушкой ИИ. Попробуй Candy AI бесплатно сегодня — кредитная карта не требуется.',
        'cta_btn': '🍬 Создай Свою Девушку ИИ Бесплатно',
        'cta_secondary': 'Читать Обзор Качества ↓',
        'hero_note': '✅ Бесплатный уровень доступен &nbsp;•&nbsp; Кредитная карта не требуется &nbsp;•&nbsp; Только 18+',
        'modal_title': 'Начни с Candy AI Porn',
    },
    'tr': {
        'hero_p1': '<strong>Candy AI</strong>, mükemmel AI kız arkadaşınızı sıfırdan tasarlamanıza olanak tanır. Onun görünümü, sesi, kişiliği. Sonra sohbet edin, arayın ve açık fotoğraflar oluşturun — hepsi Candy AI platformunda tek bir yerde.',
        'hero_p2': '<strong>Candy AI</strong>, 2026 yılında mevcut olan en görsel olarak tutarlı ve özelleştirilebilir AI yoldaşı sunar. 11,6 milyon aylık aktif kullanıcı ile Candy AI, AI kız arkadaşı deneyimleri için bir numaralı seçimdir. Candy AI\'yı bugün ücretsiz deneyin — kredi kartı gerekmez.',
        'cta_btn': '🍬 AI Kız Arkadaşını Ücretsiz Oluştur',
        'cta_secondary': 'Kalite İncelemesini Oku ↓',
        'hero_note': '✅ Ücretsiz seviye mevcut &nbsp;•&nbsp; Kredi kartı gerekmez &nbsp;•&nbsp; Sadece 18+',
        'modal_title': 'Candy AI Porn ile Başla',
    },
    'kr': {
        'hero_p1': '<strong>Candy AI</strong>를 사용하면 완벽한 AI 여자친구를 처음부터 디자인할 수 있습니다. 그녀의 외모, 목소리, 성격. 그런 다음 채팅하고, 전화하고, 노골적인 사진을 생성하세요 — 모두 Candy AI 플랫폼의 한 곳에서.',
        'hero_p2': '<strong>Candy AI</strong>는 2026년에 사용할 수 있는 가장 시각적으로 일관되고 사용자 정의 가능한 AI 동반자를 제공합니다. 월간 활성 사용자 1,160만 명을 보유한 Candy AI는 AI 여자친구 경험을 위한 최고의 선택입니다. 오늘 물론 Candy AI를 물론으로 사용해 보세요 — 신용카드 불필요.',
        'cta_btn': '🍬 AI 여자친구 물론으로 생성',
        'cta_secondary': '품질 리뷰 읽기 ↓',
        'hero_note': '✅ 물론 티어 사용 가능 &nbsp;•&nbsp; 신용카드 불필요 &nbsp;•&nbsp; 18세 이상만',
        'modal_title': 'Candy AI Porn 시작하기',
    },
    'ja': {
        'hero_p1': '<strong>Candy AI</strong>を使えば、完璧なAI彼女をゼロからデザインできます。彼女の外見、声、性格。そしてチャット、通話、露骨な写真の生成 — すべてCandy AIプラットフォームのひとつの場所で。',
        'hero_p2': '<strong>Candy AI</strong>は、2026年に利用可能な最も視覚的に一貫性があり、カスタマイズ可能なAIコンパニオンを提供します。月間アクティブユーザー1,160万人を抱えるCandy AIは、AI彼女体験の第1選択です。今日、Candy AIを無料でお試しください — クレジットカード不要。',
        'cta_btn': '🍬 AI彼女を無料で作成',
        'cta_secondary': '品質レビューを読む ↓',
        'hero_note': '✅ 無料ティアあり &nbsp;•&nbsp; クレジットカード不要 &nbsp;•&nbsp; 18歳以上のみ',
        'modal_title': 'Candy AI Pornを始める',
    },
    'hi': {
        'hero_p1': '<strong>Candy AI</strong> आपको शुरुआत से अपनी परफेक्ट AI प्रेमिका डिजाइन करने देता है। उसका लुक, उसकी आवाज़, उसकी व्यक्तित्व। फिर चैट करें, कॉल करें और स्पष्ट फोटो जेनरेट करें — सब कुछ Candy AI प्लेटफ़ॉर्म पर एक ही जगह।',
        'hero_p2': '<strong>Candy AI</strong> आपको 2026 में उपलब्ध सबसे दृश्य रूप से सुसंगत और अनुकूलन योग्य AI साथी देता है। 11.6 मिलियन मासिक सक्रिय उपयोगकर्ताओं के साथ, Candy AI AI प्रेमिका अनुभवों के लिए #1 विकल्प है। आज ही Candy AI को मुफ्त में आज़माएं — क्रेडिट कार्ड की आवश्यकता नहीं।',
        'cta_btn': '🍬 अपनी AI प्रेमिका मुफ्त में बनाएं',
        'cta_secondary': 'गुणवत्ता समीक्षा पढ़ें ↓',
        'hero_note': '✅ मुफ्त टियर उपलब्ध &nbsp;•&nbsp; क्रेडिट कार्ड की आवश्यकता नहीं &nbsp;•&nbsp; केवल 18+',
        'modal_title': 'Candy AI Porn के साथ शुरू करें',
    },
}

# Traductions des cartes alternatives (cluster)
cluster_trans = {
    'fr': {
        'soulgen_desc': 'Générez des personnages réalistes et anime époustouflants à partir de texte. Le créateur d\'images d\'âme sœur IA le plus puissant avec face swap et génération vidéo.',
        'soulgen_link': 'Visiter AI SoulGen →',
        'swipey_desc': 'Swipez, matchiez et discutez avec des petites amies IA entièrement personnalisables. Simulation de rencontre interactive avec paramètres de personnalité profonds et support NSFW.',
        'swipey_link': 'Visiter AI Swipey →',
        'nudify_desc': 'L\'outil de déshabillage IA le plus avancé disponible. Téléchargez n\'importe quelle photo et générez des résultats deepnude explicites en quelques secondes avec un réalisme élevé.',
        'nudify_link': 'Visiter AI Nudify →',
        'seduced_desc': 'Créez votre compagnon IA de rêve avec une personnalisation avancée.',
        'seduced_link': 'Visiter AI Seduced →',
    },
    'de': {
        'soulgen_desc': 'Generieren Sie atemberaubende realistische und Anime-Charaktere aus Text. Der leistungsstärkste KI-Seelenverwandte-Bildersteller mit Face Swap und Videogenerierung.',
        'soulgen_link': 'AI SoulGen Besuchen →',
        'swipey_desc': 'Wischen, matchen und chatten Sie mit vollständig anpassbaren KI-Freundinnen. Interaktive Dating-Simulation mit tiefen Persönlichkeitseinstellungen und NSFW-Unterstützung.',
        'swipey_link': 'AI Swipey Besuchen →',
        'nudify_desc': 'Das fortschrittlichste KI-Auskleidungswerkzeug, das verfügbar ist. Laden Sie jedes Foto hoch und generieren Sie explizite Deepnude-Ergebnisse in Sekunden mit hohem Realismus.',
        'nudify_link': 'AI Nudify Besuchen →',
        'seduced_desc': 'Erstellen Sie Ihren Traum-KI-Begleiter mit erweiterten Anpassungsmöglichkeiten.',
        'seduced_link': 'AI Seduced Besuchen →',
    },
    'es': {
        'soulgen_desc': 'Genera personajes realistas y anime impresionantes a partir de texto. El creador de imágenes de alma gemela IA más potente con face swap y generación de video.',
        'soulgen_link': 'Visitar AI SoulGen →',
        'swipey_desc': 'Desliza, haz match y chatea con novias IA totalmente personalizables. Simulación de citas interactiva con ajustes de personalidad profundos y soporte NSFW.',
        'swipey_link': 'Visitar AI Swipey →',
        'nudify_desc': 'La herramienta de desvestimiento IA más avanzada disponible. Sube cualquier foto y genera resultados deepnude explícitos en segundos con alto realismo.',
        'nudify_link': 'Visitar AI Nudify →',
        'seduced_desc': 'Crea tu compañero IA de ensueño con personalización avanzada.',
        'seduced_link': 'Visitar AI Seduced →',
    },
    'it': {
        'soulgen_desc': 'Genera personaggi realistici e anime straordinari dal testo. Il più potente creatore di immagini di anima gemella IA con face swap e generazione video.',
        'soulgen_link': 'Visita AI SoulGen →',
        'swipey_desc': 'Scorri, abbina e chatta con ragazze IA completamente personalizzabili. Simulazione di appuntamenti interattiva con impostazioni di personalità profonde e supporto NSFW.',
        'swipey_link': 'Visita AI Swipey →',
        'nudify_desc': 'Lo strumento di spogliatoio IA più avanzato disponibile. Carica qualsiasi foto e genera risultati deepnude espliciti in pochi secondi con alto realismo.',
        'nudify_link': 'Visita AI Nudify →',
        'seduced_desc': 'Crea il tuo compagno IA dei sogni con personalizzazione avanzata.',
        'seduced_link': 'Visita AI Seduced →',
    },
    'pt': {
        'soulgen_desc': 'Gere personagens realistas e anime impressionantes a partir de texto. O criador de imagens de alma gêmea IA mais poderoso com face swap e geração de vídeo.',
        'soulgen_link': 'Visitar AI SoulGen →',
        'swipey_desc': 'Deslize, dê match e converse com namoradas IA totalmente personalizáveis. Simulação de encontros interativa com configurações de personalidade profundas e suporte NSFW.',
        'swipey_link': 'Visitar AI Swipey →',
        'nudify_desc': 'A ferramenta de desvestir IA mais avançada disponível. Faça upload de qualquer foto e gere resultados deepnude explícitos em segundos com alto realismo.',
        'nudify_link': 'Visitar AI Nudify →',
        'seduced_desc': 'Crie seu companheiro IA dos sonhos com personalização avançada.',
        'seduced_link': 'Visitar AI Seduced →',
    },
    'nl': {
        'soulgen_desc': 'Genereer verbluffende realistische en anime personages uit tekst. De krachtigste AI zielsverwant beeldcreator met face swap en videogeneratie.',
        'soulgen_link': 'Bezoek AI SoulGen →',
        'swipey_desc': 'Swipe, match en chat met volledig aanpasbare AI vriendinnen. Interactieve dating simulatie met diepe persoonlijkheidsinstellingen en NSFW ondersteuning.',
        'swipey_link': 'Bezoek AI Swipey →',
        'nudify_desc': 'De meest geavanceerde AI uitkleedtool beschikbaar. Upload elke foto en genereer expliciete deepnude resultaten in seconden met hoog realisme.',
        'nudify_link': 'Bezoek AI Nudify →',
        'seduced_desc': 'Creëer je droom AI metgezel met geavanceerde aanpassing.',
        'seduced_link': 'Bezoek AI Seduced →',
    },
    'pl': {
        'soulgen_desc': 'Generuj oszałamiające realistyczne i anime postacie z tekstu. Najpotężniejszy kreator obrazów bratniej duszy AI z face swap i generowaniem wideo.',
        'soulgen_link': 'Odwiedź AI SoulGen →',
        'swipey_desc': 'Przesuwaj, dopasowuj i czatuj z w pełni konfigurowalnymi dziewczynami AI. Interaktywna symulacja randkowa z głębokimi ustawieniami osobowości i wsparciem NSFW.',
        'swipey_link': 'Odwiedź AI Swipey →',
        'nudify_desc': 'Najbardziej zaawansowane narzędzie do rozbierania AI dostępne. Prześlij dowolne zdjęcie i generuj eksplicytne wyniki deepnude w ciągu sekund z wysokim realizmem.',
        'nudify_link': 'Odwiedź AI Nudify →',
        'seduced_desc': 'Stwórz wymarzonego towarzysza AI za pomocą zaawansowanej konfiguracji.',
        'seduced_link': 'Odwiedź AI Seduced →',
    },
    'ru': {
        'soulgen_desc': 'Генерируйте потрясающих реалистичных и аниме-персонажей из текста. Самый мощный создатель изображений ИИ-близнеца души с заменой лица и генерацией видео.',
        'soulgen_link': 'Посетить AI SoulGen →',
        'swipey_desc': 'Свайпай, мэтчь и общайся с полностью настраиваемыми девушками ИИ. Интерактивная симуляция свиданий с глубокими настройками личности и поддержкой NSFW.',
        'swipey_link': 'Посетить AI Swipey →',
        'nudify_desc': 'Самый продвинутый инструмент для раздевания ИИ. Загрузи любое фото и генерируй откровенные результаты deepnude за секунды с высоким реализмом.',
        'nudify_link': 'Посетить AI Nudify →',
        'seduced_desc': 'Создай своего ИИ-компаньона мечты с продвинутой настройкой.',
        'seduced_link': 'Посетить AI Seduced →',
    },
    'tr': {
        'soulgen_desc': 'Metinden çarpıcı gerçekçi ve anime karakterleri oluşturun. Yüz değiştirme ve video oluşturma özellikli en güçlü AI ruh eşi görüntü oluşturucu.',
        'soulgen_link': 'AI SoulGen Ziyaret Et →',
        'swipey_desc': 'Tamamen özelleştirilebilir AI kız arkadaşlarla kaydır, eşleş ve sohbet et. Derin kişilik ayarları ve NSFW desteğiyle etkileşimli flört simülasyonu.',
        'swipey_link': 'AI Swipey Ziyaret Et →',
        'nudify_desc': 'Mevcut en gelişmiş AI soyunma aracı. Herhangi bir fotoğrafı yükley ve yüksek gerçekçilikle saniyeler içinde açık deepnude sonuçları oluştur.',
        'nudify_link': 'AI Nudify Ziyaret Et →',
        'seduced_desc': 'Gelişmiş özelleştirme ile hayalindeki AI yoldaşını oluştur.',
        'seduced_link': 'AI Seduced Ziyaret Et →',
    },
    'kr': {
        'soulgen_desc': '텍스트에서 놀라운 사실적이고 애니메이션 캐릭터를 생성하세요. 페이스 스왑과 비디오 생성 기능을 갖춘 가장 강력한 AI 소울메이트 이미지 생성기.',
        'soulgen_link': 'AI SoulGen 방문 →',
        'swipey_desc': '완전히 사용자 정의 가능한 AI 여자친구들과 스와이프하고, 매칭하고, 채팅하세요. 깊은 성격 설정과 NSFW 지원이 있는 인터랙티브 데이팅 시뮬레이션.',
        'swipey_link': 'AI Swipey 방문 →',
        'nudify_desc': '사용 가능한 가장 고급 AI 옷 벗기기 도구. 모든 사진을 업로드하고 높은 사실감으로 몇 초 만에 노골적인 딥누드 결과를 생성하세요.',
        'nudify_link': 'AI Nudify 방문 →',
        'seduced_desc': '고급 사용자 정의 기능으로 꿈의 AI 동반자를 만드세요.',
        'seduced_link': 'AI Seduced 방문 →',
    },
    'ja': {
        'soulgen_desc': 'テキストから驚くべきリアルでアニメのキャラクターを生成します。フェイススワップとビデオ生成機能を備えた最も強力なAIソウルメイト画像クリエイター。',
        'soulgen_link': 'AI SoulGenを訪問 →',
        'swipey_desc': '完全にカスタマイズ可能なAI彼女たちとスワイプ、マッチ、チャット。深い性格設定とNSFWサポートを備えたインタラクティブなデートシミュレーション。',
        'swipey_link': 'AI Swipeyを訪問 →',
        'nudify_desc': '利用可能な最も高度なAI脱衣ツール。任意の写真をアップロードし、高いリアリズムで数秒で露骨なディープヌード結果を生成します。',
        'nudify_link': 'AI Nudifyを訪問 →',
        'seduced_desc': '高度なカスタマイズ機能で夢のAIコンパニオンを作成します。',
        'seduced_link': 'AI Seducedを訪問 →',
    },
    'hi': {
        'soulgen_desc': 'टेक्स्ट से शानदार यथार्थवादी और एनीमे कैरेक्टर आर्ट जेनरेट करें। फेस स्वैप और वीडियो जेनरेशन के साथ सबसे शक्तिशाली AI सोलमेट इमेज क्रिएटर।',
        'soulgen_link': 'AI SoulGen देखें →',
        'swipey_desc': 'पूरी तरह से अनुकूलन योग्य AI प्रेमिकाओं के साथ स्वाइप करें, मैच करें और चैट करें। गहरे व्यक्तित्व सेटिंग्स और NSFW समर्थन के साथ इंटरैक्टिव डेटिंग सिमुलेशन।',
        'swipey_link': 'AI Swipey देखें →',
        'nudify_desc': 'उपलब्ध सबसे उन्नत AI अनड्रेस टूल। कोई भी फोटो अपलोड करें और उच्च यथार्थवाद के साथ सेकंड में स्पष्ट डीपन्यूड परिणाम जेनरेट करें।',
        'nudify_link': 'AI Nudify देखें →',
        'seduced_desc': 'उन्नत अनुकूलन के साथ अपने सपनों का AI साथी बनाएं।',
        'seduced_link': 'AI Seduced देखें →',
    },
}

# Traductions du titre H1
title_trans = {
    'fr': 'Candy AI — Votre Parfaite<br><span class="gradient-text">Petite Amie IA</span><br>Sans Censure & Prête',
    'de': 'Candy AI — Ihre Perfekte<br><span class="gradient-text">KI-Freundin</span><br>Unzensiert & Bereit',
    'es': 'Candy AI — Tu Perfecta<br><span class="gradient-text">Novia IA</span><br>Sin Censura & Lista',
    'it': 'Candy AI — La Tua Perfetta<br><span class="gradient-text">Ragazza IA</span><br>Non Censurata & Pronta',
    'pt': 'Candy AI — Sua Perfeita<br><span class="gradient-text">Namorada IA</span><br>Sem Censura & Pronta',
    'nl': 'Candy AI — Jouw Perfecte<br><span class="gradient-text">AI Vriendin</span><br>Ongesensoreerd & Klaar',
    'pl': 'Candy AI — Twoja Idealna<br><span class="gradient-text">Dziewczyna AI</span><br>Bez Cenzury & Gotowa',
    'ru': 'Candy AI — Твоя Идеальная<br><span class="gradient-text">Девушка ИИ</span><br>Без Цензуры & Готова',
    'tr': 'Candy AI — Mükemmel<br><span class="gradient-text">AI Kız Arkadaşın</span><br>Sansürsüz & Hazır',
    'kr': 'Candy AI — 완벽한<br><span class="gradient-text">AI 여자친구</span><br>무삭제 & 준비 완료',
    'ja': 'Candy AI — 完璧な<br><span class="gradient-text">AI彼女</span><br>無修正 & 準備完了',
    'hi': 'Candy AI — आपकी परफेक्ट<br><span class="gradient-text">AI प्रेमिका</span><br>बिना सेंसर & तैयार',
}

for lang in LANGS:
    path = os.path.join(BASE, lang, 'index.html')
    if not os.path.exists(path):
        print(f"❌ {lang}: fichier non trouvé")
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    t = translations[lang]
    c = cluster_trans[lang]
    
    # 1. H1 Title
    old_title = 'Candy AI — Your Perfect<br><span class="gradient-text">AI Girlfriend</span><br>Uncensored & Ready'
    new_title = title_trans[lang]
    content = content.replace(old_title, new_title)
    
    # 2. Hero P1
    old_p1 = '<strong>Candy AI</strong> lets you design your perfect AI girlfriend from scratch. Her look, her voice, her personality. Then chat, call, and generate explicit photos — all in one place on the Candy AI platform.'
    content = content.replace(old_p1, t['hero_p1'])
    
    # 3. Hero P2
    old_p2 = '<strong>Candy AI</strong> gives you the most visually consistent and customizable AI companion available in 2026. With 11.6 million monthly active users, Candy AI is the #1 choice for AI girlfriend experiences. Try Candy AI free today — no credit card required.'
    content = content.replace(old_p2, t['hero_p2'])
    
    # 4. CTA Button
    old_cta = '🍬 Create Your AI Girlfriend Free'
    content = content.replace(old_cta, t['cta_btn'])
    
    # 5. Secondary CTA
    old_sec = 'Read Quality Review ↓'
    content = content.replace(old_sec, t['cta_secondary'])
    
    # 6. Hero note
    old_note = '✅ Free tier available &nbsp;•&nbsp; No credit card required &nbsp;•&nbsp; 18+ only'
    content = content.replace(old_note, t['hero_note'])
    
    # 7. Modal title
    old_modal = 'Get Started with Candy AI Porn'
    content = content.replace(old_modal, t['modal_title'])
    
    # 8. Cluster cards
    old_soulgen = 'Generate stunning realistic and anime character art from text. The most powerful AI soulmate image creator with face swap and video generation.'
    content = content.replace(old_soulgen, c['soulgen_desc'])
    
    old_soulgen_link = 'Visit AI SoulGen →'
    content = content.replace(old_soulgen_link, c['soulgen_link'])
    
    old_swipey = 'Swipe, match, and chat with fully customizable AI girlfriends. Interactive dating simulation with deep personality settings and NSFW support.'
    content = content.replace(old_swipey, c['swipey_desc'])
    
    old_swipey_link = 'Visit AI Swipey →'
    content = content.replace(old_swipey_link, c['swipey_link'])
    
    old_nudify = 'The most advanced AI undress tool available. Upload any photo and generate explicit deepnude results in seconds with high realism.'
    content = content.replace(old_nudify, c['nudify_desc'])
    
    old_nudify_link = 'Visit AI Nudify →'
    content = content.replace(old_nudify_link, c['nudify_link'])
    
    old_seduced = 'Create your dream AI companion with advanced customization.'
    content = content.replace(old_seduced, c['seduced_desc'])
    
    old_seduced_link = 'Visit AI Seduced →'
    content = content.replace(old_seduced_link, c['seduced_link'])
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {lang}: 3 sections traduites")

print("\n🎉 Toutes les sections ont été traduites dans les 12 langues!")
