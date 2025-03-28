import os

transcript_folder = "data/transcripts/long_transcripts"
output_path = "data/transcripts/transcripts.txt"

with open(output_path, "w") as outfile:
    for file in sorted(os.listdir(transcript_folder)):
        if file.endswith(".txt"):
            audio_name = file.replace(".txt", ".wav")
            txt_path = os.path.join(transcript_folder, file)

            with open(txt_path, "r") as f:
                text = f.read().strip()
                line = f"{audio_name}|{text}"
                outfile.write(line + "\n")

print(f"✅ transcripts.txt created at {output_path}")