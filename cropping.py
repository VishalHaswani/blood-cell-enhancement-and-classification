import cv2
import pandas as pa
import numpy as np

project_loc = "C:\\Users\\raj20\\OneDrive\\Desktop\\IP\\"
available_image_indexes = [];
annotations = pa.read_csv(project_loc + "Dataset\\annotations.csv")
rbc_k = wbc_k = 0

def find_in_annotations(i):
    global annotations
    search_str = "image-" + str(i) + ".png"
    ans = annotations[annotations["image"] == search_str]
    return ans

if __name__ == "__main__":
    for i in range(1, 121):
        try:
            img = cv2.imread(project_loc + "Dataset\Images\image-"+ str(i) +".png")
            available_image_indexes.append(i)
            img_ann = find_in_annotations(i)
            for j in range(len(img_ann)):
                xmin = int(img_ann.xmin.iloc[j])
                ymin = int(img_ann.ymin.iloc[j])
                xmax = int(img_ann.xmax.iloc[j])
                ymax = int(img_ann.ymax.iloc[j])
                cropped_image = img[ymin: ymax, xmin: xmax]
                if img_ann.label.iloc[j] == "rbc":
                    cv2.imwrite(project_loc + "Final Dataset\\Images 2\\RBC\\rbc-" + str(rbc_k) + ".png", cropped_image)
                    #print("rbc", rbc_k, ymin, ymax, xmin, xmax)
                    rbc_k += 1
                elif img_ann.label.iloc[j] == "wbc":
                    cv2.imwrite(project_loc + "Final Dataset\\Images 2\\WBC\\wbc-" + str(wbc_k) + ".png", cropped_image)
                    #print("wbc", rbc_k, ymin, ymax, xmin, xmax)
                    wbc_k += 1
                else:
                    print(img_ann.label.iloc[j])
        except Exception as a:
            print(i, "\n", a)
