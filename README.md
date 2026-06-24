# 🌍 TravelGenie - Agentic Travel Planner

An intelligent AI-powered travel planning assistant built using Generative AI, Agentic AI, LangChain, MCP Servers, and Google Gemini/OpenAI models.

The application helps users create personalized travel itineraries, discover hotels, find attractions, estimate budgets, and plan complete trips using AI agents.

---

## 🚀 Features

### ✈️ Trip Planning
- Generate complete travel itineraries
- Day-wise travel schedules
- Personalized recommendations
- Multi-city planning

### 🏨 Hotel Search
- Search hotels using MCP servers
- Budget-based recommendations
- Hotel comparison
- Ratings and amenities analysis

### 📍 Attraction Discovery
- Tourist attractions
- Local experiences
- Hidden gems
- Nearby places recommendation

### 🍽️ Restaurant Recommendations
- Popular restaurants
- Cuisine-based suggestions
- Budget-friendly options

### 💰 Budget Estimation
- Flight costs
- Hotel expenses
- Food expenses
- Transportation costs

### 🤖 Agentic AI Workflow
- Planner Agent
- Hotel Agent
- Budget Agent
- Local Guide Agent
- Itinerary Agent

### 🔎 RAG Support
- Travel knowledge retrieval
- Destination-specific information
- Travel policies and guidelines

---

## 🏗️ Architecture

User Query
    ↓
Travel Planner Agent
    ↓
─────────────────────────────
|      Multi-Agent System    |
─────────────────────────────
    ↓
Hotel Agent
Budget Agent
Attraction Agent
Restaurant Agent
    ↓
LLM (Gemini/OpenAI)
    ↓
Final Travel Plan

---

## 🛠️ Tech Stack

### AI Framework
- LangChain
- LangGraph
- LangSmith

### LLM
- Google Gemini
- OpenAI GPT

### MCP Servers
- Airbnb MCP
- Google Maps MCP
- Booking MCP (Optional)

### Vector Database
- FAISS
- ChromaDB
- Pinecone

### Frontend
- Streamlit

### Backend
- FastAPI

### Deployment
- Docker
- Render
- AWS
- Azure

---

## 📂 Project Structure

travelmind-ai/
│
├── app/
│   ├── agents/
│   │   ├── planner_agent.py
│   │   ├── hotel_agent.py
│   │   ├── budget_agent.py
│   │   └── itinerary_agent.py
│   │
│   ├── tools/
│   │   ├── hotel_search.py
│   │   ├── maps_tool.py
│   │   └── budget_tool.py
│   │
│   ├── prompts/
│   │   ├── planner_prompt.py
│   │   └── itinerary_prompt.py
│   │
│   ├── rag/
│   │   ├── ingestion.py
│   │   ├── retriever.py
│   │   └── vectorstore.py
│   │
│   ├── api/
│   │   └── routes.py
│   │
│   └── main.py
│
├── frontend/
│   └── streamlit_app.py
│
├── data/
│
├── tests/
│
├── requirements.txt
│
├── .env
│
└── README.md

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/travelmind-ai.git

cd travelmind-ai
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key

OPENAI_API_KEY=your_openai_api_key

LANGCHAIN_API_KEY=your_langsmith_key

LANGCHAIN_TRACING_V2=true

LANGCHAIN_PROJECT=TravelMindAI
```

---

## ▶️ Run Backend

```bash
uvicorn app.main:app --reload
```

---

## ▶️ Run Streamlit Frontend

```bash
streamlit run frontend/streamlit_app.py
```

---

## Example Queries

### Example 1

User:

```text
Plan a 5-day trip to Goa under ₹30,000.
```

### Example Output

```text
Day 1:
- Arrival
- Check-in
- Beach Visit

Day 2:
- Water Sports
- Local Sightseeing

Day 3:
- Dudhsagar Falls

Day 4:
- Shopping

Day 5:
- Departure
```

---

### Example 2

User:

```text
Find hotels in Hyderabad near Hitech City under ₹5000/night.
```

---

## Future Enhancements

- Flight Booking Integration
- Live Weather Information
- Currency Conversion
- Visa Guidance
- Travel Insurance Suggestions
- Voice-based Travel Planning
- Multi-language Support

---

## Skills Demonstrated

- Generative AI
- Agentic AI
- LangChain
- LangGraph
- MCP Servers
- RAG
- Vector Databases
- FastAPI
- Streamlit
- Prompt Engineering
- Multi-Agent Systems

---

## Author

Praveen Puli

Generative AI Engineer