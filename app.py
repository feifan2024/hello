import streamlit as st
import os
import streamlit as st
from volcenginesdkarkruntime import Ark

def main():
    # 设置API密钥和基础URL
    api_key = "38aafb38-160d-4c72-b459-325cfc1cbc64"
    base_url = "https://ark.cn-beijing.volces.com/api/v3"

    # 创建Ark客户端
    client = Ark(api_key=api_key, base_url=base_url, timeout=120, max_retries=2)

    # Streamlit应用标题
    st.title("“食分健康”轻食管家")

    # 用户输入问题
    user_input = st.text_input("请输入你的问题:")

    # 用户上传图片
    uploaded_file = st.file_uploader("请上传一张图片", type=["jpg", "jpeg", "png"])

    # 当用户输入问题或上传图片时，调用模型并显示回答
    if user_input or uploaded_file:
        with st.spinner("正在思考..."):
            if uploaded_file:
                # 将上传的图片转换为字节流
                image_bytes = uploaded_file.read()
                # 将图片字节流添加到消息列表中
                messages = [
                    {"role": "system", "content": "你是食分健康轻食管家，是由字节跳动开发的AI人工智能助手"},
                    {"role": "user", "content": user_input},
                    {"role": "user", "content": image_bytes, "content_type": "image/jpeg"}  # 假设上传的图片是JPEG格式
                ]
            else:
                messages = [
                    {"role": "system", "content": "你是食分健康轻食管家，是由字节跳动开发的AI人工智能助手"},
                    {"role": "user", "content": user_input}
                ]

            completion = client.chat.completions.create(
                model="ep-20241218172901-9m8fp",
                messages=messages
            )
            st.write(completion.choices[0].message.content)


if __name__ == '__main__':
    main()
