
import os
from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

try:
    response = client.text.translate(
        input="The Government of India has launched a new scheme for farmers.",
        source_language_code="en-IN",
        target_language_code="hi-IN",
        model="sarvam-translate:v1"
    )

    print("Original English Text:")
    print("The Government of India has launched a new scheme for farmers.")

    print("\nHindi Translation:")
    print(response.translated_text)

    print("\nTranslation API working successfully!")

except Exception as e:
    print("\nTranslation API Error:")
    print(e)
