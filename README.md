# منصة TechVerse - النظام البيئي التقني الموحد

## 📋 نظرة عامة

TechVerse هي منصة متكاملة تجمع بين التعليم، العمل، التواصل، الابتكار، والتمويل في نظام بيئي واحد. تستخدم أحدث التقنيات مثل الذكاء الاصطناعي، البلوك تشين، والواقع المعزز لتقديم تجربة مستخدم فريدة.

## 🚀 الميزات الرئيسية

### 🎓 TechLearn - التعليم التفاعلي
- دورات تعليمية متقدمة
- شهادات NFT قابلة للتحقق
- تعلم تفاعلي مع مشاريع عملية

### 💼 TechMarket - السوق التجاري
- بيع وشراء الخدمات التقنية
- فرص عمل ومشاريع
- نظام تقييم ومراجعة

### 💬 TechConnect - التواصل المتقدم
- ترجمة فورية بين 100+ لغة
- اجتماعات افتراضية بالواقع المعزز
- تواصل آمن ومشفر

### 💡 TechInnovation - الابتكار المتقدم
- مختبرات افتراضية للابتكار
- حماية الملكية الفكرية
- سوق الابتكار المفتوح

### 💰 TechFinance - التمويل المتقدم
- تمويل جماعي للمشاريع
- محفظة رقمية متكاملة
- تحليلات مالية متقدمة

## 🛠️ التقنيات المستخدمة

### Backend
- **Python** مع FastAPI
- **قواعد بيانات**: MySQL, PostgreSQL, MongoDB, Redis
- **WebSocket** للتواصل الفوري
- **JWT** للمصادقة

### Frontend
- **React** مع TypeScript
- **Material-UI** للتصميم
- **Tailwind CSS** للأنماط
- **Redux** لإدارة الحالة

## 📁 هيكل المشروع

```
techverse/
├── backend/                 # تطبيق FastAPI
│   ├── app/
│   │   ├── models/         # نماذج قاعدة البيانات
│   │   ├── schemas/        # مخططات Pydantic
│   │   ├── api/           # واجهات API
│   │   ├── services/      # خدمات الأعمال
│   │   └── main.py        # نقطة الدخول
│   ├── requirements.txt   # تبعيات Python
│   └── Dockerfile        # تكوين Docker
├── frontend/              # تطبيق React
│   ├── src/
│   │   ├── pages/        # صفحات التطبيق
│   │   ├── components/   # مكونات React
│   │   ├── store/        # إدارة الحالة
│   │   └── main.tsx      # نقطة الدخول
│   ├── package.json      # تبعيات Node.js
│   └── Dockerfile        # تكوين Docker
├── docker-compose.yml    # تكوين الحاويات
└── README.md            # هذا الملف
```

## 🚀 التشغيل المحلي

### المتطلبات الأساسية
- Docker و Docker Compose
- Node.js 18+ (للتطوير)
- Python 3.11+ (للتطوير)

### التشغيل باستخدام Docker (مستحسن)

```bash
# استنساخ المشروع
git clone <repository-url>
cd techverse

# تشغيل جميع الخدمات
docker-compose up -d

# الوصول للتطبيق
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Documentation: http://localhost:8000/docs
```

### التشغيل للتطوير

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# أو venv\Scripts\activate  # Windows

pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 🌐 النشر على الاستضافة

### الاستضافات المجانية الموصى بها

#### 1. Railway (مستحسن)
- **المزايا**: مجاني للاستخدام الأساسي، دعم Docker، قاعدة بيانات مجانية
- **الرابط**: https://railway.app
- **التكلفة**: مجاني مع حدود معقولة

#### 2. Render
- **المزايا**: مجاني، دعم مستمر، سهولة النشر
- **الرابط**: https://render.com
- **التكلفة**: مجاني مع حدود

#### 3. Vercel (لـ Frontend)
- **المزايا**: مجاني، أداء ممتاز، CDN عالمي
- **الرابط**: https://vercel.com
- **التكلفة**: مجاني

#### 4. Heroku (بديل)
- **المزايا**: معروف، مجاني مع حدود
- **الرابط**: https://heroku.com
- **التكلفة**: مجاني مع حدود

### خطوات النشر على Railway

1. **إنشاء حساب على Railway**
   ```bash
   npm install -g @railway/cli
   railway login
   ```

2. **نشر Backend**
   ```bash
   cd backend
   railway init
   railway up
   ```

3. **نشر Frontend**
   ```bash
   cd frontend
   railway init
   railway up
   ```

4. **إعداد المتغيرات البيئية**
   - إضافة متغيرات البيئة في لوحة تحكم Railway
   - تكوين قواعد البيانات

## 🔧 التكوين

### المتغيرات البيئية

#### Backend (.env)
```env
DATABASE_URL=mysql+pymysql://user:pass@host/db
POSTGRES_URL=postgresql://user:pass@host/db
MONGODB_URL=mongodb://user:pass@host/db
REDIS_URL=redis://host:port
JWT_SECRET_KEY=your_secret_key
CORS_ORIGINS=http://localhost:3000
```

#### Frontend (.env)
```env
VITE_API_URL=https://your-backend.railway.app
VITE_WS_URL=wss://your-backend.railway.app
```

## 📊 قواعد البيانات

المشروع يستخدم 4 قواعد بيانات:

1. **MySQL**: البيانات الأساسية للمستخدمين والمشاريع
2. **PostgreSQL**: التحليلات والإحصائيات
3. **MongoDB**: البيانات غير المهيكلة والـ NoSQL
4. **Redis**: الذاكرة المؤقتة والجلسات

## 🔐 الأمان

- تشفير كلمات المرور باستخدام bcrypt
- مصادقة JWT
- CORS مكون بشكل آمن
- تحقق من صحة البيانات باستخدام Pydantic
- حماية من هجمات SQL Injection

## 🧪 الاختبار

```bash
# Backend Tests
cd backend
pytest

# Frontend Tests
cd frontend
npm test
```

## 🤝 المساهمة

1. Fork المشروع
2. إنشاء فرع للميزة الجديدة
3. Commit التغييرات
4. Push إلى الفرع
5. فتح Pull Request

## 📞 الدعم

للأسئلة والدعم:
- فتح Issue في GitHub
- التواصل عبر البريد الإلكتروني
- الانضمام لمجتمع TechVerse

## 📄 الرخصة

هذا المشروع مرخص تحت رخصة MIT.

## 🙏 الشكر

شكراً لجميع المساهمين في تطوير TechVerse!

---

**TechVerse** - إعادة تعريف النظام البيئي التقني 🌐