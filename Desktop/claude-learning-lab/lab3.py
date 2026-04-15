# LAB 3: Fine-Tuning vs Adapters vs RAG

# ── STEP 2: Knowledge Base ──────────────────────────────
kb = [
    "Agentic AI agents use memory, tools, and goals to act.",
    "LangChain and CrewAI are popular frameworks for building AI agents.",
    "Retrieval-Augmented Generation (RAG) improves accuracy by fetching external knowledge."
]
questions = [
    "What are the key components of Agentic AI?",
    "Name one framework for AI agents.",
    "How does RAG improve answers?"
]
print("✅ Step 2 done - Knowledge base loaded")

# ── STEP 3: Fine-Tuning Dataset ─────────────────────────
from datasets import Dataset

train_data = Dataset.from_dict({
    "prompt": [
        "Q: What are the key components of Agentic AI?\nA:",
        "Q: Name one framework for AI agents.\nA:",
        "Q: How does RAG improve answers?\nA:"
    ],
    "completion": [
        " Agentic AI agents use memory, tools, and goals to act.",
        " LangChain is a framework for building AI agents.",
        " RAG improves accuracy by fetching external knowledge before answering."
    ]
})
print("\n✅ Step 3 done - Fine-tuning dataset:")
print(train_data)

# ── STEP 4: Adapters/LoRA Demo ───────────────────────────
print("\n✅ Step 4 done - Adapter/LoRA concept:")
print("Model: distilgpt2")
print("Estimated parameters: ~82,000,000")
print("With LoRA, you'd train ~1% of these instead of all of them.")
print("(PyTorch skipped - Python 3.14 not yet supported)")
# ── STEP 5: RAG ─────────────────────────────────────────
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Build vector DB from knowledge base
docs = [Document(page_content=x) for x in kb]
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(docs, embeddings)

retriever = db.as_retriever()
llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_template(
    "Answer using only this context:\n{context}\n\nQuestion: {question}"
)

def ask(question):
    context = "\n".join([d.page_content for d in retriever.invoke(question)])
    chain = prompt | llm
    return chain.invoke({"context": context, "question": question}).content

# Run your questions
for q in questions:
    print("\nQ:", q)
    print("A:", ask(q))

# Bonus question
print("\nQ: Explain Agentic AI like I'm 10.")
print("A:", ask("Explain Agentic AI like I'm 10."))

print("\n✅ Step 5 done - RAG complete")
# ── STEP 6: Comparison Summary ──────────────────────────
# METHOD       | PROS                        | CONS                        | BEST FOR
# -------------|-----------------------------|-----------------------------|------------------
# Fine-Tuning  | Accurate, baked-in          | Expensive, rigid            | Narrow domains
# Adapters     | Cheaper, modular            | Still needs training infra  | Domain adaptation
# RAG          | Flexible, real-time updates | Needs good retriever        | Dynamic knowledge
#
# WHY RAG FOR AGENTIC AI:
# Agents need up-to-date, flexible knowledge. Fine-tuning bakes in static info
# that goes stale. RAG lets agents pull fresh context at runtime — perfect for
# dynamic environments where knowledge changes constantly
