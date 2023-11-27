import cv2

vid = cv2.VideoCapture("AnthonyShkraba(1).mp4")

if(vid.isOpened()==False):
    print("Unable to read the feed")


height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)

fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

out = cv2.VideoWriter('test.avi',cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))

while(True):
    ret,frame=vid.read()

    cv2.imshow("web cam",frame)

    out.write(frame)


    if cv2.waitKey(1)==32:
        break
vid.release()
cv2.destroyAllWindows()