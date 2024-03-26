from PIL import Image, ImageOps
import random
import os

wall_width = 1920
wall_height = 500
grid_size = 200
angle = [i for i in range(0,30)]+[i for i in range(-30,0)]
output_image = Image.new(mode='RGB', size=(wall_width, wall_height), color="#FFF")

folder_path = r'D:\Github\foto'
images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

cols = wall_width // grid_size
rows = wall_height // grid_size

for i in range(rows):
    for j in range(cols):
        if not images:
            break

        img_name = images.pop(0)
        img_path = os.path.join(folder_path, img_name)
        with Image.open(img_path) as img:
 
            if img.mode != 'RGBA':
                img = img.convert('RGBA')

            new_size = random.randint(int(grid_size*0.8), int(grid_size * 1.5))
            img = ImageOps.fit(img, (new_size, new_size), Image.Resampling.LANCZOS, centering=(0.5, 0.5))

            img = img.rotate(random.choice(angle), expand=True)

            mask = img.split()[3]

            x = j * grid_size + (grid_size - new_size) // 2
            y = i * grid_size + (grid_size - new_size) // 2
            
            x = max(0, min(wall_width - new_size, x))
            y = max(0, min(wall_height - new_size, y))

            output_image.paste(img, (x, y), mask)


output_image.save('wall.jpg')
