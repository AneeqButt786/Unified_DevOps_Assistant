from agents import Agent, handoff

slack_dev_assistant = Agent(name="Slack Dev Assistant", instructions="Answer CI/CD errors, build failures, PR statuses.", model="gpt-4o-mini", handoff_description="Transfer for CI/CD or debugging.")
escalation_router = Agent(name="Ticket Escalation Router", instructions="Classify tickets, escalate incidents.", model="gpt-4o-mini", handoff_description="Transfer for incident triage.")
dev_productivity_bot = Agent(name="Developer Productivity Bot", instructions="Suggest focused work, recommend flow improvements.", model="gpt-4o-mini", handoff_description="Transfer for productivity tips.")

devops_triage_agent = Agent(
    name="DevOps Triage Agent",
    instructions="Unified DevOps Assistant. Handoff to Slack Dev Assistant, Ticket Escalation Router, or Developer Productivity Bot.",
    model="gpt-4o-mini",
    handoffs=[handoff(slack_dev_assistant), handoff(escalation_router), handoff(dev_productivity_bot)],
)
