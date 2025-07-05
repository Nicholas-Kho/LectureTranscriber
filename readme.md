# Lecture Transcriber
Utilizes python libraries to transcribe audio files into text, then turns it into a nice readable format via AI. Uses the free Google Speech Recognition API by splitting audio chunks in 60 second intervals, then the text is passed to an OpenAI Model with appropriate prompts.

## Setup the Project
You must have an OpenAI account and API key for the program to use.

### The output is written in markdown. You should use a program that can read markdown files + mermaid to have the intended output, such as Notable.