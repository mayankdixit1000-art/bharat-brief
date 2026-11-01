
from backend.app.chat_service import generate_chat_response

message = "Artificial Intelligence kya hai?"

response = generate_chat_response(
    message=message,
    language_code="hi-IN"
)

print("\nBharat Brief Chatbot Response:\n")
print(response)
