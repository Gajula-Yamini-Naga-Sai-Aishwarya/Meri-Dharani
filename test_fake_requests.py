"""
Test script to create fake waste requests in MongoDB for testing
"""
from pymongo import MongoClient
from datetime import datetime
import uuid

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["meri_dharani"]
requests_collection = db["requests"]
users_collection = db["users"]

# Create fake user if doesn't exist
fake_user = {
    "_id": "test_user_001",
    "name": "Test Citizen",
    "email": "test@meri-dharani.com",
    "phone": "+91-9999999999",
    "role": "citizen",
    "city": "Telangana",
    "state": "Telangana"
}

# Check if test user exists, if not create
if not users_collection.find_one({"_id": "test_user_001"}):
    users_collection.insert_one(fake_user)
    print("✅ Test user created")
else:
    print("✅ Test user already exists")

# Create multiple fake waste requests
fake_requests = [
    {
        "request_id": f"REQ-TEST-{uuid.uuid4().hex[:8].upper()}",
        "user_id": "test_user_001",
        "description": "Large heap of plastic waste with bottles and bags",
        "waste_type": "plastic",
        "location": "Warangal, Telangana",
        "status": "pending",
        "ai_analysis": {
            "waste_detected": "plastic",
            "confidence": 0.95,
            "quantity_estimate": "50kg",
            "eco_points": 150
        },
        "images": ["test_image_1.jpg"],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    },
    {
        "request_id": f"REQ-TEST-{uuid.uuid4().hex[:8].upper()}",
        "user_id": "test_user_001",
        "description": "Mixed waste including paper, glass, and metal",
        "waste_type": "mixed",
        "location": "Hyderabad, Telangana",
        "status": "assigned",
        "ai_analysis": {
            "waste_detected": "mixed_waste",
            "confidence": 0.88,
            "quantity_estimate": "75kg",
            "eco_points": 225
        },
        "images": ["test_image_2.jpg"],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    },
    {
        "request_id": f"REQ-TEST-{uuid.uuid4().hex[:8].upper()}",
        "user_id": "test_user_001",
        "description": "Electronic waste - old computers and mobile phones",
        "waste_type": "electronic",
        "location": "Vijayawada, Telangana",
        "status": "completed",
        "ai_analysis": {
            "waste_detected": "e_waste",
            "confidence": 0.92,
            "quantity_estimate": "25kg",
            "eco_points": 300
        },
        "images": ["test_image_3.jpg"],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
]

# Insert fake requests
result = requests_collection.insert_many(fake_requests)
print(f"\n✅ {len(result.inserted_ids)} fake requests created successfully!\n")

# Display created requests
print("Created Requests:")
print("=" * 70)
for req in fake_requests:
    print(f"ID: {req['request_id']}")
    print(f"Description: {req['description']}")
    print(f"Status: {req['status']}")
    print(f"Eco Points: {req['ai_analysis']['eco_points']}")
    print("-" * 70)

print(f"\n🎉 Test data inserted! Total requests in database: {requests_collection.count_documents({})}")
