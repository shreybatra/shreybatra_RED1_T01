from redis import Redis

client = Redis()

client.publish("hello", "world")