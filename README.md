# Pupil_Control

This project is a project that controls screen scrolling through eye movements.<br>
It was developed to participate in the open source SW development contest in the school and received a silver prize.<br><br>

<h4>Purpose of the project</h4>
In a busy modern society, most people use smartphones while using public transportation.<br>
However, it is difficult to control your smartphone at will in public transportation during crowded commuting hours.<br>
In view of this, it was developed to make both hands more free to use by creating a program that can control the movement of electronic devices through the movement of eyes.<br><br>

<h4>Content of the project</h4>
<img src="https://user-images.githubusercontent.com/83286706/144562399-afc410b3-a525-4ce2-bc0b-ec69d34f552d.png" width="200" height="200">
Face and eyes were detected using Haarcascade's face and eye detector, an object detection algorithm using machine learning provided by OpenCV.<br>
After recognizing the face through the camera, it recognized the eyes and iris. (Each face is marked with a blue square, eyes with a light green square, and iris with a blue square.)<br>
The ratio from the pupil to the bottom of the eye to the height of the eye(marked it with a bold yellow line) was calculated, and the ratio for each user was applied.<br>
When eyeCnt is set according to the user's reading speed, the movement of the eyes is recognized according to the speed and automatically scrolled.<br><br>

<h4>Possibility of future development</h4>
If only the eyes are recognized and executed without facial recognition, the accuracy of the user's gaze will be reduced, but if the eye recognition rate is further improved in the future, it can only be recognized and used in small electronic devices such as smartphones.<br>
In addition, our algorithm can be applied to various functions such as screen scrolling and screen flipping to increase practicality.<br><br>

<h5>Reference data</h5>
https://wiserloner.tistory.com/1099<br>
https://www.youtube.com/watch?v=kbdbZFT9NQI<br>
https://blog.naver.com/roboholic84/22153345958
