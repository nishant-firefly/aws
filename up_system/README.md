# Set Up System

## Install localstack with Docker
Refer: 
[Installation Document](https://docs.google.com/document/d/1o_DJDGDltexrNTf4f1FwmJNnVJGHw6XuyiyKcsxeGN4/edit?usp=sharing)

### One time activity to generate environment variables 
#### Following will create a .env file with aws secret, keys and configs from config.json
```bash
cd up_system
...up_system $ python generate_env.py  

python generate_env.py --force-config --force-env
```
#### 


## Start Localstack

cd localstack 
docker-compose up 

