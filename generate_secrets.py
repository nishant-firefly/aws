import os
import random
import string

def generate_aws_access_key_id(length=20):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def generate_aws_secret_access_key(length=40):
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(length))

def generate_keys_and_save_to_env():
    # Generate AWS access keys
    access_key_id = generate_aws_access_key_id()
    secret_access_key = generate_aws_secret_access_key()

    print(f"AWS Access Key ID: {access_key_id}")
    print(f"AWS Secret Access Key: {secret_access_key}")


    print("Writing keys and env_file_path to .env file")
    with open(".env", 'w') as f:
        f.write(f"AWS_ACCESS_KEY_ID={access_key_id}\n")
        f.write(f"AWS_SECRET_ACCESS_KEY={secret_access_key}\n")
if __name__=="__main__":
    generate_keys_and_save_to_env()
