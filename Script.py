from PIL import Image
import tempfile

def watermark_script(src):
    WATERMARK_ROUTE = "resources/" # Add the name of your watermark

    main_image = Image.open(src).convert("RGBA")
    watermark_image = Image.open(WATERMARK_ROUTE).convert("RGBA")

    watermark_image = watermark_image.resize(
        size=(int(main_image.width * 0.5), int(main_image.height * 0.5))
    )
    wm_width, wm_height = watermark_image.size

    alpha = watermark_image.getchannel("A")
    alpha = alpha.point(lambda p: p * 0.6) # Reduce the opacity
    watermark_image.putalpha(alpha)

    watermark_position = (
        (main_image.width - wm_width) // 2,
        (main_image.height - wm_height) // 2
    )

    watermarked_image = main_image.copy()
    watermarked_image.paste(watermark_image, watermark_position, watermark_image)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png", dir="out") as temp_file:
        temp_file_name = temp_file
        watermarked_image.save(temp_file_name)