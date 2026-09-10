# Document Search and Abstraction

Ask a question about local text documents and get matching passages with citations. Each result identifies the source, section, and character offsets, making it easy to check the answer against the document.

## Run it on your computer

You need **Python 3.11 or newer**. Check with `python3 --version` on macOS/Linux or `py -3 --version` on Windows. If Python is missing, install it from [python.org](https://www.python.org/downloads/) and reopen your terminal.

### 1. Download the project

If you have Git, run:

```bash
git clone https://github.com/mkm-007/doc-abstraction-llm.git
cd doc-abstraction-llm
```

Without Git: select **Code → Download ZIP** on this GitHub page, extract the ZIP, and open a terminal in the extracted folder. You should see `README.md`, `start.py`, and `run_demo.py` in that folder. Open the folder in VS Code and choose **Terminal → New Terminal** if that is easier.

### 2. Start the interactive demo

**macOS / Linux:**

```bash
python3 start.py
```

**Windows PowerShell:**

```powershell
py -3 start.py
```

No package installation, API key, database account, or paid service is needed for this step. This is a terminal program: type your question/request at its prompt and press Enter. Type `quit` to stop, or press Ctrl+C.

Try this first:

```text
What is the annual leave entitlement?
```

The included sample policy says employees receive **20 days of annual leave**, with up to **5 days carried over**. The output cites `leave_policy.txt` and includes the original passage.

### 3. Run a single request

For scripts or a structured JSON response, use:

```bash
python3 run_demo.py --question "What is the annual leave entitlement?"
```

On Windows, replace `python3` with `py -3`. See [sample output](demo_output.txt) for a complete response. These commands finish after one request; `start.py` stays open for more.

## Search your own document

Save a UTF-8 `.txt` or `.md` file in the project folder, then run:

```bash
python3 run_demo.py --document "my-notes.txt" --question "What are the deadlines?"
```

On Windows, use `py -3` instead of `python3`. Paths containing spaces must be quoted. The file must already exist; the program does not create or overwrite your documents.

You can search more than one file:

```bash
python3 run_demo.py --document "policy.txt" --document "handbook.txt" --question "annual leave"
```

Or use interactive mode: type `load my-notes.txt`, then enter your question. Type `sources` to list loaded files. The sample policy is loaded when the interactive session starts.

## What happens when you run it

1. The program reads the supplied documents locally.
2. It splits them around headings and bounds the size of long sections.
3. It ranks chunks by matching words in your question.
4. It returns original passages with numbered citations. If no useful words overlap, it returns “No relevant context.”

The index lives in memory for the current process. Reloading the same file replaces its indexed content, so changes to a document do not accumulate duplicate passages. Files sharing a name have different source IDs. `start` and `end` in each citation are character offsets into the original file.

## Current scope

This version retrieves and quotes passages; it does not generate an LLM summary. The repository retains its original `doc-abstraction-llm` URL, but the runnable implementation uses lexical matching rather than embeddings or ChromaDB. It reads UTF-8 text/Markdown files up to 1 MB each. PDFs, Word files, scanned images, and persistent indexing are not supported. A matching passage may still not answer your question, so review its citation.

## Run the tests (optional)

The demos use Python's standard library. **pytest is needed only for tests.** From the repository folder:

**macOS / Linux:**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q
```

**Windows PowerShell:**

```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m pytest -q
```

The commands use the environment's Python directly, so you do not need to activate it or change PowerShell's execution policy. GitHub also runs the tests automatically.

## Troubleshooting

- **`python3` or `py` not found**: install Python, reopen your terminal, and check its version.
- **“Can't open file start.py”**: your terminal is in the wrong folder. Open the folder containing this README and `start.py`.
- **A download/install command fails**: downloading the ZIP, cloning, and installing test/compiler dependencies require internet. The Python demo runs offline once downloaded.
- **“No relevant context”**: try words that appear in the document. This version matches words rather than paraphrases.
- **File not found**: check the filename and put quotes around paths containing spaces. Relative paths are resolved from your current folder.
- **Encoding error**: export the document as UTF-8 plain text. Renaming a PDF to `.txt` does not convert it.
- **Document too large**: use a text file no larger than 1 MB.

## About this project

A personal implementation inspired by my hands-on project experience at CATS, GITAM University. It uses sample data and does not include the original CATS source code.

[Implementation notes](ENGINEERING.md) · [GitHub portfolio](https://github.com/mkm-007/MKM)
