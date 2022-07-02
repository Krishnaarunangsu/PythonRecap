from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print('Coming POST  ')
        # user = request.form['Krishna']
        user = request.form['nm']
        print(user)
        # user = 'Krishna-2'
        return redirect(url_for('success', name=user))
    else:
        print('Coming here')
        user = request.args.get('nm')
        # user = 'XYZ'
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)
