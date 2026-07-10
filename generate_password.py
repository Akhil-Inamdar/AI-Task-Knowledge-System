from app.services.auth_service import AuthService

password = "Akhil@123"

hashed = AuthService.hash_password(password)

print(hashed)