import json
import os
import random
import string
import sys

# Constants and messages
CONFIG_FILE = 'config.json'
ENV_FILE = '.env'
STRS = {
    # EnvFileManager
    'file_not_found': "Error: The file {filename} does not exist.",
    'invalid_json': "Error: The file {filename} is not a valid JSON.",
    'added_settings': "Added settings:",
    'deleted_settings': "Deleted settings:",
    'modified_settings': "Modified settings:",
    'update_prompt': "Do you want to update the .env file? (y/n): ",
    'write_success': ".env file updated successfully.",
    'write_error': "Error: Could not write to {filename}.",
    'no_changes': "No changes detected. No update needed.",
    'update_canceled': "Update canceled by the user.",

    # AWSCredentialsGenerator
    'aws_key_generated': "AWS Access Key and Secret Key generated.",
    "AKIA":"AKIA",
    "AWS_ACCESS_KEY_ID":"AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY":"AWS_SECRET_ACCESS_KEY"

}

class EnvFileManager:
    def __init__(self, json_file, env_file):
        self.json_file = json_file
        self.env_file = env_file

    def read_json(self):
        """Reads the JSON file and returns a dictionary of the configuration."""
        try:
            with open(self.json_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(STRS['file_not_found'].format(filename=self.json_file))
            return None
        except json.JSONDecodeError:
            print(STRS['invalid_json'].format(filename=self.json_file))
            return None

    def read_env(self):
        """Reads the .env file and returns a dictionary of the configuration."""
        if not os.path.exists(self.env_file):
            return {}
        with open(self.env_file, 'r') as file:
            return {line.split('=')[0]: line.split('=')[1].strip() for line in file if '=' in line}

    def write_env(self, config):
        """Writes the configuration to a .env file after checking for changes."""
        current_config = self.read_env()
        config = {**current_config, **config}  # Merge new config with existing
        try:
            with open(self.env_file, 'w') as file:
                for key, value in config.items():
                    file.write(f'{key}={value}\n')
            print(STRS['write_success'])
        except IOError:
            print(STRS['write_error'].format(filename=self.env_file))

class ConfigToEnvConverter(EnvFileManager):
    def convert(self):
        """Converts the JSON configuration to a .env file."""
        config = self.read_json()
        if config is not None:
            self.write_env(config)

class AWSCredentialsGenerator(EnvFileManager):
    def generate_credentials(self):
        """Simulates generating AWS credentials."""
        access_key = STRS['AKIA'] + ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        secret_key = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=40))
        print(STRS['aws_key_generated'])
        return {
            STRS['AWS_ACCESS_KEY_ID']: access_key,
            STRS['AWS_SECRET_ACCESS_KEY']: secret_key
        }

if __name__ == "__main__":
    converter = ConfigToEnvConverter(CONFIG_FILE, ENV_FILE)
    if '--change-aws-creds' in sys.argv:
        creds = AWSCredentialsGenerator(CONFIG_FILE, ENV_FILE).generate_credentials()
        converter.write_env(creds)
    
    # Update Config 
    ConfigToEnvConverter(CONFIG_FILE, ENV_FILE).convert()
