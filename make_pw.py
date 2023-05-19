from argon2 import PasswordHasher


print(PasswordHasher().hash("test_pw"))
# $argon2id$v=19$m=65536,t=3,p=4$1IFMQL9qi4/AH9jKPDAW7A$QhJq7jzbz+kLEUDrkL9OyOk43+P+V6+48TD7aDQw4Xw