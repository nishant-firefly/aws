# Set Up System

## Install localstack with Docker
Refer: 
[Installation Document](https://docs.google.com/document/d/1o_DJDGDltexrNTf4f1FwmJNnVJGHw6XuyiyKcsxeGN4/edit?usp=sharing)

### One time activity to generate environment variables 
#### Following will create a .env file with aws secret, keys and configs from config.json
```bash
-- One Time Activity to create .env file from config.json and generate AWS CREDS (Will be used in localstack docker compose)
path/to/up_system $ python generate_env.py --change-aws-creds

```
#### Next time onwards to update the config.json values to .env just run 
```
path/to/up_system $ python generate_env.py

```



## Start Localstack

cd localstack 
docker-compose up 

