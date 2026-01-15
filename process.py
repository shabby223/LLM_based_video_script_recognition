from zhipuai import ZhipuAI
import base64


API_KEY = your_api_key_here
client = ZhipuAI(api_key=API_KEY)

PROMPT = """请复述视频中人物所说的内容，要求：
1. 不区分说话人
2. 内容写在一行
3. 添加适当的标点符号
4. 分句、人物停顿之间使用逗号分隔，句子语义完整则打句号
5. 仅返回复述内容，不要额外说明
6. 如果无法识别内容，返回"无法识别"
7. 注意结合视频字幕和视频音频
"""

def process_video(video_path):
    # 读取视频文件并转换为base64
    with open(video_path, "rb") as video_file:
        video_base64 = base64.b64encode(video_file.read()).decode()
        print("Video file read and encoded to base64.")
    
    response = client.chat.completions.create(
        model="glm-4.6v-flash",
        messages=[
            {
                "role": "system",
                "content": "你是一个视频内容识别器，能够识别视频中人物所说的内容，并将其复述出来。注意结合视频字幕和视频音频。严格遵循用户的指示进行复述。"
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "video_url",
                        "video_url": {
                            "url": f"data:video/mp4;base64,{video_base64}"
                        }
                    },
                    {
                        "type": "text",
                        "text": PROMPT
                    }
                ]
            }
        ],
        thinking={
            "type": "disabled"
        }
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    video_path = "🐧这种企鹅最精了🐧.mp4"
    process_video(video_path)

