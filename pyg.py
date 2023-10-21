import banana_dev as banana

api_key = "insert API key"
model_key = "insert model key"
print("this is Pygmalion! What is your prompt?")
def call_model(prompt):
	out = banana.run(api_key, model_key, prompt)
	return out

while True:
	print("type your prompt:")
	user_prompt = input('')
	if user_prompt == "stop":
		exit()
		
model_inputs = {

"max_new_tokens": 5,

"prompt": user_prompt,

}
model_response = call_model(prompt=model_inputs)
print(model_response)