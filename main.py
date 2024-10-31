import  requests

user='SDzhus'
password='12Policiy'
sender='SDzhus'
receiver='79165237058'
text='Hello, World!'

url=f'https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={receiver}&text={text}'
print(url)
response = requests.get(url)
print(response)

if response.status_code == 200:
    print('Сообщение успешно отправлено!')
else:
    print(f'Ошибка при отправке сообщения {response.status_code}')
