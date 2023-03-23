from flask import Flask, render_template, request, jsonify
import requests
import openai

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('./index.html')


@app.route('/submit', methods=['POST'])
def submit():

    open_ai_cookie = request.cookies.get("not-api-cookie")

    if not open_ai_cookie:
        return jsonify({'message': 'No OpenAI key, check https://platform.openai.com/account/api-keys for your key'})
    else:
        try:
            openai.api_key = f"{open_ai_cookie}"
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": '''Break down these examples of prompts that I provide and using the user input, adapt them to provide a prompt with the style of the output is consistent with the following examples:

            Example: a photograph capturing the tranquility and beauty of a forest, with the sunlight filtering through the trees and the birds singing in the distance. The use of a shallow depth of field creates a sense of depth and focus on the foreground leaves, while the blurred background adds a sense of mystery and depth. The careful use of light and color highlights the natural beauty of the scene. --ar 16:9

            Example: A photograph capturing the beauty and simplicity of a still life arrangement of fruit and flowers, with the warm light and deep shadows creating a sense of depth and texture. The careful use of color and contrast highlights the beauty of the natural forms, emphasizing the richness and diversity of the world around us. --ar 16:9

            Example: A photograph capturing the beauty and intricacy of a handcrafted piece of pottery, with the texture and details of the clay surface adding visual interest and depth. The use of soft light and shallow depth of field creates a sense of focus on the intricate patterns and forms, emphasizing the beauty of human craftsmanship and creativity. --ar 16:9

            Example: The photograph captures the power of teamwork and collaboration, with a group of people working together to achieve a common goal. The composition is balanced, with the human figures carefully arranged to create a sense of harmony and unity. The use of depth and texture highlights the physical effort and emotional connection between the figures, adding to the overall sense of power and beauty. --ar 16:9

            Example: A photograph capturing the beauty and complexity of a spider's web, with the intricate patterns and delicate threads creating a sense of depth and texture. The use of a macro lens and careful focus emphasizes the small details of the web, highlighting the beauty of nature's design and the intricacy of the natural world. --ar 16:9

            Example: A photograph capturing the tranquility and peace of a still lake at sunset, with the reflection of the sky creating a sense of symmetry and balance. The use of warm colors and soft light adds to the overall sense of calm and relaxation, while the careful composition emphasizes the beauty of the natural landscape. --ar 16:9

            Example: A photograph capturing the tenderness and vulnerability of a mother holding her newborn baby, with their faces illuminated by soft natural light. The use of shallow depth of field creates a sense of focus on their faces, while the blurred background adds a sense of intimacy and privacy. The careful use of light and shadow highlights the contours of their faces, emphasizing the beauty of their bond. --ar 16:9

            Example: A photograph capturing the warm and comfort of a cozy fireplace, with the flickering flames creating a sense of calm and relaxation. The focus is on the fire itself, with the intricate patterns and textures of the flames adding visual interest and depth. The use of warm colors and soft light enhances the overall sense of coziness and intimacy. --ar 16:9

            Example: A photograph capturing a lone sailboat floating on a calm sea, with the warm glow of a setting sun in the distance. The use of a wide - angle lens and careful composition emphasizes the vastness and grandeur of the natural landscape, while the use of warm colors and gentle light adds to the overall sense of tranquility and serenity. --ar 16:9

            Example: A photograph capturing the beauty and simplicity of a quiet moment, with the moonlight filtering through the window and the gentle night breeze rustling the curtains. The use of shallow depth of field creates a sense of focus on the moonlit scene, while the blurred background adds a sense of depth and context. The use of muted colors and soft light adds to the overall sense of tranquility and calm. --ar 16:9

            Please note that the input will vary and it should be fill with the actual input provided by the user. Additionally, the style of the output should be consistent with the provided examples in terms of format, punctuation, vary with the writing style.

            Return me 2 answers, always as a list'''},{"role": "user", "content": f"{request.json['inputValue']}"}])

            return jsonify({'message': completion.choices[0].message.content})
        except requests.exceptions.RequestException as err:
            print('Something went wrong:', err)
            return jsonify({'message': 'Something went wrong'}), 500


if __name__ == '__main__':
    app.run(debug=True)
