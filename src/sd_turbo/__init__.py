import torch
from diffusers import AutoPipelineForText2Image

print("cargando modelo...")

modelo = AutoPipelineForText2Image.from_pretrained(
    "stabilityai/sd-turbo",
    dtype=torch.float32,
    # float 32 o 16 me indica la cantidad de
    # decimales con los cuales el modelo creara
    # la imagen, si mi pc genera una imagen negra pasa a 16
)

# Seleccion automatica del dispositivo:
# cuda - nvidia
# xpu - grafica intel (requiere torch con soporte XPU)
# mps - mac con procesadores m 1 . 2 . 3
# cpu - cualquier equipo (mas lento)
if torch.cuda.is_available():
    dispositivo = "cuda"
elif hasattr(torch, "xpu") and torch.xpu.is_available():
    dispositivo = "xpu"
elif torch.backends.mps.is_available():
    dispositivo = "mps"
else:
    dispositivo = "cpu"

print(f"Usando dispositivo: {dispositivo}")
modelo = modelo.to(dispositivo)

prompt = input("Escribe el prompt de la imagen: ")
negative_prompt = "blurry, low quality, worst quality, distorted face, bad anatomy, extra limbs, extra fingers, poorly drawn hands, watermark, signature, text, error"

print("Generando la imagen...")

imagen = modelo(
    prompt=prompt,
    negative_prompt=negative_prompt,
    num_inference_steps=10,  # Numero de veces que corregira o creara la imagen
    guidance_scale=2.0,  # que tan fiel sera al prompt
    height=1024,
    width=1024,
).images[0]

imagen.save("imagen.png")
print("Imagen guardada !")
