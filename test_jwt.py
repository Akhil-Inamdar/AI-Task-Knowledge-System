from app.services.auth_service import AuthService

token = AuthService.create_access_token({
    "sub": "akhil@gmail.com",
    "role": "Admin"
})

print("Generated Token:")
print(token)

print("\nDecoded Token:")
print(AuthService.verify_token(token))