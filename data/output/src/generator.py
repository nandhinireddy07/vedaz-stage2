import os
import json
from dotenv import load_dotenv
from google import genai
from checker import check_structure, check_safety

# Load API Key
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

output_file = "generated_chats.jsonl"

with open(output_file, "a", encoding="utf-8") as f:

    for i in range(4):

        prompt = """
Generate ONE unique astrology conversation.

Every conversation must be different from previous ones.

Use different zodiac signs, astrology topics, life situations, questions, and answers.

Return ONLY valid JSON.

Format:

{
  "messages":[
    {
      "role":"system",
      "content":"You are a helpful astrology assistant."
    },
    {
      "role":"user",
      "content":"Ask any astrology question."
    },
    {
      "role":"assistant",
      "content":"Give a safe, balanced astrology response."
    }
  ]
}

Do not add markdown.
Do not use ```json.
Return only JSON.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        # Remove markdown if Gemini adds it
        text = text.replace("```json", "").replace("```", "").strip()

        try:
            obj = json.loads(text)

            if check_structure(obj) and check_safety(obj):
                f.write(json.dumps(obj, ensure_ascii=False) + "\n")
                print(f"✅ Chat {i+1} saved")
            else:
                print(f"❌ Chat {i+1} rejected")

        except Exception:
            print(f"❌ Chat {i+1} invalid")