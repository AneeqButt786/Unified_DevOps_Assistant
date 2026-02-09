# Unified DevOps Assistant

## Overview

Multi-agent DevOps helper that triages developer requests, answers CI/CD and debugging questions, routes incident tickets, and coaches developer productivity. Triage agent hands off to Slack Dev Assistant, Ticket Escalation Router, or Developer Productivity Bot.

## Features

- CI/CD and debugging support
- Ticket escalation routing
- Developer productivity coaching

## Tech Stack

Python 3.12+, OpenAI Agents SDK, Chainlit, python-dotenv

## Setup

1. cd Unified_DevOps_Assistant
2. pip install -r requirements.txt
3. Copy .env.example to .env and set OPENAI_API_KEY

## Run Commands

chainlit run app.py
