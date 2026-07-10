from app.services.auth_service import AuthService

password = "123456"

hashed = AuthService.hash_password(password)

print("Original Password:", password)
print("Hashed Password:", hashed)

print()

print("Password Match:",
      AuthService.verify_password(password, hashed))

token = AuthService.create_access_token(
    {"sub": "akhil@gmail.com"}
)

print()

print("JWT Token:")
print(token)