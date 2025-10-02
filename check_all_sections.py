#!/usr/bin/env python3
"""
Comprehensive TechVerse Platform Testing Script
Tests all sections and functionality of the TechVerse platform
"""

import requests
import json
import time
import sys
from typing import Dict, List, Tuple

class TechVerseTester:
    def __init__(self):
        self.base_url = "http://localhost:8000"
        self.frontend_url = "http://localhost:3003"
        self.session = requests.Session()
        
    def test_backend_api(self, endpoint: str) -> Tuple[bool, str]:
        """Test a backend API endpoint"""
        try:
            url = f"{self.base_url}{endpoint}"
            response = self.session.get(url, timeout=10)
            return response.status_code == 200, f"Status: {response.status_code}"
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def test_frontend_page(self, route: str) -> Tuple[bool, str]:
        """Test a frontend page route"""
        try:
            url = f"{self.frontend_url}{route}"
            response = self.session.get(url, timeout=10)
            return response.status_code == 200, f"Status: {response.status_code}"
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def test_api_docs(self) -> Tuple[bool, str]:
        """Test API documentation"""
        try:
            url = f"{self.base_url}/api/docs"
            response = self.session.get(url, timeout=10)
            return response.status_code == 200, f"Status: {response.status_code}"
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def test_openapi_spec(self) -> Tuple[bool, str]:
        """Test OpenAPI specification"""
        try:
            url = f"{self.base_url}/openapi.json"
            response = self.session.get(url, timeout=10)
            if response.status_code == 200:
                spec = response.json()
                paths = list(spec.get('paths', {}).keys())
                return True, f"Found {len(paths)} API paths"
            return False, f"Status: {response.status_code}"
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def run_comprehensive_test(self):
        """Run comprehensive tests on all platform sections"""
        print(">>> Starting Comprehensive TechVerse Platform Test")
        print("=" * 60)
        
        test_results = []
        
        # Test Backend APIs
        print("\n>>> Testing Backend APIs:")
        print("-" * 30)
        
        backend_endpoints = [
            ("/api/docs", "API Documentation"),
            ("/openapi.json", "OpenAPI Specification"),
            ("/api/auth/", "Authentication API"),
            ("/api/users/", "Users API"),
            ("/api/techconnect/", "TechConnect API"),
            ("/api/techfinance/", "TechFinance API"),
            ("/api/translation/", "Translation API"),
            ("/api/techinnovation/", "TechInnovation API"),
        ]
        
        for endpoint, description in backend_endpoints:
            success, details = self.test_backend_api(endpoint)
            status = "[PASS]" if success else "[FAIL]"
            print(f"{status} {description}: {details}")
            test_results.append(("Backend", description, success, details))
            time.sleep(0.5)  # Small delay between requests
        
        # Test Frontend Pages
        print("\n>>> Testing Frontend Pages:")
        print("-" * 30)
        
        frontend_routes = [
            ("/", "Home Page"),
            ("/tech-learn", "TechLearn Section"),
            ("/tech-market", "TechMarket Section"),
            ("/tech-hub", "TechHub Section"),
            ("/tech-connect", "TechConnect Section"),
            ("/tech-finance", "TechFinance Section"),
            ("/tech-innovation", "TechInnovation Section"),
            ("/tech-wallet", "TechWallet Section"),
            ("/translation", "Translation Section"),
            ("/about", "About Page"),
            ("/privacy", "Privacy Page"),
        ]
        
        for route, description in frontend_routes:
            success, details = self.test_frontend_page(route)
            status = "[PASS]" if success else "[FAIL]"
            print(f"{status} {description}: {details}")
            test_results.append(("Frontend", description, success, details))
            time.sleep(0.5)  # Small delay between requests
        
        # Test API Documentation
        print("\n>>> Testing API Documentation:")
        print("-" * 30)
        
        success, details = self.test_api_docs()
        status = "[PASS]" if success else "[FAIL]"
        print(f"{status} Swagger UI: {details}")
        test_results.append(("Documentation", "Swagger UI", success, details))
        
        success, details = self.test_openapi_spec()
        status = "[PASS]" if success else "[FAIL]"
        print(f"{status} OpenAPI Spec: {details}")
        test_results.append(("Documentation", "OpenAPI Spec", success, details))
        
        # Generate Summary
        print("\n" + "=" * 60)
        print(">>> TEST SUMMARY")
        print("=" * 60)
        
        total_tests = len(test_results)
        passed_tests = sum(1 for _, _, success, _ in test_results if success)
        failed_tests = total_tests - passed_tests
        
        print(f"Total Tests: {total_tests}")
        print(f"[PASS] Passed: {passed_tests}")
        print(f"[FAIL] Failed: {failed_tests}")
        print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        # Show failed tests
        if failed_tests > 0:
            print("\n>>> Failed Tests Details:")
            for category, test, success, details in test_results:
                if not success:
                    print(f"  [FAIL] {category} - {test}: {details}")
        
        # Platform Status
        print("\n>>> PLATFORM STATUS:")
        backend_success = all(success for cat, _, success, _ in test_results if cat == "Backend")
        frontend_success = all(success for cat, _, success, _ in test_results if cat == "Frontend")
        
        if backend_success and frontend_success:
            print("[SUCCESS] EXCELLENT: Both Frontend and Backend are fully operational!")
            print("   The TechVerse platform is ready for use.")
        elif backend_success and not frontend_success:
            print("[WARNING] PARTIAL: Backend is working but some frontend pages have issues.")
        elif not backend_success and frontend_success:
            print("[WARNING] PARTIAL: Frontend is working but some backend APIs have issues.")
        else:
            print("[ERROR] CRITICAL: Both Frontend and Backend have significant issues.")
        
        return test_results

def main():
    """Main function to run the comprehensive test"""
    tester = TechVerseTester()
    
    try:
        results = tester.run_comprehensive_test()
        
        # Exit with appropriate code
        failed_tests = sum(1 for _, _, success, _ in results if not success)
        sys.exit(1 if failed_tests > 0 else 0)
        
    except KeyboardInterrupt:
        print("\n[STOP] Test interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()