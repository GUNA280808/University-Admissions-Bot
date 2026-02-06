# University-Admissions-Bot
AI chatbot for university admissions assistance
AI University Admissions Assistant

An intelligent chatbot designed to help students understand university admission processes, eligibility criteria, required documents, deadlines, and career opportunities through conversational interaction.

This project was developed as part of the Intel Unnati Program to simplify the admissions journey for students by providing a centralized, interactive information system.

**Problem Statement**

Students often face difficulties in:

Understanding admission eligibility criteria

Identifying required documents

Comparing programs across universities

Following the correct application steps

Tracking important deadlines

Admission information is usually scattered across multiple websites, brochures, and portals, making the process confusing and time-consuming.

**Proposed Solution**

The AI University Admissions Assistant is a conversational chatbot that:

Provides instant answers about academic programs

Explains eligibility requirements

Lists required documents

Shows career opportunities

Guides students through the admission process step by step

It functions as a virtual admissions counselor available at any time.

**Key Features
Core Capabilities**

Conversational chatbot interface

Multi-university knowledge base

Program-specific admission information

Step-by-step application guidance

Career path suggestions

Information Provided

Eligibility criteria

Entrance examinations

Required documents

Application deadlines

Fee structure

Program duration

Career opportunities

Knowledge Base Design

The chatbot uses a structured JSON knowledge base containing:

Multiple universities

Multiple programs per university

Admission requirements

Fees and program duration

Career outcomes

This structure makes the system:

Easy to update

Scalable to additional universities

Simple to maintain

System Architecture
User
  ↓
Streamlit Chat Interface
  ↓
Chatbot Logic (Python)
  ↓
Knowledge Base (JSON)
  ↓
Response Generator

Technology Stack
Layer	Technology
Frontend	Streamlit
Backend	Python
Chatbot Engine	Rule-based NLP logic
Knowledge Base	JSON
Version Control	Git and GitHub
Project Structure
University-Admissions-Bot
│
├── app.py                 # Streamlit interface
├── chatbot.py             # Chatbot logic
├── knowledge_base.json    # Admissions data


**Installation and Setup**
Step 1: Install Python

**Download and install Python from:**

https://www.python.org/downloads/

Step 2: Clone the Repository
git clone https://github.com/GUNA280808/University-Admissions-Bot.git
cd University-Admissions-Bot

Step 3: Install Dependencies
pip install streamlit

Step 4: Run the Application
streamlit run app.py

Step 5: Open in Browser

The application will open automatically at:

http://localhost:8501

**Sample Questions**
General

Tell me about computer science

What is the MBA program?

Eligibility

What marks are required for computer science?

What is the eligibility for MBA?

Entrance Exams

Which entrance exams are needed?

Is JEE required for computer science?

Documents

What documents are required for admission?

List documents for MBA.

Careers

What jobs can I get after computer science?

Career options after MBA.

Application Process

How do I apply for computer science?

What are the admission steps?
**
Example Conversation
**
User: I want to study computer science
Bot: Computer Science is a B.Tech program of four years duration.

User: What is the eligibility?
Bot: Minimum 60% in 12th with Physics, Chemistry, and Mathematics.

User: What documents are required?
Bot: 10th marks card, 12th marks card, entrance scorecard, and ID proof.

Future Enhancements

Integration with large language models for advanced conversational ability

PDF admission brochure question answering

Student profile-based program recommendations

Voice-enabled interaction

Web-based frontend with API backend

Multi-language support

**Author**

Gunashree R G
AI and Data Science Engineering Student

GitHub:
https://github.com/GUNA280808

License

This project is developed for educational purposes as part of the Intel Unnati Program.
