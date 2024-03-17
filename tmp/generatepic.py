from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
import torch
import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
model_id = "stabilityai/stable-diffusion-2-1-base"

scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
print("11")
pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16)
print("22")
pipe = pipe.to("cuda:2")

prompt = "a real delicious hamburger"
print("33")
image = pipe(prompt).images[0]  
print("44")
image.save("astronaut_rides_horse.png")