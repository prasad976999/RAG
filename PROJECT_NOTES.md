FINANCIAL-REPORT RESEARCH ASSISTANT — PROJECT NOTES

1. PROJECT GOAL

Build an advanced Retrieval-Augmented Generation (RAG)
application with an evaluation harness for a portfolio
targeting AI jobs in Ireland and the UK.

RAG retrieves relevant evidence from documents and gives
that evidence to a language model to help answer questions.

The evaluation harness runs repeatable checks to measure
how well retrieval and answer generation work.


2. LEARNING APPROACH

Current knowledge:
- Comfortable with APIs.
- A little SQL.
- Need to learn Python and Git.

Teach Python, APIs, SQL, and Git while building the project.
Use small steps and explain:
- What each piece of code does.
- Why we chose a particular design.
- How to run and verify it.
- Common failures and how to diagnose them.
- How to explain decisions in an interview.


3. BUDGET

Use free tools and local models.
No paid APIs or subscriptions required.

Local models still require downloads, storage, memory,
and electricity. Hardware suitability must be checked.


4. APPLICATION SCOPE

Build a financial-report research assistant.

Start with three public annual reports from one UK or
Irish company across different years.

The company and reports have not been selected yet.

The assistant should:
- Answer questions using evidence from the reports.
- Cite the report and page supporting each answer.
- Distinguish financial years, currencies, and units.
- Say when evidence is insufficient.
- Handle questions requiring multiple passages.

Start with text-based questions.
Add financial table extraction and calculations later.


5. PROPOSED TECHNOLOGY

Python 3.12:
Application logic, document processing, and evaluations.

FastAPI:
Expose the application through HTTP API endpoints.

SQLite:
Store document metadata and evaluation results.
SQLite is included with Python.

SQLite FTS5:
Keyword search over document passages.

Local embedding model:
Represent questions and passages for semantic search.

Hybrid retrieval:
Combine keyword search and semantic search.

Reranker:
Reorder retrieved passages by relevance.
Add this after measuring the baseline.

Ollama:
Run the answer-generation model locally.

pytest:
Automated tests for important application behaviour.

Git and GitHub:
Track changes and publish the project history.

Visual Studio Code:
Code editor, with Microsoft's Python extension.

These choices are proposed, not implemented yet.


6. TENTATIVE MODEL CANDIDATES

Answer generation:
Qwen3 4B through Ollama, using a quantized version.
Ollama model tag proposed: qwen3:4b

Embeddings:
BGE-small-en-v1.5

Reranking:
BGE-reranker-base

These are starting candidates, not confirmed best models.
None has been installed or benchmarked.

Check the Windows laptop's RAM and GPU before selecting
the answer model. Earlier Mac hardware details do not apply.

Quantization reduces model memory requirements by storing
weights at lower precision, with possible quality tradeoffs.

Choose models using measured answer quality, retrieval
quality, latency, and resource use.


7. EVALUATION PLAN

Measure:
- Retrieval success: did we retrieve the required evidence?
- Answer correctness: does the answer match the evidence?
- Citation support: do cited passages support the claims?
- Abstention: does the system decline unsupported questions?
- Latency: how long does each stage take?
- Resource use: memory and compute requirements.

Create manually reviewed questions, reference answers,
and supporting evidence passages.

Keep a held-out test set separate from development questions.

An LLM judge may help, but must not be the only source
of truth.

Compare:
- Basic semantic retrieval.
- Different chunking settings.
- Hybrid retrieval.
- Hybrid retrieval with reranking.
- Suitable generation models.

Record configurations and results so experiments can
be reproduced. Document failures honestly.


8. CURRENT COMPUTER

Personal Windows laptop.
User reports no company permission restrictions.

Still need to check:
- Processor.
- Installed RAM.
- GPU model.
- Dedicated GPU memory, if available.

Previous computer was a company-managed M4 MacBook Air.
Mac Homebrew and sudo instructions do not apply to Windows.

No Mac system files or Python environments need transferring.


9. WINDOWS TOOL STATUS

Earlier PowerShell output showed:
- Python was not found.
- Git was not recognised.
- brew was not recognised, which is expected on Windows.

No successful Windows tool installation has been verified.

WinGet is the Windows package manager we plan to use.
It is normally available through Microsoft's App Installer.

Required installations:
- Python 3.12.
- Git.
- Visual Studio Code.
- Ollama.
- Microsoft's Python extension for VS Code.

Docker, a separate database server, and manual CUDA
installation are not needed initially.


10. WINDOWS INSTALLATION COMMANDS

Open PowerShell.

First check:

winget --version

If WinGet is missing, install or update Microsoft's
App Installer from the Microsoft Store, then reopen PowerShell.

Run these installation commands individually, waiting
for each to finish:

winget install --id Python.Python.3.12 --exact

winget install --id Git.Git --exact

winget install --id Microsoft.VisualStudioCode --exact

winget install --id Ollama.Ollama --exact

After installation, close and reopen PowerShell.

Verify:

py -3.12 --version

git --version

code --version

ollama --version

Install the Python extension published by Microsoft
from VS Code's Extensions tab.

Do not download a model until we check the laptop hardware.

These commands have been proposed; success on the laptop
has not yet been verified.


11. REPOSITORY AND SAVED FILES

GitHub repository:
https://github.com/prasad976999/RAG

At initial inspection, it contained:
- README.md
- LICENSE

No application code, reports, evaluation dataset, or
downloaded models have been created yet.

The repository ZIP has now been downloaded and extracted
on the Windows laptop.

The screenshot showed the extracted folder under:
Downloads > RAG-main > RAG-main

The complete absolute path has not been confirmed.

Save this file as PROJECT_NOTES.md in that same folder.

Expected files:
- LICENSE
- README.md
- PROJECT_NOTES.md

The downloaded ZIP does not include Git history.
Later, use a Git clone for normal development and copy
these notes into that checkout.

Notes were also saved in the cloud workspace.
They have not been committed or pushed to GitHub.


12. BUILD ORDER

1. Save these notes locally.
2. Install and verify the Windows development tools.
3. Check RAM and GPU.
4. Clone the GitHub repository and preserve these notes.
5. Create an isolated Python environment.
6. Define the project requirements and select reports.
7. Create initial evaluation questions.
8. Learn Python and store report metadata in SQLite.
9. Extract report content with page metadata.
10. Build basic retrieval and cited answers.
11. Build the evaluation harness.
12. Compare chunking, hybrid retrieval, and reranking.
13. Improve abstention and reliability.
14. Add API and interface.
15. Write architecture and experiment documentation.
16. Prepare a reproducible portfolio demonstration.


13. FIRST IMPLEMENTATION MILESTONE

Read report content and store its metadata in SQLite.

Explain the Python code and SQL statements step by step.
Use Git to record completed, understandable changes.

Build a small working baseline before adding complexity.


14. FINAL PORTFOLIO DELIVERABLES

- Working financial-report assistant.
- Answers with evidence citations.
- Evaluation dataset and repeatable evaluation commands.
- Baseline and improved-system comparison.
- Latency and resource measurements.
- Architecture diagram.
- Clear setup documentation.
- Meaningful tests.
- Demonstration.
- Honest limitations and failure analysis.


15. WHERE TO RESUME

First verify the Windows tools and laptop hardware.
Then begin the first Python lesson and project setup.

Suggested message for continuing:

"I am continuing my financial-report RAG portfolio project.
Read PROJECT_NOTES.md and teach me step by step.
First help me verify my Windows tools and hardware."