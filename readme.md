# Lecture Transcriber
Utilizes python libraries to transcribe audio files into text, then turns it into a nice readable format via AI. Uses the free Google Speech Recognition API by splitting audio chunks in 60 second intervals, then the text is passed to an OpenAI Model with appropriate prompts.

## Setup the Project
You must have an OpenAI account and API key for the program to use.
Download Python 3.12 
> Other version will most likely work, but this is the version it was developed on.

### The output is written in markdown. You should use a program that can read markdown files + mermaid to have the intended output, such as Notable.

Create a `.env` file and input your OpenAI API key named `OPENAPI_KEY`.

The project will create 4 additional directories.
- `audioChunk` - This is where chunks of audios are stored to be transcripted
- `inputFiles` - You may add videos/audios here
- `outputFiles` - Summarized transcripts will go here
- `transcripts` - Generated transcripts will go here

There is an instruction which acts as the developer instruction to OpenAI's model. However this seems to be less efficient than having it as an actual prompt in the OpenAI's model. Consider adding the prompt from `instruction.txt` into a model.

## Instructions
> You will need a connection to the internet in order to connect to Google Speech Recognition and OpenAI
1. Run `transcriptgenerator.py` and select a video `.mp4` file. This will start generating a transcript of the file.
2. With a transcript generated in the `transcripts` folder, run `transcriptsummariser.py` and select the transcript from there.
3. A summarized version in markdown format will be generated in the `outputFiles` folder.
4. Read it using a markdown reader or a default text editor.
