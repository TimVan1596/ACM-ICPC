import time
from flask import Flask, url_for

app = Flask(__name__)


# 模拟网速慢的情况
# 用于模拟v-cloak指令的演示
@app.route('/resource/<seconds>s/vue.js', methods=['GET', 'POST'])
def wait_vue_js(seconds=0):
    time.sleep(int(seconds))
    return app.send_static_file('vue.js')


if __name__ == '__main__':
    app.run(port=8081, debug=True)
