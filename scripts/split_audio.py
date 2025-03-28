from pydub import AudioSegment
import os

def split_audio_by_time(input_folder, output_folder, chunk_length=4000):
    """
    Splits all audio files in a folder into fixed-length chunks.

    Parameters:
    - input_folder: Path to the folder containing input audio files.
    - output_folder: Directory to save the output chunks.
    - chunk_length: Target length of each chunk in ms (default: 4 seconds).
    """

    # Ensure output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each file in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".wav"):  # Only process WAV files
            file_path = os.path.join(input_folder, file_name)
            audio = AudioSegment.from_file(file_path)

            # Generate unique prefix for each file's chunks
            base_name = os.path.splitext(file_name)[0]  # Remove .wav extension

            # Split into fixed-length chunks
            chunks = [audio[i:i+chunk_length] for i in range(0, len(audio), chunk_length)]
            print(f"Split {file_name} into {len(chunks)} chunks of ~{chunk_length / 1000} seconds each.")

            # Export chunks with a unique filename
            for i, chunk in enumerate(chunks):
                chunk_filename = f"{base_name}_chunk_{i}.wav"
                chunk.export(os.path.join(output_folder, chunk_filename), format="wav")
                print(f"Exported: {chunk_filename}")

if __name__ == "__main__":
    input_folder = "data/long_audio_clips"  # Folder with 1-2 min audio files
    output_folder = "data/my_custom_voice/wavs"  # Folder to store the 1-2 sec chunks
    split_audio_by_time(input_folder, output_folder)



