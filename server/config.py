from environs import Env

env = Env()
env.read_env()

TIMEWEB_TOKEN = env('TIMEWEB_TOKEN')
TIMEWEB_SERVER_ID = env.int('TIMEWEB_SERVER_ID')