from flask import Flask, request, jsonify, Response, stream_with_context  
import json
  
app = Flask(__name__)  
  
# 定义一个处理GET请求的路由  
@app.route('/hello', methods=['GET'])  
def hello_world():  
    return 'Hello, World!'  
  
# 定义一个处理POST请求的路由  
@app.route('/create', methods=['POST'])  
def create_resource():  
    data = request.get_json()  # 获取POST请求体中的JSON数据  
    # 在这里，你可以对data进行处理，例如保存到数据库等  
    return jsonify({'message': 'Resource created successfully', 'data': data}), 201  
  
# 定义一个处理GET请求并返回资源的路由  
@app.route('/resource/<int:id>', methods=['GET'])  
def get_resource(id):  
    # 在这里，你可以根据id从数据库中获取资源  
    # 这里只是返回一个示例  
    resource = {'id': id, 'name': 'Example Resource'}  
    return jsonify(resource)  
  
# 定义一个处理DELETE请求的路由  
@app.route('/resource/<int:id>', methods=['DELETE'])  
def delete_resource(id):  
    # 在这里，你可以根据id从数据库中删除资源  
    # 这里只是返回一个示例  
    return jsonify({'message': f'Resource with ID {id} deleted successfully'})  

# 假设isNotEmptyString是一个函数，用于检查字符串是否为空  
# 在Python中，我们可以简单地使用字符串长度来检查  
def is_not_empty_string(s):  
    return isinstance(s, str) and len(s.strip()) > 0  
  
# 假设currentModel是一个函数，返回当前模型的信息  
# 这里我们简单地返回一个模拟的模型数据  
def current_model():  
    return "ExampleModel"  
  
# 定义处理POST请求的路由  
@app.route('/session', methods=['POST'])  
def session_handler():  

    try:  

        print("Received data:", request.json) 
          
        response_data = {  
            'status': 'Success',  
            'message': 'Session handled successfully.',  # 添加了一个消息  
            'data': {  
                'model': current_model()  
            }  
        }  
          
        # 发送响应  
        return jsonify(response_data)  # jsonify会自动设置Content-Type为application/json，并返回tuple (response, status_code)  
 
      
    except Exception as error:  
        # 捕获异常并发送错误响应  
        response_data = {  
            'status': 'Fail',  
            'message': str(error),  
            'data': None  
        }  
        return jsonify(response_data), 500  


@app.route('/verify', methods=['POST'])  
def verify_token():  
    try:  
        # 从请求体中获取token  
        token = request.json.get('token')  
        # 验证成功，返回响应  
        return jsonify({  
            'status': 'Success',  
            'message': 'Verify successfully',  
            'data': None  
        })  
  
    except ValueError as error:  
        # 捕获异常，返回错误信息  
        return jsonify({  
            'status': 'Fail',  
            'message': str(error),  
            'data': None  
        }), 400  # 使用400状态码表示请求错误 


# 假设的chatReplyProcess函数，用于模拟聊天回复过程  
def chatReplyProcess(prompt, parent_message_id):  
    # 构建包含text和parentMessageId的响应  
    response = {  
        "text": "Hello there! How can I help you?",  
        "parentMessageId": parent_message_id  
    }  
    return response  
  
def generate_response(response):  
    # 将响应字典转换为JSON字符串，并添加换行符以模拟SSE  
    yield json.dumps(response) + '\n'  
  
@app.route('/chat-process', methods=['POST'])  
def chat_process():  
    data = request.get_json()  
    prompt = data.get('prompt')  
    options = data.get('options', {})  
    parent_message_id = options.get('parentMessageId')  
      
    # 调用chatReplyProcess函数并获取响应  
    response = chatReplyProcess(prompt, parent_message_id)  
      
    # 使用Response对象和stream_with_context装饰器来创建流式响应  
    return Response(stream_with_context(generate_response(response)))  

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=3002, debug=True)
