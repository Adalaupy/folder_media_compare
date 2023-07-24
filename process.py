import glob
import os
from PIL import Image
from moviepy.editor import VideoFileClip
import shutil


# The Path got from GUI is string, convert them into list for handling multiple path.
def Str_To_List(String_text):
    
    New_List = []

    for item in String_text.splitlines():
        
        New_List.append(item.strip())


    New_List = [i for i in New_List if i !=""]

    return New_List


# Find all video,image file from the path
def find_media(path_list):

    img_extension = ('*.jpg', '*.jpeg', '*.png', '*.bmp', '*.gif')
    vdo_extension = ('*.mp4', '*.avi', '*.mkv', '*.mov')


    img_file = []
    vdo_file = []

    for path_item in path_list:        

        for ext in img_extension:

            img_file.append(glob.glob(os.path.join(path_item,ext)))


        for ext in vdo_extension:

            vdo_file.append(glob.glob(os.path.join(path_item,ext)))


    img_file = [item for item in img_file for item in item]
    vdo_file = [item for item in vdo_file for item in item]


    return img_file,vdo_file



# Compare the images from two folder and copy the new photo to the default destination
def img_compare(imgList_from,imgList_to):

    not_in_List = []

    for i in range(len(imgList_from)):

        isFound = False

        img_hist_from = Image.open(imgList_from[i]).histogram()

        for y in range(len(imgList_to)):
            
            img_hist_to = Image.open(imgList_to[y]).histogram()

            if img_hist_from == img_hist_to:
                
                isFound = True

                break

        
        if not isFound:

            not_in_List.append(imgList_from[i])   
            
            fileName = os.path.basename(imgList_from[i])
            
            destination_file = default_destination + "\\" + fileName

            shutil.copy(imgList_from[i],destination_file)


            
    
    return not_in_List



# Compare the video from two folder and copy the new photo to the default destination
def vdo_compare(vdoList_from,vdoList_to):

    not_in_List = []

    for i in range(len(vdoList_from)):

        isFound = False

        video_from = VideoFileClip(vdoList_from[i])

        for y in range(len(vdoList_to)):

            video_to = VideoFileClip(vdoList_to[y])

            if video_from.duration == video_to.duration and video_from.fps == video_to.fps and video_from.size == video_to.size:

                with open(vdoList_from[i],'rb') as f1, open(vdoList_to[y],'rb') as f2:
                    
                    if f1.read() == f2.read():

                        isFound = True
                    
                        break
            
            video_to.close()


        if not isFound:

            not_in_List.append(vdoList_from[i])   
            
            fileName = os.path.basename(vdoList_from[i])
            destination_file = default_destination + "\\" + fileName

            shutil.copy(vdoList_from[i],destination_file)


        video_from.close()


    
    return not_in_List





# Main process
def Process(from_str,to_str):

    

    From_List = Str_To_List(from_str)
    To_List = Str_To_List(to_str)


    global default_destination
    default_destination = To_List[0]



    imgList_from,vdoList_from = find_media(From_List)
    imgList_to,vdoList_to = find_media(To_List)




    not_in_List_photo = img_compare(imgList_from,imgList_to)
    print(f"You have copied {str(len(not_in_List_photo))} photos")


    not_in_List_video = vdo_compare(vdoList_from,vdoList_to)
    print(f"You have copied {str(len(not_in_List_video))} videos")