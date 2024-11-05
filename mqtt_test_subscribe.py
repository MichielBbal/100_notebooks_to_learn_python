import paho.mqtt.client as mqtt #import the client1

#broker_address="iot.eclipse.org" #use external broker
broker_address="test.mosquitto.org"
client = mqtt.Client() #create new instance
client.connect(broker_address) #connect to broker
client.subscribe("Test")
