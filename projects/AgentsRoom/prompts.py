# USER INPUT
INPUT = """
Write a science fiction story about someone who is a time traveler and has dedicated everything in their life towards a goal, and now wonders if it was worth it. The story should be between 850 and 900 words. The story should begin with the main character waking up on a frozen tundra. He looks for shelter from the cold. He sees a dead wooly mammoth and realizes he traveled back to the ice age. The character should find shelter, and a predator is outside his shelter at night. The ending should not be happy.
"""

# PLANNING AGENTS PROMPTS
CONFLICT_AGENT_PROMPT = """
Given <identifiers found in the scratchpad>, describe the central conflict in detail (more than 5 sentences). The description should answer the following questions:  
	⋆ What’s the protagonist’s main goal in this story?  
	⋆ Why do they want it?  
	⋆ What’s stopping them from achieving it?  
<scratchpad>
"""
CHARACTER_AGENT_PROMPT = """
Given <identifiers found in the scratchpad>, describe the characters in detailed bullet points (more than 5 sentences for each character). The description should answer the following questions:
	⋆ What do the characters sound like? Are they talkative or quiet? What kind of slang do they use? What is their sense of humor like?  
	⋆ What do they look like? Do they have any defining gestures? What’s the first thing people notice about them?  
	⋆ What are their motivations and internal characteristics? What are their flaws? What are their values? What are they afraid of? How will they change and grow over the course of this story?
<scratchpad>
"""

SETTING_AGENT_PROMPT = """
Given <identifiers found in the scratchpad>, describe the setting in detail (more than 5 sentences). The description should answer the following questions:
	⋆ Where does the story take place? Is it set in a fictional world, or is it simply set in someone’s backyard?
	⋆ When does the story take place? What decade is it set in? How much time elapses over the course of the story?
<scratchpad>
"""

PLOT_AGENT_PROMPT = """
Given <identifiers found in the scratchpad>, describe the key plot points in detailed bullet points.  
<scratchpad>
"""

# WRITING AGENT PROMPTS
EXPOSITION_AGENT_PROMPT = """
Given <identifiers found in the scratchpad>, continue the story by writing the Exposition part.  
<If previous sections have been written, include the following in the prompt:>  
Begin your portion of the story in a way that naturally flows from the previous ending. Match the writing style, vocabulary, and overall mood of the existing text. Do not re-explain details or events that have already been described.  
<If this is not the meant to be the last section, include the following in the prompt:>  
Focus only on the Exposition part of the story. Do not write about the following parts of the story. Do not end the story.  
<scratchpad>
"""

RISING_ACTION_AGENT_PROMPT = """
Given <identifiers found in the scratchpad>, continue the story by writing the Rising Action part.  
<If previous sections have been written, include the following in the prompt:>  
Begin your portion of the story in a way that naturally flows from the previous ending. Match the writing style, vocabulary, and overall mood of the existing text. Do not re-explain details or events that have already been described.  
<If this is not the meant to be the last section, include the following in the prompt:>  
Focus only on the Rising Action part of the story. Do not write about the following parts of the story. Do not end the story.  
<scratchpad>
"""

CLIMAX_AGENT_PROMPT = """
Given <identifiers found in the scratchpad>, continue the story by writing the Climax part.  
<If previous sections have been written, include the following in the prompt:>  
Begin your portion of the story in a way that naturally flows from the previous ending. Match the writing style, vocabulary, and overall mood of the existing text. Do not re-explain details or events that have already been described.  
<If this is not the meant to be the last section, include the following in the prompt:>  
Focus only on the Climax part of the story. Do not write about the following parts of the story. Do not end the story.  
<scratchpad>
"""

FALLING_ACTION_AGENT_PROMPT = """
Given <identifiers found in the scratchpad>, continue the story by writing the Falling Action part.  
<If previous sections have been written, include the following in the prompt:>  
Begin your portion of the story in a way that naturally flows from the previous ending. Match the writing style, vocabulary, and overall mood of the existing text. Do not re-explain details or events that have already been described.  
<If this is not the meant to be the last section, include the following in the prompt:>  
Focus only on the Falling Action part of the story. Do not write about the following parts of the story. Do not end the story.  
<scratchpad>
"""

RESOLUTION_AGENT_PROMPT = """
Given <identifiers found in the scratchpad>, continue the story by writing the Resolution part.  
<If previous sections have been written, include the following in the prompt:>  
Begin your portion of the story in a way that naturally flows from the previous ending. Match the writing style, vocabulary, and overall mood of the existing text. Do not re-explain details or events that have already been described.  
<If this is not the meant to be the last section, include the following in the prompt:>  
Focus only on the Resolution part of the story. Do not write about the following parts of the story. Do not end the story.  
<scratchpad>
"""







