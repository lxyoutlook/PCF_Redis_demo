import redis
#r = redis.Redis(host='123.12.148.95', port='5379')
#r = redis.Redis(host='123.12.148.95', port='15379', password='ABCDEFG1231LQ4L')

r = redis.Redis(host='redis-18247.c100.us-east-1-4.ec2.cloud.redislabs.com', port='18247', password='V2whbLgAGFLIbvjrc4WhvZVPI5OUmhTX')

######################
#### WORKING WITH KEYS
r.set('mykey','PiedPiper')
#### Single key
print (r.get('mykey'))
print (r.exists('mykey'))
r.delete('mykey')

