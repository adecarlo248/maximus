"""
Lab 1: Building Short-Term and Long-Term Memory Modules
Course: Certified Master in Agentic AI

Short-term memory  → conversation history in the context window (resets per session)
Long-term memory   → ChromaDB vector store (persists across sessions)
"""

import os
import sys
sys.stdout.reconfigure(encoding="utf-8")
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

client = OpenAI()

# ─────────────────────────────────────────────
# STEP 2: Short-Term Memory (Context Window)
# ─────────────────────────────────────────────
# The model only "remembers" what's in the messages list.
# No messages = no memory. Pass the full history = recall works.

def chat_with_memory(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return response.choices[0].message.content

print("=" * 50)
print("STEP 2: SHORT-TERM MEMORY DEMO")
print("=" * 50)

conversation = [
    {"role": "system", "content": "You are a helpful tutor."},
    {"role": "user",   "content": "My name is Alex."},
]

reply1 = chat_with_memory(conversation)
conversation.append({"role": "assistant", "content": reply1})
print(f"AI (after intro): {reply1}")

conversation.append({"role": "user", "content": "What is my name?"})
reply2 = chat_with_memory(conversation)
print(f"AI (recalls name): {reply2}")

# Demonstrate forgetting: start fresh, ask without history
fresh = [
    {"role": "system", "content": "You are a helpful tutor."},
    {"role": "user",   "content": "What is my name?"},
]
reply_no_memory = chat_with_memory(fresh)
print(f"\nAI (fresh session, no history): {reply_no_memory}")
print("→ Without history, the model can't know your name.\n")


# ─────────────────────────────────────────────
# STEP 3: Long-Term Memory (ChromaDB Vector Store)
# ─────────────────────────────────────────────
# Facts stored here survive across sessions.
# ChromaDB persists to disk so a new script run can still retrieve them.

print("=" * 50)
print("STEP 3: LONG-TERM MEMORY DEMO")
print("=" * 50)

embeddings = OpenAIEmbeddings()

docs = [
    Document(page_content="Agentic AI agents use tools and memory to complete tasks."),
    Document(page_content="LangChain helps build autonomous agents with chains and tools."),
    Document(page_content="RAG improves accuracy by retrieving knowledge before answering."),
    Document(page_content="CrewAI enables multi-agent orchestration for complex workflows."),
]

# persist_directory keeps the DB on disk between runs
db = Chroma.from_documents(
    docs,
    embeddings,
    collection_name="long_term_memory",
    persist_directory="./chroma_db"
)

def recall(query):
    """Retrieve the most relevant stored facts for a query."""
    retriever = db.as_retriever(search_kwargs={"k": 2})
    results = retriever.invoke(query)
    return [r.page_content for r in results]

print("Query: 'How do agents use knowledge?'")
for fact in recall("How do agents use knowledge?"):
    print(f"  → {fact}")

# Dynamically add a new fact
new_fact = Document(page_content="OpenClaw runs always-on agents accessible via WhatsApp.")
db.add_documents([new_fact])
print("\nAdded new fact. Querying for it:")
for fact in recall("How can agents be accessed remotely?"):
    print(f"  → {fact}")


# ─────────────────────────────────────────────
# STEP 4: Combined Short-Term + Long-Term Memory
# ─────────────────────────────────────────────
# Short-term holds the conversation context (user preferences, recent turns).
# Long-term retrieves stored knowledge to augment the answer.

print("\n" + "=" * 50)
print("STEP 4: COMBINED MEMORY DEMO")
print("=" * 50)

llm = ChatOpenAI(model="gpt-4o-mini")
retriever = db.as_retriever(search_kwargs={"k": 2})

# LCEL chain: retrieve relevant docs, inject into prompt, generate answer
prompt = ChatPromptTemplate.from_template(
    "Use the context below to answer the question.\n\n"
    "Context:\n{context}\n\n"
    "Question: {question}"
)

def format_docs(docs):
    return "\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Simulate short-term memory: model knows user's favorite framework from conversation
conversation2 = [
    {"role": "system",    "content": "You are a teaching AI agent."},
    {"role": "user",      "content": "Remember my favorite framework is LangChain."},
    {"role": "assistant", "content": "Got it, your favorite framework is LangChain."},
    {"role": "user",      "content": "What's my favorite framework and how do agents use memory?"},
]

short_term_ans = chat_with_memory(conversation2)
print(f"Short-term only:\n  {short_term_ans}\n")

long_term_ans = rag_chain.invoke("How do agents use memory?")
print(f"Long-term (RAG) augmented:\n  {long_term_ans}\n")


# ─────────────────────────────────────────────
# STEP 5: Reflection Experiment
# ─────────────────────────────────────────────
# Reset short-term → model forgets LangChain preference.
# Long-term always recalls stored facts regardless of session.

print("=" * 50)
print("STEP 5: REFLECTION — SHORT-TERM RESET")
print("=" * 50)

reset_conversation = [
    {"role": "system", "content": "You are a teaching AI agent."},
    {"role": "user",   "content": "What's my favorite framework?"},
]
forgot = chat_with_memory(reset_conversation)
print(f"After reset (short-term): {forgot}")
print("→ Short-term forgot — conversation history was cleared.\n")

print("Long-term still recalls stored knowledge:")
for fact in recall("What frameworks help build agents?"):
    print(f"  → {fact}")

print("\n✅ Lab 1 complete.")
print("Key insight: Short-term = what's in the prompt. Long-term = what's in the vector store.")
print("Agents need both: conversation context for flow, persistent DB for durable knowledge.")
