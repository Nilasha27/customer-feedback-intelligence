# Customer Feedback Intelligence Platform

> **Turning unstructured customer feedback into actionable intelligence and automated customer support workflows.**

An **LLM-powered customer feedback intelligence platform** that analyzes unstructured feedback, extracts actionable insights and automates the initial customer-support workflow.

The platform is designed with a **banking/retail customer experience use case** in mind, where feedback needs to be converted into structured intelligence for both **customer service teams and business stakeholders**.

---

### 🚀 What It Does

* 💬 Captures customer feedback through a **Streamlit application**
* 🧠 Uses **LangChain + LLMs** pipeline to analyze feedback
* 🏷️ Extracts **sentiment, category, priority & summary**
* 💡 Generates **recommended actions and customer responses**
* 🎫 Identifies **feedback requiring support** and generates **support tickets**
* 💾 Stores raw and LLM-enriched feedback in **SQLite**
* ⚡ Supports **batch processing of historical feedback**

---

### 🛠️ Technology Stack

#### Application

* Python
* Streamlit

#### LLM / AI

* LangChain
* Large Language Models(Gemini)
* Structured LLM outputs
* Prompt engineering

#### Database

* SQLite

#### Development

* VS Code
* Git
* GitHub
* Python virtual environment

---

### 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │   Streamlit UI      │
                    │                     │
                    │ Customer Feedback   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Application Layer  │
                    │                     │
                    │ process_customer_   │
                    │ feedback()          │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
        ┌─────────────────┐        ┌─────────────────┐
        │ customer_       │        │ Feedback        │
        │ feedback        │        │ Analyzer        │
        │                 │        │                 │
        │ Raw Feedback    │        │ LangChain + LLM │
        └─────────────────┘        └────────┬────────┘
                                            │
                                            ▼
                                  ┌─────────────────────┐
                                  │ Structured Output   │
                                  │                     │
                                  │ Sentiment           │
                                  │ Category            │
                                  │ Priority            │
                                  │ Summary             │
                                  │ Recommended Action  │
                                  │ Requires Support    │
                                  │ Customer Response   │
                                  └──────────┬──────────┘
                                             │
                                             ▼
                                  ┌─────────────────────┐
                                  │ Support Ticket      │
                                  │ Generation          │
                                  └──────────┬──────────┘
                                             │
                                             ▼
                                  ┌─────────────────────┐
                                  │ llm_enriched_       │
                                  │ feedback            │
                                  │                     │
                                  │ AI-generated        │
                                  │ intelligence        │
                                  └─────────────────────┘
```
---

### 🔄 Current Workflow

When a customer submits feedback:

```text
1. Customer enters feedback
             ↓
2. Generate feedback_id
             ↓
3. Store raw feedback
   → customer_feedback
             ↓
4. Send feedback to LLM
             ↓
5. Generate structured analysis
             ↓
6. Determine requires_support
             ↓
7. Generate support ticket if required
             ↓
8. Store LLM enrichment
   → llm_enriched_feedback
             ↓
9. Return customer response
             ↓
10. Display response in Streamlit
```

---

### 🧠 LLM Processing Pipeline

The feedback analysis pipeline is built using **LangChain**.

```text
Customer Feedback
       ↓
   Cleaner
       ↓
 Feedback Prompt
       ↓
 Structured LLM
       ↓
 Pydantic / Structured Output
       ↓
 Enriched Feedback
```

The structured output makes the LLM response predictable and suitable for downstream database storage and analytics.

---

### 🗂️ Historical Feedback Processing Workflow

```text
Existing customer_feedback
          ↓
Identify unprocessed records
          ↓
Process in batches
          ↓
feedback_analyzer.batch()
          ↓
Generate structured LLM output
          ↓
Generate support ticket where required
          ↓
llm_enriched_feedback
```
---

### 🎯 Planned Enhancements

The next stage of the project will focus on moving from an **LLM-powered application** toward a more production-oriented **Customer Feedback Intelligence Platform**.

#### 📚 RAG

* [ ] Add knowledge base for product policies and FAQs
* [ ] Implement Retrieval-Augmented Generation
* [ ] Ground customer responses in approved business knowledge
* [ ] Add metadata-aware retrieval

#### 🤖 Agentic AI

* [ ] Introduce tool calling
* [ ] Build feedback-resolution agents
* [ ] Integrate support-ticket workflows
* [ ] Explore MCP-based tool integration
* [ ] Add human-in-the-loop escalation

#### 📊 Business Intelligence

* [ ] Feedback trend analysis
* [ ] Product-level issue identification
* [ ] Customer pain-point analysis
* [ ] Sentiment trends over time
* [ ] Priority and escalation dashboards
* [ ] Root-cause analysis
* [ ] Business recommendation layer

#### 🧪 LLM Evaluation

* [ ] Build evaluation datasets
* [ ] Measure classification accuracy
* [ ] Evaluate response quality
* [ ] Monitor hallucinations
* [ ] Implement LLM evaluation framework

#### ☁️ Production & MLOps

* [ ] Containerize application using Docker
* [ ] Deploy on GCP
* [ ] Integrate BigQuery
* [ ] Add CI/CD
* [ ] Add application monitoring
* [ ] Add LLM observability
* [ ] Implement authentication and access control

---

### 💼 Business Value

The platform can help organizations move from:

```text
Unstructured Feedback
        ↓
Manual Review
        ↓
Delayed Action
```

to:

```text
Unstructured Feedback
        ↓
AI-powered Analysis
        ↓
Structured Intelligence
        ↓
Automated Action
        ↓
Human Escalation When Required
        ↓
Business Insights
```
---

> 🚧 **Project Status:** Actively under development — evolving from an LLM-powered feedback analysis application toward a production-oriented AI customer intelligence platform.


