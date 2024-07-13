import json
import os
import random
import string

# Usage
CONFIG_FILE = 'config.json'
ENV_FILE = '.env'
MESSAGES = {
    ### ConfigToEnvConverter messages 
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

    ### AWSCredentialsGenerator messages 
    'aws_key_generated': "AWS Access Key and Secret Key generated."
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
            print(MESSAGES['file_not_found'].format(filename=self.json_file))
            return None
        except json.JSONDecodeError:
            print(MESSAGES['invalid_json'].format(filename=self.json_file))
            return None

    def read_env(self):
        """Reads the .env file and returns a dictionary of the configuration."""
        if not os.path.exists(self.env_file):
            return {}
        with open(self.env_file, 'r') as file:
            return {line.split('=')[0]: line.split('=')[1].strip() for line in file if '=' in line}

    def compare_configs(self, new_config, old_config):
        """Compares new and old configurations and prints differences."""
        added = {k: v for k, v in new_config.items() if k not in old_config}
        deleted = {k: v for k, v in old_config.items() if k not in new_config}
        modified = {k: v for k, v in new_config.items() if k in old_config and v != old_config[k]}
        
        if added:
            print(MESSAGES['added_settings'])
            for k, v in added.items():
                print(f"  {k} = {v}")
        if deleted:
            print(MESSAGES['deleted_settings'])
            for k, v in deleted.items():
                print(f"  {k} = {v}")
        if modified:
            print(MESSAGES['modified_settings'])
            for k, v in modified.items():
                print(f"  {k}: {old_config[k]} -> {v}")
        
        return added, deleted, modified

    def write_env(self, config_json):
        """Writes the configuration to a .env file after checking for changes."""
        current_config = self.read_env()
        added, deleted, modified = self.compare_configs(config_json, current_config)

        if added or deleted or modified:
            if input(MESSAGES['update_prompt']).lower() == 'y':
                try:
                    with open(self.env_file, 'w') as file:
                        for key, value in {**current_config, **config_json}.items():
                            file.write(f'{key}={value}\n')
                    print(MESSAGES['write_success'])
                except IOError:
                    print(MESSAGES['write_error'].format(filename=self.env_file))
            else:
                print(MESSAGES['update_canceled'])
        else:
            print(MESSAGES['no_changes'])


class ConfigToEnvConverter(EnvFileManager):
    def convert(self):
        """Converts the JSON configuration to a .env file."""
        config = self.read_json()
        if config is not None:
            self.write_env(config)


class AWSCredentialsGenerator(EnvFileManager):
    def generate_credentials(self):
        """Simulates generating AWS credentials."""
        access_key = 'AKIA' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        secret_key = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=40))
        print(MESSAGES['aws_key_generated'])
        return {
            'AWS_ACCESS_KEY_ID': access_key,
            'AWS_SECRET_ACCESS_KEY': secret_key
        }

if __name__=="__main__":
    converter = ConfigToEnvConverter(CONFIG_FILE, ENV_FILE)
    converter.convert()
    creds = AWSCredentialsGenerator(CONFIG_FILE, ENV_FILE).generate_credentials()
    converter.write_env(creds)
