from openai import OpenAI
client = OpenAI()

config = """
From now on I will only write English words in the prompts. Your job will be to send me back two JSONs in the next format:
{
  "ipa": "[The IPA representation of the word]",
  "example": "[A common example of the word in the language]",
  "example-meaning": "[The translation of the example to Spanish]",
  "synonyms": "[Common synonyms of the word]"

  "noun": "(optional) [If the word can be a noun, put its meanings as a noun]",
  "verb": "(optional) [If the word can be a verb, put its meanings as a verb]",
  "adjective": "(optional) [If the word can be an adjective, put its meanings as an adjective]",
  "preposition": "(optional) [If the word can be a preoposition, put its meanings as a preposition]",
  "adverb": "(optional) [If the word can be an adverb, put its meanings as an adverb]",
  "conjuction": "(optional) [If the word can be a conjuction, put its meanings as a conjuction]",
  "conjuction": "(optional) [If the word can be a conjuction, put its meanings as a conjuction]",
}"""

response = client.chat.completions.create(
  model="gpt-4 turbo",
  messages=[
    {"role": "system", "content": "You are a assistant that provides information about words."},
    {"role": "user", "content": config},
    {"role": "assistant", "content": "Okay, start with a word."},
    {"role": "user", "content": ""} # TODO: Crear un ejemplo de prueba
  ]
)