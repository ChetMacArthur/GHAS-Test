# app.py
import hashlib

# 1. THE WRAPPER (Hidden Risk)
# This is a custom helper function your company might have.
# Standard tools ignore it because it looks like a normal function.
def unsafe_hash_algo(data):
    return hashlib.md5(data.encode()).hexdigest()

# 2. THE VIOLATION
def process_user_password(password):
    # We are using the banned wrapper here!
    print(f"Storing password hash: {unsafe_hash_algo(password)}")

if __name__ == "__main__":
    process_user_password("supersecret")
