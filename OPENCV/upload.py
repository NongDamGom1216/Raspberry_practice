import requests

# url = 'http://172.30.1.21:8000/api/upload_record/'

# data = {
#     'file_name' : '20220317_162122.mp4',
# }
# # http의 body로
# # file_name=20220317_162122.mp4&size=1000

# # binary 데이터를 보내기 위해 만든 사전(여기서는 video)
# files = {
#     'video' : open('./data/20220317_162122.mp4', 'rb')
# }

# res = requests.post(url, data=data, files=files)
# print(res.status_code)
# print(res.json())

def upload(url, file_path):
    data = {
        'file_name' : file_path.split('/')[-1]
    }

    files = {
        'video' : open(file_path, 'rb')
    }

    res = requests.post(url, data=data, files=files)
    if res.status_code == 200:
        result = res.json()
        if result.get('result') == 'success':
            return True
        
    return False


url = 'http://172.30.1.21:8000/api/upload_record/'
file_path = './data/20220317_162122.mp4'
result = upload(url, file_path)

if result:
    print('upload success')
else:
    print('upload fail')