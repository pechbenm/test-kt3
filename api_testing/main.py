from user_api import UserAPI
from store_api import StoreAPI
import time
import random

def test_store_api():
    print("ТЕСТ STORE")
    print("=" * 40)
    
    store_api = StoreAPI("https://petstore.swagger.io/v2")
    order_id = random.randint(100, 999)
    
    try:
        print("получение инвентаря")
        response = store_api.get_inventory()
        
        print("\nсоздание заказа")
        order_data = {
            "id": order_id,
            "petId": 12345,
            "quantity": 1,
            "shipDate": "2024-01-20T10:00:00.000Z",
            "status": "placed",
            "complete": True
        }
        response = store_api.create_order(order_data)
        print(f"ID заказа: {order_id}")
        
        print("\nполучения заказа по ID")
        response = store_api.get_order(order_id)

        
        print("\nудаление заказа")
        response = store_api.delete_order(order_id)

        
    except Exception as e:
        print(f"ошибка: {e}")
    
    print("=" * 40)
    print("тестирование store завершено\n")

def test_user_api():
    print("ТЕСТ USER")
    print("=" * 40)
    
    user_api = UserAPI("https://petstore.swagger.io/v2")
    timestamp = int(time.time())
    username = f"student_{timestamp}"
    
    try:
        print("создание пользователя")
        user_data = {
            "id": timestamp,
            "username": username,
            "firstName": "Иван",
            "lastName": "Иванов",
            "email": f"ivan{timestamp}@mail.ru",
            "password": "password123",
            "phone": "1234567890",
            "userStatus": 1
        }
        response = user_api.create_user(user_data)
        print(f"пользователь: {username}")
        
        print("\nполучение пользователя")
        response = user_api.get_user(username)
        if response.status_code == 200:
            user_info = response.json()
            print(f"имя: {user_info['firstName']} {user_info['lastName']}")
        
        print("\nобновление пользователя")
        updated_data = {
            "id": timestamp,
            "username": username,
            "firstName": "Петр",
            "lastName": "Петров",
            "email": f"petr{timestamp}@mail.ru",
            "password": "newpassword456",
            "phone": "0987654321",
            "userStatus": 1
        }
        response = user_api.update_user(username, updated_data)
        
        print("\nудаление пользователя")
        response = user_api.delete_user(username)
        
    except Exception as e:
        print(f"ошибка: {e}")
    
    print("=" * 40)
    print("тестирование user заверешено\n")

def main():
    print("API: https://petstore.swagger.io/v2")
    print("=" * 50)
    
    test_store_api()
    test_user_api()
    
    print("ПРОТЕСТИРОВАНО 8 ЗАПРОСОВ")

if __name__ == "__main__":
    main()