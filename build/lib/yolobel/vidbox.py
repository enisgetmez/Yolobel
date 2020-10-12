from yolobel import enums
import cv2
def yolo_calculator(point1,point2,w,h,rectangle):
    centre = [0.5*(point1[1]+point2[1])/w, 0.5*(point1[0]+point2[0])/h]
    width, height = (rectangle[3]/w, rectangle[2]/h)
    yolo_result = (f'{centre[0]:.6f} {centre[1]:.6f} {width:.6f} {height:.6f}\n')
    return yolo_result

def save_out(yolo_result,frame):

    cv2.imwrite(enums.out_directory +"/{}{}.jpg".format(enums.out_name,enums.out_count),frame)
    out_text = open(enums.out_directory+"/{}{}.txt".format(enums.out_name,enums.out_count), "w")
    out_text.write(yolo_result)
    out_text.close()
    if(enums.out_count == 0):
        classes_text = open(enums.out_directory+"/classes.txt", "w")
        classes_text.write(str(enums.out_name))
        classes_text.close()



    enums.out_count +=1

