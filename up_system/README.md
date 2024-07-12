# Set Up System

## Localstack with Docker Installation Instructions
Refer: 
[Installation Document](https://docs.google.com/document/d/1o_DJDGDltexrNTf4f1FwmJNnVJGHw6XuyiyKcsxeGN4/edit?usp=sharing)

## Commands to set up

```bash
cd ./aws-step-functions/up_system
python generate_env.py --force-config --force-env
# Note: Add a message if the environment already exists.
docker-compose up
```

