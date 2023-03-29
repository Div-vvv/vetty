from flask import Flask, send_file, request

app = Flask(__name__)


@app.route('/render', methods=['GET'])
def render_file():
    global contents
    try:
        file_name = request.args.get('file_name')
        start_index = request.args.get('start_index')
        end_index = request.args.get('end_index')
        filename = 'static/' + file_name
        f = open(filename, 'r', encoding="utf-8", errors='ignore')
        if f.mode == 'r':
            contents = f.readlines()

        mytext = ""
        if start_index and end_index is not None:
            mytext = mytext.join(contents[int(start_index):int(end_index) + 1])
            return mytext
        else:
            mytext = mytext.join(contents)
            return mytext
    except FileNotFoundError:
        return {'status': 400, 'data': 'FILE NOT FOUND ERROR'}
    except EnvironmentError:
        return {'status': 400, 'data': 'ENVIRONMENT ERROR'}
    except TypeError:
        return {'status': 400, 'data': 'TYPE ERROR'}
    except RuntimeError:
        return {'status': 400, 'data': 'RUNTIME ERROR'}
    except IndexError:
        return {'status': 400, 'data': 'INDEX OUT OF RANGE'}


if __name__ == '__main__':
    app.run(debug=True)
