from flask import Flask, request

app = Flask(__name__)


@app.route('/render', methods=['GET'])
def render_file():
    try:
        file_name = request.args.get('file_name')
        start_index = request.args.get('start_index')
        end_index = request.args.get('end_index')
        filename = 'static/' + file_name
        f = open(filename, 'r', encoding="utf-8", errors='ignore')
        contents = f.readlines()

        text = ''
        if start_index and end_index is not None:
            text = text.join(contents[int(start_index):int(end_index) + 1])
            return text
        else:
            text = text.join(contents)
            return text
    except FileNotFoundError:
        return {'error': 'FILE NOT FOUND ERROR'}
    except EnvironmentError:
        return {'error': 'ENVIRONMENT ERROR'}
    except TypeError:
        return {'error': 'TYPE ERROR'}
    except RuntimeError:
        return {'error': 'RUNTIME ERROR'}
    except IndexError:
        return {'error': 'INDEX OUT OF RANGE'}
    except Exception as e:
        return {'error': str(e)}


if __name__ == '__main__':
    app.run(debug=True)
