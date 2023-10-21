# pip3 install banana-dev

import banana_dev as client

# Create a reference to your project on Banana
my_client = client.Client(
    api_key="daaf1805-4bcc-4109-9548-f90ffd28c660",
    # model_key="", # for SDK versions < 6.0.0, you need to pass in an empty model_key
    url="https://bananapyg-lo0j9untda.run.banana.dev",
)

# Specify the call's input JSON, what you expect 
# to receive in your Potassium app. Here is an 
# example for a basic BERT endpoint:
inputs = {
    "prompt": "In the summer I like [MASK].",
}

# Call your project's inference endpoint on Banana.
# If you have set up your Potassium app with a
# non-default endpoint, change the first 
# method argument ("/")to specify a 
# different route.
result, meta = my_client.call("/", inputs)

print(result)
