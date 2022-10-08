#### Download and install Google Chrome

#### Open Chrome=>Help=>about Google Chrome=>check chrome version

#### Go to: https://sites.google.com/chromium.org/driver/downloads?authuser=0 and download chrome drvier version same with the version of google chrome=>place the downloaded file into source folder

#### I Recommended use Pycharm as Editor to easy run test and install requirement file

#### If you want to run all tests, you should type: 
```sh
python -m unittest 
```


#### If you want to run just a suit, you should type: 
```sh
python -m unittest tests.test_sign_in_page.TestSignInPage
```

#### If you want to run just a test case, you should type: 
```sh
python -m unittest tests.test_sign_in_page.TestSignInPage."name_of_test_case"
```
