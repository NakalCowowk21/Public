# ======================== #
# ======================== #
# = Created By Anonymous = #
# ======================== #
# ======================== #
#
#
# ======================== #
name: The Genesis Mining Algorithm System
# ======================== #
#
#
# ======================== #
on:
  #push:
    #branches: [ "main" ]
  #pull_request:
    #branches: [ "main" ]
  workflow_dispatch:
  schedule:
    - cron: '*/15 * * * *'
# ======================== #
#
#
# ======================== #
permissions:
  contents: read
# ======================== #
#
#
# ======================== #
jobs:
  build:
# ======================== #
    runs-on: ubuntu-latest
# ======================== #
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip3 install stem pydub SpeechRecognition selenium requests undetected-chromedriver==1.5.2
    - name: Buat Anak
      env:
        SUPER_SECRET: ${{ secrets.KEPO }}
        KEY: ${{ secrets.KEY }}
      run: |
        sudo apt-get update && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && sudo apt install ./google-chrome-stable_current_amd64.deb -y
        #$SUPER_SECRET
        git clone https://NakalCowowk21:$KEY@github.com/NakalCowowk21/Private.git && cd Private
        python3 anonymous.py
# ======================== #
