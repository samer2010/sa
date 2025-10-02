#!/usr/bin/env python3
"""
اختبار نظام TechVerse للتأكد من أن جميع المكونات تعمل بشكل صحيح
"""

import sys
import os

# إضافة مسار الـ backend إلى sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

def test_imports():
    """اختبار استيراد جميع المكونات الأساسية"""
    print("🔍 اختبار استيراد المكونات...")
    
    try:
        from app.main import app
        print("✅ FastAPI app تم استيراده بنجاح")
    except Exception as e:
        print(f"❌ خطأ في استيراد FastAPI app: {e}")
        return False
    
    try:
        from app.api import techfinance, techconnect, techinnovation, translation
        print("✅ جميع وحدات API تم استيرادها بنجاح")
    except Exception as e:
        print(f"❌ خطأ في استيراد وحدات API: {e}")
        return False
    
    try:
        from app.models import techfinance as tf_models, techconnect as tc_models, techinnovation as ti_models
        print("✅ جميع النماذج تم استيرادها بنجاح")
    except Exception as e:
        print(f"❌ خطأ في استيراد النماذج: {e}")
        return False
    
    try:
        from app.schemas import techfinance as tf_schemas, techconnect as tc_schemas, techinnovation as ti_schemas
        print("✅ جميع الـ schemas تم استيرادها بنجاح")
    except Exception as e:
        print(f"❌ خطأ في استيراد الـ schemas: {e}")
        return False
    
    return True

def test_routes():
    """اختبار وجود جميع المسارات في التطبيق"""
    print("\n🔍 اختبار المسارات...")
    
    try:
        from app.main import app
        
        routes = [route.path for route in app.routes]
        required_routes = [
            '/api/health',
            '/api/techfinance',
            '/api/techconnect', 
            '/api/techinnovation',
            '/api/translation'
        ]
        
        for route in required_routes:
            if any(route in r for r in routes):
                print(f"✅ المسار {route} موجود")
            else:
                print(f"❌ المسار {route} غير موجود")
                return False
                
        print("✅ جميع المسارات الأساسية موجودة")
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار المسارات: {e}")
        return False

def test_config():
    """اختبار إعدادات التطبيق"""
    print("\n🔍 اختبار الإعدادات...")
    
    try:
        from app.core.config import settings
        
        required_settings = [
            'DATABASE_URL',
            'REDIS_URL', 
            'MONGODB_URL',
            'SECRET_KEY',
            'DEBUG'
        ]
        
        for setting in required_settings:
            if hasattr(settings, setting):
                value = getattr(settings, setting)
                if value:
                    print(f"✅ الإعداد {setting} مضبوط: {value[:20]}..." if len(str(value)) > 20 else f"✅ الإعداد {setting} مضبوط: {value}")
                else:
                    print(f"⚠️  الإعداد {setting} موجود لكن فارغ")
            else:
                print(f"❌ الإعداد {setting} غير موجود")
                return False
                
        print("✅ جميع الإعدادات الأساسية مضبوطة")
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار الإعدادات: {e}")
        return False

def test_frontend_structure():
    """اختبار هيكل الـ frontend"""
    print("\n🔍 اختبار هيكل الـ frontend...")
    
    frontend_path = os.path.join(os.path.dirname(__file__), 'frontend')
    
    required_files = [
        'package.json',
        'vite.config.ts',
        'tsconfig.json',
        'src/App.tsx',
        'src/main.tsx',
        'src/pages/TechFinancePage.tsx',
        'src/pages/TechConnectPage.tsx',
        'src/pages/TechInnovationPage.tsx',
        'src/components/techfinance/WalletOverview.tsx',
        'src/components/techinnovation/InnovationLabCard.tsx',
        'src/components/techinnovation/InnovationProjectCard.tsx'
    ]
    
    all_files_exist = True
    for file in required_files:
        file_path = os.path.join(frontend_path, file)
        if os.path.exists(file_path):
            print(f"✅ ملف {file} موجود")
        else:
            print(f"❌ ملف {file} غير موجود")
            all_files_exist = False
    
    return all_files_exist

def main():
    """الدالة الرئيسية لاختبار النظام"""
    print("🚀 بدء اختبار نظام TechVerse...")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_routes,
        test_config,
        test_frontend_structure
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ خطأ غير متوقع في الاختبار: {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    print("📊 نتائج الاختبار:")
    
    passed = sum(results)
    total = len(results)
    
    print(f"✅ الاختبارات الناجحة: {passed}/{total}")
    print(f"❌ الاختبارات الفاشلة: {total - passed}/{total}")
    
    if passed == total:
        print("🎉 جميع الاختبارات نجحت! النظام جاهز للتشغيل.")
        print("\n📋 الخطوات التالية:")
        print("1. قم بتشغيل الـ backend: cd techverse/backend && uvicorn app.main:app --reload")
        print("2. قم بتشغيل الـ frontend: cd techverse/frontend && npm run dev")
        print("3. افتح المتصفح على http://localhost:5173")
        return 0
    else:
        print("⚠️  هناك مشاكل تحتاج للإصلاح قبل تشغيل النظام.")
        return 1

if __name__ == "__main__":
    exit(main())