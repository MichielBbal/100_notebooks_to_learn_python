import paho.mqtt.client as mqtt #import the client1

#broker_address="iot.eclipse.org" #use external broker
#broker_address="test.mosquitto.org"
broker_address = "sensemakers-vm.dev.sda-projects.nl"
client = mqtt.Client() #create new instance
client.connect(broker_address, keepalive=60) #connect to broker
client.subscribe("test/test")