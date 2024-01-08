import cv2
import pickle

width, height = 107, 48

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except FileNotFoundError:
    posList = []


def mouseClick(events, x, y, flags, params):
    global posList
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)


def draw_numbers(image, positions):
    for idx, pos in enumerate(positions, start=1):
        cv2.rectangle(image, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
        cv2.putText(image, str(idx), (pos[0] + 10, pos[1] + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


while True:
    img = cv2.imread('carParkImg.png')
    draw_numbers(img, posList)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    key = cv2.waitKey(1)
    if key == ord('q'):  # Press 'q' to exit
        break

cv2.destroyAllWindows()
