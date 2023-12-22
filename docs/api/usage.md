# Usage

## Fix Audio

POST request

```text
https://voicefixer-voicefixer-api.hf.space/process_audio
```

Submit an audio file as an input. The API returns the contents of a WAV file.

:::{dropdown} CURL
```bash
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@test.mp3" https://voicefixer-voicefixer-api.hf.space/process_audio > processed_audio.wav
```
:::

:::{dropdown} Python
```python
import requests

url = "https://voicefixer-voicefixer-api.hf.space/process_audio"

files = {'file': ('test.mp3', open('test.mp3', 'rb'))}
headers = {}
response = requests.post(url, files=files, headers=headers)
if response.status_code == 200:
    with open('processed_audio.wav', 'wb') as f:
        f.write(response.content)
else:
    print(response.text)
```
:::

:::{dropdown} NodeJS
```javascript
const axios = require('axios');
const fs = require('fs');
const FormData = require('form-data');

const url = 'https://voicefixer-voicefixer-api.hf.space/process_audio';
const filePath = 'test.mp3';

const formData = new FormData();
formData.append('file', fs.createReadStream(filePath));
axios({
    method: 'post',
    url: url,
    data: formData,
    headers: {
        ...formData.getHeaders(),
    },
    responseType: 'stream',
})
    .then((response) => {
        response.data.pipe(fs.createWriteStream('processed_audio.wav'));
        console.log('File saved as processed_audio.wav');
    })
    .catch((error) => {
        console.error('Error:', error.response.status, error.response.data);
    });
```
:::

## Authentication

No authentication is required to use the API, however we rate limit requests by IP address. If you have multiple users using your application, we recommend making calls from individual users to prevent rate limits.

## Rate Limits

Currently, requests are limited to 1 request every 5 seconds per IP address.

## Formats

We support a variety of input formats (wav, mp3, m4a, etc). The API outputs a wav file.

