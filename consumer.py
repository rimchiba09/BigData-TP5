import json
from kafka import KafkaConsumer

TOPIC = "campus-sensors"
# TOPIC = "campus-sensors-one"

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="tp05-campus-monitor",
    # group_id="tp05-campus-monitor-2",
    # group_id="tp05-campus-one-group",
    value_deserializer=lambda value: json.loads(value.decode("utf-8")),
)

count = 0
total_temperature = 0.0

print(f"Listening to topic: {TOPIC}")

try:
    for message in consumer:
        event = message.value
        temperature = event["temperature_c"]

        count += 1
        total_temperature += temperature
        average = total_temperature / count

        print(
            f'{event["timestamp"]} | {event["sensor_id"]} | '
            f'T={temperature}°C | RH={event["humidity_pct"]}%'
        )

        print(f"Running Average Temperature: {average:.2f}°C")

        if temperature >= 35:
            print("ALERT: High temperature detected!")

except KeyboardInterrupt:
    print("Consumer stopped by user.")

finally:
    consumer.close()