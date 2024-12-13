import tkinter as tk
from gtts import gTTS
import os

# وظيفة لتحويل النص إلى كلام
def text_to_speech():
    text = entry.get()
    if text:
        tts = gTTS(text=text, lang='en')
        tts.save("speech.mp3")
        os.system("start speech.mp3")

# وظيفة لمسح النص
def clear_text():
    entry.delete(0, tk.END)

# إنشاء النافذة
root = tk.Tk()
root.title("GUI Application")
root.geometry("300x200")

# مربع الإدخال
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=20)

# الزر الأول: تشغيل النص كصوت
play_button = tk.Button(root, text="Play", command=text_to_speech, font=("Arial", 12), width=10)
play_button.pack(pady=5)

# الزر الثاني: زر الخروج
exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 12), bg="red", fg="white", width=10)
exit_button.pack(pady=5)

# الزر الثالث: مسح النص
set_button = tk.Button(root, text="Set", command=clear_text, font=("Arial", 12), width=10)
set_button.pack(pady=5)

# تشغيل الواجهة
root.mainloop()