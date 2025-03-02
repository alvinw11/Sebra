"""
Translation utilities and dictionaries for the Clinical Trial Analysis Platform.
"""

SUPPORTED_LANGUAGES = {
    'English': 'en',
    'Spanish (Español)': 'es',
    'French (Français)': 'fr',
    'German (Deutsch)': 'de',
    'Chinese (中文)': 'zh',
    'Japanese (日本語)': 'ja',
    'Polish (Polski)': 'pl',
    'Hindi (हिन्दी)': 'hi'
}

TRANSLATIONS = {
    'welcome_title': {
        'en': 'Welcome to OrangeCC',
        'es': 'Bienvenido a OrangeCC',
        'fr': 'Bienvenue sur OrangeCC',
        'de': 'Willkommen bei OrangeCC',
        'zh': '欢迎使用OrangeCC',
        'ja': 'OrangeCCにようこそ',
        'pl': 'Witaj na platformie OrangeCC',
        'hi': 'OrangeCC में आपका स्वागत है'
    },
    'language_selector': {
        'en': 'Select Language',
        'es': 'Seleccionar Idioma',
        'fr': 'Choisir la Langue',
        'de': 'Sprache Auswählen',
        'zh': '选择语言',
        'ja': '言語を選択する',
        'pl': 'Wybierz język',
        'hi': 'भाषा चुनें'
    },
    'login_title': {
        'en': 'Login',
        'es': 'Iniciar Sesión',
        'fr': 'Connexion',
        'de': 'Anmelden',
        'zh': '登录',
        'ja': 'ログイン',
        'pl': 'Zaloguj się',
        'hi': 'लॉग इन करें'
    },
    'username_prompt': {
        'en': 'Username',
        'es': 'Usuario',
        'fr': 'Nom d\'utilisateur',
        'de': 'Benutzername',
        'zh': '用户名',
        'ja': 'ユーザー名',
        'pl': 'Nazwa użytkownika',
        'hi': 'उपयोगकर्ता नाम'
    },
    'password_prompt': {
        'en': 'Password',
        'es': 'Contraseña',
        'fr': 'Mot de passe',
        'de': 'Passwort',
        'zh': '密码',
        'ja': 'パスワード',
        'pl': 'Hasło',
        'hi': 'पासवर्ड'
    },
    'sign_in': {
        'en': 'Sign In',
        'es': 'Entrar',
        'fr': 'Se Connecter',
        'de': 'Einloggen',
        'zh': '登录',
        'ja': 'ログイン',
        'pl': 'Zaloguj się',
        'hi': 'लॉग इन करें'
    },
    'medical_info_title': {
        'en': 'Medical Information Entry',
        'es': 'Ingreso de Información Médica',
        'fr': 'Saisie des Informations Médicales',
        'de': 'Eingabe medizinischer Informationen',
        'zh': '医疗信息录入',
        'ja': '医療情報入力',
        'pl': 'Wprowadzanie Informacji Medycznych',
        'hi': 'विद्यालय जानकारी दर्ज करें'
    },
    'upload_title': {
        'en': 'Document Upload',
        'es': 'Carga de Documentos',
        'fr': 'Téléchargement de Documents',
        'de': 'Dokumenten-Upload',
        'zh': '文档上传',
        'ja': 'ドキュメントアップロード',
        'pl': 'Przesyłanie Dokumentów',
        'hi': 'दस्तावेज़ अपलोड करें'
    },
    'analysis_start': {
        'en': 'Start Analysis',
        'es': 'Iniciar Análisis',
        'fr': 'Démarrer l\'Analyse',
        'de': 'Analyse Starten',
        'zh': '开始分析',
        'ja': '分析を開始する',
        'pl': 'Rozpoczęcie Analizy',
        'hi': 'विश्लेषण शुरू करें'
    },
    'results_title': {
        'en': 'Clinical Trial Sites',
        'es': 'Sitios de Ensayos Clínicos',
        'fr': 'Sites de Tests Cliniques',
        'de': 'Klinische Studienorte',
        'zh': '临床试验地点',
        'ja': 'クリニカルトライアルサイト',
        'pl': 'Lokalizacje Badan Klinicznych',
        'hi': 'क्लिनिकल ट्रायल साइट्स'
    },
    'active_diagnoses': {
        'en': 'Active Diagnoses',
        'es': 'Diagnósticos Activos',
        'fr': 'Diagnostics Actifs',
        'de': 'Aktive Diagnosen',
        'zh': '活跃诊断',
        'ja': 'アクティブな診断',
        'pl': 'Aktywne Diagnostyki',
        'hi': 'सक्रिय डायग्नस्टिक्स'
    },
    'past_conditions': {
        'en': 'Past Medical Conditions',
        'es': 'Condiciones Médicas Pasadas',
        'fr': 'Antécédents Médicaux',
        'de': 'Frühere Erkrankungen',
        'zh': '既往医疗条件',
        'ja': '過去の医療条件',
        'pl': 'Poprzednie Zdrowotne Stany',
        'hi': 'पिछले स्वास्थ्य स्थितियाँ'
    },
    'matching_trials': {
        'en': 'Matching Clinical Trials',
        'es': 'Ensayos Clínicos Coincidentes',
        'fr': 'Essais Cliniques Correspondants',
        'de': 'Passende Klinische Studien',
        'zh': '匹配的临床试验',
        'ja': '一致するクリニカルトライアル',
        'pl': 'Pasujące Badania Kliniczne',
        'hi': 'मेंटिंग क्लिनिकल ट्रायल्स'
    },
    'demographics': {
        'en': 'Demographics',
        'es': 'Demografía',
        'fr': 'Démographie',
        'de': 'Demografie',
        'zh': '人口统计',
        'ja': '人口統計',
        'pl': 'Demografia',
        'hi': 'जनसंख्या आँकड़े'
    },
    'vital_signs': {
        'en': 'Vital Signs',
        'es': 'Signos Vitales',
        'fr': 'Signes Vitaux',
        'de': 'Vitalzeichen',
        'zh': '生命体征',
        'ja': 'バイタルサイン',
        'pl': 'Parametry Życiowe',
        'hi': 'जीवन संकेत'
    },
    'medical_history': {
        'en': 'Medical History',
        'es': 'Historia Médica',
        'fr': 'Antécédents Médicaux',
        'de': 'Krankengeschichte',
        'zh': '病史',
        'ja': '病歴',
        'pl': 'Historia Medyczna',
        'hi': 'विद्यालय जानकारी'
    },
    'medications': {
        'en': 'Medications',
        'es': 'Medicamentos',
        'fr': 'Médicaments',
        'de': 'Medikamente',
        'zh': '药物',
        'ja': '薬物治療',
        'pl': 'Leki',
        'hi': 'दवाई'
    },
    'lab_results': {
        'en': 'Lab Results',
        'es': 'Resultados de Laboratorio',
        'fr': 'Résultats de Laboratoire',
        'de': 'Laborergebnisse',
        'zh': '化验结果',
        'ja': '検査結果',
        'pl': 'Wyniki Badań',
        'hi': 'लेब रिजल्ट्स'
    },
    'imaging': {
        'en': 'Imaging',
        'es': 'Imágenes Médicas',
        'fr': 'Imagerie',
        'de': 'Bildgebung',
        'zh': '影像学',
        'ja': '画像診断',
        'pl': 'Obrazowanie',
        'hi': 'इमेजिंग'
    },
    'procedures': {
        'en': 'Procedures',
        'es': 'Procedimientos',
        'fr': 'Procédures',
        'de': 'Eingriffe',
        'zh': '医疗程序',
        'ja': '処置',
        'pl': 'Procedury',
        'hi': 'प्रकार'
    },
    'lifestyle': {
        'en': 'Lifestyle',
        'es': 'Estilo de Vida',
        'fr': 'Mode de Vie',
        'de': 'Lebensstil',
        'zh': '生活方式',
        'ja': 'ライフスタイル',
        'pl': 'Styl Życia',
        'hi': 'जीवन शैली'
    },
    'family_history': {
        'en': 'Family History',
        'es': 'Historia Familiar',
        'fr': 'Antécédents Familiaux',
        'de': 'Familienanamnese',
        'zh': '家族史',
        'ja': '家族歴',
        'pl': 'Historia Rodzinna',
        'hi': 'परिवार इतिहास'
    },
    'rare_diseases': {
        'en': 'Rare Diseases',
        'es': 'Enfermedades Raras',
        'fr': 'Maladies Rares',
        'de': 'Seltene Krankheiten',
        'zh': '罕见疾病',
        'ja': '希少疾患',
        'pl': 'Choroby Rzadkie',
        'hi': 'असामान्य बीमारियाँ'
    },
    'date_of_birth': {
        'en': 'Date of Birth',
        'es': 'Fecha de Nacimiento',
        'fr': 'Date de Naissance',
        'de': 'Geburtsdatum',
        'zh': '出生日期',
        'ja': '生年月日',
        'pl': 'Data Urodzenia',
        'hi': 'जन्म तिथि'
    },
    'gender': {
        'en': 'Gender',
        'es': 'Género',
        'fr': 'Genre',
        'de': 'Geschlecht',
        'zh': '性别',
        'ja': '性別',
        'pl': 'Płeć',
        'hi': 'लिंग'
    },
    'gender_male': {
        'en': 'Male',
        'es': 'Masculino',
        'fr': 'Masculin',
        'de': 'Männlich',
        'zh': '男',
        'ja': '男性',
        'pl': 'Mężczyzna',
        'hi': 'पुरुष'
    },
    'gender_female': {
        'en': 'Female',
        'es': 'Femenino',
        'fr': 'Féminin',
        'de': 'Weiblich',
        'zh': '女',
        'ja': '女性',
        'pl': 'Kobieta',
        'hi': 'महिला'
    },
    'gender_other': {
        'en': 'Other',
        'es': 'Otro',
        'fr': 'Autre',
        'de': 'Andere',
        'zh': '其他',
        'ja': 'その他',
        'pl': 'Inne',
        'hi': 'अन्य'
    },
    'race/ethnicity': {
        'en': 'Race/Ethnicity',
        'es': 'Raza/Etnicidad',
        'fr': 'Race/Ethnicité',
        'de': 'Rasse/Ethnizität',
        'zh': '种族/人种',
        'ja': '民族/人種',
        'pl': 'Pochodzenie Etniczne',
        'hi': 'इंथनिक पूल'
    },
        'caucasian or white': {
        'en': 'Caucasian or White',
        'es': 'Caucasión o Blanca',
        'fr': 'Caucasien ou Blanc',
        'de': 'Kaukasisch oder Weiß',
        'zh': '高加索人或白人',
        'ja': 'カウカシアンまたは白人',
        'pl': 'Kaukazjański lub Biały',
        'hi': 'कुकासियन या सफेद'
    },
    'asian': {
        'en': 'Asian',
        'es': 'Asiático',
        'fr': 'Asiatique',
        'de': 'Asiatisch',
        'zh': '亚洲人',
        'ja': 'アジア人',
        'pl': 'Azjatycki',
        'hi': 'एशियन'
    },
    'black or african american': {
        'en': 'Black or African American',
        'es': 'Negro o Afroamericano',
        'fr': 'Noir ou Africain',
        'de': 'Schwarzer oder Afrikanischer',
        'zh': '黑人或非洲裔美国人',
        'ja': 'ブラックまたはアフリカアメリカン',
        'pl': 'Czarny lub Afrykański',
        'hi': 'ब्लैक या अफ्रीकी अमेरिकन'
    },
    'hispanic': {
        'en': 'Hispanic or Latino',
        'es': 'Hispano o Latino',
        'fr': 'Hispanique ou Latino',
        'de': 'Hispanisch oder Latino',
        'zh': '西班牙裔或拉丁裔',
        'ja': 'ヒスパニックまたはラテン系',
        'pl': 'Hiszpański lub Latynoski',
        'hi': 'हिस्पानिक या लेटिनो'
    },
    'other': {
        'en': 'Other',
        'es': 'Otro',
        'fr': 'Autre',
        'de': 'Andere',
        'zh': '其他',
        'ja': 'その他',
        'pl': 'Inne',
        'hi': 'अन्य'
    },
    'emergency_contact_name': {
        'en': 'Emergency Contact Name',
        'es': 'Nombre del Contacto de Emergencia',
        'fr': 'Nom du Contact d\'Urgence',
        'de': 'Name des Notfallkontakts',
        'zh': '紧急联系人姓名',
        'ja': '緊急連絡先名',
        'pl': 'Nazwa Kontaktu Awaryjnego',
        'hi': 'आंकड़े के नाम'
    },
    'emergency_contact_phone': {
        'en': 'Emergency Contact Phone',
        'es': 'Teléfono del Contacto de Emergencia',
        'fr': 'Téléphone du Contact d\'Urgence',
        'de': 'Telefon des Notfallkontakts',
        'zh': '紧急联系人电话',
        'ja': '緊急連絡先電話番号',
        'pl': 'Telefon Kontaktu Awaryjnego',
        'hi': 'आंकड़े के नाम'
    },
    'primary_care_physician': {
        'en': 'Primary Care Physician',
        'es': 'Médico de Atención Primaria',
        'fr': 'Médecin Traitant',
        'de': 'Hausarzt',
        'zh': '主治医生',
        'ja': 'かかりつけ医',
        'pl': 'Lekarz Pierwszego Kontaktu',
        'hi': 'प्रमुख कार्यालय चिकित्सक'
    },
    'insurance_provider': {
        'en': 'Insurance Provider',
        'es': 'Proveedor de Seguros',
        'fr': 'Assureur',
        'de': 'Versicherungsanbieter',
        'zh': '保险提供商',
        'ja': '保険会社',
        'pl': 'Ubezpieczyciel',
        'hi': 'बीमा प्रदाता'
    },
    'height': {
        'en': 'Height (cm)',
        'es': 'Altura (cm)',
        'fr': 'Taille (cm)',
        'de': 'Größe (cm)',
        'zh': '身高 (厘米)',
        'ja': '身長 (cm)',
        'pl': 'Wzrost (cm)',
        'hi': 'ऊंचाई (सेमी)'
    },
    'weight': {
        'en': 'Weight (kg)',
        'es': 'Peso (kg)',
        'fr': 'Poids (kg)',
        'de': 'Gewicht (kg)',
        'zh': '体重 (公斤)',
        'ja': '体重 (kg)',
        'pl': 'Waga (kg)',
        'hi': 'वजन (किलो)'
    },
    'body_temperature': {
        'en': 'Body Temperature (°C)',
        'es': 'Temperatura Corporal (°C)',
        'fr': 'Température Corporelle (°C)',
        'de': 'Körpertemperatur (°C)',
        'zh': '体温 (°C)',
        'ja': '体温 (°C)',
        'pl': 'Temperatura Ciała (°C)',
        'hi': 'शरीर तापमान (°C)'
    },
    'blood_pressure_systolic': {
        'en': 'Blood Pressure (Systolic)',
        'es': 'Presión Arterial (Sistólica)',
        'fr': 'Pression Artérielle (Systolique)',
        'de': 'Blutdruck (Systolisch)',
        'zh': '血压（收缩压）',
        'ja': '血圧（最高血圧）',
        'pl': 'Ciśnienie Krwi (Skurczowe)',
        'hi': 'शरीर तापमान'
    },
    'blood_pressure_diastolic': {
        'en': 'Blood Pressure (Diastolic)',
        'es': 'Presión Arterial (Diastólica)',
        'fr': 'Pression Artérielle (Diastolique)',
        'de': 'Blutdruck (Diastolisch)',
        'zh': '血压（舒张压）',
        'ja': '血圧（最低血圧）',
        'pl': 'Ciśnienie Krwi (Rozkurczowe)',
        'hi': 'शरीर तापमान'
    },
    'heart_rate': {
        'en': 'Heart Rate (bpm)',
        'es': 'Frecuencia Cardíaca (lpm)',
        'fr': 'Fréquence Cardiaque (bpm)',
        'de': 'Herzfrequenz (bpm)',
        'zh': '心率（次/分）',
        'ja': '心拍数（bpm）',
        'pl': 'Tętno (ud./min)',
        'hi': 'शरीर तापमान'
    },
    'respiratory_rate': {
        'en': 'Respiratory Rate (breaths/min)',
        'es': 'Frecuencia Respiratoria (resp/min)',
        'fr': 'Fréquence Respiratoire (resp/min)',
        'de': 'Atemfrequenz (Atemzüge/min)',
        'zh': '呼吸频率（次/分）',
        'ja': '呼吸数（回/分）',
        'pl': 'Częstość Oddechów (odd./min)',
        'hi': 'शरीर तापमान'
    },
    'current_medical_conditions': {
        'en': 'Current Medical Conditions',
        'es': 'Condiciones Médicas Actuales',
        'fr': 'Conditions Médicales Actuelles',
        'de': 'Aktuelle Medizinische Zustände',
        'zh': '当前医疗状况',
        'ja': '現在の健康状態',
        'pl': 'Obecne Schorzenia',
        'hi': 'शरीर तापमान'
    },
    'past_medical_history': {
        'en': 'Past Medical History',
        'es': 'Historia Médica Pasada',
        'fr': 'Antécédents Médicaux',
        'de': 'Frühere Krankengeschichte',
        'zh': '既往病史',
        'ja': '既往歴',
        'pl': 'Historia Chorób',
        'hi': 'शरीर तापमान'
    },
    'previous_conditions': {
        'en': 'Previous Conditions',
        'es': 'Condiciones Anteriores',
        'fr': 'Conditions Précédentes',
        'de': 'Vorherige Erkrankungen',
        'zh': '既往病症',
        'ja': '既往症',
        'pl': 'Przebyte Choroby',
        'hi': 'शरीर तापमान'
    },
    'allergies_adverse_reactions': {
        'en': 'Allergies and Adverse Reactions',
        'es': 'Alergias y Reacciones Adversas',
        'fr': 'Allergies et Réactions Indésirables',
        'de': 'Allergien und Unerwünschte Reaktionen',
        'zh': '过敏和不良反应',
        'ja': 'アレルギーと副作用',
        'pl': 'Alergie i Reakcje Niepożądane',
        'hi': 'शरीर तापमान'
    },
    'medication_allergies': {
        'en': 'Medication Allergies',
        'es': 'Alergias a Medicamentos',
        'fr': 'Allergies aux Médicaments',
        'de': 'Medikamentenallergien',
        'zh': '药物过敏',
        'ja': '薬物アレルギー',
        'pl': 'Alergie na Leki',
        'hi': 'शरीर तापमान'
    },
    'reaction_description': {
        'en': 'Reaction Description',
        'es': 'Descripción de la Reacción',
        'fr': 'Description de la Réaction',
        'de': 'Beschreibung der Reaktion',
        'zh': '反应描述',
        'ja': '反応の説明',
        'pl': 'Opis Reakcji',
        'hi': 'शरीर तापमान'
    },
    'immunizations': {
        'en': 'Immunizations',
        'es': 'Inmunizaciones',
        'fr': 'Vaccinations',
        'de': 'Impfungen',
        'zh': '免疫接种',
        'ja': '予防接種',
        'pl': 'Szczepienia',
        'hi': 'शरीर तापमान'
    },
    'vaccination_history': {
        'en': 'Vaccination History',
        'es': 'Historial de Vacunación',
        'fr': 'Historique des Vaccinations',
        'de': 'Impfgeschichte',
        'zh': '疫苗接种史',
        'ja': 'ワクチン接種歴',
        'pl': 'Historia Szczepień',
        'hi': 'शरीर तापमान'
    },
    'current_medications': {
        'en': 'Current Medications',
        'es': 'Medicamentos Actuales',
        'fr': 'Médicaments Actuels',
        'de': 'Aktuelle Medikamente',
        'zh': '当前用药',
        'ja': '現在の投薬',
        'pl': 'Obecne Leki',
        'hi': 'शरीर तापमान'
    },
    'medication_name': {
        'en': 'Medication Name',
        'es': 'Nombre del Medicamento',
        'fr': 'Nom du Médicament',
        'de': 'Medikamentenname',
        'zh': '药物名称',
        'ja': '薬剤名',
        'pl': 'Nazwa Leku',
        'hi': 'शरीर तापमान'
    },
    'dosage': {
        'en': 'Dosage',
        'es': 'Dosis',
        'fr': 'Posologie',
        'de': 'Dosierung',
        'zh': '剂量',
        'ja': '用量',
        'pl': 'Dawkowanie',
        'hi': 'शरीर तापमान'
    },
    'frequency': {
        'en': 'Frequency',
        'es': 'Frecuencia',
        'fr': 'Fréquence',
        'de': 'Häufigkeit',
        'zh': '频率',
        'ja': '服用頻度',
        'pl': 'Częstotliwość',
        'hi': 'शरीर तापमान'
    },
    'once_daily': {
        'en': 'Once daily',
        'es': 'Una vez al día',
        'fr': 'Une fois par jour',
        'de': 'Einmal täglich',
        'zh': '每日一次',
        'ja': '1日1回',
        'pl': 'Raz dziennie',
        'hi': 'शरीर तापमान'
    },
    'twice_daily': {
        'en': 'Twice daily',
        'es': 'Dos veces al día',
        'fr': 'Deux fois par jour',
        'de': 'Zweimal täglich',
        'zh': '每日两次',
        'ja': '1日2回',
        'pl': 'Dwa razy dziennie',
        'hi': 'शरीर तापमान'
    },
    'three_times_daily': {
        'en': 'Three times daily',
        'es': 'Tres veces al día',
        'fr': 'Trois fois par jour',
        'de': 'Dreimal täglich',
        'zh': '每日三次',
        'ja': '1日3回',
        'pl': 'Trzy razy dziennie',
        'hi': 'शरीर तापमान'
    },
    'four_times_daily': {
        'en': 'Four times daily',
        'es': 'Cuatro veces al día',
        'fr': 'Quatre fois par jour',
        'de': 'Viermal täglich',
        'zh': '每日四次',
        'ja': '1日4回',
        'pl': 'Cztery razy dziennie',
        'hi': 'शरीर तापमान'
    },
    'as_needed': {
        'en': 'As needed',
        'es': 'Según sea necesario',
        'fr': 'Au besoin',
        'de': 'Nach Bedarf',
        'zh': '按需',
        'ja': '必要に応じて',
        'pl': 'W razie potrzeby',
        'hi': 'शरीर तापमान'
    },
    'weekly': {
        'en': 'Weekly',
        'es': 'Semanal',
        'fr': 'Hebdomadaire',
        'de': 'Wöchentlich',
        'zh': '每周',
        'ja': '週1回',
        'pl': 'Tygodniowo',
        'hi': 'शरीर तापमान'
    },
    'monthly': {
        'en': 'Monthly',
        'es': 'Mensual',
        'fr': 'Mensuel',
        'de': 'Monatlich',
        'zh': '每月',
        'ja': '月1回',
        'pl': 'Miesięcznie',
        'hi': 'शरीर तापमान'
    },
    'past_medications': {
        'en': 'Past Medications',
        'es': 'Medicamentos Anteriores',
        'fr': 'Médicaments Antérieurs',
        'de': 'Frühere Medikamente',
        'zh': '既往用药',
        'ja': '過去の投薬',
        'pl': 'Poprzednie Leki',
        'hi': 'शरीर तापमान'
    },
    'previous_medications_history': {
        'en': 'Previous Medications History',
        'es': 'Historial de Medicamentos Anteriores',
        'fr': 'Historique des Médicaments Antérieurs',
        'de': 'Frühere Medikamentengeschichte',
        'zh': '既往用药史',
        'ja': '過去の投薬歴',
        'pl': 'Historia Poprzednich Leków',
        'hi': 'शरीर तापमान'
    },
    'recent_laboratory_results': {
        'en': 'Recent Laboratory Results',
        'es': 'Resultados Recientes de Laboratorio',
        'fr': 'Résultats Récents de Laboratoire',
        'de': 'Aktuelle Laborergebnisse',
        'zh': '近期化验结果',
        'ja': '最近の検査結果',
        'pl': 'Ostatnie Wyniki Laboratoryjne',
        'hi': 'शरीर तापमान'
    },
    'complete_blood_count': {
        'en': 'Complete Blood Count (CBC)',
        'es': 'Hemograma Completo',
        'fr': 'Numération Formule Sanguine (NFS)',
        'de': 'Komplettes Blutbild',
        'zh': '全血细胞计数',
        'ja': '全血球計算（CBC）',
        'pl': 'Morfologia Krwi',
        'hi': 'शरीर तापमान'
    },
    'hemoglobin': {
        'en': 'Hemoglobin (g/dL)',
        'es': 'Hemoglobina (g/dL)',
        'fr': 'Hémoglobine (g/dL)',
        'de': 'Hämoglobin (g/dL)',
        'zh': '血红蛋白 (g/dL)',
        'ja': 'ヘモグロビン (g/dL)',
        'pl': 'Hemoglobina'
    },
    'white_blood_cell_count': {
        'en': 'White Blood Cell Count (K/µL)',
        'es': 'Recuento de Glóbulos Blancos (K/µL)',
        'fr': 'Numération des Globules Blancs (K/µL)',
        'de': 'Leukozyten (K/µL)',
        'zh': '白细胞计数 (K/µL)',
        'ja': '白血球数 (K/µL)',
        'pl': 'Liczba Krwinek Białych (K/µL)',
        'hi': 'शरीर तापमान'
    },
    'platelet_count': {
        'en': 'Platelet Count (K/µL)',
        'es': 'Recuento de Plaquetas (K/µL)',
        'fr': 'Numération des Plaquettes (K/µL)',
        'de': 'Thrombozyten (K/µL)',
        'zh': '血小板计数 (K/µL)',
        'ja': '血小板数 (K/µL)',
        'pl': 'Liczba Płytek Krwi (K/µL)',
        'hi': 'शरीर तापमान'
    },
    'test_date': {
        'en': 'Test Date',
        'es': 'Fecha del Análisis',
        'fr': 'Date du Test',
        'de': 'Testdatum',
        'zh': '检测日期',
        'ja': '検査日',
        'pl': 'Data Badania',
        'hi': 'शरीर तापमान'
    },
    'basic_metabolic_panel': {
        'en': 'Basic Metabolic Panel',
        'es': 'Panel Metabólico Básico',
        'fr': 'Bilan Métabolique de Base',
        'de': 'Basis-Stoffwechselprofil',
        'zh': '基础代谢检查',
        'ja': '基本代謝パネル',
        'pl': 'Podstawowy Panel Metaboliczny',
        'hi': 'शरीर तापमान'
    },
    'glucose': {
        'en': 'Glucose (mg/dL)',
        'es': 'Glucosa (mg/dL)',
        'fr': 'Glucose (mg/dL)',
        'de': 'Glukose (mg/dL)',
        'zh': '血糖 (mg/dL)',
        'ja': '血糖値 (mg/dL)',
        'pl': 'Glukoza (mg/dL)',
        'hi': 'शरीर तापमान'
    },
    'creatinine': {
        'en': 'Creatinine (mg/dL)',
        'es': 'Creatinina (mg/dL)',
        'fr': 'Créatinine (mg/dL)',
        'de': 'Kreatinin (mg/dL)',
        'zh': '肌酐 (mg/dL)',
        'ja': 'クレアチニン (mg/dL)',
        'pl': 'Kreatynina (mg/dL)',
        'hi': 'शरीर तापमान'
    },
    'sodium': {
        'en': 'Sodium (mEq/L)',
        'es': 'Sodio (mEq/L)',
        'fr': 'Sodium (mEq/L)',
        'de': 'Natrium (mEq/L)',
        'zh': '钠 (mEq/L)',
        'ja': 'ナトリウム (mEq/L)',
        'pl': 'Sód (mEq/L)',
        'hi': 'शरीर तापमान'
    },
    'potassium': {
        'en': 'Potassium (mEq/L)',
        'es': 'Potasio (mEq/L)',
        'fr': 'Potassium (mEq/L)',
        'de': 'Kalium (mEq/L)',
        'zh': '钾 (mEq/L)',
        'ja': 'カリウム (mEq/L)',
        'pl': 'Potas (mEq/L)',
        'hi': 'शरीर तापमान'
    },
    'imaging_studies': {
        'en': 'Imaging Studies',
        'es': 'Estudios de Imagen',
        'fr': 'Études d\'Imagerie',
        'de': 'Bildgebende Untersuchungen',
        'zh': '画像检查',
        'ja': '画像検査',
        'pl': 'Badania Obrazowe',
        'hi': 'शरीर तापमान'
    },
    'study_date': {
        'en': 'Study Date',
        'es': 'Fecha del Estudio',
        'fr': 'Date de l\'Étude',
        'de': 'Untersuchungsdatum',
        'zh': '检查日期',
        'ja': '検査日',
        'pl': 'Data Badania',
        'hi': 'शरीर तापमान'
    },
    'body_region': {
        'en': 'Body Region',
        'es': 'Región del Cuerpo',
        'fr': 'Région du Corps',
        'de': 'Körperregion',
        'zh': '身体部位',
        'ja': '身体部位',
        'pl': 'Region Ciała',
        'hi': 'शरीर तापमान'
    },
    'findings': {
        'en': 'Findings',
        'es': 'Hallazgos',
        'fr': 'Résultats',
        'de': 'Befunde',
        'zh': '结论',
        'ja': '所見',
        'pl': 'Wyniki',
        'hi': 'शरीर तापमान'
    },
    'surgical_procedures': {
        'en': 'Surgical Procedures',
        'es': 'Procedimientos Quirúrgicos',
        'fr': 'Procédures Chirurgicales',
        'de': 'Chirurgische Eingriffe',
        'zh': '手术操作',
        'ja': '手術処置',
        'pl': 'Zabiegi Chirurgiczne',
        'hi': 'शरीर तापमान'
    },
    'procedure_name': {
        'en': 'Procedure Name',
        'es': 'Nombre del Procedimiento',
        'fr': 'Nom de la Procédure',
        'de': 'Name des Eingriffs',
        'zh': '手术名称',
        'ja': '処置名',
        'pl': 'Nazwa Zabiegu',
        'hi': 'शरीर तापमान'
    },
    'procedure_date': {
        'en': 'Procedure Date',
        'es': 'Fecha del Procedimiento',
        'fr': 'Date de la Procédure',
        'de': 'Datum des Eingriffs',
        'zh': '手术日期',
        'ja': '処置日',
        'pl': 'Data Zabiegu',
        'hi': 'शरीर तापमान'
    },
    'procedure_notes': {
        'en': 'Procedure Notes',
        'es': 'Notas del Procedimiento',
        'fr': 'Notes de Procédure',
        'de': 'Eingriffsnotizen',
        'zh': '手术记录',
        'ja': '処置記録',
        'pl': 'Notatki z Zabiegu',
        'hi': 'शरीर तापमान'
    },
    'other_procedures': {
        'en': 'Other Procedures',
        'es': 'Otros Procedimientos',
        'fr': 'Autres Procédures',
        'de': 'Andere Eingriffe',
        'zh': '其他操作',
        'ja': 'その他の処置',
        'pl': 'Inne Zabiegi',
        'hi': 'शरीर तापमान'
    },
    'non_surgical_procedures': {
        'en': 'Non-surgical procedures and interventions',
        'es': 'Procedimientos e intervenciones no quirúrgicos',
        'fr': 'Procédures et interventions non chirurgicales',
        'de': 'Nicht-chirurgische Eingriffe und Interventionen',
        'zh': '非手术操作和介入',
        'ja': '非手術的処置と介入',
        'pl': 'Zabiegi i interwencje nieoperacyjne',
        'hi': 'शरीर तापमान'
    },
    'smoking_status': {
        'en': 'Smoking Status',
        'es': 'Estado de Fumador',
        'fr': 'Statut Tabagique',
        'de': 'Raucherstatus',
        'zh': '吸烟状态',
        'ja': '喫煙状況',
        'pl': 'Status Palenia',
        'hi': 'शराब का सेवन'
    },
    'never': {
        'en': 'Never',
        'es': 'Nunca',
        'fr': 'Jamais',
        'de': 'Nie',
        'zh': '从不',
        'ja': '吸わない',
        'pl': 'Nigdy',
        'hi': 'शरीर तापमान'
    },
    'former': {
        'en': 'Former',
        'es': 'Ex-fumador',
        'fr': 'Ancien',
        'de': 'Ehemalig',
        'zh': '已戒烟',
        'ja': '以前吸っていた',
        'pl': 'Były Palacz',
        'hi': 'शरीर तापमान'
    },
    'current': {
        'en': 'Current',
        'es': 'Actual',
        'fr': 'Actuel',
        'de': 'Aktuell',
        'zh': '目前吸烟',
        'ja': '現在吸っている',
        'pl': 'Obecnie',
        'hi': 'शरीर तापमान'
    },
    'years_of_smoking': {
        'en': 'Years of smoking',
        'es': 'Años fumando',
        'fr': 'Années de tabagisme',
        'de': 'Jahre des Rauchens',
        'zh': '吸烟年数',
        'ja': '喫煙年数',
        'pl': 'Lata palenia',
        'hi': 'शरीर तापमान'
    },
    'cigarettes_per_day': {
        'en': 'Cigarettes per day',
        'es': 'Cigarrillos por día',
        'fr': 'Cigarettes par jour',
        'de': 'Zigaretten pro Tag',
        'zh': '每日吸烟量',
        'ja': '1日の喫煙本数',
        'pl': 'Papierosy dziennie',
        'hi': 'शरीर तापमान'
    },
    'physical_activity_level': {
        'en': 'Physical Activity Level',
        'es': 'Nivel de Actividad Física',
        'fr': 'Niveau d\'Activité Physique',
        'de': 'Körperliche Aktivität',
        'zh': '体力活动水平',
        'ja': '身体活動レベル',
        'pl': 'Poziom Aktywności Fizycznej',
        'hi': 'शरीर तापमान'
    },
    'sedentary': {
        'en': 'Sedentary',
        'es': 'Sedentario',
        'fr': 'Sédentaire',
        'de': 'Sitzend',
        'zh': '久坐不动',
        'ja': '座りがち',
        'pl': 'Siedzący',
        'hi': 'शरीर तापमान'
    },
    'light': {
        'en': 'Light',
        'es': 'Ligero',
        'fr': 'Léger',
        'de': 'Leicht',
        'zh': '轻度',
        'ja': '軽い',
        'pl': 'Lekki',
        'hi': 'शरीर तापमान'
    },
    'moderate': {
        'en': 'Moderate',
        'es': 'Moderado',
        'fr': 'Modéré',
        'de': 'Mäßig',
        'zh': '中度',
        'ja': '中程度',
        'pl': 'Umiarkowany',
        'hi': 'शरीर तापमान'
    },
    'very_active': {
        'en': 'Very Active',
        'es': 'Muy Activo',
        'fr': 'Très Actif',
        'de': 'Sehr Aktiv',
        'zh': '非常活跃',
        'ja': '非常に活動的',
        'pl': 'Bardzo Aktywny',
        'hi': 'बहुत सक्रिय'
    },
    'extremely_active': {
        'en': 'Extremely Active',
        'es': 'Extremadamente Activo',
        'fr': 'Extrêmement Actif',
        'de': 'Extrem Aktiv',
        'zh': '极度活跃',
        'ja': '極めて活動的',
        'pl': 'Wyjątkowo Aktywny',
        'hi': 'अत्यंत सक्रिय'
    },
    'alcohol_consumption': {
        'en': 'Alcohol Consumption',
        'es': 'Consumo de Alcohol',
        'fr': 'Consommation d\'Alcool',
        'de': 'Alkoholkonsum',
        'zh': '饮酒情况',
        'ja': '飲酒',
        'pl': 'Spożycie Alkoholu',
        'hi': 'शराब का सेवन'
    },
    'none': {
        'en': 'None',
        'es': 'Ninguno',
        'fr': 'Aucun',
        'de': 'Keiner',
        'zh': '无',
        'ja': 'なし',
        'pl': 'Brak',
        'hi': 'कुछ नहीं'
    },
    'occasional': {
        'en': 'Occasional',
        'es': 'Ocasional',
        'fr': 'Occasionnel',
        'de': 'Gelegentlich',
        'zh': '偶尔',
        'ja': '時々',
        'pl': 'Okazjonalnie',
        'hi': 'कभी-कभी'
    },
    'regular': {
        'en': 'Regular',
        'es': 'Regular',
        'fr': 'Régulier',
        'de': 'Regelmäßig',
        'zh': '经常',
        'ja': '定期的',
        'pl': 'Regularnie',
        'hi': 'नियमित'
    },
    'drinks_per_week': {
        'en': 'Drinks per week',
        'es': 'Bebidas por semana',
        'fr': 'Verres par semaine',
        'de': 'Getränke pro Woche',
        'zh': '每周饮酒量',
        'ja': '週の飲酒量',
        'pl': 'Drinki tygodniowo',
        'hi': 'प्रति सप्ताह पेय'
    },
    'dietary_restrictions': {
        'en': 'Dietary Restrictions',
        'es': 'Restricciones Dietéticas',
        'fr': 'Restrictions Alimentaires',
        'de': 'Ernährungseinschränkungen',
        'zh': '饮食限制',
        'ja': '食事制限',
        'pl': 'Ograniczenia Żywieniowe',
        'hi': 'आहार संबंधी प्रतिबंध'
    },
    'family_member_history': {
        'en': '%s\'s History',
        'es': 'Historia de %s',
        'fr': 'Antécédents de %s',
        'de': 'Krankengeschichte von %s',
        'zh': '%s的病史',
        'ja': '%sの病歴',
        'pl': 'Historia %s',
        'hi': '%s का इतिहास'
    },
    'mother': {
        'en': 'Mother',
        'es': 'Madre',
        'fr': 'Mère',
        'de': 'Mutter',
        'zh': '母亲',
        'ja': '母',
        'pl': 'Matka',
        'hi': 'माता'
    },
    'father': {
        'en': 'Father',
        'es': 'Padre',
        'fr': 'Père',
        'de': 'Vater',
        'zh': '父亲',
        'ja': '父',
        'pl': 'Ojciec',
        'hi': 'पिता'
    },
    'siblings': {
        'en': 'Siblings',
        'es': 'Hermanos',
        'fr': 'Frères et Sœurs',
        'de': 'Geschwister',
        'zh': '兄弟姐妹',
        'ja': '兄弟姉妹',
        'pl': 'Rodzeństwo',
        'hi': 'भाई-बहन'
    },
    'children': {
        'en': 'Children',
        'es': 'Hijos',
        'fr': 'Enfants',
        'de': 'Kinder',
        'zh': '子女',
        'ja': '子供',
        'pl': 'Dzieci',
        'hi': 'बच्चे'
    },
    'grandparents': {
        'en': 'Grandparents',
        'es': 'Abuelos',
        'fr': 'Grands-parents',
        'de': 'Großeltern',
        'zh': '祖父母',
        'ja': '祖父母',
        'pl': 'Dziadkowie',
        'hi': 'दादा-दादी/नाना-नानी'
    },
    'medical_conditions': {
        'en': 'Medical Conditions - %s',
        'es': 'Condiciones Médicas - %s',
        'fr': 'Conditions Médicales - %s',
        'de': 'Medizinische Zustände - %s',
        'zh': '%s的医疗状况',
        'ja': '%sの健康状態',
        'pl': 'Schorzenia - %s',
        'hi': 'चिकित्सा स्थिति - %s'
    },
    'additional_details': {
        'en': 'Additional Details - %s',
        'es': 'Detalles Adicionales - %s',
        'fr': 'Détails Supplémentaires - %s',
        'de': 'Weitere Details - %s',
        'zh': '%s的其他详情',
        'ja': '%sの追加詳細',
        'pl': 'Dodatkowe Informacje - %s',
        'hi': 'अतिरिक्त विवरण - %s'
    },
    'heart_disease': {
        'en': 'Heart Disease',
        'es': 'Enfermedad Cardíaca',
        'fr': 'Maladie Cardiaque',
        'de': 'Herzerkrankung',
        'zh': '心脏病',
        'ja': '心臓病',
        'pl': 'Choroba Serca',
        'hi': 'हृदय रोग'
    },
    'diabetes': {
        'en': 'Diabetes',
        'es': 'Diabetes',
        'fr': 'Diabète',
        'de': 'Diabetes',
        'zh': '糖尿病',
        'ja': '糖尿病',
        'pl': 'Cukrzyca',
        'hi': 'मधुमेह'
    },
    'cancer': {
        'en': 'Cancer',
        'es': 'Cáncer',
        'fr': 'Cancer',
        'de': 'Krebs',
        'zh': '癌症',
        'ja': 'がん',
        'pl': 'Nowotwór',
        'hi': 'कैंसर'
    },
    'hypertension': {
        'en': 'Hypertension',
        'es': 'Hipertensión',
        'fr': 'Hypertension',
        'de': 'Bluthochdruck',
        'zh': '高血压',
        'ja': '高血圧',
        'pl': 'Nadciśnienie',
        'hi': 'उच्च रक्तचाप'
    },
    'stroke': {
        'en': 'Stroke',
        'es': 'Accidente Cerebrovascular',
        'fr': 'AVC',
        'de': 'Schlaganfall',
        'zh': '中风',
        'ja': '脳卒中',
        'pl': 'Udar',
        'hi': 'स्ट्रोक'
    },
    'mental_health_conditions': {
        'en': 'Mental Health Conditions',
        'es': 'Condiciones de Salud Mental',
        'fr': 'Troubles de Santé Mentale',
        'de': 'Psychische Erkrankungen',
        'zh': '精神健康状况',
        'ja': '精神疾患',
        'pl': 'Zaburzenia Psychiczne',
        'hi': 'मानसिक स्वास्थ्य स्थितियां'
    },
    'diagnosed_rare_diseases': {
        'en': 'Diagnosed Rare Diseases',
        'es': 'Enfermedades Raras Diagnosticadas',
        'fr': 'Maladies Rares Diagnostiquées',
        'de': 'Diagnostizierte Seltene Krankheiten',
        'zh': '已确诊罕见病',
        'ja': '診断された希少疾患',
        'pl': 'Zdiagnozowane Choroby Rzadkie',
        'hi': 'निदान की गई दुर्लभ बीमारियां'
    },
    'additional_notes_diagnosed': {
        'en': 'Additional Notes on Diagnosed Conditions',
        'es': 'Notas Adicionales sobre Condiciones Diagnosticadas',
        'fr': 'Notes Supplémentaires sur les Conditions Diagnostiquées',
        'de': 'Zusätzliche Hinweise zu Diagnostizierten Erkrankungen',
        'zh': '已确诊病症的补充说明',
        'ja': '診断された状態に関する追加メモ',
        'pl': 'Dodatkowe Uwagi o Zdiagnozowanych Schorzeniach',
        'hi': 'निदान की गई स्थितियों पर अतिरिक्त टिप्पणियां'
    },
    'suspected_rare_diseases': {
        'en': 'Suspected Rare Diseases',
        'es': 'Enfermedades Raras Sospechadas',
        'fr': 'Maladies Rares Suspectées',
        'de': 'Vermutete Seltene Krankheiten',
        'zh': '疑似罕见病',
        'ja': '疑われる希少疾患',
        'pl': 'Podejrzewane Choroby Rzadkie',
        'hi': 'संदिग्ध दुर्लभ बीमारियां'
    },
    'symptoms_observations': {
        'en': 'Symptoms and Observations',
        'es': 'Síntomas y Observaciones',
        'fr': 'Symptômes et Observations',
        'de': 'Symptome und Beobachtungen',
        'zh': '症状和观察',
        'ja': '症状と観察',
        'pl': 'Objawy i Obserwacje',
        'hi': 'लक्षण और टिप्पणियां'
    },
    'genetic_testing': {
        'en': 'Genetic Testing',
        'es': 'Pruebas Genéticas',
        'fr': 'Tests Génétiques',
        'de': 'Genetische Tests',
        'zh': '基因检测',
        'ja': '遺伝子検査',
        'pl': 'Badania Genetyczne',
        'hi': 'आनुवंशिक परीक्षण'
    },
    'genetic_testing_status': {
        'en': 'Genetic Testing Status',
        'es': 'Estado de Pruebas Genéticas',
        'fr': 'Statut des Tests Génétiques',
        'de': 'Status der Genetischen Tests',
        'zh': '基因检测状态',
        'ja': '遺伝子検査状況',
        'pl': 'Status Badań Genetycznych',
        'hi': 'आनुवंशिक परीक्षण की स्थिति'
    },
    'not_done': {
        'en': 'Not Done',
        'es': 'No Realizado',
        'fr': 'Non Effectué',
        'de': 'Nicht Durchgeführt',
        'zh': '未完成',
        'ja': '未実施',
        'pl': 'Nie Wykonano',
        'hi': 'नहीं किया गया'
    },
    'scheduled': {
        'en': 'Scheduled',
        'es': 'Programado',
        'fr': 'Programmé',
        'de': 'Geplant',
        'zh': '已预约',
        'ja': '予定済み',
        'pl': 'Zaplanowano',
        'hi': 'निर्धारित'
    },
    'completed': {
        'en': 'Completed',
        'es': 'Completado',
        'fr': 'Terminé',
        'de': 'Abgeschlossen',
        'zh': '已完成',
        'ja': '完了',
        'pl': 'Ukończono',
        'hi': 'पूर्ण'
    },
    'testing_date': {
        'en': 'Testing Date',
        'es': 'Fecha de la Prueba',
        'fr': 'Date du Test',
        'de': 'Testdatum',
        'zh': '检测日期',
        'ja': '検査日',
        'pl': 'Data Badania',
        'hi': 'परीक्षण की तिथि'
    },
    'genetic_testing_results': {
        'en': 'Genetic Testing Results',
        'es': 'Resultados de Pruebas Genéticas',
        'fr': 'Résultats des Tests Génétiques',
        'de': 'Ergebnisse der Genetischen Tests',
        'zh': '基因检测结果',
        'ja': '遺伝子検査結果',
        'pl': 'Wyniki Badań Genetycznych',
        'hi': 'आनुवंशिक परीक्षण के परिणाम'
    },
    'family_genetic_conditions': {
        'en': 'Family History of Genetic Conditions',
        'es': 'Historia Familiar de Condiciones Genéticas',
        'fr': 'Antécédents Familiaux de Conditions Génétiques',
        'de': 'Familiengeschichte Genetischer Erkrankungen',
        'zh': '家族遗传病史',
        'ja': '遺伝性疾患の家族歴',
        'pl': 'Historia Rodzinna Chorób Genetycznych',
        'hi': 'आनुवंशिक स्थितियों का पारिवारिक इतिहास'
    },
    'analysis_controls': {
        'en': 'Analysis Controls',
        'es': 'Controles de Análisis',
        'fr': 'Contrôles d\'Analyse',
        'de': 'Analyse-Steuerungen',
        'zh': '分析控制',
        'ja': '分析制御',
        'pl': 'Kontrole Analizy',
        'hi': 'विश्लेषण नियंत्रण'
    },
    'select_analysis_type': {
        'en': 'Select Analysis Type',
        'es': 'Seleccionar Tipo de Análisis',
        'fr': 'Sélectionner le Type d\'Analyse',
        'de': 'Analysetyp auswählen',
        'zh': '选择分析类型',
        'ja': '分析タイプを選択',
        'pl': 'Wybierz Typ Analizy',
        'hi': 'विश्लेषण प्रकार चुनें',
    },
    'basic_match': {
        'en': 'Basic Match',
        'es': 'Coincidencia Básica',
        'fr': 'Correspondance de Base',
        'de': 'Grundlegendes Übereinstimmung',
        'zh': '基本匹配',
        'ja': '基本一致',
        'pl': 'Podstawowa Dopasowanie',
        'hi': 'बेसिक मैच'
    },
    'comprehensive_match': {
        'en': 'Comprehensive Match',
        'es': 'Coincidencia Completa',
        'fr': 'Correspondance Complète',
        'de': 'Vollständige Übereinstimmung',
        'zh': '全面匹配',
        'ja': '完全一致',
        'pl': 'Pełne Dopasowanie',
        'hi': 'पूर्ण मैच'
    },
    'advanced_match': {
        'en': 'Advanced Match with Preferences',
        'es': 'Coincidencia Avanzada con Preferencias',
        'fr': 'Correspondance Avancée avec Préférences',
        'de': 'Erweiterte Übereinstimmung mit Präferenzen',
        'zh': '高级匹配偏好',
        'ja': '高度なマッチングの優先順位',
        'pl': 'Zaawansowane Dopasowanie z Preferencjami',
        'hi': 'उन्नत मैच प्राथमिकताओं के साथ'
    },
    'maximum_distance': {
        'en': 'Maximum Distance to Trial Location (km)',
        'es': 'Distancia Máxima a la Ubicación de la Prueba (km)',
        'fr': 'Distance Maximale à la Location du Test (km)',
        'de': 'Maximale Entfernung zur Versuchsstandort (km)',
        'zh': '最大距离到试验地点（公里）',
        'ja': '最大距離を試験場所に (km)',
        'pl': 'Maksymalna Odległość do Lokalizacji Badania (km)',
        'hi': 'अधिकतम दूरी परीक्षण स्थान के लिए (किमी)'
    },
    'include_pending_trials': {
        'en': 'Include Pending Trials',
        'es': 'Incluir Pruebas Pendientes',
        'fr': 'Inclure les essais en attente',
        'de': 'Einschließen von Ausstehenden Studien',
        'zh': '包含待定试验',
        'ja': '保留試験を含める',
        'pl': 'Uwzględnij badania oczekujące',
        'hi': 'अपेक्षित परीक्षण शामिल करें'
    },
    'include_remote_trials': {
        'en': 'Include Remote Trials',
        'es': 'Incluir Pruebas Remotas',
        'fr': 'Inclure les essais distants',
        'de': 'Fernstudien einschließen',
        'zh': '包含远程试验',
        'ja': '遠隔試験を含める',
        'pl': 'Uwzględnij badania zdalne',
        'hi': 'रिमोट परीक्षण शामिल करें'
    },
    'add_diagnosis': {
        'en': 'Add Diagnosis',
        'es': 'Añadir Diagnóstico',
        'fr': 'Ajouter un Diagnostic',
        'de': 'Diagnose Hinzufügen',
        'zh': '添加诊断',
        'ja': '診断を追加',
        'pl': 'Dodaj Diagnozę',
        'hi': 'निदान जोड़ें'
    },
    'remove_diagnosis': {
        'en': 'Remove this diagnosis',
        'es': 'Eliminar este diagnóstico',
        'fr': 'Supprimer ce diagnostic',
        'de': 'Diese Diagnose entfernen',
        'zh': '删除此诊断',
        'ja': 'この診断を削除',
        'pl': 'Usuń tę diagnozę',
        'hi': 'यह निदान हटाएं'
    },
    'diagnosis': {
        'en': 'Diagnosis',
        'es': 'Diagnóstico',
        'fr': 'Diagnostic',
        'de': 'Diagnose',
        'zh': '诊断',
        'ja': '診断',
        'pl': 'Diagnoza',
        'hi': 'निदान'
    },
    'active_diagnoses': {
        'en': 'Active Diagnoses',
        'es': 'Diagnósticos Activos',
        'fr': 'Diagnostics Actifs',
        'de': 'Aktive Diagnosen',
        'zh': '活跃诊断',
        'ja': 'アクティブな診断',
        'pl': 'Aktywne Diagnostyki',
        'hi': 'सक्रिय निदान'
    },
    'past_medical_history': {
        'en': 'Past Medical History',
        'es': 'Historia Médica Pasada',
        'fr': 'Historique Médical Passé',
        'de': 'Vergangene Medizinische Geschichte',
        'zh': '过去医疗历史',
        'ja': '過去の医療歴史',
        'pl': 'Historia Medyczna Przeszłości',
        'hi': 'पिछली चिकित्सा इतिहास'
    },
    'current_medical_conditions': {
        'en': 'Current Medical Conditions',
        'es': 'Condiciones Médicas Actuales',
        'fr': 'Conditions Médicales Actuelles',
        'de': 'Aktuelle Medizinische Beschwerden',
        'zh': '当前医疗状况',
        'ja': '現在の医療状態',
        'pl': 'Aktualne Stany Zdrowia',
        'hi': 'वर्तमान चिकित्सा स्थितियां'
    },
    'add_immunization': {
        'en': 'Add Immunization',
        'es': 'Añadir Vacuna',
        'fr': 'Ajouter une Vaccination',
        'de': 'Impfung hinzufügen',
        'zh': '添加疫苗接种',
        'ja': 'ワクチン接種を追加',
        'pl': 'Dodaj Immunizację',
        'hi': 'टीका लागू करें'
    },
    'immunizations': {
        'en': 'Immunizations',
        'es': 'Vacunas',
        'fr': 'Vaccinations',
        'de': 'Impfungen',
        'zh': '疫苗接种',
        'ja': 'ワクチン接種',
        'pl': 'Immunizacje',
        'hi': 'टीका लागू करें'
     },
     'save_imaging': {
        'en': 'Save Imaging Studies',
        'es': 'Guardar Estudios de Imágenes',
        'fr': 'Enregistrer les Études d\'Imagerie',
        'de': 'Bilderstudien speichern',
        'zh': '保存影像研究',
        'ja': '画像研究を保存',
        'pl': 'Zapisz badania obrazowe',
        'hi': 'छवि अध्ययनों को सहेजें'
    },
    'imaging_saved': {
        'en': 'Imaging studies saved successfully!',
        'es': 'Estudios de imágenes guardados exitosamente!',
        'fr': 'Études d\'imagerie enregistrées avec succès!',
        'de': 'Bilderstudien erfolgreich gespeichert!',
        'zh': '影像研究保存成功！',
        'ja': '画像研究を保存しました！',
        'pl': 'Badania obrazowe zapisane pomyślnie!',
        'hi': 'छवि अध्ययनों को सहेजें सफलतापूर्वक!'
    },
    'save_procedures': {
        'en': 'Save Surgical Procedures',
        'es': 'Guardar Procedimientos Quirúrgicos',
        'fr': 'Enregistrer les Procédures Chirurgicales',
        'de': 'Operationen speichern',
        'zh': '保存手术程序',
        'ja': '手術手順を保存',
        'pl': 'Zapisz procedury operacyjne',
        'hi': 'सर्जरी प्रकार सहेजें'
    },
    'procedures_saved': {
        'en': 'Surgical procedures saved successfully!',
        'es': 'Procedimientos quirúrgicos guardados exitosamente!',
        'fr': 'Procédures chirurgicales enregistrées avec succès!',
        'de': 'Operationen erfolgreich gespeichert!',
        'zh': '手术程序保存成功！',
        'ja': '手術手順を保存しました！',
        'pl': 'Procedury operacyjne zapisane pomyślnie!',
        'hi': 'सर्जरी प्रकार सहेजें सफलतापूर्वक!'
    },
    'surgical_procedures': {
        'en': 'Surgical Procedures',
        'es': 'Procedimientos Quirúrgicos',
        'fr': 'Procédures Chirurgicales',
        'de': 'Chirurgische Verfahren',
        'zh': '手术程序',
        'ja': '手術手順',
        'pl': 'Procedury operacyjne',
        'hi': 'सर्जरी प्रकार'
    },
    'save_medications': {
        'en': 'Save Medications',
        'es': 'Guardar Medicamentos',
        'fr': 'Enregistrer les Médicaments',
        'de': 'Medikamente speichern',
        'zh': '保存药物',
        'ja': '薬を保存',
        'pl': 'Zapisz leki',
        'hi': 'दवाई सहेजें'
    },
    'medications_saved': {
        'en': 'Medications saved successfully!',
        'es': 'Medicamentos guardados exitosamente!',
        'fr': 'Médicaments enregistrés avec succès!',
        'de': 'Medikamente erfolgreich gespeichert!',
        'zh': '药物保存成功！',
        'ja': '薬を保存しました！',
        'pl': 'Leki zapisane pomyślnie!',
        'hi': 'दवाई सहेजें सफलतापूर्वक!'
    },
    'medications': {
        'en': 'Medications',
        'es': 'Medicamentos',
        'fr': 'Médicaments',
        'de': 'Medikamente',
        'zh': '药物',
        'ja': '薬',
        'pl': 'Leki',
        'hi': 'दवाई'
    },
    'save_lab_results': {
        'en': 'Save Lab Results',
        'es': 'Guardar Resultados de Laboratorio',
        'fr': 'Enregistrer les Résultats de Laboratoire',
        'de': 'Laborergebnisse speichern',
        'zh': '保存实验室结果',
        'ja': '実験室の結果を保存',
        'pl': 'Zapisz wyniki badań laboratoryjnych',
        'hi': 'प्रयोगशाला परिणामों को सहेजें'
    },
    'lab_results_saved': {
        'en': 'Lab results saved successfully!',
        'es': 'Resultados de laboratorio guardados exitosamente!',
        'fr': 'Résultats de laboratoire enregistrés avec succès!',
        'de': 'Laborergebnisse erfolgreich gespeichert!',
        'zh': '实验室结果保存成功！',
        'ja': '実験室の結果を保存しました！',
        'pl': 'Wyniki badań laboratoryjnych zapisane pomyślnie!',
        'hi': 'प्रयोगशाला परिणामों को सहेजें सफलतापूर्वक!'
    },
    'lab_results': {
        'en': 'Lab Results',
        'es': 'Resultados de Laboratorio',
        'fr': 'Résultats de Laboratoire',
        'de': 'Laborergebnisse',
        'zh': '实验室结果',
        'ja': '実験室の結果',
        'pl': 'Wyniki badań laboratoryjnych',
        'hi': 'प्रयोगशाला परिणामों'
    },
    'save_lifestyle': {
        'en': 'Save Lifestyle',
        'es': 'Guardar Vida Cotidiana',
        'fr': 'Enregistrer la Vie Cotidienne',
        'de': 'Lebensstil speichern',
        'zh': '保存生活方式',
        'ja': '生活習慣を保存',
        'pl': 'Zapisz tryb życia',
        'hi': 'जीवनवारंग सहेजें'
    },
    'lifestyle_saved': {
        'en': 'Lifestyle saved successfully!',
        'es': 'Vida cotidiana guardada exitosamente!',
        'fr': 'Vie quotidienne enregistrée avec succès!',
        'de': 'Lebensstil erfolgreich gespeichert!',
        'zh': '生活方式保存成功！',
        'ja': '生活習慣を保存しました！',
        'pl': 'Tryb życia zapisany pomyślnie!',
        'hi': 'जीवनवारंग सहेजें सफलतापूर्वक!'
    },
    'lifestyle': {
        'en': 'Lifestyle',
        'es': 'Vida Cotidiana',
        'fr': 'Vie Quotidienne',
        'de': 'Lebensstil',
        'zh': '生活方式',
        'ja': '生活習慣',
        'pl': 'Tryb życia',
        'hi': 'जीवनवारंग'
    },
    'save_family_history': {
        'en': 'Save Family History',
        'es': 'Guardar Historia Familiar',
        'fr': 'Enregistrer l\'Histoire Familiale',
        'de': 'Familienhistorie speichern',
        'zh': '保存家族历史',
        'ja': '家族の歴史を保存',
        'pl': 'Zapisz historię rodziny',
        'hi': 'परिवार का इतिहास सहेजें'
    },
    'family_history_saved': {
        'en': 'Family history saved successfully!',
        'es': 'Historia familiar guardada exitosamente!',
        'fr': 'Histoire familiale enregistrée avec succès!',
        'de': 'Familienhistorie erfolgreich gespeichert!',
        'zh': '家族历史保存成功！',
        'ja': '家族の歴史を保存しました！',
        'pl': 'Historia rodzinna zapisana pomyślnie!',
        'hi': 'परिवार का इतिहास सहेजें सफलतापूर्वक!'
    },
    'family_history': {
        'en': 'Family History',
        'es': 'Historia Familiar',
        'fr': 'Histoire Familiale',
        'de': 'Familienhistorie',
        'zh': '家族历史',
        'ja': '家族の歴史',
        'pl': 'Historia Rodzinna',
        'hi': 'परिवार का इतिहास'
    },
    'save_rare_diseases': {
        'en': 'Save Rare Diseases Information',
        'es': 'Guardar Información de Enfermedades Raras',
        'fr': 'Enregistrer les Informations sur les Maladies Rares',
        'de': 'Informationen über seltene Krankheiten speichern',
        'zh': '保存罕见疾病信息',
        'ja': '珍しい病気の情報を保存',
        'pl': 'Zapisz informacje o rzadkich chorobach',
        'hi': 'असामान्य बीमारियों की जानकारी सहेजें'
    },
    'rare_diseases_saved': {
        'en': 'Rare diseases information saved successfully!',
        'es': 'Información de enfermedades raras guardada exitosamente!',
        'fr': 'Informations sur les maladies rares enregistrées avec succès!',
        'de': 'Informationen über seltene Krankheiten erfolgreich gespeichert!',
        'zh': '罕见疾病信息保存成功！',
        'ja': '珍しい病気の情報を保存しました！',
        'pl': 'Informacje o rzadkich chorobach zapisane pomyślnie!',
        'hi': 'असामान्य बीमारियों की जानकारी सहेजें सफलतापूर्वक!'
    },
    'rare_diseases': {
        'en': 'Rare Diseases',
        'es': 'Enfermedades Raras',
        'fr': 'Maladies Rares',
        'de': 'Seltene Krankheiten',
        'zh': '罕见疾病',
        'ja': '珍しい病気',
        'pl': 'Rzadkie Choroby',
        'hi': 'असामान्य बीमारियों'
    }
}

def get_translation(key: str, language: str) -> str:
    """
    Get the translation for a given key in the specified language.
    
    Args:
        key (str): The translation key to look up
        language (str): The language code (e.g., 'en', 'es', 'fr', 'de')
        
    Returns:
        str: The translated text, or the key itself if translation is not found
    """
    if key in TRANSLATIONS and language in TRANSLATIONS[key]:
        return TRANSLATIONS[key][language]
    return key 