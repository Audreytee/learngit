from app import create_app

# 主线程
app = create_app()

if __name__ == '__main__':
    # 生产环境：nginx+uwsigi执行


    # threaded:单进程，多线程
    app.run(debug=app.config['DEBUG'], port=81, threaded=True)
