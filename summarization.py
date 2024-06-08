#Note: The openai-python library support for Azure OpenAI is in preview.
#Note: This code sample requires OpenAI Python library version 1.0.0 or higher.
from openai import AzureOpenAI
from PyPDF2 import PdfReader
import os

def extract_pdf_pages(pdf_file_path, max_tokens = 20000):
    pdf_pages = []
    tokens_count = 0
    with open(pdf_file_path, 'rb') as pdf_file:
        reader = PdfReader(pdf_file)
        for page_number in range(len(reader.pages)):
            pdf_page_info = {
                'information': reader.pages[page_number].extract_text(),
                'source_file_name': os.path.basename(pdf_file_path),
                'page_number': page_number + 1
            }
            tokens_count += len(pdf_page_info['information'].split())
            if tokens_count >= max_tokens:
                break
            pdf_pages.append(pdf_page_info)
    return pdf_pages

client = AzureOpenAI(
  azure_endpoint = "https://rag-openai-aueast.openai.azure.com/", 
  api_key=os.getenv(""),  
  api_version="2024-02-15-preview"
)

message_text = [{"role":"system","content":"You are an AI assistant that helps people summarize documents."},
                {"role":"user","content":str(extract_pdf_pages('telecom-development.pdf'))}] # enter the path of the document here

completion = client.chat.completions.create(
  model="gpt4model", # model = "deployment_name"
  messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)

print(completion.choices[0].message.content)