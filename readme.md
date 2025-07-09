# Lecture Transcriber
Utilizes python libraries to transcribe audio files into text, then turns it into a nice readable format via AI. Uses the free Google Speech Recognition API by splitting audio chunks in 60 second intervals, then the text is passed to an OpenAI Model with appropriate prompts.

## Setup the Project
You must have an OpenAI account and API key for the program to use.

### The output is written in markdown. You should use a program that can read markdown files + mermaid to have the intended output, such as Notable.

Create a `.env` file and input your OpenAI API key named `OPENAPI_KEY`.

The project will create 4 additional directories.
- `audioChunk` - This is where chunks of audios are stored to be transcripted
- `inputFiles` - You may add videos/audios here
- `outputFiles` - Summarized transcripts will go here
- `transcripts` - Generated transcripts will go here

There is an instruction which acts as the developer instruction to OpenAI's model. However this seems to be less efficient than having it as an actual prompt in the OpenAI's model. Consider adding the prompt from `instruction.txt` into a model.
