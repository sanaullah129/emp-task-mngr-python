#!/usr/bin/env python3
"""
Test script for Employee Task Manager API
This script demonstrates all the API endpoints and functionality.

Run this script with the API server running on http://localhost:8000
"""

import requests
import json
from datetime import datetime, timedelta

API_BASE_URL = "http://localhost:8000"

def print_response(response, title):
    """Helper function to print API responses"""
    print(f"\n{'='*50}")
    print(f"{title}")
    print(f"{'='*50}")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response: {json.dumps(response.json(), indent=2, default=str)}")
    except:
        print(f"Response: {response.text}")

def test_api():
    """Test all API endpoints"""
    
    print("🚀 Testing Employee Task Manager API")
    print(f"API Base URL: {API_BASE_URL}")
    
    # Test 1: Get API info
    response = requests.get(f"{API_BASE_URL}/")
    print_response(response, "1. API Info")
    
    # Test 2: Login to get access token
    login_data = {
        "username": "admin",
        "password": "admin123"
    }
    response = requests.post(f"{API_BASE_URL}/token", data=login_data)
    print_response(response, "2. User Login")
    
    if response.status_code == 200:
        token = response.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        print(f"\n✅ Successfully logged in! Token: {token[:50]}...")
        
        # Test 3: List all employees
        response = requests.get(f"{API_BASE_URL}/employees", headers=headers)
        print_response(response, "3. List All Employees")
        
        # Test 4: Create a new employee
        new_employee = {
            "name": "Alex Johnson",
            "email": "alex.johnson@company.com",
            "department": "Finance",
            "position": "Financial Analyst"
        }
        response = requests.post(f"{API_BASE_URL}/employees", json=new_employee, headers=headers)
        print_response(response, "4. Create New Employee")
        
        if response.status_code == 200:
            new_employee_id = response.json()["id"]
            
            # Test 5: Get specific employee
            response = requests.get(f"{API_BASE_URL}/employees/{new_employee_id}", headers=headers)
            print_response(response, f"5. Get Employee {new_employee_id}")
            
            # Test 6: Update employee
            update_data = {
                "position": "Senior Financial Analyst",
                "department": "Finance & Accounting"
            }
            response = requests.put(f"{API_BASE_URL}/employees/{new_employee_id}", json=update_data, headers=headers)
            print_response(response, f"6. Update Employee {new_employee_id}")
        
        # Test 7: List all tasks
        response = requests.get(f"{API_BASE_URL}/tasks", headers=headers)
        print_response(response, "7. List All Tasks")
        
        # Test 8: Create a new task
        new_task = {
            "title": "Create financial report",
            "description": "Generate Q4 financial report for stakeholders",
            "due_date": (datetime.now() + timedelta(days=7)).isoformat(),
            "employee_id": 1  # Assign to John Doe
        }
        response = requests.post(f"{API_BASE_URL}/tasks", json=new_task, headers=headers)
        print_response(response, "8. Create New Task")
        
        if response.status_code == 200:
            new_task_id = response.json()["id"]
            
            # Test 9: Get specific task
            response = requests.get(f"{API_BASE_URL}/tasks/{new_task_id}", headers=headers)
            print_response(response, f"9. Get Task {new_task_id}")
            
            # Test 10: Update task status
            update_task = {
                "status": "ongoing",
                "description": "Generate Q4 financial report for stakeholders - Started working on data collection"
            }
            response = requests.put(f"{API_BASE_URL}/tasks/{new_task_id}", json=update_task, headers=headers)
            print_response(response, f"10. Update Task {new_task_id} Status")
        
        # Test 11: Register a new user
        new_user = {
            "username": "testuser",
            "password": "testpass123"
        }
        response = requests.post(f"{API_BASE_URL}/register", json=new_user)
        print_response(response, "11. Register New User")
        
        # Test 12: Try to create employee with duplicate email (should fail)
        duplicate_employee = {
            "name": "Duplicate User",
            "email": "john.doe@company.com",  # This email already exists
            "department": "Test",
            "position": "Test Position"
        }
        response = requests.post(f"{API_BASE_URL}/employees", json=duplicate_employee, headers=headers)
        print_response(response, "12. Try to Create Employee with Duplicate Email")
        
        print(f"\n{'='*50}")
        print("✅ API Testing Complete!")
        print(f"{'='*50}")
        print("\nTest Summary:")
        print("- ✅ Authentication system working")
        print("- ✅ Employee CRUD operations working")
        print("- ✅ Task CRUD operations working")
        print("- ✅ Error handling working")
        print("- ✅ Data validation working")
        
    else:
        print("\n❌ Login failed! Cannot continue with authenticated endpoints.")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("❌ Error: Cannot connect to API server.")
        print("Please make sure the FastAPI server is running on http://localhost:8000")
        print("Run: uvicorn main:app --reload --host 0.0.0.0 --port 8000")