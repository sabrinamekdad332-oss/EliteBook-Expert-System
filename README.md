HP EliteBook 845 G8 Diagnostic Expert System
Project Overview
This project is an interactive Expert System designed to troubleshoot and diagnose common hardware and software issues specifically for the HP EliteBook 845 G8 Notebook PC. Unlike traditional procedural scripts, this system utilizes a declarative approach to match user-reported symptoms against a specialized knowledge base to provide expert-level recommendations.  

🧠 Expert System Theory
This project demonstrates the core principles of AI rule-based systems:

Knowledge Base: A set of predefined rules that represent expert-level troubleshooting logic.  

Working Memory: A collection of facts declared by the user during the diagnostic interview.  

Inference Engine: The underlying mechanism (provided by the experta library) that matches facts to rules to reach a conclusion.  

In contrast to regular programming, which relies on linear if-else flow, this system is Declarative. The rules are independent, and the engine determines the execution path based on the pattern of facts provided.  

📁 Project Structure
The code is organized into modular files to satisfy academic requirements for class-based organization:  

facts.py: Defines the Fact classes, representing the "vocabulary" of symptoms and issues the system can recognize.  

rules.py: Contains the EliteBookTroubleshooter engine and the @Rule logic for diagnosis.  

main.py: The user interface that conducts the interactive interview and executes the inference engine.  

🚀 Installation & Usage
Prerequisites
Python 3.10 or higher

experta library

Setup
Clone this repository:

Bash
git clone https://github.com/sabrinamekdad332-oss/EliteBook-Expert-System.git
Install the required library:

Bash
pip install experta
Running the System
Execute the main script to start the interactive diagnostic session:

Bash
python main.py
🛠️ Technical Compatibility Note
This project includes a compatibility bridge for Python 3.10+. Because the experta library relies on a deprecated collections.Mapping attribute, a "shim" was implemented in main.py to ensure the system runs correctly on modern Python environments.  

👥 Team Members
Mekada Sara Sabrina
