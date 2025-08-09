from autogen_agentchat.agents import AssistantAgent
from client import model_client
from prompts import *


# Planning Agents
CONFLICT_AGENT = AssistantAgent(
    name = "CONFLICT",
    model_client = model_client,
    system_message= CONFLICT_AGENT_PROMPT
)

CHARACTER_AGENT = AssistantAgent(
    name = "CHARACTER",
    model_client = model_client,
    system_message= CHARACTER_AGENT_PROMPT
)

SETTING_AGENT = AssistantAgent(
    name = "SETTING",
    model_client = model_client,
    system_message= SETTING_AGENT_PROMPT
)

PLOT_AGENT = AssistantAgent(
    name = "PLOT",
    model_client = model_client,
    system_message= PLOT_AGENT_PROMPT
)

# Writing Agents
EXPOSITION_AGENT = AssistantAgent(
    name = "EXPOSITION",
    model_client = model_client,
    system_message= EXPOSITION_AGENT_PROMPT
)

RISING_ACTION_AGENT = AssistantAgent(
    name = "RISING_ACTION",
    model_client = model_client,
    system_message= RISING_ACTION_AGENT_PROMPT
)

CLIMAX_AGENT = AssistantAgent(
    name = "CLIMAX",
    model_client = model_client,
    system_message= CLIMAX_AGENT_PROMPT
)

FALLING_ACTION_AGENT = AssistantAgent(
    name = "FALLING_ACTION",
    model_client = model_client,
    system_message= FALLING_ACTION_AGENT_PROMPT
)

RESOLUTION_AGENT = AssistantAgent(
    name = "RESOLUTION",
    model_client = model_client,
    system_message= RESOLUTION_AGENT_PROMPT
)

# Agents Order List
ALL_AGENTS = [
    CONFLICT_AGENT,
    CHARACTER_AGENT,
    SETTING_AGENT,
    PLOT_AGENT,
    EXPOSITION_AGENT,
    RISING_ACTION_AGENT,
    CLIMAX_AGENT,
    FALLING_ACTION_AGENT,
    RESOLUTION_AGENT
]
