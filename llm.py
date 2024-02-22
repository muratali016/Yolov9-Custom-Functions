from openai import OpenAI
client = OpenAI(api_key ="sk-xxx")
def get_response(prompt):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
      {"role": "system", "content": "You are my helpful Yolov9 assistant in blurring harmful objects in images. I will provide you a list of objects and you will respond like this: 'Cigarette, Beer'. Just give me the censored object names in a python list. Examples of some harmful objects: Things related to Alcohol and smoking. Knives. Adult explicit, naked images etc"},
      {"role": "user", "content":  f"{prompt}"}
    ]
  )

  if completion.choices[0].message.content!=None:
    print(completion.choices[0].message.content)
  return completion.choices[0].message.content
