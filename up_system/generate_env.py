import os
import random
import string
import json
import argparse
from dotenv import dotenv_values
CONFIG_FILE="config.json"
ENV_FILE=".env"
class ConfigManager:
    def __init__(self):
        # This will always exist and not part of gitigniore
        with open(CONFIG_FILE, 'r') as config_file:
            self.config = json.load(config_file)
        
        # .env file may or may not exists at the first time.
        # Even if not exist will return and Empty Ordered Dict : OrderedDict()
        self.env_vars = dotenv_values(ENV_FILE)
        # e.g. when no .env file :  {'SERVICES': {'config': 's3,sqs,iam,step', 'env': None}, 'DEBUG': {'config': '1', 'env': None}, 'DATA_DIR': {'config': './localstack/data', 'env': None}}
        
        self.config_to_env_changes=self.get_config_to_env_changes()

    def get_config_to_env_changes(self):
        config_to_env_changes = {}
        for key, value in self.config.items():
            if self.config.get(key) != self.env_vars.get(key):
                config_to_env_changes[key] = {"config":value, "env":self.env_vars.get(key)}
        return config_to_env_changes

    def generate_aws_access_key_id(self, length=20):
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def generate_aws_secret_access_key(self, length=40):
        chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
        return ''.join(random.choice(chars) for _ in range(length))


    def write_to_env_file(self, force_env=False):
        # Check if .env file exists and handle --force-env option
        if os.path.exists(".env") and not force_env:
            print(".env file already exists. Use --force-env to overwrite.")
            return False

        print("Writing keys and environment variables to .env file")

        # Generate AWS access keys
        access_key_id = self.generate_aws_access_key_id()
        secret_access_key = self.generate_aws_secret_access_key()
        print(f"AWS Access Key ID: {access_key_id}")
        print(f"AWS Secret Access Key: {secret_access_key}")

        # Update environment variables with config values
        for key in self.config.keys():
            self.env_vars[key] = self.config[key]

        # Add AWS keys to environment variables
        self.env_vars["AWS_ACCESS_KEY_ID"] = access_key_id
        self.env_vars["AWS_SECRET_ACCESS_KEY"] = secret_access_key

        # Write to .env file
        with open(".env", 'w') as f:
            for key, value in self.env_vars.items():
                f.write(f"{key}={value}\n")

        return True



    def generate_keys_and_save_to_env(self, force_env=False, force_config=False):
        self.read_config()
        self.read_env()

        # Handle .env file
        env_overwritten = self.write_to_env_file(force_env=force_env)
        if not env_overwritten:
            return

        # Handle config.json changes
        if self.detect_config_changes():
            if not force_config:
                print("Config.json has been modified. Use --force-config to update .env accordingly.")
                return

            # Update .env if force_config is True
            self.write_to_env_file(force_env=True)
            print("config.json and .env updated successfully.")

        else:
            print("Values in config.json match current .env file.")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate AWS keys and update environment variables.")
    parser.add_argument('--force-env', action='store_true', help='Force overwrite .env file if it exists.')
    parser.add_argument('--force-config', action='store_true', help='Force modify config.json.')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    config_manager = ConfigManager()
    config_manager.generate_keys_and_save_to_env(force_env=args.force_env, force_config=args.force_config)
