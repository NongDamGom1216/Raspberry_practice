import requests

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