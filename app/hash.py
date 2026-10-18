import bcrypt


def generate_password(password: str):
    pass_to_bytes = password.encode("utf-8")

    print("byte password", pass_to_bytes)
    salt = bcrypt.gensalt()

    print("salt generated", salt)
    hashed_password = bcrypt.hashpw(password=pass_to_bytes, salt=salt)
    print("generated hash value ", hashed_password)
    return hashed_password.decode("utf-8")


print(generate_password("bhavesh"))

def check_password(password,hashvalue)->bool:
    plain_pass_to_bytes = password.encode("utf-8")
    hash_value_to_bytes = hashvalue.encode("utf-8")

    return bcrypt.checkpw(password=plain_pass_to_bytes, hashed_password=hash_value_to_bytes)

print(
    check_password(
        "bhavesh", "$2b$12$7g0Z1k5y6J8F3Q9K1L2M3O4P5Q6R7S8T9U0V1W2X3Y4Z5A6B7C8D9E0F1G2H3I4"
    )
)

import bcrypt


def generate_password(password: str):
    pass_to_bytes = password.encode("utf-8")

    print("byte password", pass_to_bytes)

    salt = bcrypt.gensalt()
    print("salt generated", salt)

    hashed_password = bcrypt.hashpw(
        password=pass_to_bytes,
        salt=salt
    )

    print("generated hash value", hashed_password)

    return hashed_password.decode("utf-8")


def check_password(password: str, hashvalue: str) -> bool:
    plain_pass_to_bytes = password.encode("utf-8")
    hash_value_to_bytes = hashvalue.encode("utf-8")

    return bcrypt.checkpw(
        password=plain_pass_to_bytes,
        hashed_password=hash_value_to_bytes
    )


# SIGN UP
hashed_password = generate_password("bhavesh")
print("Stored Hash:", hashed_password)


# SIGN IN / LOGIN
password = "bhavesh"

if check_password(password, hashed_password):
    print("Login successful")
else:
    print("Invalid password")