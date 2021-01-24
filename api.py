import pika
import requests
import json
import time

class RabbitChat:
    ip=None
    login=None
    passe=None

    conn=None
    ch=None

    def connect(self):
        credentials = pika.PlainCredentials(self.login, self.passe)

        self.conn = pika.BlockingConnection(
            pika.ConnectionParameters(self.ip,
                                      5672,
                                      '/',
                                      credentials)
            )
        self.ch = self.conn.channel()
        
    
    def __init__(self,ip,login,passe):
        self.ip=ip
        self.login=login
        self.passe=passe

        self.connect()

    def send(self,dst,msg):

        obj={"typ":"chat","dst":dst,"msg":msg}
        
        self.ch.basic_publish(exchange="minetest",
                              routing_key=".minetest.server",
                              body=json.dumps(obj))

    def close(self):
        self.ch.close()
        self.conn.close()

        
with open('credentials.txt','r') as json_file:
    data = json.load(json_file)

IP=data['ip']
LOGIN=data['login']
PASS=data['pass']

    



class live:
    def send(message):
        try:
            r=RabbitChat(IP,LOGIN,PASS)
            r.send("all","[FRANCTUBE] %s" % (message));
            r.close()
        except:
            pass
    
class minetest:
    def postToChat(pseudo, message):
        try:
            r=RabbitChat(IP,LOGIN,PASS)
            r.send("all","<%s@console> %s" % (pseudo, message));
            r.close()
        except:
            pass
