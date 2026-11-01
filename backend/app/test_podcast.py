
from backend.app.podcast_service import (
    generate_podcast_script,
    generate_podcast_audio
)

import os


articles = [
    {
        "title": "Artificial Intelligence in India",
        "description": "India is increasing its focus on artificial intelligence and digital technology.",
        "content": "Artificial intelligence is becoming an important part of India's technology ecosystem. Educational institutions and companies are exploring AI applications in healthcare, agriculture and education."
    },
    {
        "title": "Digital Education Growth",
        "description": "Digital learning is expanding across India.",
        "content": "Digital education platforms are helping students access educational resources online. Technology is supporting learning opportunities in different parts of the country."
    }
]


print("Generating podcast script...")

script = generate_podcast_script(
    articles=articles,
    language_code="hi-IN",
    duration=2
)

print("\nPODCAST SCRIPT:\n")
print(script)


print("\nGenerating podcast audio...")

audio = generate_podcast_audio(
    script=script,
    language_code="hi-IN"
)

output_path = "test_podcast.mp3"

with open(output_path, "wb") as file:
    file.write(audio)

print("\nPodcast generated successfully!")
print("Audio saved at:", os.path.abspath(output_path))
