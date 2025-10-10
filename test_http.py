import requests, json

url = "http://localhost:11434/api/chat"

# 🟢 Step 1: Planner Prompt
planner_prompt = """
Convert the user instruction into the exact plan JSON as specified below.

Schema:
{
  "task_type": "<one of: generate_meal | get_news | get_weather | search | todo | multi>",
  "steps": [
    {
      "action": "<generate_meal|get_news|get_weather|search|todo>",
      "params": { ... }
    }
  ]
}

Rules:
- Return JSON only, no extra words.
- If multiple requests, use "task_type":"multi" and include steps in order.
- For generate_meal: { "target_kcal": number, "when":"breakfast|lunch|dinner|day", "diet": string or null }
- For get_news: { "topic": string, "country": string or null, "max_results": number }
- For get_weather: { "location": string }
- For search: { "query": string, "max_results": number }
- For todo: { "tasks": [ { "title": string, "deadline": ISO8601 or null, "priority":"low|med|high" } ] }

Example:
User: "I need 1000 kcal today vegetarian. Also give me top 3 tech news."
Output:
{
  "task_type":"multi",
  "steps":[
    {"action":"generate_meal","params":{"target_kcal":1000,"when":"day","diet":"vegetarian"}},
    {"action":"get_news","params":{"topic":"technology","country":"global","max_results":3}}
  ]
}
"""

# 🟢 Change this line to any real instruction you want to test
user_instruction = "I want 1000 kcal today vegetarian. Also give me top 3 tech news."

payload = {
  "model": "gemma:2b",
  "messages": [
    {"role":"user","content": planner_prompt + "\nUser instruction: " + user_instruction}
  ],
  "stream": False
}

r = requests.post(url, json=payload, timeout=20)

print("STATUS", r.status_code)
print("RESPONSE:\n", r.text[:2000])
