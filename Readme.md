# LangGraph Basic Examples

This repository demonstrates the use of [LangGraph](https://github.com/langchain-ai/langgraph) for building stateful, composable, and flexible workflows with language models. The examples cover sequential, parallel, and conditional workflows, as well as a basic chatbot using Streamlit.

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Examples](#examples)
  - [1. Sequential Workflow: BMI Calculator](#1-sequential-workflow-bmi-calculator)
  - [2. Simple LLM Workflow](#2-simple-llm-workflow)
  - [3. Parallel LLM Workflow](#3-parallel-llm-workflow)
  - [4. Conditional Workflow](#4-conditional-workflow)
  - [5. Basic Chatbot (Streamlit)](#5-basic-chatbot-streamlit)
- [Environment Variables](#environment-variables)
- [Requirements](#requirements)

## Overview

This repo contains Jupyter notebooks and a Streamlit app that showcase how to use LangGraph to:

- Build sequential and conditional state graphs
- Run parallel LLM evaluations
- Create a simple chatbot interface

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd Langgraph_basic
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up your OpenAI API key:**
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## Examples

### 1. Sequential Workflow: BMI Calculator

- File: `1-langgraph-sequential.ipynb`
- Demonstrates a simple state graph to calculate BMI and classify it into categories.

### 2. Simple LLM Workflow

- File: `2_simple_llm.ipynb`
- Shows how to use LangGraph with an LLM (OpenAI) to answer questions in a stateful workflow.

### 3. Parallel LLM Workflow

- File: `3_parallel_llm.ipynb`
- Runs multiple LLM evaluations in parallel (e.g., language quality and completeness for an essay) and aggregates results.

### 4. Conditional Workflow

- File: `4_conditional_workflow.ipynb`
- Demonstrates conditional branching in a workflow, such as sentiment analysis and response generation based on user input.

### 5. Basic Chatbot (Streamlit)

- Folder: `5_basic_chatbot/`
- Run with:
  ```bash
  streamlit run 5_basic_chatbot/app.py
  ```
- A simple chatbot interface using LangGraph and OpenAI LLM.

## Environment Variables

- **Required:**
  - `OPENAI_API_KEY` (add to your `.env` file)

## Requirements

- Python 3.8+
- See `requirements.txt` for all dependencies.

---

**Note:**

- All examples require a valid OpenAI API key. Make sure to create a `.env` file in the root directory and add your key as shown above.
- For the chatbot, ensure you have Streamlit installed (included in the chatbot's requirements.txt).

## References

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Streamlit](https://streamlit.io/)
