import requests

API_URL = "https://www.stack-inference.com/inference/v0/run/3d4904b4-95d8-4f91-8413-598cd6ad6e28/65ec7764f55f2d6ba176042d"
headers = {'Authorization':
			 'Bearer d6c868e4-dd77-433a-b8f6-40264a0fd870',
			 'Content-Type': 'application/json'
		}

def query(payload):
 response = requests.post(API_URL, headers=headers, json=payload)
 return response.json()

output = query({"in-0": """Find resources on the internet that are primarily related to the haskell and functional programming, give links for A-Level related resources for students.""", 
                "user_id": """d6c868e4-dd77-433a-b8f6-40264a0fd870"""})
print(output)