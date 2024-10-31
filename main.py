import  requests
import re


def validate_phone_number(phone_number):
    pattern = r'^79\d{9}$'
    return bool(re.match(pattern, phone_number))

user='SDzhus'
password='12Policiy'
sender='SDzhus'
receiver='79165237058'
text='Hello, World!'

if not validate_phone_number(receiver):
    print('Ошибка! Некорректный номер телефона!')
else:
    url = f'https://my3.webcom.mob/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={receiver}&text={text}'
    print(url)
    try:
        response = requests.get(url)
        print(response)

        if response.status_code == 200:
            print('Сообщение успешно отправлено!')
        else:
            print(f'Ошибка при отправке сообщения {response.status_code}')
    except Exception as e:
        print(f'Непредвиденная ошибка с кодом {e}')