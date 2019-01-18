# kafka

## basic
```bash
# install command line tool
brew install kafka
```

## topic
```bash
# create topic
kafka-topics --create --zookeeper <ip:port> --replication-factor 3 --partitions 1 --topic <topic>

# topic list
kafka-topics --zookeeper <ip:port> --list

# describe topic
kafka-topics --describe --zookeeper <ip:port> --topic <topic>
```

## jaas.properties file

> sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="<username>" password="<password>";
> security.protocol=SASL_PLAINTEXT
> sasl.mechanism=PLAIN

## consumer
```bash
# consume message
kafka-console-consumer --bootstrap-server <ip:port> --from-beginning --topic <topic> --consumer.config <path_to_jaas> --group <consumer_group> --property print.key=true --property print.value=true
```
