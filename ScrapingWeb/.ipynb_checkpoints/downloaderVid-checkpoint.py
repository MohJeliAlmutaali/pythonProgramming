{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "51b4c3bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    }
   ],
   "source": [
    "import m3u8\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "9fefc814",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"https://manifest.prod.boltdns.net/manifest/v1/hls/v4/clear/3588749423001/9a54515e-9a8c-43d1-8e82-aef7ac91361b/10s/master.m3u8?fastly_token=NjMzNzVmYjFfZDZlNjZiNWQ2ZjU5M2VlYThiZGNjOTUwNjEzOWRjNThmZGRlNWQ5MGYyZjhmYWFlOWViYjYxMmFiMjU2NmI5NQ%3D%3D&seq=12_0\"\n",
    "r = requests.get(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "6d79048c",
   "metadata": {},
   "outputs": [],
   "source": [
    "m3u8_master = m3u8.loads(r.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "7693a8be",
   "metadata": {},
   "outputs": [],
   "source": [
    "playlist_uri = m3u8_master.data['playlists'][0]['uri']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "ec3e5925",
   "metadata": {},
   "outputs": [],
   "source": [
    "r = requests.get(playlist_uri)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "15c092bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "playlist = m3u8.loads(r.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "0a0e89a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://house-fastly-signed-eu-west-1-prod.brightcovecdn.com/media/v1/hls/v4/clear/3588749423001/9a54515e-9a8c-43d1-8e82-aef7ac91361b/7e6e2005-4af3-4665-b3e1-2e2155c98486/5x/segment0.ts?fastly_token=NjMzNzYzNWRfNDE0OWJhYjNhMmMyOWJiOTJjNzA5M2EyOWU4NjczMWVlY2M1OTI1MGI1OWQ1NGE3MDU5OWE2NjZmNmFkNjlmNF8vL2hvdXNlLWZhc3RseS1zaWduZWQtZXUtd2VzdC0xLXByb2QuYnJpZ2h0Y292ZWNkbi5jb20vbWVkaWEvdjEvaGxzL3Y0L2NsZWFyLzM1ODg3NDk0MjMwMDEvOWE1NDUxNWUtOWE4Yy00M2QxLThlODItYWVmN2FjOTEzNjFiLzdlNmUyMDA1LTRhZjMtNDY2NS1iM2UxLTJlMjE1NWM5ODQ4Ni8%3D'"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "playlist.data['segments'][0]['uri']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "f44ec095",
   "metadata": {},
   "outputs": [],
   "source": [
    "r = requests.get(playlist.data['segments'][0]['uri'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "a3ab206e",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('vid1.ts', 'wb') as f:\n",
    "    f.write(r.content)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9555700",
   "metadata": {},
   "outputs": [],
   "source": [
    "subprocess.run(['ffmpeg', '-i', 'vid1.ts' 'vid1'])\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
