# Agents' Room: NARRATIVE GENERATION THROUGH MULTI-STEP COLLABORATION

This project is an implementation of the paper *"Agents' Room: Narrative Generation through Multi-step Collaboration"* using the Autogen framework.  
It reproduces the multi-agent creative story generation pipeline proposed in the paper, coordinating specialized agents to collaboratively generate a structured, long-form narrative. The system manages key story elements such as conflict, characters, setting, plot, and various story arcs.

## Paper

This project is based on the research paper:

**Agents' Room: Narrative Generation through Multi-step Collaboration**  
[https://arxiv.org/abs/2410.02603](https://arxiv.org/abs/2410.02603)

## Requirements

1. Create a `.env` file in the project root directory.  
2. Add your OpenAI API key or other necessary environment variables inside the `.env` file, for example:  

```raw
API_KEY=your_openai_api_key_here
```

## Running the Project

```python
python orchestrator.py
```


- The script will sequentially run all story agents, passing accumulated story context from one to the next.

- Partial results and the final structured story will be saved incrementally to `scratchpad_output.txt`.

- After completion, the entire generated narrative structured by story elements will be printed to the console.

You can customize the initial creative writing prompt by modifying the `INPUT` variable in the `prompts.py` file.
