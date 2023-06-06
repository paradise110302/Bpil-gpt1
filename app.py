import torch
from transformers import BlipForConditionalGeneration, BlipProcessor, GPT2LMHeadModel, GPT2Tokenizer
from flask import Flask, request, render_template
from PIL import Image

app=Flask(__name__)

device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

blip_processor= BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
blip_model=BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large").to(device)

gpt_model_name='gpt2'
gpt_model= GPT2LMHeadModel.from_pretrained(gpt_model_name).to(device)
gpt_tokenizer = GPT2Tokenizer.from_pretrained(gpt_model_name)

def generate_caption(raw_image):
  inputs = blip_processor(images=raw_image, return_tensors="pt")
  caption= blip_model.generate(**inputs)
  caption_text=blip_processor.batch_decode(caption,skip_special_tokens=True)[0]
  return caption_text

def generate_text_output(caption,prompt):
  prompt_text=f"{caption} {prompt}"
  input_ids=gpt_tokenizer.encode(prompt_text,return_tensor='pt').to(device)
  max_length = 100
  output = gpt_model.generate(input_ids=input_ids,max_length=max_length,num_return_sequences=1)
  text_output= gpt_tokenizer.decode(output[0],skip_special_tokens=True)
  return text_output

@app.route('/',methods=['GET','POST'])
def index():
  if request.method == 'POST':
    image = request.files['image']
    prompt=request.form['prompt']
    image_path=f"uploads/{image.filename}"
    image.save(image_path)
    image.pil = Image.open(image_path)
    caption = generate_caption(image_pil)
    text_output=generate_text_output(caption,prompt)
    return render_template('index.html',caption=caption,prompt=prompt,text_output=text_output)
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
