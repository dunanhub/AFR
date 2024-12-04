import bcrypt

# Ваш обычный пароль
plain_password = "Aktiv702"

# Генерация хеша пароля
hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())

# Вывод хешированного пароля
print(hashed_password.decode('utf-8'))
