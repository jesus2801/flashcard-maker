from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

CONFIG = """From now on I will only write English words in the prompts. Your job will be to send me back one JSON in the next format:
{
  "ipa": "[The IPA representation of the word]",
  "example": "[A common example of the word in the English language]",
  "example-meaning": "[The translation of the example to Spanish]",
  "synonyms": "[Common synonyms of the word]"

  "noun": "(optional) [If the word can be a noun, put its meanings as a noun]",
  "verb": "(optional) [If the word can be a verb, put its meanings as a verb]",
  "adjective": "(optional) [If the word can be an adjective, put its meanings as an adjective]",
  "preposition": "(optional) [If the word can be a preoposition, put its meanings as a preposition]",
  "adverb": "(optional) [If the word can be an adverb, put its meanings as an adverb]",
  "conjuction": "(optional) [If the word can be a conjuction, put its meanings as a conjuction]",
}"""

RESPONSE_EXAMPLE = """{
  "ipa": "blaɪnd",
  "example": "The blind man navigated the city with the help of his guide dog.",
  "example-meaning": "El hombre ciego navegó por la ciudad con la ayuda de su perro guía.",
  "synonyms": "Visually impaired - Sightless"

  "noun": "ciego - persiana",
  "verb": "cegar",
  "adjective": "ciego",
  "adverb": "a ciegas",
}"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a assistant that provides information about words."},
        {"role": "user", "content": CONFIG},
        {"role": "assistant", "content": "Okay, start with a word."},
        {"role": "user", "content": "blind"},
        {"role": "assistant", "content": RESPONSE_EXAMPLE},
        {"role": "user", "content": "work"},
    ]
)

print(response.choices[0].message)
