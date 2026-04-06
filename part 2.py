import hashlib

def hash_string(data):
    return hashlib.sha256(data.encode()).hexdigest()

def verify_hash(data, hashed):
    return hash_string(data) == hashed

# Original password
input_data = "secure_password"
hashed_data = hash_string(input_data)

print(f"Original Data: {input_data}")
print(f"Hashed Data: {hashed_data}")


# tambahan kode
# Verify password
correct_data = "secure_password"
incorrect_data = "wrong_password"

print("Verification (correct):", verify_hash(correct_data, hashed_data))
print("Verification (incorrect):", verify_hash(incorrect_data, hashed_data))