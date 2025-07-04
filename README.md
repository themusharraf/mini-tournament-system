# 🏆 Mini Tournament System

Minimalist turnirlar va o'yinchilarni boshqarish backend ilovasi. Ushbu loyiha FastAPI asosida qurilgan bo‘lib, asinxron
SQLAlchemy, Alembic va Docker orqali zamonaviy backend arxitektura amaliyotlarini namoyon etadi.

---

## 🎯 Maqsad

> Turnirlar yaratish, ularga o'yinchilarni ro'yxatdan o'tkazish va ro'yxatga olingan ishtirokchilarni ko'rsatish
> funksiyalarini amalga oshiruvchi mini-backend API yaratish.

---

## 🧱 Arxitektura

## 📁 Loyihaning papka tuzilmasi

```bash
mini-tournament-system/
├── app/                  # Asosiy ilova logikasi
│   ├── api/              # Routerlar (API endpointlar)
│   ├── dependencies/     # FastAPI dependency funksiyalari
│   ├── models/           # SQLAlchemy ORM modellari
│   ├── schemas/          # Pydantic validatorlari (Request/Response DTO)
│   ├── services/         # Domen logika (biznes qoidalar)
│   ├── config.py         # Sozlamalar va ENV o‘qish
│   ├── db.py             # DB sessiyasi, engine konfiguratsiyasi
│   ├── logger.py         # Log konfiguratsiyasi
│   └── main.py           # FastAPI ilovasini ishga tushirish
├── alembic/              # Migratsiya fayllari
├── tests/                # Pytest test fayllari
├── logs/                 # Ilova log fayllari
├── Dockerfile            # Docker konteyner fayli
├── docker-compose.yml    # Servislarni orchestration qilish
├── pyproject.toml        # Build, lint, test va umumiy konfiguratsiyalar
├── requirements.txt      # Python kutubxonalar ro‘yxati
└── README.md             # Loyihaga oid hujjat
```

---

## 🚀 Ishlatilgan texnologiyalar

| Texnologiya          | Maqsadi                                 |
|----------------------|-----------------------------------------|
| Python 3.13+         | Asosiy dasturlash tili                  |
| FastAPI              | Asosiy web framework                    |
| Async SQLAlchemy 2.0 | Asinxron ORM                            |
| Alembic              | Migratsiyalar                           |
| Pydantic             | Validatsiya va seriyalizatsiya          |
| PostgreSQL           | Ma’lumotlar bazasi                      |
| Docker + Compose     | Konteynerlash va servis orkestratsiyasi |
| Mypy                 | Tip tekshiruvi                          |
| Ruff                 | Linting (yengil va tez)                 |
| Black                | Kod formatlash                          |
| Pytest               | Unit test framework                     |

---

## ⚙️ Ishga tushirish

### 1. Talablar:

- Docker & Docker Compose
- `make` komandasi (MacOS/Linux foydalanuvchilari uchun)

### 2. Ishga tushirish (Docker orqali)

```bash
cp .env_dist .env
docker-compose up --build
```

## ✅ Endpoints

API hujjatlar Swagger UI orqali:

📍 `http://localhost:8000/docs`

---

## 📂 Misol API imkoniyatlari

* `POST /tournaments/` – Yangi turnir yaratish
* `POST /tournaments/{id}/register` – Turnirga o'yinchi qo'shish
* `GET /tournaments/{id}/players` – Ro'yxatdan o‘tgan o'yinchilarni olish

---

## ✨ Kelajakdagi imkoniyatlar

* JWT autentifikatsiya qo‘shish
* Turnirlar tarixini loglash
* Admin interfeys

---

## 🤝 Hissa qo‘shish

Pull requestlar va issue'lar ochish orqali loyihani rivojlantirishda ishtirok etishingiz mumkin.

---

Made with ❤️ by [Musharraf Ibragimov](https://github.com/themusharraf)
