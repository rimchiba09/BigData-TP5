# Real-Time Data Streaming and Processing Using Apache Kafka

## 1. Project Overview

This project implements a simple real-time monitoring system for a university campus using Apache Kafka and Python.

The system simulates temperature and humidity sensors. It sends sensor data to Kafka, where a consumer receives and processes the messages.

## 2. System Architecture

The system consists of three main components:

- **Producer:** Generates simulated sensor data and sends it to Kafka.
- **Kafka:** Receives and stores messages in the `campus-sensors` topic.
- **Consumer:** Reads sensor data, calculates the running average temperature, and detects high temperatures.

## 3. Technologies Used

- Python
- Apache Kafka 3.9.1
- kafka-python 3.0.12
- Docker and Docker Compose

## 4. Main Features

- Real-time sensor data streaming.
- Temperature and humidity monitoring.
- Running average temperature calculation.
- High-temperature alerts when temperature is 35°C or higher.
- Support for multiple consumer groups.
- Comparison between one and three Kafka partitions.

## 5. Installation and Execution

### Start Kafka

```bash
docker compose up -d
```

### Create and activate the virtual environment

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Consumer

```bash
python consumer.py
```

### Run the Producer

Open another terminal and execute:

```bash
python producer.py
```

## 6. Experiments and Results

The following experiments were performed:

- Sending 30 and 100 sensor messages.
- Calculating the running average temperature.
- Detecting high temperatures.
- Testing different consumer groups and their independent offsets.
- Comparing a topic with one partition to a topic with three partitions.

The consumer successfully processed messages, calculated average temperatures, and generated alerts when the temperature reached 35°C or higher.

All tested consumer groups reached a lag of zero after processing their messages.

## 7. Project Structure

- `compose.yaml`: Kafka Docker configuration.
- `producer.py`: Generates and sends sensor messages.
- `consumer.py`: Receives and processes messages.
- `requirements.txt`: Python dependencies.
- `.gitignore`: Excludes unnecessary files.
- `screenshots/`: Project execution screenshots.

## 8. Conclusion

This project demonstrates how Apache Kafka can be used for real-time data streaming and processing. It also shows the importance of partitions and consumer groups in managing distributed message processing.