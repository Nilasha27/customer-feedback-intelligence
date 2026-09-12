# AI Customer Feedback Analyzer

An AI-powered customer feedback analysis application built using LangChain and an LLM.

## Features

- Customer sentiment classification
- Feedback categorization
- Priority detection
- Automatic summarization
- Recommended action generation
- Pydantic structured output
- LCEL-based pipeline
- Runnable components

## Architecture

Customer Feedback
        |
        v
RunnableLambda
        |
        v
Clean Feedback
        |
        v
ChatPromptTemplate
        |
        v
Chat Model
        |
        v
Structured Output
        |
        v
Pydantic Validation
        |
        v
Feedback Analysis

## Tech Stack

- Python
- LangChain
- Gemini
- Pydantic
- LCEL

## LangChain Concepts Demonstrated

- Chat Models
- ChatPromptTemplate
- Structured Output
- Pydantic
- Runnable
- RunnableLambda
- RunnableParallel
- LCEL
- invoke()


## Future Enhancements

- RAG over customer service policies
- Vector database
- Agentic workflows
- Customer/order API integration
- FastAPI
- Docker
- LangSmith observability
- Evaluation framework