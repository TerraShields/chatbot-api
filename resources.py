from flask_restful import Resource
from middleware import token_required
from flask import request
from dotenv import load_dotenv
from util import groq_client

load_dotenv()


class ChatBot(Resource):
    @token_required
    def post(self):
        user_message = request.form['caption']
        test_case = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Kamu adalah Petani Yang Hebat Dan bisa menjawab semua masalah tentang pertanian. Nama anda adalah anita asisten dari HAPETANI. jika ada pertanyaan yang bukan tentang pertanian bilang saja anda tidak tahu"
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            model="llama3-70b-8192",
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )

        respon = test_case.choices[0].message.content

        result = {
            "system": respon,
            "user": user_message
        }
        return result
