#!/usr/bin/env python3
"""
Comprehensive System Test for TechVerse Platform
This script tests all major components of the TechVerse platform
"""

import sys
import os
import requests
import json
import time
from datetime import datetime

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

class TechVerseSystemTest:
    def __init__(self):
        self.base_url = "http://localhost:8000/api/v1"
        self.access_token = None
        self.refresh_token = None
        self.user_id = None
        self.test_results = []
        
    def log_test(self, test_name, success, message=""):
        """Log test result"""
        result = {
            "test": test_name,
            "success": success,
            "message": message,
            "timestamp": datetime.now().isoformat()
        }
        self.test_results.append(result)
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}: {message}")
        
    def run_all_tests(self):
        """Run all system tests"""
        print("🚀 Starting TechVerse Comprehensive System Test")
        print("=" * 60)
        
        # Test sequence
        self.test_health_check()
        self.test_auth_system()
        self.test_user_management()
        self.test_techfinance_system()
        self.test_techconnect_system()
        self.test_techinnovation_system()
        self.test_translation_system()
        self.test_security_features()
        
        # Generate report
        self.generate_report()
        
    def test_health_check(self):
        """Test API health endpoint"""
        try:
            response = requests.get(f"{self.base_url}/health")
            if response.status_code == 200:
                self.log_test("Health Check", True, "API is running")
            else:
                self.log_test("Health Check", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_test("Health Check", False, f"Error: {str(e)}")
    
    def test_auth_system(self):
        """Test authentication system"""
        print("\n🔐 Testing Authentication System...")
        
        # Test registration
        user_data = {
            "email": f"test_{int(time.time())}@techverse.com",
            "username": f"testuser_{int(time.time())}",
            "password": "SecurePassword123!",
            "full_name": "System Test User",
            "phone_number": "+1234567890",
            "language": "en"
        }
        
        try:
            # Register
            response = requests.post(f"{self.base_url}/auth/register", json=user_data)
            if response.status_code == 200:
                self.log_test("User Registration", True, "User registered successfully")
            else:
                self.log_test("User Registration", False, f"Status: {response.status_code}")
                return
                
            # Login
            login_data = {
                "username": user_data["username"],
                "password": user_data["password"]
            }
            response = requests.post(f"{self.base_url}/auth/login", data=login_data)
            if response.status_code == 200:
                data = response.json()
                self.access_token = data["access_token"]
                self.refresh_token = data["refresh_token"]
                self.log_test("User Login", True, "Login successful")
            else:
                self.log_test("User Login", False, f"Status: {response.status_code}")
                return
                
            # Test token refresh
            if self.refresh_token:
                response = requests.post(f"{self.base_url}/auth/refresh", 
                                       json={"refresh_token": self.refresh_token})
                if response.status_code == 200:
                    self.log_test("Token Refresh", True, "Token refreshed successfully")
                else:
                    self.log_test("Token Refresh", False, f"Status: {response.status_code}")
                    
            # Test get current user
            headers = {"Authorization": f"Bearer {self.access_token}"}
            response = requests.get(f"{self.base_url}/auth/me", headers=headers)
            if response.status_code == 200:
                user_data = response.json()
                self.user_id = user_data["id"]
                self.log_test("Get Current User", True, "User data retrieved")
            else:
                self.log_test("Get Current User", False, f"Status: {response.status_code}")
                
        except Exception as e:
            self.log_test("Authentication System", False, f"Error: {str(e)}")
    
    def test_user_management(self):
        """Test user management features"""
        print("\n👤 Testing User Management...")
        
        if not self.access_token:
            self.log_test("User Management", False, "No access token available")
            return
            
        headers = {"Authorization": f"Bearer {self.access_token}"}
        
        try:
            # Test update profile
            update_data = {
                "full_name": "Updated Test User",
                "phone_number": "+1987654321"
            }
            response = requests.put(f"{self.base_url}/auth/me", 
                                  json=update_data, headers=headers)
            if response.status_code == 200:
                self.log_test("Update Profile", True, "Profile updated successfully")
            else:
                self.log_test("Update Profile", False, f"Status: {response.status_code}")
                
            # Test change password
            password_data = {
                "current_password": "SecurePassword123!",
                "new_password": "NewSecurePassword123!"
            }
            response = requests.post(f"{self.base_url}/auth/change-password",
                                   json=password_data, headers=headers)
            if response.status_code == 200:
                self.log_test("Change Password", True, "Password changed successfully")
            else:
                self.log_test("Change Password", False, f"Status: {response.status_code}")
                
        except Exception as e:
            self.log_test("User Management", False, f"Error: {str(e)}")
    
    def test_techfinance_system(self):
        """Test TechFinance features"""
        print("\n💰 Testing TechFinance System...")
        
        if not self.access_token:
            self.log_test("TechFinance", False, "No access token available")
            return
            
        headers = {"Authorization": f"Bearer {self.access_token}"}
        
        try:
            # Test wallet operations
            response = requests.get(f"{self.base_url}/techfinance/wallet", headers=headers)
            if response.status_code == 200:
                self.log_test("Get Wallet", True, "Wallet data retrieved")
            else:
                self.log_test("Get Wallet", False, f"Status: {response.status_code}")
                
            # Test transactions
            response = requests.get(f"{self.base_url}/techfinance/transactions", headers=headers)
            if response.status_code == 200:
                self.log_test("Get Transactions", True, "Transactions retrieved")
            else:
                self.log_test("Get Transactions", False, f"Status: {response.status_code}")
                
            # Test investments
            response = requests.get(f"{self.base_url}/techfinance/investments", headers=headers)
            if response.status_code == 200:
                self.log_test("Get Investments", True, "Investments retrieved")
            else:
                self.log_test("Get Investments", False, f"Status: {response.status_code}")
                
        except Exception as e:
            self.log_test("TechFinance System", False, f"Error: {str(e)}")
    
    def test_techconnect_system(self):
        """Test TechConnect features"""
        print("\n💬 Testing TechConnect System...")
        
        if not self.access_token:
            self.log_test("TechConnect", False, "No access token available")
            return
            
        headers = {"Authorization": f"Bearer {self.access_token}"}
        
        try:
            # Test chat rooms
            response = requests.get(f"{self.base_url}/techconnect/chat-rooms", headers=headers)
            if response.status_code == 200:
                self.log_test("Get Chat Rooms", True, "Chat rooms retrieved")
            else:
                self.log_test("Get Chat Rooms", False, f"Status: {response.status_code}")
                
            # Test collaboration projects
            response = requests.get(f"{self.base_url}/techconnect/collaboration-projects", headers=headers)
            if response.status_code == 200:
                self.log_test("Get Collaboration Projects", True, "Projects retrieved")
            else:
                self.log_test("Get Collaboration Projects", False, f"Status: {response.status_code}")
                
        except Exception as e:
            self.log_test("TechConnect System", False, f"Error: {str(e)}")
    
    def test_techinnovation_system(self):
        """Test TechInnovation features"""
        print("\n💡 Testing TechInnovation System...")
        
        if not self.access_token:
            self.log_test("TechInnovation", False, "No access token available")
            return
            
        headers = {"Authorization": f"Bearer {self.access_token}"}
        
        try:
            # Test innovation labs
            response = requests.get(f"{self.base_url}/techinnovation/labs", headers=headers)
            if response.status_code == 200:
                self.log_test("Get Innovation Labs", True, "Labs retrieved")
            else:
                self.log_test("Get Innovation Labs", False, f"Status: {response.status_code}")
                
            # Test innovation projects
            response = requests.get(f"{self.base_url}/techinnovation/projects", headers=headers)
            if response.status_code == 200:
                self.log_test("Get Innovation Projects", True, "Projects retrieved")
            else:
                self.log_test("Get Innovation Projects", False, f"Status: {response.status_code}")
                
        except Exception as e:
            self.log_test("TechInnovation System", False, f"Error: {str(e)}")
    
    def test_translation_system(self):
        """Test Translation features"""
        print("\n🌐 Testing Translation System...")
        
        if not self.access_token:
            self.log_test("Translation", False, "No access token available")
            return
            
        headers = {"Authorization": f"Bearer {self.access_token}"}
        
        try:
            # Test translation
            translation_data = {
                "text": "Hello, world!",
                "target_language": "ar",
                "source_language": "en"
            }
            response = requests.post(f"{self.base_url}/translation/translate",
                                   json=translation_data, headers=headers)
            if response.status_code == 200:
                self.log_test("Text Translation", True, "Text translated successfully")
            else:
                self.log_test("Text Translation", False, f"Status: {response.status_code}")
                
            # Test supported languages
            response = requests.get(f"{self.base_url}/translation/languages", headers=headers)
            if response.status_code == 200:
                self.log_test("Get Languages", True, "Languages retrieved")
            else:
                self.log_test("Get Languages", False, f"Status: {response.status_code}")
                
        except Exception as e:
            self.log_test("Translation System", False, f"Error: {str(e)}")
    
    def test_security_features(self):
        """Test security features"""
        print("\n🔒 Testing Security Features...")
        
        if not self.access_token:
            self.log_test("Security", False, "No access token available")
            return
            
        headers = {"Authorization": f"Bearer {self.access_token}"}
        
        try:
            # Test security settings
            response = requests.get(f"{self.base_url}/auth/security/settings", headers=headers)
            if response.status_code == 200:
                self.log_test("Get Security Settings", True, "Settings retrieved")
            else:
                self.log_test("Get Security Settings", False, f"Status: {response.status_code}")
                
            # Test login history
            response = requests.get(f"{self.base_url}/auth/login-history", headers=headers)
            if response.status_code == 200:
                self.log_test("Get Login History", True, "History retrieved")
            else:
                self.log_test("Get Login History", False, f"Status: {response.status_code}")
                
            # Test invalid token
            invalid_headers = {"Authorization": "Bearer invalid_token"}
            response = requests.get(f"{self.base_url}/auth/me", headers=invalid_headers)
            if response.status_code == 401:
                self.log_test("Invalid Token Protection", True, "Invalid token rejected")
            else:
                self.log_test("Invalid Token Protection", False, f"Status: {response.status_code}")
                
        except Exception as e:
            self.log_test("Security Features", False, f"Error: {str(e)}")
    
    def generate_report(self):
        """Generate test report"""
        print("\n" + "=" * 60)
        print("📊 TEST REPORT SUMMARY")
        print("=" * 60)
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result["success"])
        failed_tests = total_tests - passed_tests
        
        print(f"Total Tests: {total_tests}")
        print(f"✅ Passed: {passed_tests}")
        print(f"❌ Failed: {failed_tests}")
        print(f"📈 Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        # Show failed tests
        if failed_tests > 0:
            print("\n🔍 Failed Tests:")
            for result in self.test_results:
                if not result["success"]:
                    print(f"  - {result['test']}: {result['message']}")
        
        # Save detailed report
        report = {
            "summary": {
                "total_tests": total_tests,
                "passed_tests": passed_tests,
                "failed_tests": failed_tests,
                "success_rate": (passed_tests/total_tests)*100,
                "timestamp": datetime.now().isoformat()
            },
            "detailed_results": self.test_results
        }
        
        with open("system_test_report.json", "w") as f:
            json.dump(report, f, indent=2)
            
        print(f"\n📄 Detailed report saved to: system_test_report.json")
        
        # Overall status
        if failed_tests == 0:
            print("\n🎉 ALL TESTS PASSED! System is ready for deployment.")
        else:
            print(f"\n⚠️  {failed_tests} test(s) failed. Please check the issues above.")

if __name__ == "__main__":
    # Check if backend is running
    try:
        response = requests.get("http://localhost:8000/api/v1/health", timeout=5)
    except:
        print("❌ Backend server is not running. Please start the backend first.")
        print("   Command: uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload")
        sys.exit(1)
    
    # Run tests
    tester = TechVerseSystemTest()
    tester.run_all_tests()