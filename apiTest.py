# # import requests

# # API_URL = "https://www.stack-inference.com/inference/v0/run/3d4904b4-95d8-4f91-8413-598cd6ad6e28/65ec7764f55f2d6ba176042d"
# # headers = {'Authorization':
# # 			 'Bearer d6c868e4-dd77-433a-b8f6-40264a0fd870',
# # 			 'Content-Type': 'application/json'
# # 		}

# # def query(payload):
# #  response = requests.post(API_URL, headers=headers, json=payload)
# #  return response.json()

# # output = query({"in-0": """Find resources on the internet that are primarily related to the haskell and functional programming, give links for A-Level related resources for students.""", "user_id": """<USER or Conversation ID>"""})
# import requests

# API_URL = "https://www.stack-inference.com/inference/v0/run/87a0f031-97dd-4577-a4c9-93c4ae154122/65ed800431b5c269a6c0b018"
# headers = {'Authorization':
# 			 'Bearer 5064899d-f14e-4837-877f-e2b700d63f70',
# 			 'Content-Type': 'application/json'
# 		}

# def query(payload):
#  response = requests.post(API_URL, headers=headers, json=payload)
#  return response.json()

# output = query({"in-2": """Generate 5 A-level objective type questions from the following information
# (give A ,B,C,D). List all the questions below Add a slash after listing all options to seperate each question from the previous one.""", "user_id": """<USER or Conversation ID>"""})
# print(output)
# # print(output['outputs']['out-0'])
# # print(output['outputs']['out-	`1'])
# lst = output['outputs']['out-3'].split(" /")
# for i in lst:
#  print(i)

# import os

# concatfile =''

# for dirpath,dirname,filenames in os.walk('txtOutputs'):
#     for filename in filenames:
#         if filename.endswith('.txt'):
# 			file=open(os.path.join(dirpath,filename), encoding='utf-8')
# 			print(filename)
#         for x in file:
#             concatfile+=x

# with open("concatFile.txt", "w") as f:
#     f.write(concatfile)


import os

concat = ''
directory = '//txtOutputs'
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        if filename.endswith('.txt'):
            with open(os.path.join(dirpath, filename)) as f:
                concat+=f.read()

with open("concat.txt", "w", encoding='utf-8') as f:
    f.write(concat)