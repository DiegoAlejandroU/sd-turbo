# sd-turbo

Generador de imágenes a partir de texto con [Stable Diffusion Turbo](https://huggingface.co/stabilityai/sd-turbo) (`stabilityai/sd-turbo`), usando la librería `diffusers` de Hugging Face.

El script pide un prompt por consola, genera la imagen y la guarda como `imagen.png`.

## Requisitos

- Python 3.12
- [uv](https://docs.astral.sh/uv/) para gestionar el entorno y las dependencias
- Conexión a internet la primera vez (el modelo pesa varios GB y se guarda en la caché de Hugging Face)
- Opcional: GPU NVIDIA (CUDA), Intel (XPU) o Mac con Apple Silicon (MPS). Sin GPU funciona en CPU, pero es más lento.

## Instalación

```powershell
git clone https://github.com/DiegoAlejandroU/sd-turbo.git
cd sd-turbo
uv sync
```

Si Windows bloquea el Python que descarga `uv` ("Una directiva de Control de aplicaciones bloqueó este archivo"), instala Python 3.12 desde python.org o con `winget install Python.Python.3.12` y usa:

```powershell
uv venv --python-preference only-system --python 3.12
uv sync
```

## Uso

```powershell
uv run .\src\sd_turbo\__init__.py
```

Escribe el prompt en inglés cuando el programa lo pida, por ejemplo:

```
A cozy mountain village at golden hour, snow-capped peaks in the background, warm light glowing from wooden cabins, highly detailed, cinematic lighting
```

La imagen se guarda en `imagen.png` en la carpeta desde la que ejecutas el comando.

### Ejemplo de resultado

![Imagen generada](imagen.png)

## Configuración

Los parámetros están en `src/sd_turbo/__init__.py`:

| Parámetro | Valor actual | Descripción |
|---|---|---|
| `dtype` | `torch.float32` | Precisión numérica. Si la imagen sale negra en GPU, prueba `torch.float16`. En CPU conviene dejar `float32`. |
| `num_inference_steps` | `10` | Número de pasos de generación. `sd-turbo` está pensado para 1 a 4. |
| `guidance_scale` | `2.0` | Fidelidad al prompt. Con `0.0` el `negative_prompt` no tiene efecto. |
| `height` / `width` | `1024` | Tamaño de la imagen. El modelo está entrenado para 512×512. |

Para una generación rápida, sobre todo en CPU, usa `num_inference_steps=4`, `guidance_scale=0.0`, `height=512` y `width=512`.

El dispositivo se elige automáticamente: CUDA, XPU, MPS o CPU, en ese orden de prioridad.

## Problemas frecuentes

- **`Torch not compiled with CUDA enabled`**: tu equipo no tiene GPU NVIDIA compatible. La versión actual del script usa CPU automáticamente.
- **Imagen negra**: cambia `dtype` a `torch.float16` (solo en GPU).
- **Se queda sin memoria o tarda demasiado**: reduce `height`, `width` y `num_inference_steps`.
- **Advertencias de `torchvision` o de enlaces simbólicos**: son informativas y no afectan el resultado.

## Autor

[DiegoAlejandroU](https://github.com/DiegoAlejandroU)
