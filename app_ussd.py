from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    '''
    Route path of the Application
    :return:
    '''
    return 'Hello World!'


@app.route('/ussd', methods=['GET', 'POST'])
def ussd():
    '''
    Callbacks Requests Entry Point
    :return:
    '''

    input_text = request.values.get('text')
    txt = ussd_handler(input_text)

    resp = make_response(txt, 200)
    resp.headers['Content-type'] = 'text/plain'
    return resp


def ussd_handler(input_value):
    '''
    flask_ussd Inputs Logic Handler
    :return:
    '''
    end_text = '\n00: Menu\
                '
    list_events = '\n1. Climbing Mt. Kenya\
                    \n2. Serengeti Nat. Park\
                    \n3. Jinja Falls\
                    \n4. Aberdares\
                   '

    if input_value == '' or input_value[-3:] == '*00' or input_value is None:
        view_text = f'CON Welcome to ABC Tours\
                      \n\n1: Book Event\
                      \n2: View Events\
                      \n{end_text}\
                    '
    elif input_value == '1':
        view_text = f'CON Choose Package:-\
                      \n{list_events}\
                    '
    elif input_value == '2':
        view_text = f'END Upcoming Events:-\
                      \n{list_events}\
                    '
    elif input_value == '1*1':
        view_text = f'END You Have Successfully\
                      \nBooked an event to Climb Mt. Kenya\
                    '
    elif input_value == '1*2':
        view_text = f'END You Have Successfully\
                      \nBooked an event to Serengeti Nat. Park\
                    '
    elif input_value == '1*3':
        view_text = f'END You Have Successfully\
                      \nBooked an event to visit Jinja Falls\
                    '
    elif input_value == '1*4':
        view_text = f'END You Have Successfully\
                      \nBooked an event to visit Aberdares\
                    '
    else:
        view_text = f'CON Invalid Choice, Try Again\
                      \n{end_text}\
                   '
    return view_text


if __name__ == "__main__":
    app.run(debug=True)