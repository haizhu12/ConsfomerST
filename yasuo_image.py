from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None
import os
filePath = 'datasets/CelebAMask_HQ/trainB'
list_file_name=os.listdir(filePath)
path_image='datasets/CelebAMask_HQ/trainB/'
save_path="datasets/CelebAMask_HQ/trainB_yasuo/"
for image_number in range(len(list_file_name)):
    file_path=path_image+list_file_name[image_number]
    imagePath = os.path.join(file_path)
    imageSize = os.path.getsize(imagePath)
    #imageSize /= 1024  # 除以1024是代表Kb
    img = Image.open(file_path)
    # 获取图片的像素信息
    #pixels = img.getdata()

    if imageSize>=20000000:
        continue
    if img.mode == "P" or img.mode == "RGBA" or img.mode == "LA":
        img = img.convert('RGB')

    new_img = img.resize((256, 256))
    save_full_path=save_path+list_file_name[image_number]
    new_img.save(save_full_path)
    if image_number%100==0:
        print(imageSize)
        print("========",image_number,"=========")
