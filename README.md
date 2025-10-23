# Autonomous Car Monitoring System

This project represents my first step into the world of IoT and autonomous systems.
It was developed during my summer training at the Samsung Innovation Campus, organized by Samsung Electronics and Life Makers, where I explored the fundamentals of IoT architecture — from data collection and communication to visualization and automation.

# Project Overview

The Autonomous Car Monitoring System is designed to track and analyze key vehicle parameters such as speed, acceleration, and battery status in real time.
It delivers a complete monitoring experience by combining hardware, software, and networking components into one intelligent IoT system.

System Components
MQTT Communication (Mosquitto Broker)

Utilizes the MQTT protocol with a locally hosted Mosquitto broker.

Implements publish–subscribe mechanisms for efficient and reliable data exchange.

OwnTracks Integration

Sends JSON files containing location, speed, and status data.

Enables real-time car tracking on a Node-RED dashboard with live map visualization.

Node-RED Dashboard

Collects and visualizes live data for speed, acceleration, and battery health.

Includes JavaScript functions to simulate random speed and acceleration values for testing and validation.

Python (Paho MQTT Library)

Subscribes to MQTT topics and gathers incoming sensor data.

Creates battery health logs for long-term analysis of energy performance.

Linux (Ubuntu) Automation

Configures and manages the MQTT broker through command-line tools.

Uses Bash scripting and nohup to automate logging and maintain continuous background operation.

Runs a shell script every 15 minutes to keep battery logs updated in real time.

# Project Goal

This project demonstrates the power of IoT by integrating communication, automation, and data analysis into one ecosystem — showing how smart systems can improve vehicle monitoring, battery health management, and energy efficiency.
