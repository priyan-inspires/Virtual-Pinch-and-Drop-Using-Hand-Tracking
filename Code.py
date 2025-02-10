import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

boxes = [
    (100, 100, 225, 225),
    (400, 100, 225, 225),
    (700, 100, 225, 225),
    (1000, 100, 225, 225),
    (1300, 100, 225, 225)
]
selected_box = None
box_color = (255, 105, 180)  # Pink color

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            label = handedness.classification[0].label  
            
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            
            distance = np.sqrt((index_x - thumb_x) ** 2 + (index_y - thumb_y) ** 2)

            # Detect Pinch Gesture 
            if distance < 30: # (Threshold distance between thumb & index)
                if selected_box is None:
                    for i, (bx, by, bw, bh) in enumerate(boxes):
                        if bx < index_x < bx + bw and by < index_y < by + bh:
                            selected_box = i
                            break
            else:
                selected_box = None  
            
            if selected_box is not None:
                bx, by, bw, bh = boxes[selected_box]
                boxes[selected_box] = (index_x - 112, index_y - 112, 225, 225) 

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            cv2.putText(frame, label, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    
    for bx, by, bw, bh in boxes:
        cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), box_color, -1)

    cv2.imshow("Virtual Pitch-and-Drop Using Hand Tracking by JSP", frame) #you can also rename this title
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
