sudo apt install python3.10-venv unzip wget redis
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list' \
&& apt-get update \
&& apt-get install -y google-chrome-stable \
&& rm -rf /var/lib/apt/lists/*

python3 -m venv venv
. venv/bin/activate
pip install -r ./api/requirements.txt 
pip install -r ./frontend/requirements.txt 
pip install -r ./parser/requirements.txt 
pip install -r ./redis/requirements.txt 

curl -O https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.141/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
cp chromedriver-linux64/chromedriver ./parser

set -a # automatically export all variables
source .env
set +a


python3 ./parser/main.py > parser.log &