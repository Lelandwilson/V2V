# V2V Stage 1:

Audio Transcription Script
This script uses the STT (Speech-to-Text) library to transcribe audio files into text. It takes audio files from the input directory, transcribes them, and saves the transcriptions as separate text files in the output directory.

Getting Started
Prerequisites
Python 3.x
STT library (install instructions: link to STT library)
Installation
Clone this repository to your local machine:

git clone [https://github.com/Lelandwilson/V2V.git]
Install the required dependencies:


pip install -r requirements.txt

Usage:
Place your (input)audio files (in WAV format) in the ./stripped_vocals/ directory.
It will generate both audio chunks and place them in the ./audio-chunks/ directory & transcripts in the transcriptions directory.
These will be numbered so that they correspind. Warning, files in these directories will be overwritten with subsequent operations of the script.


Run the script using the following command:

python transcribe_audio.py
The script will transcribe each audio file in the input directory and save the transcriptions as separate text files in the transcriptions/ directory.

Configuration
You can modify the input_directory and output_directory variables in the transcribe_audio.py script to customize the input and output directories.

Acknowledgments
The STT library used in this script: STT GitHub repository
Librosa for audio processing
License
This project is licensed under the MIT License.

