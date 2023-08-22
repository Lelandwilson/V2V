from STT import AudioTranscription
import os


def generate_transcription_files(input_directory, output_directory):
    audio_transcription = AudioTranscription()

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # List all files in the input directory
    input_files = os.listdir(input_directory)

    for idx, input_file in enumerate(input_files):
        if input_file.endswith(".wav"):
            input_path = os.path.join(input_directory, input_file)
            output_txt_path = os.path.join(output_directory, f"transcription_{idx + 1}.txt")

            print(f"[✓] Loading input audio sample: {input_path}")
            print(f"[✓] Generating transcription for: {output_txt_path}")

            audio_transcription.get_large_audio_transcription_on_silence(input_path, output_txt_path)


if __name__ == "__main__":
    input_directory = './stripped_vocals/'
    output_directory = './transcriptions/'

    generate_transcription_files(input_directory, output_directory)
    print("[✓] Transcription files generated for all input audio files.")
