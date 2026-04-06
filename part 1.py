import hashlib

def hash_string(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Test the function
input_data = "secure_password"
hashed_data = hash_string(input_data)

print(f"Original Data: {input_data}")
print(f"Hashed Data: {hashed_data}")