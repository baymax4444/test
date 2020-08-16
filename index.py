from flask import Flask, request, render_template, redirect, url_for, flash, session
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/regist', methods=['GET','POST'])
def regist():
    error = None
    if request.method == 'POST':
        if request.form['password1'] != request.form['password2']:
            error = '两次密码不相同！'
        elif valid_regist(request.form['username'], request.form['email']):
            user = User(username=request.form['username'], password=request.form['password1'], email=request.form['email'])
            db.session.add(user)
            db.session.commit()
            
            flash("成功注册！")
            return redirect(url_for('login'))
        else:
            error = '该用户名或邮箱已被注册！'
    
    return render_template('regist.html', error=error)




if __name__ == "__main__":
    app.run()